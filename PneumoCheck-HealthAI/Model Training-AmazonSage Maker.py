#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install -q kaggle')


# In[7]:


get_ipython().system('mkdir ~/.kaggle')


# In[8]:


get_ipython().system('touch ~/.kaggle/kaggle.json')


# In[9]:


api_token = {"username":"idlisambar","key":"8f3b7fc4084e3c1c17f5b0a9ae3da84f"}


# In[10]:


import json

with open('/root/.kaggle/kaggle.json', 'w') as file:
    json.dump(api_token,file)


# In[11]:


get_ipython().system('chmod 600 ~/.kaggle/kaggle.json')


# In[5]:


get_ipython().system('kaggle datasets download -d paultimothymooney/chest-xray-pneumonia --force')


# In[ ]:


import zipfile
with zipfile.ZipFile('./chest-xray-pneumonia.zip','r') as zip_ref:
    zip_ref.extractall('./data')


# In[20]:


import glob
import random
import matplotlib.pyplot as plt

def get_random_image(dir,condition):
    placeholder=''
    if condition=='n':
        placeholder='NORMAL'
    elif condition=='p':
        placeholder='PNEUMONIA'
    else:
        raise Exception("Sorry,invalid condition")
    folder=f"./data/chest_xray/{dir}/{placeholder}/*.jpeg"
    img_paths=glob.glob(folder)
    max_length=len(img_paths)
    randomNumber=random.randint(0,max_length)
    
    for index,item in enumerate(img_paths,start=1):
        if index==randomNumber:
            print(index,item)
            image=plt.imread(item)
            readyImage=plt.imshow(image)
            return readyImage
        
        
        
    


# In[62]:


get_random_image("test","p")


# In[47]:


import glob
import matplotlib.pyplot as plt
from PIL import Image

folder='./data/chest_xray/train/*/*.jpeg'

counterPneu=0
counterNormal=0

img_paths=glob.glob(folder)

for i in img_paths:
    if "person" in i:
        full_size_image=Image.open(i)
        im=full_size_image.resize((224,224))
        plt.imsave(fname='./data/chest_xray/train' + '/train_pneumonia' + str(counterPneu) + '.jpeg',arr=im, format='jpeg', cmap='gray')
        counterPneu+=1
    else:
        full_size_image=Image.open(i)
        im=full_size_image.resize((224,224))
        plt.imsave(fname='./data/chest_xray/train' + '/train_normal' + str(counterNormal) + '.jpeg',arr=im, format='jpeg', cmap='gray')
        counterNormal+=1
        


# In[48]:


import glob
import matplotlib.pyplot as plt
from PIL import Image

folder='./data/chest_xray/test/*/*.jpeg'

counterPneu=0
counterNormal=0

img_paths=glob.glob(folder)

for i in img_paths:
    if "person" in i:
        full_size_image=Image.open(i)
        im=full_size_image.resize((224,224))
        plt.imsave(fname='./data/chest_xray/test' + '/test_pneumonia' + str(counterPneu) + '.jpeg', arr=im, format='jpeg', cmap='gray')
        counterPneu+=1
    else:
        full_size_image=Image.open(i)
        im=full_size_image.resize((224,224))
        plt.imsave(fname='./data/chest_xray/test' + '/test_normal' + str(counterNormal) + '.jpeg', arr=im, format='jpeg', cmap='gray')
        counterNormal+=1
        


# In[17]:


import glob
import matplotlib.pyplot as plt
from PIL import Image

folder='./data/chest_xray/val/*/*.jpeg'
counterPneu=0
counterNormal=0

img_paths=glob.glob(folder)

for i in img_paths:
    if "person" in i:
        full_size_image=Image.open(i)
        im=full_size_image.resize((224,224))
        plt.imsave(fname='./data/chest_xray/val' + '/val_pneumonia' + str(counterPneu) + '.jpeg', arr=im, format='jpeg', cmap='gray')
        counterPneu+=1
    else:
        full_size_image=Image.open(i)
        im=full_size_image.resize((224,224))
        plt.imsave(fname='./data/chest_xray/val' + '/val_normal' + str(counterNormal) + '.jpeg', arr=im, format='jpeg', cmap='gray')
        counterNormal+=1
        


# In[49]:


import glob
import pandas as pd

folder='./data/chest_xray/*/*/.jpeg'

category=[]
condition_of_lung=[]
filenames=[]

all_files=glob.glob(folder)

for filename in all_files:
    if "train" in filename:
        if "pneumonia" in filename:
            category.append("train")
            filenames.append(filename)
            condition_of_lung.append("pneumonia")
        elif "normal" in filename:
            category.append("train")
            filenames.append(filename)
            condition_of_lung.append("normal")
    elif "test" in filename:
        if "pneumonia" in filename:
            category.append("test")
            filenames.append(filename)
            condition_of_lung.append("pneumonia")
        elif "normal" in filename:
            category.append("test")
            filenames.append(filename)
            condition_of_lung.append("normal")
    elif "val" in filename:
        if "pneumonia" in filename:
            category.append("val")
            filenames.append(filename)
            condition_of_lung.append("pneumonia")
        elif "normal" in filename:
            category.append("val")
            filenames.append(filename)
            condition_of_lung.append("normal")
            
all_data_df=pd.DataFrame({"dataset type": category,"x-ray result":condition_of_lung,"filename":filenames})
print(all_data_df.head())


# In[52]:





# In[50]:


import glob
import pandas as pd
import os
train_folder='./data/chest_xray/train/*.jpeg'
train_df_lst=pd.DataFrame(columns=['labels','s3_path'],dtype=object)
train_imgs_path=glob.glob(train_folder)
counter=0
class_arg=''

for i in train_imgs_path:
    if "pneumonia" in i:
        class_arg=1
    else:
        class_arg=0
    train_df_lst.loc[counter]=[class_arg,os.path.basename(i)]
    counter+=1
print(train_df_lst.head())


# In[51]:


import glob
import pandas as pd
import os
test_folder='./data/chest_xray/test/*.jpeg'
test_df_lst=pd.DataFrame(columns=['labels','s3_path'],dtype=object)
test_imgs_path=glob.glob(test_folder)
counter=0
class_arg=''

for i in test_imgs_path:
    if "pneumonia" in i:
        class_arg=1
    else:
        class_arg=0
    test_df_lst.loc[counter]=[class_arg,os.path.basename(i)]
    counter+=1
print(test_df_lst.head())


# In[52]:


def save_to_lst(df,prefix):
    return df[["labels","s3_path"]].to_csv(
    f"{prefix}.lst", sep='\t',index=True,header=False
    )

save_to_lst(train_df_lst.copy(),"train")
save_to_lst(test_df_lst.copy(),"test")


# In[53]:


bucket='pneumo-check-chest-xray'
print("bucket:{}".format(bucket))
region='us-east-1'
print("region:{}".format(region))
roleArn='arn:aws:s3:::pneumo-check-chest-xray'
print("roleArn:{}".format(roleArn))


# In[54]:


import os

os.environ["DEFAULT_S3_BUCKET"]=bucket


# In[69]:


get_ipython().system('aws s3 sync ./data/chest_xray/train s3://${DEFAULT_S3_BUCKET}/train/')


# In[70]:


get_ipython().system('aws s3 sync ./data/chest_xray/test s3://${DEFAULT_S3_BUCKET}/test/')


# In[55]:


import boto3

boto3.Session().resource('s3').Bucket(bucket).Object("train.lst").upload_file('./train.lst')


# In[56]:


boto3.Session().resource('s3').Bucket(bucket).Object("test.lst").upload_file('./test.lst')


# In[57]:


import sagemaker
from sagemaker import image_uris
import boto3
from sagemaker import get_execution_role
sess=sagemaker.Session()

algorithm_image=image_uris.retrieve(
    region=boto3.Session().region_name,
    framework="image-classification"
)

s3_output_location=f"s3://{bucket}/models/image_model"
print(algorithm_image)


# In[58]:


role=get_execution_role()
print(role)


# In[59]:


import sagemaker
img_classifier_model=sagemaker.estimator.Estimator(
    algorithm_image,
    role=role,
    instance_count=1,
    instance_type="ml.p2.xlarge",
    volume_size=50,
    max_run=432000,
    input_mode="File",
    output_path=s3_output_location,
    sagemaker_session=sess
)
print(img_classifier_model)


# In[60]:


import glob 
count=0

for filepath in glob.glob('./data/chest_xray/train/*.jpeg'):
    count+=1
print(count)


# In[61]:


img_classifier_model.set_hyperparameters(
image_shape='3,224,224',
num_classes=2,
use_pretrained_model=1,
num_training_samples=count,
augmentation_type='crop_color_transform',
epochs=15,
early_stopping=True,
early_stopping_min_epochs=8,
early_stopping_tolerance=0.0,
early_stopping_patience=5,
lr_scheduler_factor=0.1,
lr_scheduler_step='8,10,12')


# In[62]:


from sagemaker.tuner import CategoricalParameter,ContinuousParameter,HyperparameterTuner

hyperparameter_ranges={
    "learning_rate":ContinuousParameter(0.01,0.1),
    "mini_batch_size":CategoricalParameter([8,16,32]),
    "optimizer":CategoricalParameter(["sgd","adam"])
}


# In[63]:


objective_metric_name="validation:accuracy"
objective_type="Maximize"
max_jobs=5
max_parallel_jobs=1


# In[64]:


tuner=HyperparameterTuner(estimator=img_classifier_model,
                         objective_metric_name=objective_metric_name,
                         hyperparameter_ranges=hyperparameter_ranges,
                         objective_type=objective_type,
                         max_jobs=max_jobs,
                         max_parallel_jobs=max_parallel_jobs  
                         )


# In[65]:


from sagemaker.session import TrainingInput

model_inputs={
    "train":sagemaker.inputs.TrainingInput(s3_data=f"s3://{bucket}/train/",content_type="application/x-image"),
    "validation":sagemaker.inputs.TrainingInput(s3_data=f"s3://{bucket}/test/",content_type="application/x-image"),
    "train_lst":sagemaker.inputs.TrainingInput(s3_data=f"s3://{bucket}/train.lst",content_type="application/x-image"),
    "validation_lst":sagemaker.inputs.TrainingInput(s3_data=f"s3://{bucket}/test.lst",content_type="application/x-image"),
}


# In[66]:


import time 
job_name_prefix="classifier"
timestamp=time.strftime("-%Y-%m-%d-%H-%M-%S",time.gmtime())
job_name=job_name_prefix+timestamp


# In[67]:


tuner.fit(inputs=model_inputs,job_name=job_name,logs=True)


# In[68]:


import sagemaker
from sagemaker import get_execution_role


# In[69]:


role=get_execution_role()


# In[81]:


model=sagemaker.model.Model(
image_uri=algorithm_image,
model_data='s3://pneumo-check-chest-xray/model.tar.gz',
role=role)


# In[80]:


endpoint_name='image-classification-2022-05-19-09-45-35-731'

deployment=model.deploy(
initial_instance_count=1,
instance_type='ml.m4.xlarge',
endpoint_name=endpoint_name)


# In[82]:


from sagemaker.predictor import Predictor
predictor=Predictor("image-classification-2022-05-19-09-45-35-731")


# In[83]:


from sagemaker.serializers import IdentitySerializer
import base64

file_name='data/chest_xray/val/val_pneumonia0.jpeg'

predictor.serializer= IdentitySerializer("image/jpeg")
with open(file_name,"rb")as f:
    payload=f.read()
    
inference=predictor.predict(data=payload)
print(inference)


# In[84]:


print(inference[1])


# In[20]:


import glob
import json
import numpy as np
file_path='data/chest_xray/val/*.jpeg'
files=glob.glob(file_path)

y_true=[]
y_pred=[]

def make_pred():
    for file in files:
        if "normal" in file:
            with open(file,"rb") as f:
                payload=f.read()
                inference=predictor.predict(data=payload).decode("utf-8")
                result=json.loads(inference)
                predicted_class=np.argmax(result)
                y_true.append(0)
                y_pred.append(predicted_class)
        elif "pneumonia" in file:
            with open(file,"rb") as f:
                payload=f.read()
                inference=predictor.predict(data=payload).decode("utf-8")
                result=json.loads(inference)
                predicted_class=np.argmax(result)
                y_true.append(1)
                y_pred.append(predicted_class)

make_pred()
print(y_true)
print(y_pred)


# In[45]:


from sklearn.metrics import confusion_matrix

confusion_matrix(y_true,y_pred)


# In[21]:


from sklearn.metrics import classification_report
print(classification_report(y_true,y_pred))


# In[ ]:




