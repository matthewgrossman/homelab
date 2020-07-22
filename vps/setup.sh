#!/usr/bin/env bash

# setup bash_profile
source "$HOME/lab/vps/bash_profile"
ln -s "$HOME/lab/vps/bash_profile" "$HOME/.bash_profile"

# unencrypt ssh keys from pass
pass vps/id_rsa > "$HOME/.ssh/id_rsa"
pass vps/id_rsa.pub > "$HOME/.ssh/id_rsa.pub"

# now that we have our ssh keys, modify lab repo to use ssh instead of https
git -C "$HOME/lab" remote set-url "$GITHUB_SSH_URL"
