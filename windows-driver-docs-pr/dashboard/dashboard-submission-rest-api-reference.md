---
title: Dashboard submission REST API reference
description: Dashboard submission REST API reference
MS-HAID:
- 'p\_dashboard.dashboard\_submission\_rest\_api\_reference'
- 'hw\_dashboard.dashboard\_submission\_rest\_api\_reference'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6a01d44b-1bd4-4992-98ee-e8d6813522be
---

# Dashboard submission REST API reference


**Important**  The dashboard submission REST APIs will no longer be available for use as of the end of November 10th, 2016. APIs for driver submissions are under consideration for a future release.

 

The dashboard submission API lets you build certification submissions into your existing development and deployment framework and eliminate manual file submission altogether.

The dashboard submission API is the primary tool for getting files signed by Microsoft, certification validation reports, and Driver Update Acceptable (DUA) shell packages. You can use this API to get production and pre-production signed drivers.

The following table shows the supported operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Create a request](https://msdn.microsoft.com/library/windows/hardware/dn800659.aspx)</p></td>
<td><p>Creates a request for file signing, certification, or Driver Update Acceptable (DUA).</p></td>
</tr>
<tr class="even">
<td><p>[List all submissions](https://msdn.microsoft.com/library/windows/hardware/dn800653.aspx)</p></td>
<td><p>Returns all device submissions uploaded by your organization.</p></td>
</tr>
<tr class="odd">
<td><p>[Get metadata for an existing submission](https://msdn.microsoft.com/library/windows/hardware/dn800658.aspx)</p></td>
<td><p>Returns the metadata for an existing device request. Use this operation to determine the status of a submission.</p></td>
</tr>
<tr class="even">
<td><p>[Get assets for a submission](https://msdn.microsoft.com/library/windows/hardware/dn800652.aspx)</p></td>
<td><p>Returns an array of all assets associated with a device request. Use this operation to get signed files, certificate validation reports, and DUA shell packages for a device request.</p></td>
</tr>
<tr class="odd">
<td><p>[Get a specific asset within a submission](https://msdn.microsoft.com/library/windows/hardware/dn800656.aspx)</p></td>
<td><p>Returns a specified asset associated with your device request. Use this operation to get signed files, certificate validation reports, and DUA shell packages for a device request.</p></td>
</tr>
<tr class="even">
<td><p>[Update an existing submission](https://msdn.microsoft.com/library/windows/hardware/dn800650.aspx)</p></td>
<td><p>Updates the metadata for an existing device request.</p></td>
</tr>
</tbody>
</table>

 

The following table shows the dashboard submission objects:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Object</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#asset)</p></td>
<td><p>The collateral associated with the dashboard submission, such as Hardware Certification Kit (HCK) packages and signed catalogs.</p></td>
</tr>
<tr class="even">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#assettype)</p></td>
<td><p>An enumeration describing an asset associated with a dashboard submission.</p></td>
</tr>
<tr class="odd">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#marketingname)</p></td>
<td><p>The name describing your product. These names appear on the Windows Certified Products List in the SysDev dashboard.</p></td>
</tr>
<tr class="even">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#osselection)</p></td>
<td><p>The list of supported operating systems for your product. It also contains the classification of your submission as listed in the [Hardware Certification Taxonomy](http://download.microsoft.com/download/2/3/6/23662F33-71E8-43C1-8547-5DE49B0374AB/windows-hck-product-type-matrix.zip). You can also use this object to get down-level signatures.</p></td>
</tr>
<tr class="odd">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequest)</p></td>
<td><p>The initial input object in the File Signing Services submission.</p></td>
</tr>
<tr class="even">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestinfo)</p></td>
<td><p>A Dashboard submission. You can use this object to determine whether Dashboard processing is complete, select assets for download, or view qualifications that have been granted.</p></td>
</tr>
<tr class="odd">
<td><p>[Dashboard submission objects](https://msdn.microsoft.com/library/windows/hardware/dn800651.aspx#signingrequestupdate)</p></td>
<td><p>The object used for updating an existing submission. You can also use this object to mark a submission as UploadComplete to start backend processing.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Dashboard%20submission%20REST%20API%20reference%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




