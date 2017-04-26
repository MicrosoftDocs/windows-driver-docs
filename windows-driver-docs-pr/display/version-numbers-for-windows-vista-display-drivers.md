---
title: Version Numbers for WDDM Drivers
description: Version Numbers for WDDM Drivers
ms.assetid: 14608626-cd01-4756-8329-187153a8b99a
keywords:
- display driver model WDK Windows Vista , version numbers
- Windows Vista display driver model WDK , version numbers
- version numbers WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Version%20Numbers%20for%20WDDM%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




