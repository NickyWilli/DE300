# HW2 Readme file

To run the code user needs to first create a docker container for a jupyter notebook. The following steps were taken:

- Connect to EC2 instance, open github repo, navigate to homework 2 folder
- vim Dockerfile
- sudo chmod 666 /var/run/docker.sock
- docker build -t homework_2 .
- docker run -p 8888:8888 -v ~/.aws:/home/jovyan/.aws -v ~/Nicky_Williams_DE300/homework_2:/home/jovyan/work homework_2
- then open http://127.0.0.1:8888/lab in browser and open notebook to edit the ipynb

1. Install required packages (cassandra, etc. if not already on computer) - in the code as well
2. Running the code will automatically unzip the dataset and load the required CSVs into DuckDB tables (make sure zipped filed is uploaded to computer)
3. Run the cells one at a time in order provided
4. Expected outputs are provided in the pdf with written analysis. Each part 1 question provides the table and graph to support the answers provided. Each part 2 question prints a cassandra table that matches the output from the part 1 questions.

  
