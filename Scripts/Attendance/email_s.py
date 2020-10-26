from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
import csv
import sys
import os
import re

#Update EMAIL ID and PASWORD with yours, remove square brackets
USERNAME = "username"
PASSWORD = "pass"
file_name = "csv file here"


#update subject and content of email
subject="Invitation for Campus Recruitment at IIT (BHU) Varanasi 2019-20"


content_part1="""\

Dear Sir/Ma'am,

Greetings from Indian Institute of Technology (BHU), Varanasi!

It is an honour to invite your esteemed organisation to participate in the
placement/internship process of the Institute for the academic session
2019-20.

Ours is the oldest institution in the country to offer degree level
programs in engineering subjects. The Institute currently offers
undergraduate and graduate level courses over a total of 16 disciplines,
the details of which are available here
<https://www.iitbhu.ac.in/admissions/index.php/academic-programmes.html#>.
B.Tech./IDD students are admitted through the reputed JEE-Advanced and
M.Tech./M.Pharma. students are admitted through GATE/GPAT. Ph.D. Scholars
who have qualified CSIR-NET/GATE/GPAT, etc. are also available. Further
information can be found in the Placement Brochure
<https://drive.google.com/open?id=1Q4EgQvKEW7M94M7ZniOwBH56DmWfoFXk>.

We are proud to mention that our Institute has been ranked 7th among
engineering institutions in the country
<https://www.nirfindia.org/2019/EngineeringRanking.html> *in terms of
Graduate Outcome* (GO) by the MHRD, Govt. Of India, for the session
2018-19. Our reputation as India’s premier engineering institution is
further corroborated by being honoured with the *"Top Institute of
India" *award
given by Competition Success Review in 2017.

You are requested to communicate your requirements and offering to our
students by submitting the Job Announcement Form (JAF)/Internship
Announcement Form (IAF), the link for which can be found below.

The Training and Placement Cell allots a date to the company for final
Placement (Group Discussion/Interview) on the basis of criteria given in
the Placement Policy. The link for the same has been provided below.

I am looking forward to your early response.

*Professor In-charge*
Training and Placement Cell
Indian Institute of Technology (BHU)
Varanasi – 221005 Phone: (+91 542)2368160, 2369162
Web: http://placement.iitbhu.ac.in  <http://placement.iitbhu.ac.in/>
Email: tpo@iitbhu.ac.in  <http://tpo@iitbhu.ac.in/>


*Documents:*
1. Placement Policy
<https://drive.google.com/file/d/1fE58jJxwHDwkHQY5eDexYYHjSEEyntDK/view#>
(Alternate
Link)
<https://www.placement.iitbhu.ac.in/media/uploads/placement_policy_company.pdf>
2. Job Announcement Form (JAF)
<https://drive.google.com/open?id=1uiNI9zNRwLI3Hy0L0cuDDPn0XzN4uNYN> (Alternate
Link) <https://www.placement.iitbhu.ac.in/media/uploads/jaf.pdf>
3. Internship Policy
<https://drive.google.com/open?id=16MEyK8DXmACP5cRI1J7d3Z5qe4xbZC4f> (Alternate
Link)
<https://www.placement.iitbhu.ac.in/media/uploads/internship_policy_company.pdf>
4. Internship Announcement Form (IAF)
<https://drive.google.com/open?id=15q4xNlBLx2U79oxz4R9Su_GaRszgWIW4> (Alternate
Link) <https://www.placement.iitbhu.ac.in/media/uploads/iaf.pdf>
5. Placement Calendar
<https://drive.google.com/file/d/1PKBxxKPiWNneGiAPYQzU0FvM91VP4suD/view#>
(Alternate
Link) <https://www.placement.iitbhu.ac.in/media/uploads/calendar.pdf>

For the Placement Brochure, visit here
<https://drive.google.com/open?id=1Q4EgQvKEW7M94M7ZniOwBH56DmWfoFXk> or
here.
<https://www.placement.iitbhu.ac.in/media/uploads/placement_brochure.pdf>

"""


content_part2="""\

<html>
<body>

<p>
Dear Sir/Ma'am,
</p>
<p>
Greetings from Indian Institute of Technology (BHU), Varanasi!
</p>
<p>
It is an honour to invite your esteemed organisation to participate in the
placement/internship process of the Institute for the academic session
2019-20.
</p>
<p>
Ours is the oldest institution in the country to offer degree level
programs in engineering subjects. The Institute currently offers
undergraduate and graduate level courses over a total of 16 disciplines,
the details of which are available <a href='https://www.iitbhu.ac.in/admissions/index.php/academic-programmes.html#'>
here</a>.
B.Tech./IDD students are admitted through the reputed JEE-Advanced and
M.Tech./M.Pharma. students are admitted through GATE/GPAT. Ph.D. Scholars
who have qualified CSIR-NET/GATE/GPAT, etc. are also available. Further
information can be found in the <a href='https://drive.google.com/open?id=1Q4EgQvKEW7M94M7ZniOwBH56DmWfoFXk'>
Placement Brochure.</a>
</p>
<p>
We are proud to mention that our Institute has been <a href='https://www.nirfindia.org/2019/EngineeringRanking.html'>
ranked 7th among engineering institutions in the country</a>
<strong>in terms of Graduate Outcome</strong> (GO) by the MHRD, Govt. Of India, for the session
2018-19. Our reputation as India’s premier engineering institution is
further corroborated by being honoured with the <strong>"Top Institute of
India" </strong>award
given by Competition Success Review in 2017.
</p>
<p>
You are requested to communicate your requirements and offering to our
students by submitting the Job Announcement Form (JAF)/Internship
Announcement Form (IAF), the link for which can be found below.
</p>
<p>
The Training and Placement Cell allots a date to the company for final
Placement (Group Discussion/Interview) on the basis of criteria given in
the Placement Policy. The link for the same has been provided below.
</p>
<p>
I am looking forward to your early response.
</p>
<p>
<strong>Professor In-charge</strong> <br>
Training and Placement Cell <br>
Indian Institute of Technology (BHU) <br>
Varanasi – 221005 Phone: (+91 542)2368160, 2369162 <br>
Web: <a href='http://placement.iitbhu.ac.in/'>
http://placement.iitbhu.ac.in</a> <br>
Email: <a href='mailto:http://tpo@iitbhu.ac.in/'> tpo@iitbhu.ac.in</a>

</p><p>
<strong>Documents:</strong> <br>
1. <a href='https://drive.google.com/file/d/1fE58jJxwHDwkHQY5eDexYYHjSEEyntDK/view#'>Placement Policy </a>
 <a href='https://www.placement.iitbhu.ac.in/media/uploads/placement_policy_company.pdf'> (Alternate Link) </a> <br>
2. <a href='https://drive.google.com/open?id=1uiNI9zNRwLI3Hy0L0cuDDPn0XzN4uNYN'> Job Announcement Form (JAF) </a>
<a href='https://www.placement.iitbhu.ac.in/media/uploads/jaf.pdf'> (Alternate Link) </a> <br>
3. <a href='https://drive.google.com/open?id=16MEyK8DXmACP5cRI1J7d3Z5qe4xbZC4f'> Internship Policy </a>
<a href='https://www.placement.iitbhu.ac.in/media/uploads/internship_policy_company.pdf'> (Alternate Link) </a> <br>
4. <a href='https://drive.google.com/open?id=15q4xNlBLx2U79oxz4R9Su_GaRszgWIW4' > Internship Announcement Form (IAF) </a>
 <a href='https://www.placement.iitbhu.ac.in/media/uploads/iaf.pdf'> (Alternate Link) <a/><br>
5. <a href='https://drive.google.com/file/d/1PKBxxKPiWNneGiAPYQzU0FvM91VP4suD/view#'> Placement Calendar </a>
<a href='https://www.placement.iitbhu.ac.in/media/uploads/calendar.pdf'>(Alternate Link) </a>
</p><p>

For the Placement Brochure, visit <a href='https://drive.google.com/open?id=1Q4EgQvKEW7M94M7ZniOwBH56DmWfoFXk'>here</a>
or <a href='https://www.placement.iitbhu.ac.in/media/uploads/placement_brochure.pdf'> here. </a>

</body>
</html>

"""

#GMAIL connect settings
conn = SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login(USERNAME, PASSWORD)


with open(file_name,'rt') as csvfile:

	csvreader = csv.reader(csvfile, delimiter='\t')
	try:
		for row in csvreader:
			emailid=row[0]

			try:
				conn.verify(emailid)
			except Exception:
				print ("mail {0} not found".format(emailid)) 
				continue

			msg = MIMEMultipart("alternative")   	
			msg['Subject']= subject
			msg['From']   = "\" Your name here \" <{0}>".format(USERNAME)
			msg['To']= emailid
			msg.attach(MIMEText(content_part1, 'plain'))
			msg.attach(MIMEText(content_part2, 'html'))

			conn.sendmail(USERNAME, (emailid), msg.as_string())
			print("mail sent to {0}".format(emailid)) 

	except:
		print("error on {0}".format(emailid)) 

