FROM debian:trixie as base

FROM base AS dev

CMD ["bash"]

RUN apt update \
    && DEBIAN_FRONTEND=noninteractive apt install -y \
    sudo \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# add dev user
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && usermod -aG users $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN chmod 777 /mnt
RUN mkdir -p /usr/local/history && chmod 777 /usr/local/history
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

USER $USERNAME

# https://code.visualstudio.com/remote/advancedcontainers/avoid-extension-reinstalls
RUN mkdir -p /home/$USERNAME/.vscode-server/extensions
