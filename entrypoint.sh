#!/usr/bin/env bash
# entrypoint.sh


set -e

cd app/ 

function main() {



    if [[ $# -eq 0 ]]; then
        
        export dir="-d=."
        export lang="-l=python" 

    else
        
        export dir="${1}" 
        export lang="${2}" 

    fi
}

main "$@"

python3 sast.py $dir $lang


