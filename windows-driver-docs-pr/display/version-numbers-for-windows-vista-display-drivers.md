---
title: Version Numbers for WDDM Drivers
description: Version Numbers for WDDM Drivers
ms.assetid: 14608626-cd01-4756-8329-187153a8b99a
keywords:
- display driver model WDK Windows Vista , version numbers
- Windows Vista display driver model WDK , version numbers
- version numbers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Version Numbers for WDDM Drivers


To ensure that a display driver that conforms to the Windows Display Driver Model (WDDM) or the [Windows 2000 display driver model (XDDM)](windows-2000-display-driver-model-design-guide.md) runs on Microsoft Windows with a specific version of Microsoft DirectX, you must apply an appropriate version number to that driver. If a vendor distributes a display driver with the wrong version number or a version number that uses the wrong format, end users will encounter difficulties when they install any DirectX application.

**Note**   The **DriverVer** directive provides a way to add version information for the driver package, including the driver file and the INF file itself, to the INF file. By using the **DriverVer** directive, you can safely and definitively replace driver packages by future versions of the same package. For more information about this directive, see [**INF DriverVer Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394).

 

This table gives examples of the range of version numbers that are appropriate for vendor-supplied display drivers that conform to WDDM for compatibility with various versions of DirectX. \\

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target system</th>
<th align="left">Range of version numbers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WDDM and DirectX 9.0-compatible display drivers</p></td>
<td align="left"><p>7.14.01.0000 - 7.14.99.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>WDDM and DirectX 10.0-compatible display drivers</p></td>
<td align="left"><p>7.15.01.0000 - 7.15.99.9999</p></td>
</tr>
</tbody>
</table>

 

This table gives the range of version numbers that are appropriate for vendor-supplied display drivers that conform to the [Windows 2000 display driver model](windows-2000-display-driver-model-design-guide.md) for compatibility with DirectX 9.0.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target system</th>
<th align="left">Range of version numbers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>XDDM and DirectX 9.0-compatible display drivers</p></td>
<td align="left"><p>6.14.01.0000 - 6.14.99.9999</p></td>
</tr>
</tbody>
</table>

 

For more information about versioning for display drivers, see [Version Numbers for Display Drivers](version-numbers-for-display-drivers.md).

 

 





