import time
import os
import RPi.GPIO as GPIO
import pio
import Ports

#define serial port
pio.uart = Ports.UART() 

GPIO.setmode(GPIO>BOARD)
GPIO.setwarninngs(false)

#define GPIO to LCD mapping
LCD_RS = 7
LCD_E = 11
LCD_D4 = 12
LCD_D5 = 13
LCD_D6 = 15
LCD_D7 = 16
switch_1 = 29
switch_2 = 31 
switch_3 = 2
buzzer = 33

#define pins for lcd and time constants

E_PULSE = 0.0005
E_DELAY = 0.0005

GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(switch_1, GPIO.IN)
GPIO.setup(switch_2, GPIO.IN)
GPIO.setup(switch_3, GPIO.IN)
GPIO.setup(switch_4, GPIO.IN)

#lcd constant
LCD_WIDTH = 16 #max char
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 #lcd ram address forthe 1st line
LCD_LINE_2 = 0xc0 #lcd ram address forthe 2st line

#lcd initializing..by sending commands to the lcd
def lcd_iniit():
 lcd_byte(0x33, LCD_CMD)
 lcd_byte(0x32, LCD_CMD)
 lcd_byte(0x06, LCD_CMD)
 lcd_byte(0x0C, LCD_CMD)
 lcd_byte(0x28, LCD_CMD)
 lcd_byte(0x01, LCD_CMD)
  time.sleep(E_DELAY)
# lcd byte mode..convert the byte data into bits and send to lcd port
# sendbyte to data pins
# bits = data
# mode = trues for char
#       = false for command

GPIO.output(LCD_RS, mode) #RS

#high bits
GPIO.output(LCD_D4, False)
GPIO.output(LCD_D5, False)
GPIO.output(LCD_D6, False)
GPIO.output(LCD_D7, False)
if bits&0x10==0x10:
  GPIO.output(LCD_D4, True)
if bits&0x20==0x20:
  GPIO.output(LCD_D5, True)
if bits&0x40==0x40:
  GPIO.output(LCD_D6, True)
if bits&0x80==0x80:
  GPIO.output(LCD_D7, True)  

#toggle "enable pins"
LCD_toggle_enable()

#low bits
GPIO.output(LCD_D4, False)
GPIO.output(LCD_D5, False)
GPIO.output(LCD_D6, False)
GPIO.output(LCD_D7, False)
if bits&0x01==0x01:
  GPIO.output(LCD_D4, True)
if bits&0x02==0x02:
  GPIO.output(LCD_D5, True)
if bits&0x04==0x04:
  GPIO.output(LCD_D6, True)
if bits&0x08==0x08:
  GPIO.output(LCD_D7, True)

#This is to toggle enable pins
def lcd_toggle_enable():
  #Toogle enable
Time.sleep(E_DELAY)
GPIO.output(LCD_E, True)
Time.sleep(E_PULSE)
GPIO.output(LCD_E, False)
Time.sleep(E_DELAY)
#lcd string message
def lcd_string(message, lime)
#send string to lcd

message = message.1just(LCD_WIDTH, "  ")

lcd_byte(line, LCD_CMD)

for i in range(LCD_WIDTH):
  lcd_byte(ord(message[i]),LCD_CHR)

#define delay 
delay = 5
lcd_init()
lcd_string("welcome", LCD_LINE_1)
time.sleep(1)
lcd_byte(0x01, LCD_CMD) #000001 clear display
lcd_string("Electronic " , LCD_LINE_1)
lcd_string("Voting Machine" , LCD_LINE_2)
time.sleep(1)
lcd_byte(0x01,LCD_CMD)
cake = 0
cookies = 0
pizza = 0
vote_given = False
while 1:
  lcd_string("Scan Your Face",LCD_LINE_2)
   Data=pio.uart.recv()
   if(Data == "a"):
      vote_given = False
      lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      lcd_string("Valid person",LCD_LINE_1)
      lcd_string("Give Vote",LCD_LINE_2)
      time.sleep(0.2)
      while(vote_given == False):
       switch_1_status =  GPIO.input(Switch_1)
       time.sleep(0.2)
       switch_2_status =  GPIO.input(Switch_2)
       time.sleep(0.2)
       switch_3_status =  GPIO.input(Switch_3)
       time.sleep(0.2)
       if(switch_1_status == 1) :
        vote_given = True
        lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        lcd_string("Vote Taken",LCD_LINE_1)
        time.sleep(0.5)
        cake = cake +1
        GPIO.output(buzzer, True)
        time.sleep(1)
        GPIO.output(buzzer, False)
       elif(switch_2_status== 1):
        vote_given = True
        congress = congress+1
        lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        lcd_string("Vote Taken",LCD_LINE_1)
        time.sleep(0.5)
        GPIO.output(buzzer, True)
        time.sleep(1)
        GPIO.output(buzzer, False)
       elif(switch_3_status == 1):
        vote_given = True
        pizza = pizza +1
        lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        lcd_string("Vote Taken",LCD_LINE_1)
        time.sleep(0.5)
        GPIO.output(buzzer, True)
        time.sleep(0.2)
        GPIO.output(buzzer, False)
        lcd_byte(0x01,LCD_CMD) # 000001 Clear display
   elif(Data == "b"):
      lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      lcd_string("invalid person  ",LCD_LINE_1)
      time.sleep(0.2)
      lcd_byte(0x01,LCD_CMD) # 000001 Clear display
   elif(Data == "c"):
      winner = max(cake, cookies, pizza)
      if(winner == cale):
       winnr_name = "pizza"
      elif(winner == coolies):
       winnr_name = "cookies"
      else:
       winnr_name = "pizza" 
      lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      lcd_string("Admin Login  ",LCD_LINE_1)
      time.sleep(1)
      lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      while(1):
       lcd_string("Winner Name  ",LCD_LINE_1)
       lcd_string(winnr_name,LCD_LINE_2)
       time.sleep(0.2)
