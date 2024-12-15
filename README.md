

# MACHINE LEARNING PROJECT 2

In this project, I will work with the Bank Marketing dataset to run the model. Using Azure Machine Learning Studio, I will deploy the model. I will create and publish a pipeline. This project shows my skills in using AutoML, deploying the best model, enabling logging for monitoring, creating Swagger documentation for APIs, and consuming model endpoints effectively. I have already deploy the endpoint and run it already.

## Architectural Diagram

![image](https://github.com/user-attachments/assets/b60dd01d-e729-44eb-ab15-451972dcab7e)


## Key Steps




### 1. AutoML process
1.1 Dataset upload to Azure Machine Learning Studio

![image](https://github.com/user-attachments/assets/5ab9e360-bfb1-4fff-bfdd-b9fd4f8478d6)


1.2 Compute cluster resource is available

![image](https://github.com/user-attachments/assets/d469e73c-819a-4e32-905b-d10dd765719a)


1.3 Experiment submit

![image](https://github.com/user-attachments/assets/afe88900-c098-4577-8b83-66089e530761)


### 2. Deploy the best model
2.1 The best model deployment is Voting Ensemble
- The best model is Voting Ensemble
- The accuracy is around 95%
- The model is already registered and deployed.

![image](https://github.com/user-attachments/assets/0220ead2-3a6d-4c2e-ab07-b618910ec698)



2.2 The application Insights is enable 
- The deployment status is healthy
![image](https://github.com/user-attachments/assets/eceaa482-a6e4-4fc4-b20f-5826459913cb)

- The application insights is enable
![image](https://github.com/user-attachments/assets/6ac0b6c1-8454-4635-a894-a8812ecfe910)


Run the logs.py

![image](https://github.com/user-attachments/assets/ac726032-ab6e-4760-9240-86a69c2ae003)



### 3. Consume endpoint
3.1 Swagger documentation

Run the swagger as screen below

![image](https://github.com/user-attachments/assets/acfd0580-239d-4292-97a0-7f2385c52511)



3.2 Classification Result

![image](https://github.com/user-attachments/assets/f84e21ae-3a65-4fbd-84d3-16965bff26a9)


### 4. Publish the pipelines
   
4.1 Pipeline created

![image](https://github.com/user-attachments/assets/8e60081a-bfa0-4568-9175-7295c4fd770d)


4.2 Pipeline endpoint

![image](https://github.com/user-attachments/assets/81e18bef-2a47-4e96-95e7-fc0357584edd)


4.3 The Bankmarketing dataset with the AutoML module

![image](https://github.com/user-attachments/assets/c977c221-cb05-4890-8853-8f8cfad127ab)


4.4 Public pipeline

![image](https://github.com/user-attachments/assets/afcdfd9c-0d67-4e65-b2f9-7596daa50949)


4.5 Pipeline run in notebook

![image](https://github.com/user-attachments/assets/80b45832-f16c-4d88-b6ed-3aca5ff6e286)



## Standout Suggestions
- Test a local container with a downloaded model: Run machine learning model in a local container to ensure it works correctly before production.
- Export model to support ONNX: Convert model to ONNX format for compatibility across various platforms and tools.


## Screen Recording
Please select quality 720p for better quality
https://youtu.be/f8VjPFDr2CM
