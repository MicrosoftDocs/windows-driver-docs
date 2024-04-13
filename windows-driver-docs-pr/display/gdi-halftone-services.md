---
title: GDI Halftone Services
description: GDI Halftone Services
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-ht_computergbgammatable" data-raw-source="[&lt;strong&gt;HT_ComputeRGBGammaTable&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-ht_computergbgammatable)"><strong>HT_ComputeRGBGammaTable</strong></a></p></td>
<td align="left"><p>Causes GDI to compute device red, green, and blue intensities based on gamma numbers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-ht_get8bppformatpalette" data-raw-source="[&lt;strong&gt;HT_Get8BPPFormatPalette&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-ht_get8bppformatpalette)"><strong>HT_Get8BPPFormatPalette</strong></a></p></td>
<td align="left"><p>Returns a halftone palette for use on standard 8-bits per pixel device types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-ht_get8bppmaskpalette" data-raw-source="[&lt;strong&gt;HT_Get8BPPMaskPalette&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-ht_get8bppmaskpalette)"><strong>HT_Get8BPPMaskPalette</strong></a></p></td>
<td align="left"><p>Returns a mask palette for an 8-bits per pixel device type.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-htui_devicecoloradjustment" data-raw-source="[&lt;strong&gt;HTUI_DeviceColorAdjustment&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-htui_devicecoloradjustment)"><strong>HTUI_DeviceColorAdjustment</strong></a></p></td>
<td align="left"><p>Displays a dialog box that allows a user to adjust a device's halftoning properties.</p></td>
</tr>
</tbody>
</table>

 

