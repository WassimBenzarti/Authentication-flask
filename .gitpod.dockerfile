FROM gitpod/workspace-full

RUN sudo apt-get update \
 && sudo rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 1