#!/bin/bash

case "$1" in
    structure)
        find . -not -path '*/.*' -not -path './node_modules*'
        ;;
        
    build_generator)
        docker build -t hw_generator ./generator
        ;;
        
    create_local_data)
        mkdir -p local_data
        python3 generator/generate.py local_data
        ;;

    run_generator)
        mkdir -p data
        docker run --rm -v "/$(pwd)/data:/data" hw_generator
        ;;
    build_reporter)
        docker build -t hw_reporter ./reporter
        ;;

    run_reporter)
        docker run --rm -v "/$(pwd)/data:/data" hw_reporter
        ;;
    clear_data)
        rm -f data/*.csv data/*.html
        ;;

   inside_generator)
        docker run --rm -v "/$(pwd)/data:/data" hw_generator ls -la //data
        ;;

    inside_reporter)
        docker run --rm -v "/$(pwd)/data:/data" hw_reporter ls -la //data
        ;;
esac