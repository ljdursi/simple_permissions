#!/bin/bash
set -euo pipefail

readonly PORT=8180
readonly URL="http://localhost:${PORT}/v1/data/permissions"

readonly TOKENS="[\"faketoken\"]"
readonly SVC_TOKEN="fakeservicetoken"

curl -k "${URL}" -X POST \
    -H "Content-Type: application/json" -H "Accept: application/json" \
    -H "Authorization: Bearer ${SVC_TOKEN}" \
    -d "{\"method\": \"GET\", \"path\": [\"phenopackets\"], \"user_tokens\": ${TOKENS}}"
