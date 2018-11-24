---
title: Device Metadata Error Codes
description: Device Metadata Error Codes
ms.assetid: 7ca3b9d3-8e7d-4421-affa-bddea2d4c262
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Metadata Error Codes


Starting with Windows 7, the operating system logs the following error codes within events that are related to the download and processing of device metadata packages. These events are managed by the Event Tracing for Windows (ETW) service and can be viewed by using Event Viewer. For more information about these events, see [Debugging Device Metadata Packages By Using Event Viewer](debugging-device-metadata-packages-by-using-event-viewer.md).

<a href="" id="windows-metadata-and-internet-services--wmis--errors--200000xx-"></a>Windows Metadata and Internet Services (WMIS) Errors (200000xx)  
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>20000021</p></td>
<td align="left"><p>The request does not contain a device metadata request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>20000022</p></td>
<td align="left"><p>The request batch size exceeds the maximum allowed value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>20000023</p></td>
<td align="left"><p>The locale value is invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>20000024</p></td>
<td align="left"><p>The request does not contain valid header information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>20000025</p></td>
<td align="left"><p>The request format is invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>20000031</p></td>
<td align="left"><p>An error occurred at the service side when processing the request.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="device-metadata-retrieval-client--dmrc--errors--0x400000xx-"></a>Device Metadata Retrieval Client (DMRC) Errors (0x400000xx)  
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>40000011</p></td>
<td align="left"><p>There is no local metadata cache.</p></td>
</tr>
<tr class="even">
<td align="left"><p>40000012</p></td>
<td align="left"><p>The structure (folders) in the local metadata cache is not correct.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>40000021</p></td>
<td align="left"><p>There is no local metadata store.</p></td>
</tr>
<tr class="even">
<td align="left"><p>40000022</p></td>
<td align="left"><p>The structure (folders) in the local metadata store is corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>40000031</p></td>
<td align="left"><p>The DMRC index data is missing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>40000032</p></td>
<td align="left"><p>The DMRC index data is corrupted.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="device-metadata-package-errors--0x500000xx-"></a>Device Metadata Package Errors (0x500000xx)  
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>50000011</p></td>
<td align="left"><p>The<em>.devicemetadata-ms</em> cabinet (<em>cab</em>) file is corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>50000012</p></td>
<td align="left"><p>The <em>.devicemetadata-ms</em> cab file does not have correct device metadata structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>50000021</p></td>
<td align="left"><p><em>PackageInfo.xml</em> is missing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>50000022</p></td>
<td align="left"><p><em>PackageInfo.xml</em> is not well-formed and cannot be parsed.</p>
<div class="alert">
<strong>Note</strong>   This error code includes the cases where either the <em>PackageInfo.xml</em> document is missing required elements, or one or more of its elements are not valid based on the syntax of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549614" data-raw-source="[PackageInfo XML Schema](https://msdn.microsoft.com/library/windows/hardware/ff549614)">PackageInfo XML Schema</a>.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td align="left"><p>50000031</p></td>
<td align="left"><p><em>DeviceInfo.xml</em> is missing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>50000032</p></td>
<td align="left"><p><em>DeviceInfo.xml</em> is not well-formed and cannot be parsed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>50000033</p></td>
<td align="left"><p><em>DeviceInfo.xml</em> is missing required elements.</p></td>
</tr>
<tr class="even">
<td align="left"><p>50000034</p></td>
<td align="left"><p>Elements in <em>DeviceInfo.xml</em> are not valid based on the XML schema definition.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>50000041</p></td>
<td align="left"><p><em>WindowsInfo.xml</em> is missing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>50000042</p></td>
<td align="left"><p><em>WindowsInfo.xml</em> is not well-formed and cannot be parsed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>50000043</p></td>
<td align="left"><p><em>WindowsInfo.xml</em> is missing required elements.</p></td>
</tr>
<tr class="even">
<td align="left"><p>50000044</p></td>
<td align="left"><p>Elements in <em>WindowsInfo.xml</em> are not valid based on the XML schema definition.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="wmis-query--0x7000xxxx-"></a>WMIS Query (0x7000xxxx)  
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>70000408</p></td>
<td align="left"><p>The WMIS server is not down, but the request timed out.</p></td>
</tr>
<tr class="even">
<td align="left"><p>70000500</p></td>
<td align="left"><p>The WMIS server returned an internal error, but a detailed error code is not available.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>70000503</p></td>
<td align="left"><p>The WMIS server is busy and cannot service the request.</p></td>
</tr>
</tbody>
</table>

 

 

 





