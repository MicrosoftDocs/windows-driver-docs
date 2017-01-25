---
title: Update an existing submission
description: Update an existing submission
MS-HAID:
- 'p\_dashboard.update\_an\_existing\_submission'
- 'hw\_dashboard.update\_an\_existing\_submission'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 09d55f98-d915-46a8-a96e-ef414f6e4f18
---

# Update an existing submission


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Update%20an%20existing%20submission%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




