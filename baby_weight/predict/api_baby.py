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

from googleapiclient        import discovery
from oauth2client.client    import GoogleCredentials
from google.appengine.api   import app_identity


credentials   = GoogleCredentials.get_application_default()
api           = discovery.build("ml", "v1", credentials=credentials)
project       = app_identity.get_application_id()
model_name    = 'babyweight'
model_version = 'dec_30'



#model_h5_path = path.join(settings.STATICFILES_DIRS[0], 'predict', 'baby.h5')
#model_h5_path = 'gs://aat-ai-models/babyweight/20201229152705'
#h5_model      = load_model( model_h5_path )

def get_weight_old( j_input ):
    try:
        tf_dic        = {name: [value] for name, value in j_input.items()}

        parent        = "projects/{0}/models/{1}/versions/{2}".format(
            project, model_name, model_version)

        predictions   = api.projects().predict( body = tf_dic, name=parent ).execute()

        weight_pounds = predictions[0][0]
        weight_kilos  = weight_pounds * 0.45359237

        result        = {
                            'weight_pounds' : weight_pounds,
                            'weight_kilos'  : weight_kilos
                        }

        return result

    except Exception as e:
        print( 'predict.api_baby.get_weight(), error:  {}'.format( e ) )
        raise


'''def get_weight_old( j_input ):
    try:
        tf_dic        = {name: tf.convert_to_tensor([value]) for name, value in j_input.items()}
        predictions   = h5_model.predict( tf_dic )
        weight_pounds = predictions[0][0]
        weight_kilos  = weight_pounds * 0.45359237

        result        = {
                            'weight_pounds' : predictions[0][0],
                            'weight_kilos'  : weight_pounds * 0.45359237
                        }

        return result

    except Exception as e:
        print( 'predict.api_baby.get_weight(), error:  {}'.format( e ) )
        raise'''