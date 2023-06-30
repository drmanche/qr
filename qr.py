import os, time, sys, cv2, platform, pathlib
from qrcode import QRCode

#The length of sys.argv must be equal to 2, otherwise the correct syntax is printed
if len(sys.argv) != 2:
    #Gets the current operating system the script is running on to provide the correct syntax
    platform_current = platform.system()
    os.system('cls' if platform_current == 'Windows' else 'clear')
    print(f"\nSyntax: {'py' if platform_current == 'Windows' else 'python3'} {pathlib.Path(__file__).name} URL\n")
else:
    #Create an object for the QRCode class and add the parameter that you get via the terminal
    qr = QRCode(version=1, box_size=10, border=2)
    qr.add_data(sys.argv[1])
    qr.make(fit=True)

    #Create a path based on the location of the python file and the current date and time
    path = f"{os.path.dirname(os.path.abspath(__file__))}/{time.strftime('%d-%m-%y ][ %H-%M-%S')}.png"

    #Create the qr code image based on the parameter you get via terminal and save the image using the path
    qr.make_image(fill_color="#3c3c3c", back_color="#c3c3c3").save(path)

    #Read and show the image that contains the qr code
    cv2.imshow("QR", cv2.imread(path))
    cv2.waitKey(0)
    cv2.destroyAllWindows()