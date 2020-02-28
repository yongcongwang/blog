#!/bin/bash
# By yongcong.wang @ 27/02/2020
set -x
set -e

# env
REPO_DIR="$(cd $(dirname $0); pwd)/.."
echo "Repo dir is ${REPO_DIR}"

# nodejs
curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs

# hexo
npm install -g hexo-cli

# theme
THEME_NEXT_DIR=${REPO_DIR}/themes/next
git clone https://github.com/theme-next/hexo-theme-next ${REPO_DIR}/themes/next
mv ${THEME_NEXT_DIR}/_config.yml ${THEME_NEXT_DIR}/_config.ym.bk
ln -s ${REPO_DIR}/themes/_config.yml ${THEME_NEXT_DIR}/_config.yml
cp ${REPO_DIR}/source/images/websie/* ${THEME_NEXT_DIR}/source/images/
