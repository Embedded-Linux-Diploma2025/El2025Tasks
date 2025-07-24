#!/bin/bash

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

examine_session() {
    local session_dir="$1"
    cd "$session_dir" || exit 1
    for file in *.py; do
        pylint --disable=C0301 "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running pylint for $file"
            exit 1
        fi
        python3 "$file"
        if [ $? -ne 0 ]; then
            echo "[🟥] Error running $file"
            exit 1
        fi
        echo "[🟩] $file ran successfully"
    done
    cd "$BASE_DIR"
}

#----------------- Session 1 -----------------#
examine_session "$BASE_DIR/python/session1"

#----------------- Session 2 -----------------#
python3 "$BASE_DIR/python/session2/lab1_get_your_location.py"
if [ $? -ne 0 ]; then
    echo "[🟥] Session 2 is not Solved yet"
    exit 1
else
    examine_session "$BASE_DIR/python/session2"
fi

#----------------- Session 3 -----------------#
python3 "$BASE_DIR/python/session3/lab1_dictionary_problems.py"
if [ $? -ne 0 ]; then
    echo "[🟥] Session 3 is not solved yet"
else
    examine_session "$BASE_DIR/python/session3"
fi