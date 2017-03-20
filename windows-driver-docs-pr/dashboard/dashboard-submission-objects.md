---
title: Dashboard submission objects
description: Dashboard submission objects
MS-HAID:
- 'p\_dashboard.dashboard\_submission\_objects'
- 'hw\_dashboard.dashboard\_submission\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ce17c11-901b-4f8d-8e79-8bf490a94ba7
---

# Dashboard submission objects


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

These objects contain information about the dashboard submissions.

The following list shows the dashboard submission objects:

-   [Asset](#asset)

-   [AssetType](#assettype)

-   [MarketingName](#marketingname)

-   [OSSelection](#osselection)

-   [SigningRequest](#signingrequest)

-   [SigningRequestInfo](#signingrequestinfo)

-   [SigningRequestUpdate](#signingrequestupdate)

## <span id="Asset"></span><span id="asset"></span><span id="ASSET"></span>Asset


The collateral associated with the dashboard submission, such as Hardware Certification Kit (HCK) packages and signed catalogs.

These assets are stored in Azure Storage and can be accessed using the Shared Access Signature (SAS) URI and the [Azure Storage API](http://go.microsoft.com/fwlink/p/?linkid=507706). For more information about downloading assets, see [Create a production device submission](https://msdn.microsoft.com/library/windows/hardware/dn800660.aspx#download).

### <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties

The following table shows the asset properties.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DeviceSigningAssetID</strong></p></td>
<td><p>GUID</p></td>
<td><p>The unique identifier for the asset. Use this property to request an SAS URL to download the asset.</p></td>
</tr>
<tr class="even">
<td><p><strong>Name</strong></p></td>
<td><p>String</p></td>
<td><p>A user-friendly description of the asset.</p></td>
</tr>
<tr class="odd">
<td><p><strong>AssetType</strong></p></td>
<td><p>[AssetType](#assettype)</p></td>
<td><p>An enumeration identifying a specific asset.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Methods"></span><span id="methods"></span><span id="METHODS"></span>Methods

**Get** and **Put** methods are supported on all properties.

### <span id="Example_object"></span><span id="example_object"></span><span id="EXAMPLE_OBJECT"></span>Example object

``` syntax
Asset : {
 "DeviceSigningAssetID" : "4e53d41f-4ccc-481c-bd00-0f73400f5d6a",
 "Name" : "contoso_toaster.hckx",
 "AssetType" : "InitialUpload"
}
```

## <span id="AssetType"></span><span id="assettype"></span><span id="ASSETTYPE"></span>AssetType


An enumeration describing an asset associated with a dashboard submission.

Possible values:

-   InitialUpload – a submission that has been uploaded.

-   SignedFile – a signed file.

## <span id="MarketingName"></span><span id="marketingname"></span><span id="MARKETINGNAME"></span>MarketingName


Name describing your product. These names appear on the [Windows Certified Products List](http://go.microsoft.com/fwlink/p/?linkid=316443) in the SysDev Dashboard.

### <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties

The following table shows the MarketingName properties.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Name</p></td>
<td><p>String</p></td>
<td><p>A custom string describing your product.</p></td>
</tr>
<tr class="even">
<td><p>Locale</p></td>
<td><p>String</p></td>
<td><p>A set of strings defining the locale for your product.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Methods"></span><span id="methods"></span><span id="METHODS"></span>Methods

Get and Put methods are supported on all properties.

### <span id="Example_object"></span><span id="example_object"></span><span id="EXAMPLE_OBJECT"></span>Example object

``` syntax
MarketingName : {
"Name" : "Localized Contoso Toaster",
"Locales" : ["en-US"]
}
```

## <span id="OSSelection"></span><span id="osselection"></span><span id="OSSELECTION"></span>OSSelection


Describes the supported operating systems for your product. It also contains the classification of your submission as listed in the [Hardware Certification Taxonomy](http://go.microsoft.com/fwlink/p/?linkid=264221). You can also use this object to get down-level signatures.

### <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties

The following table shows the **OSSelection** properties.

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
<th>Property name</th>
<th>Type</th>
<th>Description</th>
<th>Required?</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>OS</strong></p></td>
<td><p>String</p></td>
<td><p>The operating system for this product.</p></td>
<td><p>Yes</p></td>
<td><p>Unclassified</p></td>
</tr>
<tr class="even">
<td><p><strong>ProductType</strong></p></td>
<td><p>String</p></td>
<td><p>The product type as listed in the [Hardware Certification Taxonomy](http://go.microsoft.com/fwlink/p/?linkid=264221). You can also find this value in the [Hardware Certification Object Model](http://go.microsoft.com/fwlink/p/?linkid=252800).</p></td>
<td><p>No</p></td>
<td><p>SignatureOnly</p></td>
</tr>
<tr class="odd">
<td><p><strong>QualificationLevel</strong></p></td>
<td><p>String</p></td>
<td><p>A string defining the requested qualification for the specified operating system. Possible values:</p>
<ul>
<li><p><strong>SignatureOnly</strong></p></li>
<li><p><strong>Accepted</strong></p></li>
<li><p><strong>Certified</strong></p></li>
</ul></td>
<td><p>Ni</p></td>
<td><p>SignatureOnly</p></td>
</tr>
</tbody>
</table>

 

### <span id="Methods"></span><span id="methods"></span><span id="METHODS"></span>Methods

**Get** and **Put** methods are supported on all properties.

### <span id="Example_object"></span><span id="example_object"></span><span id="EXAMPLE_OBJECT"></span>Example object

``` syntax
{
"OS" : "Windows 8",
"ProductType" : "Printer",
"QualificationLevel" : "Signature Only"
}
```

## <span id="SigningRequest"></span><span id="signingrequest"></span><span id="SIGNINGREQUEST"></span>SigningRequest


The initial input object for the File Signing Services.

### <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties

The following table shows the asset properties.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Type</th>
<th>Description</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>ProductName</strong></p></td>
<td><p>String</p></td>
<td><p>The primary product name.</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><strong>AnnouncementDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the product will appear on Dashboard reports, such as the Certified Products List and Windows Compatibility Center.</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p><strong>PublishingDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the product will be published to Windows Update.</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p><strong>MarketingNames</strong></p></td>
<td><p>[MarketingName](#marketingname)[]</p></td>
<td><p>The list of marketing names for the product. Each request has one primary name (required), and any number of aliases.</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p><strong>OSSelections</strong></p></td>
<td><p>String</p></td>
<td><p>Describes the supported operating systems for your product. It also contains the classification of your submission as listed in the [Hardware Certification Taxonomy](http://go.microsoft.com/fwlink/p/?linkid=264221). You can also use this object to get down-level signatures.</p></td>
<td></td>
</tr>
<tr class="even">
<td><p><strong>InitialUploadFileSize</strong></p></td>
<td><p>Long</p></td>
<td><p>The length in bytes of the file to be uploaded.</p></td>
<td><p></p></td>
</tr>
<tr class="odd">
<td><p><strong>TestHarnessType</strong></p></td>
<td><p>String</p></td>
<td><p>The type of kit that was used to create this package. Value should be either HLK or HCK.</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

 

### <span id="Methods"></span><span id="methods"></span><span id="METHODS"></span>Methods

**Get** and **Put** methods are supported on all properties.

### <span id="Example_object"></span><span id="example_object"></span><span id="EXAMPLE_OBJECT"></span>Example object

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
"InitialUploadFileSize":1233334563,
“TestHarnessType”:”HLK”
}
```

## <span id="SigningRequestInfo"></span><span id="signingrequestinfo"></span><span id="SIGNINGREQUESTINFO"></span>SigningRequestInfo


Describes a Dashboard submission. You can use this object to determine whether Dashboard processing is complete, select assets for download, or view qualifications that have been granted.

### <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties

The following table shows the **SigningRequestInfo** properties.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>RequestID</strong></p></td>
<td><p>GUID</p></td>
<td><p>The unique identifier for this submission. Use this to access the request through <strong>PATCH</strong> and <strong>GET</strong> service calls.</p></td>
</tr>
<tr class="even">
<td><p><strong>ProductName</strong></p></td>
<td><p>String</p></td>
<td><p>The primary product name.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SubmissionID</strong></p></td>
<td><p>String</p></td>
<td><p>The Dashboard submission ID for the submission.</p></td>
</tr>
<tr class="even">
<td><p><strong>Status</strong></p></td>
<td><p>String</p></td>
<td><p>The processing status of the request.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CreatedDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the request was generated.</p></td>
</tr>
<tr class="even">
<td><p><strong>AnnouncementDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the product will appear on Microsoft reports, such as the [Windows Certified Products List](http://go.microsoft.com/fwlink/p/?linkid=316443) and [Windows Compatibility Center](http://go.microsoft.com/fwlink/p/?linkid=507702).</p></td>
</tr>
<tr class="odd">
<td><p><strong>PublishingDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the product will be published to Windows Update.</p></td>
</tr>
<tr class="even">
<td><p><strong>VerificationReport</strong></p></td>
<td><p>URL</p></td>
<td><p>The location of the Certification Verification Report PDF file.</p></td>
</tr>
<tr class="odd">
<td><p><strong>MarketingNames</strong></p></td>
<td><p>[MarketingName](#marketingname) []</p></td>
<td><p>The list of marketing names for the submission. Each submission has one primary name (required), and any number of aliases in this collection.</p></td>
</tr>
<tr class="even">
<td><p><strong>Assets</strong></p></td>
<td><p>[Asset](#asset)[]</p></td>
<td><p>The list of asset associated with the submission. Assets describe the uploaded packages, signed files, and DUA shell packages.</p></td>
</tr>
<tr class="odd">
<td><p><strong>OSSelections</strong></p></td>
<td><p>String</p></td>
<td><p>Describes the supported operating systems for your product. It also contains the classification of your submission as listed in the [Hardware Certification Taxonomy](http://go.microsoft.com/fwlink/p/?linkid=264221). You can also use this object to get down-level signatures.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Methods"></span><span id="methods"></span><span id="METHODS"></span>Methods

**Get** and **Put** methods are supported on all properties.

### <span id="Example_object"></span><span id="example_object"></span><span id="EXAMPLE_OBJECT"></span>Example object

``` syntax
{
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
"Name" : " Localized Contoso Toaster ",
"Locales" : ["en-US"]
}
],
"Assets" : [{
"DeviceSigningAssetID" : "4e53d41f-4ccc-481c-bd00-0f73400f5d6a",
"Name" : "32.hckx",
"AssetType" : 1
}
]
}
```

## <span id="SigningRequestUpdate"></span><span id="signingrequestupdate"></span><span id="SIGNINGREQUESTUPDATE"></span>SigningRequestUpdate


The object used for updating an existing submission. You can also use this object to mark a submission as UploadComplete to start backend processing.

### <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties

The following table shows the asset properties.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Type</th>
<th>Description</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>RequestID</strong></p></td>
<td><p>GUID</p></td>
<td><p>The unique identifier for this submission. Use this to access the request through <strong>PATCH</strong> and <strong>GET</strong> service calls.</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p><strong>ProductName</strong></p></td>
<td><p>String</p></td>
<td><p>The primary product name.</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p><strong>AnnouncementDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the product will appear on Dashboard reports, such as the Certified Products List and Windows Compatibility Center.</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p><strong>PublishingDate</strong></p></td>
<td><p>DateTime</p></td>
<td><p>The date and time that the product will be published to Windows Update.</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p><strong>MarketingNames</strong></p></td>
<td><p>[MarketingName](#marketingname)[]</p></td>
<td><p>The list of marketing names for the product. Each request has one primary name (required), and any number of aliases.</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p><strong>UploadComplete</strong></p></td>
<td><p>Bool</p></td>
<td><p>A flag specifying when you have successfully uploaded the initial package for this submission. Use [Update an existing submission](https://msdn.microsoft.com/library/windows/hardware/dn800650.aspx) procedure to set this property to TRUE to start backend processing.</p></td>
<td><p>No</p></td>
</tr>
</tbody>
</table>

 

### <span id="Methods"></span><span id="methods"></span><span id="METHODS"></span>Methods

**Get** and **Put** methods are supported on all properties.

### <span id="Example_object"></span><span id="example_object"></span><span id="EXAMPLE_OBJECT"></span>Example object

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Dashboard%20submission%20objects%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




