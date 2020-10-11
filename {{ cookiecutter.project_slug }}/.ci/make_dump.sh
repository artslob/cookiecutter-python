#!/usr/bin/env bash

# exit immediately if a any command exits with a non-zero status
set -e

METHOD="$1"
URL="${{ cookiecutter.project_slug.upper() }}_TEST_DB_URL"

if [[ -z ${URL} ]]; then
    echo "ERROR: {{ cookiecutter.project_slug.upper() }}_TEST_DB_URL variable is empty. Export like this:" >&2
    exit 1
fi

# full directory name of the script no matter where it is being called from
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
DIR="${DIR%/}"

python3 "${DIR}/upgrade_db.py" --method "$METHOD" >&2
pg_dump "$URL" -s --no-owner | sed '/^--/d' | python "${DIR}/sort_dump.py"
