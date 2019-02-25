---
title: Controlling Color Management
description: Controlling Color Management
ms.assetid: cb210b8d-fee1-4904-8c50-f03d2445085e
keywords:
- color management WDK print , controlling
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling Color Management





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

 

 




