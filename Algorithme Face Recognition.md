##ALGORITHME ‘FACE RECOGNITION’

Le code suivant est utilisé pour ajouter un algorithme de face recognition à la presentation du robot.<BR>
Pour l’utilisation il faut avoir:

&nbsp;&nbsp;&nbsp; - OpenCV installé <BR>
sudo apt-get install python-opencv <BR>
&nbsp;&nbsp;&nbsp; - caméra en service <BR>
&nbsp;&nbsp;&nbsp; - le fichier haarcascade_frontalface_alt2.xml dans le même dossier où il y a le code <BR>

`cd Bureau/poppy/my_code` <BR>
`python presentation_with_camera.py`<BR>

“presentation_with_camera.py”

def Recognition(): <BR>
	cascPath = os.getcwd()+'/haarcascades/haarcascade_frontalface_alt2.xml' # Name of the file from which the classifier is <BR> loaded. It is a trained classifier for detecting faces <BR>
	faceCascade = cv2.CascadeClassifier(cascPath) #Object detector <BR>
	video_capture = cv2.VideoCapture(0) #It sets the video source to the default webcam <BR>
	flag = 1 <BR>
	print 'Press Ctrl-C to stop the current program' <BR>
	try: <BR>
		while True: <BR>
		    # Capture frame-by-frame <BR>
			ret, frame = video_capture.read() <BR>
		
			if not ret: continue <BR>

		    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts an image from one color space to another <BR>

		    	faces = faceCascade.detectMultiScale(  <BR>
				gray, # Matrix of the type CV_8U containing an image where objects are detected <BR>
				scaleFactor=1.1, #Parameter specifying how much the image size is reduced at each image scale  <BR>
				minNeighbors=5, #Parameter specifying how many neighbors each candidate rectangle should have to retain it <BR>
				minSize=(40, 40), <BR>
				#minSize=(30, 30),# Minimum possible object size. Objects smaller than that are ignored <BR>
				flags=cv2.cv.CV_HAAR_SCALE_IMAGE <BR>
		    	) # It detects objects of different sizes in the input image. The detected objects are returned as a list of <BR> rectangles <BR>
			faces2= list(faces)	# It changes the face object in list type to simplify the If loop.	 <BR>
			if not faces2: <BR>
				print 'no face' <BR>
			else: <BR>
				print 'got face' <BR>
				flag = flag + 1 <BR>
				if flag is 10: #the robot move after 9 positive results <BR>
					k[idm54].goto_position(80, 2.0)  <BR>
					k[idm51].goto_position(-100, 2.0) <BR>
					flag= 11 <BR>

		    # Draw a rectangle around the faces <BR>
			for (x, y, w, h) in faces: <BR>
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) <BR>

		    # Display the resulting frame <BR>
			cv2.imshow('Video', frame) <BR>

			if cv2.waitKey(1) & 0xFF == ord('q'): <BR>
				break <BR>

	# When everything is done, release the capture <BR>
	except KeyboardInterrupt: <BR>
		video_capture.release() <BR>
		cv2.destroyAllWindows()	 <BR>
		BackPosition() <BR>
		pass <BR>
		
Le détecteur d'objet décrit a été initialement proposée par Paul Viola et développé par Rainer Lienhart.
Tout d’abord, un classificateur est formé avec quelques image d’example d'un objet particulier (dans ce cas un visage) appelés exemples positifs qui ont tous la même taille (par exemple, 30x30), et des exemples négatifs qui sont images arbitraires de la même taille.
Après que le classificateur est formé, il peut être appliqué à une région d’intérêt.
Le classificateur est conçu de sorte qu'il peut être facilement redimensionné afin de trouver les objets d’intérêt des tailles différentes, ce qui est plus efficace que le redimensionnement de l'image elle-même.
Le mot “cascade" signifie que le classificateur se compose de plusieurs classificateurs similaires (étapes) qui sont appliqués à une région d'intérêt jusqu'à le candidat est rejeté ou toutes les étapes sont transmis. Les classificateurs de base sont classificateurs ‘decision-tree’ avec au moins 2 feuilles.

 

