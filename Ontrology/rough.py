{
    "name" : "Michelin",
    "collection" : "michelin",
    "companyID" : "",
    "clientID" : "",
    "userID" : ObjectId("66336f3dac7972717c13d422"),
    "type" : "Careers Page",
    "website" : "https://jobs.michelin.in",
    "landingPageUrl" : [
        "https://jobs.michelin.in/job-offer-result-list?"
    ],
    "shortJobUrl" : "https://jobs.michelin.in",
    "createdAt" : ISODate("2024-12-04T06:30:40.697Z"),
    "updatedAt" : ISODate("2024-12-04T06:31:33.109Z"),
    "scraperTool" : "Selenium",
    "deleted" : false,
    "browser" : "Google Chrome",
    "headless" : false,
    "searchKeywords" : [],
    "pages" : 0,
    "nextPage" : {
        "pageType" : "by_button",
        "url" : "",
        "pageIncrement" : 0
    },
    "externalSources" : [],
    "automate" : {
        "enabled" : true,
        "startDate" : ISODate("2024-10-17T18:30:00.000Z"),
        "endDate" : ISODate("2025-10-17T18:29:59.999Z"),
        "timingsIn24Format" : [
            "07:00"
        ],
        "timeZone" : "",
        "timeZoneName" : "",
        "timeZoneFullName" : "",
        "userID" : ObjectId("66336f3dac7972717c13d422"),
        "weekDays" : [
            "Tuesday",
            "Wednesday"
        ]
    },
    "pipline" : [
        "Scrape"
    ],
    "elementDetails" : {
        "searchButton" : {},
        "jobURL" : {
            "name" : "",
            "description" : "",
            "multi" : false,
            "props" : [
                {
                    "attr" : "css_selector",
                    "value" : "h1.ds__heading",
                    "text" : ""
                }
            ]
        },
        "nextPage" : {
            "name" : "",
            "description" : "",
            "multi" : false,
            "props" : [
                {
                    "attr" : "css_selector",
                    "value" : " div.career-result-list__pagination-arrow.career-result-list__pagination-arrow--right > svg",
                    "text" : ""
                }
            ]
        },
        "jobCount" : {
            "name" : "",
            "description" : "",
            "multi" : false,
            "props" : [
                {
                    "attr" : "css_selector",
                    "value" : "div.career-result-list__counter",
                    "text" : ""
                }
            ]
        },
        "title" : {},
        "acceptCookies" : {},
        "popUpWindow" : {},
        "sortButton" : {},
        "dropDownSort" : {},
        "jsonIdentifier" : {
            "name" : "",
            "description" : "",
            "multi" : false,
            "props" : [
                {
                    "attr" : "@type",
                    "value" : "JobPosting",
                    "text" : ""
                }
            ]
        },
        "expandJd" : {}
    },

}
