---
title: GDI Halftone Services
description: GDI Halftone Services
ms.assetid: 21112cfc-f7c4-4cce-a9bb-c68d918f5678
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
ms.date: 04/20/2017
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567314" data-raw-source="[&lt;strong&gt;HT_ComputeRGBGammaTable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567314)"><strong>HT_ComputeRGBGammaTable</strong></a></p></td>
<td align="left"><p>Causes GDI to compute device red, green, and blue intensities based on gamma numbers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567317" data-raw-source="[&lt;strong&gt;HT_Get8BPPFormatPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567317)"><strong>HT_Get8BPPFormatPalette</strong></a></p></td>
<td align="left"><p>Returns a halftone palette for use on standard 8-bits per pixel device types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567320" data-raw-source="[&lt;strong&gt;HT_Get8BPPMaskPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567320)"><strong>HT_Get8BPPMaskPalette</strong></a></p></td>
<td align="left"><p>Returns a mask palette for an 8-bits per pixel device type.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567308" data-raw-source="[&lt;strong&gt;HTUI_DeviceColorAdjustment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567308)"><strong>HTUI_DeviceColorAdjustment</strong></a></p></td>
<td align="left"><p>Displays a dialog box that allows a user to adjust a device&#39;s halftoning properties.</p></td>
</tr>
</tbody>
</table>

 

 

 





