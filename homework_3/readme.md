To run the code user needs to first create a docker container for a jupyter notebook. The following steps were taken:

1. Connect to EC2 instance, open github repo, navigate to homework 3 folder

2. vim Dockerfile

3. sudo chmod 666 /var/run/docker.sock

4. docker build -t homework_3 .

5. docker run -p 8888:8888 -v $(pwd):home/jovyan/.aws -v ~/Nicky_Williams_DE300/homework_3:/home/jovyan/work homework_3

6. then open http://127.0.0.1:8888/lab in browser and open notebook to edit the ipynb

7. Install required packages - in the code as well

8. Running the code will automatically load requirements as needed

9. Run the cells one at a time in order provided

10. Expected outputs:

- Part 1 task 3: A table displaying the first five rows with 2 cols (doc_id, tfidf)
- Part 2 task 3: Loss from loss_SVM(): 0.999775
- Part 2 task 4: Top 10 predictions running the loss function on the dataset --> First 10 predictions:
[-1, -1, -1, 1, -1, 1, -1, -1, 1, -1]


