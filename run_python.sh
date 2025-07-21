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
examine_session "session2"

#----------------- Session 3 -----------------#
examine_session "session3"