from stegano import *
import os
import datetime
import tkinter as tk
from tkinter import filedialog

class Steganography():
    def __init__(self):
        print("#"*70)
        print("Welcome to CipheIT.")
        print()
        print("CipheIT is a app that encodes a text message in image and also decodes.")
        print()
        self.constructor_range=1
        self.another_operations_range=1
        self.decode_range=1
        self.text_range=1
        self.encode_range=1
        self.constructor()
        
    def constructor(self):
        try:
            print("Choose the option You want to perform!")
            print("1.Encode(To Hide Message)\n2.Decode(To Reveal Message)\n3.Exit")
            print()
            option=int(input("Enter your option: "))
            print()
        except ValueError:
            print()
            print("Invalid Input!!!")
            print()
            print("Can't be letters\nPlease enter only 1 or 2")
            print()
            print("Enter a valid option")
            print()
            if self.constructor_range<=5:
                self.constructor_range+=1
                self.constructor()
            else:
                print("You have reached maximum limitations!!!")
                print()
                print("App is exiting...")
        except:
            print()
            print("Invalid Input!!!")
            print()
            print("Please enter only 1 or 2")
            print()
            print("Enter a valid option")
            print()
            if self.constructor_range<=5:
                self.constructor_range+=1
                self.constructor()
            else:
                print("You have reached maximum limit!!!")
                print()
                print("App is exiting...")
                os._exit(0)

        else:
            if option==1:
                self.text_to_hide=input("Enter text you want to hide: ")
                
                while len(self.text_to_hide)<=0:
                    if self.text_range<=5:
                        print("Encryption message can't be empty!\n")
                        self.text_to_hide=input("Enter text you want to hide: ")
                        self.text_range+=1
                    else:
                        print()
                        print("You have reached maximum limit !!!")
                        print("App is restarting...")
                        print()
                        print()
                        self.constructor()
                    
                
                self.creating_method=self.creating_folder()
                self.hiding_method=self.hiding_method()
            elif option==2:
                
                print("Select an image to decrypt the message")
                self.decode_method=self.decode_method()
            elif option==3:
                os._exit(0)
            else:
                print()
                print("Invalid Input!!!")
                print()
                print("Enter only 1 or 2")
                print()
                print("Enter a valid option")
                print()
            if self.constructor_range<=5:
                self.constructor_range+=1
                self.constructor()
            else:
                print("You have reached maximum limitations!!!")
                print()
                print("App is exiting...")
                os._exit(0)
                
    def another_operations(self):
                try:
                    option1=str(input("Enter No to exit app.\nDo you want to perform another operation(Yes/No): "))
                except:
                    print("Invalid Input\n\nTry Again!!!")
                    self.another_operations()
                else:
                    if option1.lower()=="yes":
                        print()
                        print()
                        self.constructor()
                    elif option1.lower()=="no":
                        os._exit(0)
                    else:
                        print("Invalid Input\n\nTry Again!!!")
                        if self.another_operations_range<=3:
                            self.another_operations_range+=1
                            print()
                            self.another_operations()
                        else:
                            print("You have reached maximum limitations!!!")
                            os._exit(0)

    def creating_folder(self):
        try: os.mkdir("C:\Steganography")
        except FileExistsError: pass
        else: pass

    def hiding_method(self):
        try:
            self.img_filename=self.gui_interface()
            secret = lsb.hide(self.img_filename, self.text_to_hide)
        except AttributeError:
            self.encode_range+=1
            if self.encode_range<=5:
                self.hiding_method=self.hiding_method()
            else:
                print()
                print()
                print("You have not selected any image to encrypt")
                print()
                print("Try Again!!!")
                print()
                print("Your app is restarting!!!")
                print()
                self.constructor()
        else:
            now = datetime.datetime.now()
            dt_string=now.strftime("%Y%m%d"+"%H%M")
            dt_string1="IMG_"+dt_string
            secret.save("C:\Steganography\{}.png".format(dt_string1))
            print("Your file is saved at path C:\Steganography with filename {}".format(dt_string1))
            print()
            self.another_operations()

    def decode_method(self):
        try:
            self.decode_path=self.gui_interface()
            secret = lsb.reveal(self.decode_path)
        except AttributeError:
            self.decode_range+=1
            if self.decode_range<=5:
                self.decode_method()
            else:
                print()
                print()
                print("Try Again!!!")
                print()
                print("You have not selected an image to decrypt")
                print()
                self.another_operations()
        else:
           print("The encrypted message in image is:\n",secret)
           self.another_operations()
    
    def gui_interface(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("JPEG and PNG Files", "*.jpeg;*.jpg;*.png")])
        if file_path:
            print("Selected file: ", file_path)
        return file_path
object1=Steganography()
