#!/usr/bin/env bash

export GITHUB_SSH_URL="git@github.com:matthewgrossman/lab.git"
export PASSWORD_STORE_DIR="$HOME/lab/secrets"

whereip () {
    curl ipinfo.io
}

NODE_BASH_PROFILE="$HOME/node_bash_profile"
if [ -f "$NODE_BASH_PROFILE" ]; then
    . "$NODE_BASH_PROFILE"
fi
