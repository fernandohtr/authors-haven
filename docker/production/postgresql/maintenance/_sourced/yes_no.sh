#!/bin/bash

yes_no() {
    declare description="Prompt for confirmation. \$\"\{1\}\": confimation message"

    local argument1="${1}"

    local response=read -r -p "${argument1} (y/[n])? " response

    if [[ "${response}" =~ ^[Yy]$ ]]
    then
        exit 0
    else
        exit 1
    fi
}
