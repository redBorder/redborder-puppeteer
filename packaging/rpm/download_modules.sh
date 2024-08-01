#!/bin/bash

PUPPETEER_VERSION=${PUPPETEER_VERSION:="19.5.2"}
CHROMIUM_REVISION=${CHROMIUM_REVISION:="1069273"}

mkdir -p SOURCES

if ! command -v npm &> /dev/null; then
    echo "npm not found, installing..."
    curl -sL https://rpm.nodesource.com/setup_16.x | bash -
    yum install -y nodejs
fi

TEMP_DIR=$(mktemp -d)
pushd $TEMP_DIR
npm init -y
npm install puppeteer@${PUPPETEER_VERSION}
tar -czvf puppeteer-${PUPPETEER_VERSION}.tar.gz ./*
popd
mv $TEMP_DIR/puppeteer-${PUPPETEER_VERSION}.tar.gz SOURCES/
rm -rf $TEMP_DIR

CHROMIUM_URL="https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/${CHROMIUM_REVISION}/chrome-linux.zip"
[ ! -f SOURCES/chrome-linux-${CHROMIUM_REVISION}.zip ] && wget --no-check-certificate ${CHROMIUM_URL} -O SOURCES/chrome-linux-${CHROMIUM_REVISION}.zip

exit 0