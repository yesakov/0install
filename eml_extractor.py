import email
import os
import sys

def ext(fle):
	msg = email.message_from_file(open(fle))
	attachments=msg.get_payload()
	for attachment in attachments:
		try:
			fnam=attachment.get_filename()
			try:
				file_location = sys.argv[2] + fnam
				if (os.path.exists(file_location[:file_location.rfind('\\')])):
					f=open(os.path.join(file_location), 'wb').write(attachment.get_payload(decode=True,))
				else:
					print("no such directory for output file " + file_location)
			except:
				f=open(fle[:fle.rfind('\\')] + "\\" + fnam, 'wb').write(attachment.get_payload(decode=True,))
	
			
		except Exception as detail:
			#print(detail)
			pass

def extract(path):
	if str.lower(path[-3:])=="eml":
		ext(path)
	else:
		listing = os.listdir(path)
		for fle in listing:
			if str.lower(fle[-3:])=="eml":
				ext(path + fle)
				


if __name__ == "__main__":
	try:
		extract(sys.argv[1])
	except:
		print('Give file path as argument')