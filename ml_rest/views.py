from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle

# Create your views here.

@api_view(['GET'])
def overview(request):
    data = "Url is /predict",{
        "comments":"একটা প্রিমিয়াম ফিল আসে।",
        "Predict": "Positive"
    },{
        "comments" : "কিভাবে ব্যবহার করে সেটাই বুঝতে পারলাম না",
        "Predict": "Negative"
    }
    return Response(data)


#Predict Function
@api_view(["POST"])
def predict(request):
    try:
        comments =  request.data.get('comments',None)
        fields = [comments]
        
        if not None in fields:
            data = str(comments)
            filename = 'ml_model/a_model.pkl'
            avocado_model = pickle.load(open(filename,'rb'))
            prediction = avocado_model.predict([data])
            if prediction == 0:
                prediction = 'Negative'
            else:
                prediction = 'Positive'

            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction,
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }

    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)