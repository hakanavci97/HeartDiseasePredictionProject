from re import X
from django.shortcuts import render
from django.http import HttpResponse
import pickle 
# Create your views here.

def homePage(request):
    return render(request, "homePage/homePage.html")
    
def loading(request):
    return render(request, "partials/loading.html")


def bmiResult(request):
    tall = float(request.GET['tall'])/100 #if type(request.GET['tall'])=='int' else float(request.GET['tall'])
    weight = float(request.GET['weight'])
    result=weight/(tall*tall)
    return render(request, "homePage/homePage.html", {'result':"{:.2f}".format(result)})


def HeartDiseasePredictionResult(request):
    gender = int(request.GET['gender'])
    bmi = int(request.GET['bmi'])
    smoker = int(request.GET['smoker'])
    alcoholDrinking = int(request.GET['alcoholDrinking'])
    stroke = int(request.GET['stroke'])
    physicalHealth = int(request.GET['physicalHealth'])
    mentalHealth = int(request.GET['mentalHealth'])
    diffWalking = int(request.GET['diffWalking'])
    ageCategory = int(request.GET['ageCategory'])
    race = int(request.GET['race'])
    diabetic = int(request.GET['diabetic'])
    physicalActivity = int(request.GET['physicalActivity'])
    genHealth = int(request.GET['genHealth'])
    sleepTime = int(request.GET['sleepTime'])
    asthma = int(request.GET['asthma'])
    kidneyDisease = int(request.GET['kidneyDisease'])
    skinCancer = int(request.GET['skinCancer'])

    PersonalHealthAnswers=[bmi,smoker,alcoholDrinking,stroke,physicalHealth,mentalHealth,
    diffWalking,gender,ageCategory,race,diabetic,genHealth,physicalActivity,sleepTime,asthma,kidneyDisease,skinCancer]
    
    standardScaler=pickle.load(open('standardScaler','rb'))

    x=standardScaler.transform([PersonalHealthAnswers])
    model = pickle.load(open('heartDiseasePredictionLogisticRegression.Model','rb'))
    prediction=model.predict(x)
    pedictionRatio=model.predict_proba(x)
    if prediction[0]==0:
         result = "Kalp Hastası Değil! Risk Oranı:"+str(round(pedictionRatio[0][1] * 100, 2 ))+"%"
       # result= 'Kalp Hastası Değil, Risk Oranı:' +str(round(pedictionRatio[0][1] * 100, 2 ))+"%"
    else:
        result= 'Kalp Hastası! Risk Oranı:' +str(round(pedictionRatio[0][1] * 100, 2 ))+"%"

    return render(request, "homePage/homePage.html", {'HeartDiseasePredictionResult':result})




