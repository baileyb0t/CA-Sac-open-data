# CA-Sac-open-data
processes data for Sacramento city and county obtained from the Sacramento Open Data Portal and/or California Public Records Act requests.

# Computer-Aided Dispatch (CAD)
From City of Sacramento OpenData portal using keyword search for "dispatch": https://data.cityofsacramento.org/search?collection=dataset&q=dispatch

# Records Management Systems (RMS)
Received via PRA request to Sacramento Police Department: https://pdcityofsacramentoca.nextrequest.com/requests/24-748

# Notes
### Sourcing the data
As described in Request 24-748, when I initially searched for the CAD and RMS tables, neither were available in the City or County's OpenData portal.

After some back and forth with SacPD related to my request, the RMS tables were uploaded to the SacPD PRA portal, but the CAD tables were not included in the responsive records. I checked the city and county portals again at that time and noticed the CAD tables appeared in the City's portal, and so downloaded those files. Although there were not as many years uploaded as I had requested, SacPD had closed the request (Request 24-748) and did not respond to follow-up message under that original request, even though it appeared from their language that they intended to upload the CAD tables to the PRA portal and may have accidentally forgotten ("Further information on the CAD files: The dispatch date/time field was not available for the first several years of our current CAD system. That field starts to populate in later years." but no CAD files attached).

I submitted a new PRA request to SacPD, Request 24-989, which referenced Request 24-748 and the lack of CAD files available in the department response, but after 10 days the department responded with, "Can you please explain what you mean by CAD tables?" Seemingly having ignored the language of the request and/or the referenced prior request that contained a full explanation of what I was looking for from the department (or the County or City OpenData portal, which is intended to have both the RMS and CAD data available for download). My original request took more than 30 days of follow up and clarification until the department gave me a partial response, and this question from the department signaled that I was in for another round of delays and weeks of hovering over the PRA portal before I might get the rest of the CAD files.

So, I let it go and proceeded with the RMS tables received from PRA request and the 6 or so years of CAD data from the City of Sacramento OpenData portal. As of 11 August 2024, the publicly available CAD files go back as early as 2019 and the responsive RMS tables go back as early as 2004. There are no RMS tables available to download from the city or county OpenData portals.

### Field interpretation
In a follow-up to my original request, I specified what fields I was looking for and requested a data dictionary be included in the responsive records so that I could know how to interpret the fields in the department generated data. Here is the language of that follow up:

>From the structured database for the Computer Aided Dispatch (CAD) system, I would like a copy including these fields:
> 
> Unique call or event ID
> Date of the call
> Date of dispatch
> Unit or beat dispatched
> District or beat the call came from
> Priority code assigned to the call
> Type of call or service requested (initial and final if these are separate fields)
> Narrative of the call/caller
> An indication of whether the call originated from an actual phone call for help or from another avenue outside the call center
> 
> From the structured databased for the Records Management Systems (RMS), I would like a copy of the data including these fields:
> 
> Unique incident ID
> Date of incident or report
> Date of officer arrival
> Date of arrest if any
> District or beat of the incident
> Neighborhood of the incident
> Demographic information of the subject of the incident or arrest, including race, ethnicity, age, sex, and gender.
> First and last name of the investigator assigned
> Status of the incident or investigation
> Type of incident
> Any UCR or NIBRS codes associated with the incident or investigation (initial and current if these are separate)
> Charges booked if there was an arrest
> Any other fields related to the conclusion of the investigation, such as whether a missing person was located or whether an arrest led to DA action.
> 
> Please include a dictionary of what fields mean and how they are collected so I can be sure to accurately reference the data.

No data dictionary was included in the uploaded responsive records for either the RMS or CAD databases.

The [About](https://data.cityofsacramento.org/datasets/SacCity::sacramento-call-for-service-data-2020/about) page for the CAD data in the City's Open Data portal has an Attributes list that names every field and corresponding data type, and some fields have a plot available to view. However, no details on how the data is generated or how to appropriately interpret any of the fields is present. There is a line in the description, "For more information please visit the [Public Safety Open Data page](https://experience.arcgis.com/experience/a98f1218330f41cca325a1d6a950523b)." Which redirects to a [login page](https://www.arcgis.com/sharing/rest/oauth2/authorize?client_id=experienceBuilder&response_type=token&expiration=20160&redirect_uri=https%3A%2F%2Fexperience.arcgis.com%2Fcdn%2F2627%2Fjimu-core%2Foauth-callback.html%3FclientId%3DexperienceBuilder%26portal%3Dhttps%3A%2F%2Fwww.arcgis.com%2Fsharing%2Frest%2F%26popup%3Dfalse%26isInPortal%3Dfalse%26isDevEdition%3Dfalse%26isOutOfExb%3Dfalse%26mountPath%3D%2F%26enablePkce%3Dfalse%26fromUrl%3Dhttps%253A%252F%252Fexperience.arcgis.com%252Fexperience%252Fa98f1218330f41cca325a1d6a950523b%26redirectUri%3Dhttps%253A%252F%252Fexperience.arcgis.com%252Fcdn%252F2627%252Fjimu-core%252Foauth-callback.html%253FclientId%253DexperienceBuilder%2526portal%253Dhttps%253A%252F%252Fwww.arcgis.com%252Fsharing%252Frest%252F%2526popup%253Dfalse%2526isInPortal%253Dfalse%2526isDevEdition%253Dfalse%2526isOutOfExb%253Dfalse%2526mountPath%253D%252F%2526enablePkce%253Dfalse%2526fromUrl%253Dhttps%25253A%25252F%25252Fexperience.arcgis.com%25252Fexperience%25252Fa98f1218330f41cca325a1d6a950523b&state=%7B%22id%22%3A%22KPHYs6FsKUSY0cyneBNKcCt8-lTlGtcOKOSywLV6HAI%22%2C%22originalUrl%22%3A%22https%3A%2F%2Fexperience.arcgis.com%2Fexperience%2Fa98f1218330f41cca325a1d6a950523b%22%7D&locale=&style=&showSignupOption=true&signupType=esri&force_login=false) I do not have access to.

Since the RMS data is not publicly available, I presume I can only find a data dictionary by contacting SacPD and asking for it again. I have not submitted a request for this supplementary information for either database yet.

## JIC
---

**Here is the initial message to SacPD in Request 24-748:**

> Pursuant to the California Public Records Act, I am trying to obtain a copy of the Sacramento Police Department's Computer Aided Dispatch (CAD) and Records Management Systems (RMS) data.
>
> According to the Dispatch and Crime Data Portals page, these are available for download from the Open Data Portal, but I am unable to locate the CAD or RMS data in the Open Data Portals for both the city and county of Sacramento. Specifically, the keywords "crime", "dispatch", "police", and "record" on both the city and county open data portals do not yield the CAD or RMS tables.
>
> I would like each database copy to be made available as an Excel (.xlsx) file, if possible.


**The following was included as additional information:**
- Date Range From/To:
  - 01/01/2000 to present
- Address or Location(s):
  - No data entered
- Report Number:
  - No data entered
---

**Here is the initial message to SacPD in Request 24-989:**

>Hi there,
>
> I submitted Request 24-748 for a copy of the RMS and CAD tables that are supposed to be available in the Open Data Portal but are not. I received the RMS files in the response to that request and the CAD files were mentioned, but no CAD data was shared.
>
> Please provide a copy of the structured CAD data as described in Request 24-748 and, if possible, as Excel file(s). If my request is denied, please provide a reference to the part of the PRA used to justify the denial.
>
> Thank you!


**The following was included as additional information:**
- Date Range From/To:
  - 01/01/2000 to present
- Address or Location(s):
  - No data entered
- Report Number:
  - No data entered

---

I have also saved PDF screenshots of the PRA portal detailing the exchange between myself and SacPD, should the portal or those requests become unavailable.
