# Use the official Jenkins LTS (Long-Term Support) image from Docker Hub
FROM jenkins/jenkins:lts

# Skip the Jenkins setup wizard by setting the environment variable
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Copy plugin list to the container (optional)
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Copy initial Groovy scripts (optional)
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/

# Set Jenkins executors (optional)
COPY executors.groovy /usr/share/jenkins/ref/

# If you have custom configurations or additional setup scripts, you can copy them here

