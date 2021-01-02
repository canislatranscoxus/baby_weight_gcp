'''
This library consume the classifier model from the static folder.
We load the model from file, then we make predictions.
This is just a demo to test a tensorflow model.

For production environment, we must deploy the model to cloud exposing an api url and
have another script that consume the model using that url.



references:
https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive/06_structured/3_keras_dnn.ipynb

'''


from baby_weight import settings
from os import path
import os
#import tensorflow as tf
#from tensorflow.keras.models import load_model

import googleapiclient
from googleapiclient        import discovery
from oauth2client.client    import GoogleCredentials
#from google.appengine.api   import app_identity


from google.api_core.client_options import ClientOptions


credentials   = GoogleCredentials.get_application_default()
api           = discovery.build("ml", "v1", credentials=credentials)
project       = 'my_project_here'
region        = 'us-east1'
model_name    = 'babyweight'
model_version = 'dec_30'

# Create the ML Engine service object.
# To authenticate set the environment variable
# GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
prefix = "{}-ml".format(region) if region else "ml"
api_endpoint = "https://{}.googleapis.com".format(prefix)
client_options = ClientOptions(api_endpoint=api_endpoint)
service = googleapiclient.discovery.build( 'ml', 'v1', client_options=client_options)
name = 'projects/{}/models/{}'.format(project, model_name)


def get_weight( instances ):
    try:
        #instances      = {name: [value] for name, value in instances.items()}

        #parent        = "projects/{0}/models/{1}/versions/{2}".format(project, model_name, model_version)
        #predictions   = api.projects().predict( body = instances, name=parent ).execute()

        response = service.projects().predict(
            name=name,
            body={'instances': [ instances ] }
            #body= tf_dic
        ).execute()

        # response = {'predictions': [{'babyweight': [-1.84530771], 'key': 'kid1'}]}

        weight_pounds = response[ 'predictions' ] [0] ['babyweight' ][0]
        weight_kilos  = weight_pounds * 0.45359237

        result        = {
                            'weight_pounds' : weight_pounds,
                            'weight_kilos'  : weight_kilos
                        }

        return result

    except Exception as e:
        print( 'predict.api_baby.get_weight(), error:  {}'.format( e ) )
        raise

