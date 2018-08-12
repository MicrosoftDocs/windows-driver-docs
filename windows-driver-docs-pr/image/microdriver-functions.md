---
title: Microdriver Functions
author: windows-driver-content
description: Microdriver Functions
ms.assetid: 491b954a-8ffa-4899-8c7d-0aee409f4742
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>MicroEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545248)</p></td>
<td><p>Responds to commands sent by the WIA Flatbed Driver.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Scan</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547322)</p></td>
<td><p>Reads data from the device and returns the data to the WIA Flatbed Driver.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>SetPixelWindow</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548129)</p></td>
<td><p>Sets the area to be scanned.</p></td>
</tr>
</tbody>
</table>

 

 

 




