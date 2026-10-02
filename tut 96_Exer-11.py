# Regex Email Extractor.
import re

# Email Collector program.

# ques - we have given a large string containing many emails in-betweens, we have to extract all these email and write in the file as
# email1 -
# email2 -
# email3 -

bigStr = """Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Direction: View map fass
vaibhav bhai lekin
bahut hi badiya aadmi haiaiin"""

