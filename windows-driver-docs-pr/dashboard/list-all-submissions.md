---
title: List all submissions
description: List all submissions
MS-HAID:
- 'p\_dashboard.list\_all\_submissions'
- 'hw\_dashboard.list\_all\_submissions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5e7a803d-7764-41fe-a503-a66e7069005d
---

# List all submissions


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

Returns all device submissions uploaded by your organization.

## <span id="Request"></span><span id="request"></span><span id="REQUEST"></span>Request


### <span id="Input_parameter"></span><span id="input_parameter"></span><span id="INPUT_PARAMETER"></span>Input parameter

None

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
<td><p><strong>GET</strong></p></td>
<td><p>https://devicesigningservice.cloudapp.net/api/signing/devices</p></td>
</tr>
</tbody>
</table>

 

## <span id="Response"></span><span id="response"></span><span id="RESPONSE"></span>Response


### <span id="Response_parameter"></span><span id="response_parameter"></span><span id="RESPONSE_PARAMETER"></span>Response parameter

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
<th>Location</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestinfo)</p></td>
<td><p>An array of objects that contains all of your device signing requests.</p></td>
<td><p>Body</p></td>
<td><p>SigningRequestInfo</p></td>
</tr>
</tbody>
</table>

 

### <span id="Status_code"></span><span id="status_code"></span><span id="STATUS_CODE"></span>Status code

<span id="200"></span>200  
200 - OK

<span id="400"></span>400  
400 – Bad Request.

404 – Not Found.

401 – Not Authorized.

### <span id="Example_response"></span><span id="example_response"></span><span id="EXAMPLE_RESPONSE"></span>Example response

``` syntax
[{
"RequestID" : "2b70c57a-7898-48dc-b877-4c0541885eb9",
"ProductName" : "Contoso Toaster",
"SubmissionID" : 33,
"Status" : "Approved",
"CreatedDate" : "2014-01-01T00:00:00",
"AnnouncementDate" : "2015-01-01T00:00:00",
"PublishingDate" : "2015-11-11T00:00:00",
"VerificationReport" : "https://sysdev.microsoft.com/LogoVerificationReport.aspx?sid=32",
"OSSelections" : [{
"OS" : "Windows 8",
"ProductType" : "Printer",
"QualificationLevel" : "Signature Only"
}
],
"MarketingNames" : [{
"Name" : "Localized Contoso Toaster ",
"Locales" : ["en-US"]
}
],
"Assets" : [{
"DeviceSigningAssetID" : "4e53d41f-4ccc-481c-bd00-0f73400f5d6a",
"Name" : "32.hckx",
"AssetType" : 1
}
]
},
{
"RequestID" : "e1d8215e-0523-487b-8ec8-a2838d7a4aae",
"ProductName" : "Contoso Oven",
"SubmissionID" : 33,
"Status" : "Approved",
"CreatedDate" : "2014-01-01T00:00:00",
"AnnouncementDate" : "2015-01-01T00:00:00",
"PublishingDate" : "2015-11-11T00:00:00",
"VerificationReport" : "https://sysdev.microsoft.com/LogoVerificationReport.aspx?sid=32",
"OSSelections" : [{
"OS" : "Windows 8",
"ProductType" : "Printer",
"QualificationLevel" : "Signature Only"
}
],
"MarketingNames" : [{
"Name" : "Localized Contoso Oven",
"Locales" : ["en-US"]
}
],
"Assets" : [{
"DeviceSigningAssetID" : "2b70c57a-7898-48dc-b877-4c0541885eb9",
"Name" : "32.hckx",
"AssetType" : 1
}
]
}]
```

## <span id="related_topics"></span>Related topics


[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20List%20all%20submissions%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





