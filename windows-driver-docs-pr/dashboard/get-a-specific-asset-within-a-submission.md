---
title: Get a specific asset within a submission
description: Get a specific asset within a submission
MS-HAID:
- 'p\_dashboard.get\_a\_specific\_asset\_within\_a\_submission'
- 'hw\_dashboard.get\_a\_specific\_asset\_within\_a\_submission'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9e0c15cc-a551-4c9e-9679-3201f28b2936
---

# Get a specific asset within a submission


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

Returns a specified asset associated with your device request. Use this to get signed files, certificate validation reports, and DUA shell packages for a device request.

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
<td><p><em>RequestID</em></p></td>
<td><p>Identifier of the [Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestinfo) that you want to retrieve the asset from.</p></td>
<td><p>URL</p></td>
<td><p>Yes</p></td>
<td><p>Not applicable</p></td>
</tr>
<tr class="even">
<td><p><em>AssetID</em></p></td>
<td><p>The identifier of the [Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#asset) that you want to retrieve.</p></td>
<td><p>URL</p></td>
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
<td><p><strong>GET</strong></p></td>
<td><p>https://devicesigningservice.cloudapp.net/api/signing/devices/&lt;RequestID&gt;/assets/&lt;AssetID&gt;</p></td>
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
<td><p><em>SigningRequestInfo</em></p></td>
<td><p>The [Azure Storage secure URI](http://go.microsoft.com/fwlink/p/?linkid=507706) for downloading the asset.</p></td>
<td><p>Locationheader</p></td>
<td><p>URL</p></td>
</tr>
<tr class="even">
<td><p><em>Asset</em></p></td>
<td><p>The asset to download.</p></td>
<td><p>Body</p></td>
<td><p>Asset</p></td>
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
{
{
 "DeviceSigningAssetID" : "4e53d41f-4ccc-481c-bd00-0f73400f5d6a",
 "Name" : "contoso_toaster.hckx",
 "AssetType" : 1
},
“SharedAccessSignatureUri”:http://assetservice.blob.core.windows.net/functional17202312e9e54a5da5549d3a91b51119/Contoso/Input/3aaf936f-fdd6-46ae-8378-1fb4e94b64bf.pfx?st=2014-07-25T16%3A58%3A49Z&se=2014-07-25T17%3A58%3A49Z&sr=c&sp=r&sig=K1LTkl2eZxaiR6SIhIj5Vqb7SIJGHHiC4R98s8jOYa0%3D}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Get%20a%20specific%20asset%20within%20a%20submission%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




