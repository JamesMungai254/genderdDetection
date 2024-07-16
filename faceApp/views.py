from django.shortcuts import render,redirect
from .forms import ImageForm
import cv2 as cv
import os
from .forms import ImageForm
from .models import Image
from django.conf import settings
import uuid
from datetime import datetime
from django.http import HttpResponse


# Create your views here.

def home(request): 
    return render(request, "main.html") 




def gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
                form.save()
                return redirect(openCVproc)
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})

def openCVproc(request):
                image_instance = Image.objects.last()  # Fetch the last uploaded image
                image_path = os.path.join(settings.MEDIA_ROOT, image_instance.img.name)
                genders = ["Male","Female"]
                # Create a directory for processed images if it doesn't exist
                processed_dir = os.path.join(settings.MEDIA_ROOT, 'processed')
                os.makedirs(processed_dir, exist_ok=True)
                #savedImg = './media/images/test.jpg'
                
                facedetect = cv.CascadeClassifier("./haarcascade_frontalface_default.xml")

                faceRecognizer = cv.face.LBPHFaceRecognizer_create()
                faceRecognizer.read("./faceTrained.yml")
                
                
                
                img = cv.imread(image_path)
                   

                # Load the image using OpenCV
                

                gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

                #detect the face of the image

                faceRect = facedetect.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
                for (x,y,w,h) in faceRect:
                    #grap face region of interest
                    faceROI= gray[y:y+h,x:x+w]
                    
                    label, confidenceValue = faceRecognizer.predict(faceROI)
                    print(f"Label = {genders[label]} with a confidence of {confidenceValue}")
                    cv.putText(img, str(genders[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255),thickness=2)
                    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0),thickness=2)
                filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.jpg"
                processed_image_path = os.path.join(processed_dir, filename)
                
                
                cv.imwrite(processed_image_path,img)
                
                # Save the path to the processed image in the database
                image_instance.processed_image = os.path.join('processed', filename)
                image_instance.save()
                processed_image_url = settings.MEDIA_URL + 'processed/' + image_instance.img.name
                #pred = cv.imshow("Detected Image",img)
                #cv.waitKey(0)
                processed_dir = os.path.join(settings.MEDIA_ROOT, 'processed')
                # Get the list of files in the processed directory
                files = os.listdir(processed_dir)
                # Filter out directories and get only files
                files = [f for f in files if os.path.isfile(os.path.join(processed_dir, f))]
                # Sort files by modification time (most recent first)
                files.sort(key=lambda x: os.path.getmtime(os.path.join(processed_dir, x)), reverse=True)
                if files:
                    # Construct the URL to the most recent processed image
                    recent_processed_image = os.path.join('processed', files[0])
                    recent_processed_image_url = os.path.join(settings.MEDIA_URL, recent_processed_image)
                    return render(request, 'prediction.html', {'recent_processed_image_url': recent_processed_image_url})
                else:
                    return HttpResponse('No processed images found.')

                
                
                
                
               # return render(request, 'prediction.html', {'processed_image_url': processed_image_url,'Prediction':pred})