import pdfkit 



pdfkit.from_file("./emails_text/final_emails/0.html", "0.pdf")

# for i in range(250):
#     try: 
#         input()       
#         pdfkit.from_file(f'./emails_text/final_emails/{i}.html', f'./emails_text/final_pdf/{i}.pdf') 
#         input()
#     except:
#         print(f"there is no {i}th file")