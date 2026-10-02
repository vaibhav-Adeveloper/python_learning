# if __name__ == '__main__'  -->  usage & necessity

import if_name_main_concept
print(if_name_main_concept.add_wrong(5,3))

# Now problem arises that we use add_wrong function of other python file by importing to this python file
# but we are also getting the full display of all the things of other python file in this python file when we run the code ,jabki humanai iss python file mai
# sirf add_wrong() func ko use kiya, toh sirf isska hi output deikhna chaiye sirf when we run program in this python file
# lekin eesa nhi hua other python file ka pura code display hogya, jo hum chahtai thai ki sirf add_wrong function ka output hi
# display ho waisa nhi hua


# now here comes the use of if __name__ == '__main__':  concept

# if __name__ == '__main__': "kai neeche ka code run nhi hota hai."

# isliyai jab hu chatai ho ki jb hum other python file ko iss python file mai la rhai ho lekin uss python file ka line no 17 kai neeche ka code as a output in this python file kai output mai na deekhai,sirf jo function of that python file mai line 1 to 11 mai likha hai
# jisai hum iss python file mai istamal kar rhai sirf ussi ka output display ho use this concept


# about import
# jab bhi app import kartai ho ,toh yeh uss file kai saarai kai saaarai content ko execute bhi kar deta hai
# isliyai jo hum uss python file ka function iss python file mai use kar rahi uss ka output toh dikhta hi hai sath hi sath baaki cheezai of that python file bhi execute hokai display ho jaati hai in output window


# name ki value if_name_main_concept jab hogi jab iss program ko chala rhai.
# matlb aap if_name_main_concept python file sai content la rhai ho.
