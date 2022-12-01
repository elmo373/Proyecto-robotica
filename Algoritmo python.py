import cv2
import numpy as np
import serial
Colorconeccion = ""
formam = ""

total1 = 0
total2 = 0
total3 = 0
                            
ser = serial.Serial("com5",9600)


cap = cv2.VideoCapture(1)


RojoBajo = np.array([0,50,50], np.uint8)
RojoAlto = np.array([10,255,255], np.uint8)



font = cv2.FONT_HERSHEY_SIMPLEX 
    
while True:
    ret,frame = cap.read()
    accion = ""
    if ret == True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV, RojoBajo, RojoAlto)
        mask = cv2.inRange(frameHSV, RojoBajo, RojoAlto)
        print(mask.shape[1])
        matriz = np.zeros(shape=((int)(mask.shape[0]/20),(int)(mask.shape[1]/20) ))
        m=0
        n=0
        v1=0
        v2=0
        for i in range((int)(mask.shape[0]/20)):
            for j in range((int)(mask.shape[1]/20)):
                matriz[i][j]=0
        print(mask.shape)
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                matriz[m][n] = mask[i][j] + matriz[m][n]
                v1=v1+1
                if v1==20:
                    n=n+1
                    v1=0

            n=0
            v2=v2+1
            if v2==20:
                m=m+1
                v2=0
        m=0

        for i in range((int)(mask.shape[0]/20)):
            for j in range((int)(mask.shape[1]/20)):
                print(matriz[i][j], end=", ")
            print()

        VectorXA=np.zeros(shape=((int)(mask.shape[1]/20)))
        VectorYA=np.zeros(shape=((int)(mask.shape[0]/20)))

        VectorXR=np.zeros(shape=((int)(mask.shape[1]/20)))
        VectorYR=np.zeros(shape=((int)(mask.shape[0]/20)))

        Matriz_azul = np.zeros(shape=((int)(mask.shape[0]/20),(int)(mask.shape[1]/20) ))
        Matriz_azul[0][0]=35000

        Matriz_rojo = matriz

        for i in range((int)(mask.shape[0]/20)):
            for y in range((int)(mask.shape[1]/20)):
                if Matriz_azul[i][y]>20000:
                    VectorXA=VectorXA+[y]
                    VectorYA=VectorYA+[i]
                
                if Matriz_rojo[i][y]>20000:
                    VectorXR=VectorXR+[y]
                    VectorYR=VectorYR+[i]
                

        posinicial=[VectorXA[0],VectorYA[0]]
        X=VectorXA[0]-VectorXR[i]
        Y=VectorYA[0]-VectorYR[i]
        mx='derecha '
        my='abajo '
        X=abs(X)
        Y=abs(Y)
        if X>0:
            mx='izquierda '
            orden(mx,1750)
            orden('adelante',1600*X)
        else:
            orden(mx,0)
            orden('adelante',1600*X)
            
        if Y>0:
            my='arriba'
            orden('derecha',1750)
            orden('adelante',1600*Y)
        else:
            orden('izquierda',0)
            orden('adelante',1600*Y)
            
        X=abs(X)
        Y=abs(Y)
        orden(my,X)
        print(mx, X, my, Y)
        VectorXA[0]=VectorXR[i]
        VectorYA[0]=VectorYR[i]
        print('Posicion:',VectorXA[0],VectorYA[0])
        cadena = 'Posicion:',VectorXA[0],VectorYA[0]
        VectorXA[0]=posinicial[0]
        VectorYA[0]=posinicial[1]
        print('Posicion:',VectorXA[0],VectorYA[0])

        

        mask = cv2.inRange(frameHSV, RojoBajo, RojoAlto)
        cv2.imshow('frame', mask)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()

def orden(accion,tiempo):
    cadena = accion+",240,1666,"
    try:
        
        ser.write(cadena.encode())
        mensaje = ser.readline()
        print(str(mensaje))
    except TimeoutError:
        print("error")
    finally:
        print("done")
