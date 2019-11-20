FROM gitpod/workspace-full

RUN sudo apt-get update \
 && sudo rm -rf /var/lib/apt/lists/* \
 && alias python='/usr/bin/python3' \
 && npm install -g now \
 && python3 -m pip install --user virtualenv \
 && pip3 install pytest flask.testing flask


