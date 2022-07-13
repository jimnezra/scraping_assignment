import scrapy
import os
import csv

from sympy import jacobi_normalized

cur_dir = os.path.dirname(__file__)
url = os.path.join(cur_dir, 'Full_time_Faculty_UBC_Civil_Engineering.html')

class FullTimeFacultyUbcSpider(scrapy.Spider):
    name = 'full_time_faculty_ubc'
    allowed_domains = ['civil.ubc.ca']
    # # Online scraping
    # start_urls = ['https://civil.ubc.ca/people/full-time-faculty/']
    # Local scraping
    start_urls = [f"file:{url}"]

    def parse(self, response):
        csv_file = open('UBC_contacts_information.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(['First Name', 'Last Name', 'Email'])

        first_names = response.xpath('//span[@id="first"]/text()').getall()
        last_names = response.xpath('//span[@id="last"]/text()').getall()
        emails = response.xpath('//a[@id="email"]/text()').getall()

        for i, j in enumerate(first_names):
            writer.writerow([first_names[i], last_names[i], emails[i]])

        csv_file.close()

        print("\n")
        print("Debugging")
        print("Emails:")
        print(emails)
        print("\n")

        pass
