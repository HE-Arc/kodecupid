FROM debian:latest

ARG user_name
ARG user_id
ARG grp_id

RUN apt-get update
RUN apt-get install -y \
  lsb-release \
  ca-certificates \
  apt-transport-https \
  software-properties-common \
  gnupg2 \
  sudo 

RUN apt-get update
RUN apt-get install -y \
  curl

RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && apt-get install -y nodejs

# create user
# RUN echo "${DOCKER_USER}:x:${DOCKER_USER_ID}:${DOCKER_GRP_ID}:${DOCKER_USER}:/tmp:/bin/bash" >> /etc/passwd

RUN groupadd -g "$grp_id" "$user_name" \
    && useradd -u "$user_id" -g "$grp_id" --shell /bin/bash --create-home "$user_name"

# Add the user to the sudo group
# RUN usermod -aG sudo "$user_name"

# Allow passwordless sudo for the user
# RUN echo "$user_name ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/"$user_name"

USER "$user_name"

COPY ./startup.sh /home/user/startup.sh
ENTRYPOINT ["/home/user/startup.sh"]