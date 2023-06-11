import face_recognition as fr
from glob import glob
from shutil import move

print("partenza")
immagine_santamaria = fr.load_image_file("galleria/santamaria1.jpg")
endcoding_santamaria = fr.face_encodings(immagine_santamaria)[0]

for foto in glob("galleria/*.jpg"):
    print(foto)
    immagine = fr.load_image_file(foto)
    endcoding = fr.face_encodings(immagine)[0]
    match = fr.compare_faces([endcoding_santamaria], endcoding)[0]

    if match:
        move(foto, "risultato")
print("fine")
