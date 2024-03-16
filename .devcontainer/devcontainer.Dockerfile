FROM mcr.microsoft.com/devcontainers/base:bookworm

USER vscode

# Install Go
ENV GOTOOLCHAIN=local
ENV GOPATH /home/vscode/go
ENV PATH $GOPATH/bin:/home/vscode/.local/go/bin:$PATH
COPY --from=golang:bookworm --chown=vscode:vscode /usr/local/go /home/vscode/.local
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin"

# Install nvm
RUN <<EOF
export PROFILE=/dev/null
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
cat <<EOS | tee --append /home/vscode/.bashrc /home/vscode/.zshrc
export NVM_DIR="\$HOME/.nvm"
[ -s "\$NVM_DIR/nvm.sh" ] && \. "\$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "\$NVM_DIR/bash_completion" ] && \. "\$NVM_DIR/bash_completion"  # This loads nvm bash_completion
EOS
EOF

# Install yq
COPY --from=mikefarah/yq /usr/bin/yq /home/vscode/.local/bin/yq

# Install jq
RUN <<EOF
sudo apt-get update
export DEBIAN_FRONTEND=noninteractive
sudo apt-get -y install --no-install-recommends jq
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*
EOF
