FROM openjdk:7u91-jre-alpine
WORKDIR /opt
RUN apk add --no-cache git
RUN git clone https://github.com/irsdl/IIS-ShortName-Scanner --depth 1
WORKDIR /qemuno
ENTRYPOINT ["java", "-jar", "/opt/IIS-ShortName-Scanner/iis_shortname_scanner.jar"] 
