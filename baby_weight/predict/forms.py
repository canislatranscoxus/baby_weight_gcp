from django         import forms
from django.core    import validators


class PredictForm( forms.Form ):

    IS_MALE         = [ ( 'False', 'girl'  ), ( 'True', 'boy' ), ( 'Unknown', 'unknown' )  ]
    PLURALITY       = [ ( '1', 'Single(1)' )
            , ( '2', 'Twins(2)'       )
            , ( '3', 'Triplets(3)'    )
            , ( '4', 'Quadruplets(4)' )
            , ( '5', 'Quintuplets(5)' )
            , ( '2+', 'Multiple(2+)'  ) ]

    is_male         = forms.CharField( widget = forms.Select( choices = IS_MALE   ) )
    mother_age      = forms.FloatField( min_value= 12 )

    plurality       = forms.CharField( widget = forms.Select( choices = PLURALITY ) )
    #plurality = forms.CharField( )

    gestation_weeks = forms.IntegerField( min_value= 0,max_value= 45  )

    #weight_pounds   = forms.FloatField( min_value= 0.0, max_value= 10.0 )

    def clean(self):
        user_cleaned_data = super().clean()




