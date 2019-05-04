# Puppeteer

1. run with debug mode locally:

        npm run test --recursive ./integration-tests -- --debugMode


1. run with debug mode inside docker container:

        docker-compose run --rm tests sh -c "mocha --recursive ./integration-tests -- --debugMode"
