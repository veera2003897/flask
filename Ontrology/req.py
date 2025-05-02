from pymongo import MongoClient
import requests
import datetime
client =MongoClient("mongodb://localhost:27017/")
db_metadata = client["db_metadata"]


def scrap_jobs():
    user_input = {'portalID': "65a61a0870c0abc293de5438", 'mode': 'start', 'selection': 'all_jobs', "pages": "",
                                      'category': '', 'sub_category': '', 'keyword': '', 'location': '', 'time_sleep': 3, "scraperTool": str("selenium").lower()}
    
    try:
        requests.post(url="http://192.168.1.223:8001/scraperapi/insertscraperjob", json=user_input)
    except Exception as e:
        print(str(e))

# scrap_jobs()

def scraper_excuter_query():
    try:

        payload = {"processID":"68133b2aea65067a6485a89f", "redisName": ""}
        requests.post(url="http://192.168.1.223:8001/scraper/executeQuery", json=payload)
    except Exception as e:
        print(str(e))


scraper_excuter_query()

# print(requests.get('https://cae.wd3.myworkdayjobs.com/en-US/career/job/Comox/SAR-Mission-Systems-Instructor_110304').status_code)





# {
#     "_id" : ObjectId("65a61a0770c0abc293de5387"),
#     "name" : "Caeparcaviation",
#     "collection" : "caeparcaviation",
#     "companyID" : "",
#     "clientID" : "",
#     "userID" : "",
#     "type" : "Careers Page",
#     "website" : "https://www.cae.com/",
#     "landingPageUrl" : [
#         "https://cae.wd3.myworkdayjobs.com/career"
#     ],
#     "shortJobUrl" : "https://www.cae.com/",
#     "createdAt" : ISODate("2025-03-10T05:30:40.697Z"),
#     "updatedAt" : ISODate("2025-03-10T05:31:33.109Z"),
#     "scraperTool" : "Selenium",
#     "deleted" : false,
#     "browser" : "Google Chrome",
#     "headless" : false,
#     "searchKeywords" : [],
#     "pages" : 0,
#     "nextPage" : {
#         "pageType" : "by_button",
#         "url" : "",
#         "pageIncrement" : 0
#     },
#     "externalSources" : [],
#     "automate" : {
#         "enabled" : false,
#         "startDate" : ISODate("2024-10-17T18:30:00.000Z"),
#         "endDate" : ISODate("2025-10-17T18:29:59.999Z"),
#         "timingsIn24Format" : [
#             "05:15"
#         ],
#         "timeZone" : "",
#         "timeZoneName" : "",
#         "timeZoneFullName" : "",
#         "userID" : "",
#         "weekDays" : [
#             "Friday"
#         ]
#     },
#     "pipline" : [
#         "Scrape"
#     ],
#     "elementDetails" : {
#         "searchButton" : {},
#         "jobURL" : {
#             "name" : "",
#             "description" : "",
#             "multi" : false,
#             "props" : [
#                 {
#                     "attr" : "css_selector",
#                     "value" : " div.css-b3pn3b>h3>a",
#                     "text" : ""
#                 }
#             ]
#         },
#         "nextPage" : {
#             "name" : "",
#             "description" : "",
#             "multi" : false,
#             "props" : [
#                 {
#                     "attr" : "css_selector",
#                     "value" : " nav>div>button>span>svg",
#                     "text" : ""
#                 }
#             ]
#         },
#         "jobCount" : {},
#         "title" : {},
#         "acceptCookies" : {},
#         "popUpWindow" : {},
#         "sortButton" : {},
#         "dropDownSort" : {},
#         "jsonIdentifier" : {
#             "name" : "",
#             "description" : "",
#             "multi" : false,
#             "props" : [
#                 {
#                     "attr" : "@type",
#                     "value" : "JobPosting",
#                     "text" : ""
#                 }
#             ]
#         },
#         "expandJd" : {}
#     }
# }