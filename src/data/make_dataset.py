import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from kafka import KafkaConsumer
import pandas as pd
import os
from src.features import build_features as bf
from src.models import predict_model as pm

''' before running this you have to setup Kafka from Kafka setup folder run docker_script.sh and wait...'''

full_rows = []
# load the model to make prediction
#model = pm.load_model('../../models/model.pkl')
model = pm.load_model('E:\Resources\MY Resources\Assignment 2\Assignment 2 (Solution)\Part 2\Code\models\model.pkl')
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data') 
    
    ## get data from kafka server
    consumer = KafkaConsumer('ml-raw-dns', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    
    for index,URL in enumerate(consumer):
        # decode the URL to utf-8
        url = URL.value.decode('utf-8')
        # call build_feature_df to generate 14 features from the url 
        row = bf.build_feature_df(url)
        # drop the 2 columns which dropped in model training phase
        dropped_row = row.drop(['longest_word', 'sld'], axis=1)
        # use the saved model to predict labels and confidence score
        label, confidence = pm.predict(dropped_row, model)
        # logging the events in CMD
        logger.info('predict row ' + str(index) + ' label= ' + str(label) + ' confidence= ' + str(confidence))
        row.insert(0, 'url', url)
        row['predicted_label'] = label
        row['score'] = confidence
        full_rows.append(row)
        # to stop after 100000 iteration
        if index == 99999:
            break
    full_df = pd.concat(full_rows)
    logger.info('saving final data frame to data/processed')
    full_df.to_csv('../../data/processed/final_data.csv', index= False)

    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
