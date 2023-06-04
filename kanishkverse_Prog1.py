# Assignment done by Kanishk

# lets mention about the calculator
print ("This is to measure Body Mass Index (BMI) of a Human Being, based on Height and Weight mentioned.")

#now we ask for the person's your_name for calculating the Body Mass Index

your_name = input('What is your name: ')
#Now we ask for weight in Kilograms

weight  = float(input(f'Hi,{your_name} please enter your body weight in Kilograms: '))

#Now we ask for Height in Centimetres
height = float(input('pleae enter your height in Centimetres: '))

print (f"Now calculating the Body_Mass_Index based on your Information, {your_name}!")

#But actual formula is based on Kilograms and Metres, We need to convert Centimetre into Metre, which is 1/100 and square it for easier calculation.
height_in_metres = (height/100)**2

Body_Mass_Index = (weight/height_in_metres)
#printing Body Mass Index based on data

if(Body_Mass_Index>= 18.5 and Body_Mass_Index<= 24.5):
        print("") #this is to print empty line 
        print (your_name," you are in a good body mass index ratio")
        print("this indicates you have Fit Body")

#for the Overweight        
elif(Body_Mass_Index >= 24.7 and Body_Mass_Index <= 29.9):
        print("")
        print (your_name," You are above Normal Range, makes you a overweight person")
        print(f'{your_name}, you should consult a nutritionist to get back into normal')

elif(Body_Mass_Index < 18.4):
        print('')
        print (your_name,' you are in under weight category')
        print(f'{your_name} you should go to a doctor, get a required treatment')
        
else:
        print('')
        print (your_name,' is Obese')
        print (your_name, ' you should see a doctor ASAP and try physical activity more often')



print('')
print('Submitted by Kanishka Samrat Kolakaluri')       
print("date of creation: Sept 3, 2022")

        
