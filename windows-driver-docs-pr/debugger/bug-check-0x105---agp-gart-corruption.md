---
title: Bug Check 0x105 AGP_GART_CORRUPTION
description: The AGP_GART_CORRUPTION bug check has a value of 0x00000105. This indicates that the Graphics Aperture Remapping Table (GART) is corrupt.
keywords: ["Bug Check 0x105 AGP_GART_CORRUPTION", "AGP_GART_CORRUPTION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- AGP_GART_CORRUPTION
api_type:
- NA
---

# Bug Check 0x105: AGP\_GART\_CORRUPTION


The AGP\_GART\_CORRUPTION bug check has a value of 0x00000105. This indicates that the Graphics Aperture Remapping Table (GART) is corrupt.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## AGP\_GART\_CORRUPTION Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The base address (virtual) of the GART</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The offset into the GART where the corruption occurred</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The base address (virtual) of the GART cache (a copy of the GART)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Cause

This bug check is typically caused by improper direct memory access (DMA) by a driver.

## Resolution

Enable Driver Verifier for any unsigned drivers. Remove them or disable them one by one until the erring driver is identified.

 

 




