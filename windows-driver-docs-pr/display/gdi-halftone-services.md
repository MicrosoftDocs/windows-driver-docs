---
title: GDI Halftone Services
description: GDI Halftone Services
ms.assetid: 21112cfc-f7c4-4cce-a9bb-c68d918f5678
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Halftone Services


## <span id="ddk_gdi_halftone_services_gg"></span><span id="DDK_GDI_HALFTONE_SERVICES_GG"></span>


GDI Halftone support includes the services listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>HT_ComputeRGBGammaTable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567314)</p></td>
<td align="left"><p>Causes GDI to compute device red, green, and blue intensities based on gamma numbers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>HT_Get8BPPFormatPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567317)</p></td>
<td align="left"><p>Returns a halftone palette for use on standard 8-bits per pixel device types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>HT_Get8BPPMaskPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567320)</p></td>
<td align="left"><p>Returns a mask palette for an 8-bits per pixel device type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>HTUI_DeviceColorAdjustment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567308)</p></td>
<td align="left"><p>Displays a dialog box that allows a user to adjust a device's halftoning properties.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Halftone%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




