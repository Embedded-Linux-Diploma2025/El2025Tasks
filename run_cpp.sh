#!/bin/bash

examine_cpp_session() {
    local session_dir="$1"
    cd "$session_dir" || exit 1
    
    echo "🔧 Compiling and testing C++ files in $session_dir..."
    lab1_file=$(find . -iname "lab1_*.cpp")
    g++ -Wall -Wextra -std=c++17  "$lab1_file"
    if [ $? -ne 0 ]; then
        echo "[🟥] Error compiling $lab1_file"
        return  1
    fi
    rm a.out
    for file in *.cpp; do
        if [ ! -f "$file" ]; then
            echo "⚠️  No .cpp files found in $session_dir"
            continue
        fi
        
        filename="${file%.cpp}"
        echo "📋 Processing $file..."
        echo "🔨 Compiling $file..."
        g++ -Wall -Wextra -std=c++17 -o "$filename" "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error compiling $file"
            rm  "$filename"
            exit 1
        fi
        echo "[✅] $file compiled successfully"
        echo "🚀 Running $filename..."
        ./"$filename"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running $filename"
            rm  "$filename"
            exit 1
        fi
        echo "[🟩] $filename ran successfully"
        rm -f "$filename"
        echo ""
    done
    cd ../..
}

echo "==============================================";
echo "        C++ PROJECT TEST RUNNER";
echo "==============================================";
echo "";

#----------------- Session 1 -----------------#
echo "🎯 Testing C++ Session 1..."
examine_cpp_session "cpp/session1"

#----------------- Session 2 -----------------#
echo "🎯 Testing C++ Session 2..."
examine_cpp_session "cpp/session2"

echo "==============================================";
echo "[🎉] All C++ tests completed successfully!";
echo "==============================================";
