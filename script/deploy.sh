#!/bin/bash
# By yongcong.wang @ 24/11/2019

set -e  # exit if err

# vars
HEXO_DIR=$(cd $(dirname $0); pwd)

# cmd
cd ${HEXO_DIR}
git add .
git commit -m "update src files"
git push origin hexo

