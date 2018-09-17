---
title: GDI Halftone Services
description: GDI Halftone Services
ms.assetid: 21112cfc-f7c4-4cce-a9bb-c68d918f5678
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 

 





