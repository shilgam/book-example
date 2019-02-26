#!/bin/sh
set -e

# Wait for services to be started
dockerize -wait http://selenoid:4444/ping \
          -wait http://selenoid-ui:8080 \
          -timeout 20s

exec "$@"
