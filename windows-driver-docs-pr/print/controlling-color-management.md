---
title: Controlling Color Management
author: windows-driver-content
description: Controlling Color Management
MS-HAID:
- 'printicm\_3e18342e-a0b6-4568-85b4-161e4a801806.xml'
- 'print.controlling\_color\_management'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cb210b8d-fee1-4904-8c50-f03d2445085e
keywords: ["color management WDK print , controlling"]
---

# Controlling Color Management


## <a href="" id="ddk-controlling-color-management-gg"></a>


Color management for a printer can be controlled by an application, the system (GDI), the driver, or device hardware. The driver determines which component is managing color correction by examining flags within the [**BRUSHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff538261) and [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) structures that are passed to its implementations of graphics DDI drawing functions. The following flags are defined:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BR_DEVICE_ICM in BRUSHOBJ</p>
<p>XO_DEVICE_ICM in XLATEOBJ</p></td>
<td><p>Color management is being performed by the driver or the device.</p></td>
</tr>
<tr class="even">
<td><p>BR_HOST_ICM in BRUSHOBJ</p>
<p>XO_HOST_ICM in XLATEOBJ</p></td>
<td><p>Color management is being performed by the application or the system (GDI).</p></td>
</tr>
</tbody>
</table>

 

The following topics describe driver support for these color management scenarios:

[System Control](system-control.md)

[Driver Control and Device Control](driver-control-and-device-control.md)

[Supporting CMYK Color Space](supporting-cmyk-color-space.md)

[Color Management of JPEG and PNG Images](color-management-of-jpeg-and-png-images.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Controlling%20Color%20Management%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


