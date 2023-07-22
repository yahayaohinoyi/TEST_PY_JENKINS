# Use the official Jenkins LTS image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install system packages
USER root

# Install Python and pip
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pytest

# Switch back to the Jenkins user
USER jenkins

# If you have other custom configurations or plugins to install, you can add them here

