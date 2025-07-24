#!/bin/bash

examine_session() {
    local session_dir="$1"
    cd "$session_dir" || exit 1
    for file in *.py; do
        pylint --disable=C0301 "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running pylint for $file"
            exit 1
        fi
        python "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running $file"
            exit 1
        fi
        echo "[🟩] $file ran successfully"
    done
    cd ..
}

#----------------- Session 1 -----------------#
examine_session "python/session1"
#----------------- Session 2 -----------------#
python python/session2/lab1_get_your_location.py
if [ $? -ne 0 ]; then
    echo "[🟥] Session 2 is not Solved yet"
    exit 1
else
    examine_session "python/session2"
fi

#----------------- Session 3 -----------------#
python python/session3/lab1_dictionary_problems.py
if [ $? -ne 0 ]; then
    echo "[🟥] Session 3 is not solved yet"
    exit 1 # Comment this line if you want to bypass session3
else
    examine_session "session3"
fi
