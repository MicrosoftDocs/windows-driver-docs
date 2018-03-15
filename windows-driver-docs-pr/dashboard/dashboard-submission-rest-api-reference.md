---
title: Dashboard submission REST API reference
description: Dashboard submission REST API reference
ms.assetid: 6a01d44b-1bd4-4992-98ee-e8d6813522be
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Dashboard submission REST API reference


> [!Important]  
> The dashboard submission REST APIs have been depricated and are no longer be available for use. APIs for driver submissions are under consideration for a future release.

 

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

 

 

 





