# Multi-ttach
Multi-ttach: Adhesion Structure for Multimaterial FDM printing

Updated with Docker. Do this:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone this repository
3. Open a console and run these commands in the directory you cloned into:
    ```
    docker build -t multittach .
    docker run -p 8080:5000 multittach
    ```
4. Now open a web browser to http://localhost:8080 .
