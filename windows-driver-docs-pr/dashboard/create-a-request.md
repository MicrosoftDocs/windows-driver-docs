---
title: Create a request
description: Create a request
MS-HAID:
- 'p\_dashboard.create\_a\_request'
- 'hw\_dashboard.create\_a\_request'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bd26d6a7-c970-47b6-8095-98da63e25603
---

# Create a request


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

Creates a request for file signing, certification, or Driver Update Acceptable (DUA) package. It creates device metadata for submission.

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
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequest)</p></td>
<td><p>A JSON object that describes the detailed metadata of the device signing, certification, or DUA request.</p></td>
<td><p>Body</p></td>
<td><p>Yes</p></td>
<td><p>Not applicable</p></td>
</tr>
<tr class="even">
<td><p><em>Type</em></p></td>
<td><p>A flag that you can use to select the type of signature that Microsoft should apply to the request.</p></td>
<td><p>Query string</p></td>
<td><p>No</p></td>
<td><p>Production</p></td>
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
<td><p><strong>POST</strong></p></td>
<td><p>https://devicesigningservice.cloudapp.net/api/signing/devices</p></td>
</tr>
</tbody>
</table>

 

### <span id="Request_body"></span><span id="request_body"></span><span id="REQUEST_BODY"></span>Request body

``` syntax
{
"ProductName" : "Testing Name",
"MarketingNames" : ["Localized Contoso Toaster"],
"AnnouncementDate" : "2015-01-01T00:00:00",
"PublishingDate" : "2015-11-11T00:00:00",
"OSSelections" : [{
"OS" : "Windows 8",
"ProductType" : "Printer",
"QualificationLevel" : "Signature Only"
}
],

"InitialUploadFileSize":1233334563
}
```

## <span id="Response"></span><span id="response"></span><span id="RESPONSE"></span>Response


The response contains the URL of the submission and the Microsoft Azure Storage secure URI where you upload your package for the device request.

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
<td><p><em>SharedAccessSignatureUri</em></p></td>
<td><p>The [Azure Storage secure URI](http://go.microsoft.com/fwlink/p/?linkid=507706) where you upload your package for the device request.</p></td>
<td><p>Body</p></td>
<td><p>GUID</p></td>
</tr>
<tr class="even">
<td><p><em>Location</em></p></td>
<td><p>The SigningRequest URL, which contains the unique ID for this signing request. For example, https://api.sysdev.microsoft.com/api/signing/devices/&lt;RequestID&gt;</p></td>
<td><p>Location header</p></td>
<td><p>URL</p></td>
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
"http://assetservice.blob.core.windows.net/functional17202312e9e54a5da5549d3a91b51119/contoso/Input/3aaf936f-fdd6-46ae-8378-1fb4e94b64bf.pfx?st=2014-07-25T16%3A58%3A49Z&se=2014-07-25T17%3A58%3A49Z&sr=c&sp=r&sig=K1LTkl2eZxaiR6SIhIj5Vqb7SIJGHHiC4R98s8jOYa0%3D"
```

## <span id="related_topics"></span>Related topics


[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Create%20a%20request%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





