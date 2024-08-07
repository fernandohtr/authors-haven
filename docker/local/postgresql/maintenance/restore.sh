#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

working_directory="$(dirname ${0})"

source "${working_directory}/_sourced/constants.sh"
source "${working_directory}/_sourced/messages.sh"

if [[ -z ${1+x} ]]; then
    message_error "Backup filename is not specified yet it's a required parameter. Make sure you provide one and try again."
    exit 1
fi

backup_filename="${BACKUP_DIR_PATH}/${1}"

if [[ ! -f "${backup_filename}" ]]; then
    message_error "No backup with the specified backup filename was found. Chack out the 'backups' maintenance script output to see if there in one and try again"
    exit 1
fi

message_welcome "Restoring the '${POSTGRES_DB}' database from the '${backup_filename}' backup..."

if [[ "${POSTGRES_USER}" == "postgres" ]]; then
    message_error "Restoring as 'postgres' user is not allowed. Assign 'POSTGRES_USER' env with another one and try again."
    exit 1
fi

export PGHOST="${POSTGRES_HOST}"
export PGPORT="${POSTGRES_PORT}"
export PGUSER="${POSTGRES_USER}"
export PGPASSWORD="${POSTGRES_PASSWORD}"
export PGDATABASE="${POSTGRES_DB}"

message_info "Dropping the database..."

dropdb "${PGDATABASE}"

message_info "Creating a new database..."

createdb --owner="${POSTGRES_USER}"

gunzip -c "${backup_filename}" | psql "${POSTGRES_DB}"

message_success "The '${POSTGRES_DB}' database has been restored successfully from the '${backup_filename}' backup."