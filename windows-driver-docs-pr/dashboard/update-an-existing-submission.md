---
title: Update an existing submission
description: Update an existing submission
ms.assetid: 09d55f98-d915-46a8-a96e-ef414f6e4f18
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Update an existing submission


> [!Important]  
> The dashboard submission REST APIs have been depricated and are no longer be available for use. APIs for driver submissions are under consideration for a future release.
 

Updates the metadata for an existing submission.

## <span id="Request"></span><span id="request"></span><span id="REQUEST"></span>Request


### <span id="Input_parameter"></span><span id="input_parameter"></span><span id="INPUT_PARAMETER"></span>Input parameter

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
<th>Location</th>
<th>Required?</th>
<th>Default if not provided</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestupdate)</p></td>
<td><p>A JSON object that describes the changes to apply to the specified device signing request.</p></td>
<td><p>Body</p></td>
<td><p>Yes</p></td>
<td><p>Not applicable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Example_request"></span><span id="example_request"></span><span id="EXAMPLE_REQUEST"></span>Example request

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Request URI</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>PATCH</strong></p></td>
<td><p>https://devicesigningservice.cloudapp.net/api/signing/devices/&lt;RequestID&gt;</p></td>
</tr>
</tbody>
</table>

 

### <span id="Request_body"></span><span id="request_body"></span><span id="REQUEST_BODY"></span>Request body

``` syntax
{
"RequestID" : "2b70c57a-7898-48dc-b877-4c0541885eb9",
"ProductName" : "Contoso Toaster",
"AnnouncementDate" : "2015-01-01T00:00:00",
"PublishingDate" : "2015-11-11T00:00:00",
"MarketingNames" : [{
"Name" : "Localized Contoso Toaster",
"Locales" : ["en-US"]
}
],
"UploadComplete" : true
}
```

## <span id="Response"></span><span id="response"></span><span id="RESPONSE"></span>Response


### <span id="Status_code"></span><span id="status_code"></span><span id="STATUS_CODE"></span>Status code

<span id="200"></span>200  
200 - OK

<span id="400"></span>400  
400 – Bad Request.

404 – Not Found.

401 – Not Authorized.

 

 





