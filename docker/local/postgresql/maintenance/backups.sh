#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

working_directory="$(dirname ${0})"

source "${working_directory}/_sourced/constants.sh"
source "${working_directory}/_sourced/messages.sh"

message_welcome "These are the backups you have got:"

ls -lht "${BACKUP_DIR_PATH}"
