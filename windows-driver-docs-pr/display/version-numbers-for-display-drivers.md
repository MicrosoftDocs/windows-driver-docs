---
title: Version Numbers for Display Drivers
description: Version Numbers for Display Drivers
ms.assetid: 73d26532-61c1-45d1-a388-7c0befc53487
keywords:
- version numbers WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Version Numbers for Display Drivers


## <span id="ddk_ensuring_correct_version_numbers_gg"></span><span id="DDK_ENSURING_CORRECT_VERSION_NUMBERS_GG"></span>


To ensure that the end user is able to use a display driver on a specific operating system and with a specific version of DirectX, an appropriate version number must be applied to that driver. With DirectX, version numbers have become very important for device drivers. If a device driver is shipped with the wrong version number or a version number that uses the wrong format, the end user will encounter difficulties when any DirectX application is installed.

**Note** The **DriverVer** directive provides a way to add version information for the driver package, including the driver file and the INF file itself, to the INF file. By using and updating the **DriverVer** directive, driver packages can be safely and definitively replaced by future versions of the same package. For more information about this directive, see INF DriverVer Directive in the Device Installation section of the Windows Driver Kit (WDK) documentation.

The following table gives the range of version numbers appropriate for IHV- or OEM-supplied drivers for compatibility with various versions of DirectX.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target System</th>
<th align="left">Version Number
<div>
 
</div>
From:</th>
<th align="left">Version Number
<div>
 
</div>
Up Through:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 98-only drivers (DirectX5)</p></td>
<td align="left"><p>4.05.00.0000</p></td>
<td align="left"><p>4.05.00.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectX 1.0-compatible drivers</p></td>
<td align="left"><p>4.02.00.0095</p></td>
<td align="left"><p>4.03.00.1096</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DirectX 2.0-compatible drivers</p></td>
<td align="left"><p>4.03.00.1096</p></td>
<td align="left"><p>4.03.00.2030</p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectX 3.0-compatible drivers</p></td>
<td align="left"><p>4.03.00.2030</p></td>
<td align="left"><p>4.04.00.0000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DirectX 5.0-compatible drivers</p></td>
<td align="left"><p>4.10.10.0000</p></td>
<td align="left"><p>4.10.10.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>DirectX 6.0-compatible drivers</p></td>
<td align="left"><p>4.11.10.0000</p></td>
<td align="left"><p>4.11.10.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows 98/Me DirectX 7.0-compatible drivers</p></td>
<td align="left"><p>4.12.10.0000</p></td>
<td align="left"><p>4.12.10.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 2000 DirectX 7.0-compatible drivers</p></td>
<td align="left"><p>5.12.10.0000</p></td>
<td align="left"><p>5.12.10.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows XP and later DirectX 7.0-compatible drivers</p></td>
<td align="left"><p>6.12.10.0000</p></td>
<td align="left"><p>6.12.10.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 98/Me DirectX 8.0-compatible drivers</p></td>
<td align="left"><p>4.13.10.0000</p></td>
<td align="left"><p>4.13.10.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows 2000 DirectX 8.0-compatible drivers</p></td>
<td align="left"><p>5.13.10.0000</p></td>
<td align="left"><p>5.13.10.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP and later DirectX 8.0-compatible drivers</p></td>
<td align="left"><p>6.13.10.0000</p></td>
<td align="left"><p>6.13.10.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows 98/Me DirectX 9.0-compatible drivers</p></td>
<td align="left"><p>4.14.10.0000</p></td>
<td align="left"><p>4.14.10.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 2000 DirectX 9.0-compatible drivers</p></td>
<td align="left"><p>5.14.10.0000</p></td>
<td align="left"><p>5.14.10.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows XP and later DirectX 9.0-compatible drivers</p></td>
<td align="left"><p>6.14.10.0000</p></td>
<td align="left"><p>6.14.10.9999</p></td>
</tr>
</tbody>
</table>

 

**Note**   The DirectX 9.0 DDK documentation indicated that the version number for a Windows XP and later DirectX-compatible driver must be from 6.*nn*.01.0000 to 6.*nn*.01.9999. However, to support legacy WHQL manual test specifications, the documentation also indicated that the version number could be from 6.*nn*.10.0000 to 6.*nn*.10.9999.
Because of this legacy WHQL requirement, some DirectX applications required a display driver version number of *n*.*nn*.10.*nnnn*. If a display driver's version number was switched from *n*.*nn*.10.*nnnn* to *n*.*nn*.01.*nnnn* so that it more accurately conformed to the DirectX 9.0 DDK documentation requirement, such applications might not run because they would interpret the driver as an earlier version.

Therefore, a display driver's version number should be set to *n*.*nn*.10.*nnnn*.

 

For device drivers that do not support DirectX, the version number must be greater than 4.00.00.0095 and less than 4.02.00.0095. For example, if a display device driver is a Windows 3.1 display driver or a Windows 95-only display driver, a version number of 4.01.00.0000 would be correct.

Conversely, a version number of 4.03.00.0000 for this driver would be incorrect. Device drivers that support DirectX on Windows 95 only should have a version number equal to or greater than 4.02.00.0095 and less than 4.04.00.0000.

### <span id="storing_internal_version_numbers"></span><span id="STORING_INTERNAL_VERSION_NUMBERS"></span>Storing Internal Version Numbers

In addition to the format that Microsoft requires for the version number, many vendors have expressed the desire to store an internal version number for product support and testing purposes. Every DirectX driver has one version number that is stored in duplicate: one binary version stored as two DWORDs, and one string version. The binary version cannot be modified.

The string version, however, can be appended in the following way:

1.  The vendor creates a version number, as described earlier in this article. This version number is used "as is" in the binary version number.

2.  The vendor uses this version number as the basis for the string version number. If desired, a vendor-specific version string can be appended to the existing version number to form the complete string version number. The vendor-specific string and the version number are separated by a "-" (hyphen character).

For example, if "4.03.00.2100" is the version number for a DirectX-compliant display driver, and the vendor uses the "xx.xx.xx" number format internally, then the combined string version number in the driver is "4.03.00.2100-xx.xx.xx".

When the customer checks the version number of the driver (by right-clicking on the file in Windows Explorer, choosing **Properties**, and then clicking the **Version** tab), Windows displays the string version. The vendor's product support should be able to identify the vendor-specific portion of the version number if it exists and take appropriate action.

 

 





