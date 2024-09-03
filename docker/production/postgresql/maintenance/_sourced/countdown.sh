#!/bin/bash

countdown() {
    declare description="A simple countdown."

    local seconds="${1}"

    local duration=$(($(date +%s) + "${seconds}"))

    while [ "$d" -ge `date +%s` ]; do

        echo -ne "$(date -U --date @(($d - `date +%s`)) +%H:%M:%S)\r";

        sleep 0.1
    done
}
