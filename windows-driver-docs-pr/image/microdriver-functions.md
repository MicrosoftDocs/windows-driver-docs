---
title: Microdriver Functions
description: Microdriver Functions
ms.assetid: 491b954a-8ffa-4899-8c7d-0aee409f4742
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamicro/nf-wiamicro-microentry" data-raw-source="[&lt;strong&gt;MicroEntry&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamicro/nf-wiamicro-microentry)"><strong>MicroEntry</strong></a></p></td>
<td><p>Responds to commands sent by the WIA Flatbed Driver.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamicro/nf-wiamicro-scan" data-raw-source="[&lt;strong&gt;Scan&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamicro/nf-wiamicro-scan)"><strong>Scan</strong></a></p></td>
<td><p>Reads data from the device and returns the data to the WIA Flatbed Driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamicro/nf-wiamicro-setpixelwindow" data-raw-source="[&lt;strong&gt;SetPixelWindow&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamicro/nf-wiamicro-setpixelwindow)"><strong>SetPixelWindow</strong></a></p></td>
<td><p>Sets the area to be scanned.</p></td>
</tr>
</tbody>
</table>

 

 

 




