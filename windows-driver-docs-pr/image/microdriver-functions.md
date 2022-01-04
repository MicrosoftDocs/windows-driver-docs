---
title: Microdriver Functions
description: Microdriver Functions
ms.date: 04/20/2017
---

# Microdriver Functions





The WIA Flatbed Driver responds to requests from the WIA service by calling the WIA microdriver functions. These functions must be implemented by every vendor-supplied microdriver and consist of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-microentry" data-raw-source="[&lt;strong&gt;MicroEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-microentry)"><strong>MicroEntry</strong></a></p></td>
<td><p>Responds to commands sent by the WIA Flatbed Driver.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-scan" data-raw-source="[&lt;strong&gt;Scan&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-scan)"><strong>Scan</strong></a></p></td>
<td><p>Reads data from the device and returns the data to the WIA Flatbed Driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-setpixelwindow" data-raw-source="[&lt;strong&gt;SetPixelWindow&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-setpixelwindow)"><strong>SetPixelWindow</strong></a></p></td>
<td><p>Sets the area to be scanned.</p></td>
</tr>
</tbody>
</table>

 

