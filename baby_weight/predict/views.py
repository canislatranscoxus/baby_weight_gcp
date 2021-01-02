from django.shortcuts import render
from . import forms
import random
from . import api_baby

# Create your views here.



def predict( request ):

    print( 'app predict, views.py predict(), ... begin' )

    form          = forms.PredictForm( initial=
                    {
                        'mother_age'      : 18,
                        'gestation_weeks' : 1
                    } )
    dic           = {}
    #weight_kilos  = random.randrange( 0, 5 ) + random.random()
    #weight_pounds = weight_kilos * 2.2046
    #print('weight_kilos    : {}'.format( weight_kilos  ))
    #print('weight_pounds   : {}'.format( weight_pounds ))

    if request.method=='POST':
        form = forms.PredictForm( request.POST )
        if form.is_valid():
            print( 'form is valid' )
            print( 'is_male         : {}'.format( form.cleaned_data[ 'is_male'          ] ) )
            print( 'mother_age      : {}'.format( form.cleaned_data[ 'mother_age'       ] ) )
            print( 'plurality       : {}'.format( form.cleaned_data[ 'plurality'        ] ) )
            print( 'gestation_weeks : {}'.format( form.cleaned_data[ 'gestation_weeks'  ] ) )

            print('t- is_male         : {}'.format( type( form.cleaned_data['is_male'] )) )
            print('t- mother_age      : {}'.format( type( form.cleaned_data['mother_age'] )))
            print('t- plurality       : {}'.format( type( form.cleaned_data['plurality'] )))

            # prepare input data for prediction
            input_data = {
                        'key'            : 'kid1',
                        'is_male'        : form.cleaned_data[ 'is_male'          ],
                        'mother_age'     : form.cleaned_data[ 'mother_age'       ],
                        'plurality'      : form.cleaned_data[ 'plurality'        ],
                        'gestation_weeks': form.cleaned_data[ 'gestation_weeks'  ]
                    }

            # make prediction
            prediction = api_baby.get_weight( input_data )

            # extract results
            weight_pounds         = prediction[ 'weight_pounds' ]
            weight_kilos          = prediction[ 'weight_kilos' ]
            dic[ 'weight_kilos' ] = '{:.2f}'.format(weight_kilos)
            dic[ 'weight_pounds'] = '{:.2f}'.format(weight_pounds)

    dic[ 'form' ] = form
    print( 'app predict, views.py predict(), ... end' )

    return render( request, 'predict/gui/predict.html', dic )
