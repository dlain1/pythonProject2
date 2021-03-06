from socket import *

def smtp_client(port=25, mailserver='smtp.nyu.edu'):
   msg = "rn My Message"
   endmsg = "rn.rn"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   mailserver = ('smtp.nyu.edu', 25)

   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect(mailserver)

   recv = clientSocket.recv(1025).decode()
   print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alicern'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1025).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   mail_command = ('MAIL FROM: &..6@nyu.edu>rn') # from who the message will appear
   clientSocket.send(mail_command.encode())
   recv2 = clientSocket.recv(1024).decode()
   print(recv2)
   if recv2[:3] != '250': #if the data is not received
      print('250 reply not received from server.!')

   # Send RCPT TO command and print server response.
   rcpt_command = ('RCPT TO: &..3@hotmail.com>rn') # Recepient
   clientSocket.send(rcpt_command.encode())
   recv3 = clientSocket.recv(1025).decode()
   print(recv3)
   if recv3[:3] != '250':  # if the data is not received
      print('250 reply not received from server.')


   # Send DATA command and print server response.
   data = "DATA rn"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1025).decode()
   print(recv4)
   if recv4[:3] != '354':  # if the data is not received
      print('354 reply not received from server.')


   # Send message data.
   #subject = 'Subject: Testing SMTP Clientrn'
   subject = "Subject: testing my clientrnrn"
   clientSocket.send(subject.encode())
   #date = date + "rnrn"
   #clientSocket.send(date.encode())
   clientSocket.send(msg.encode())
   clientSocket.send(endmsg.encode())


   # Message ends with a single period.
   recv_msg = clientSocket.recv(1025)
   print("Response after sending message body:" + recv_msg.decode())
   quitcommand = ('QUITrn')
   clientSocket.send(quitcommand.encode())
   recv5 = clientSocket.recv(1025).decode()
   print(recv5)

   clientSocket.close()


if __name__ == '__main__':
   smtp_client(25, 'smtp.nyu.edu')
