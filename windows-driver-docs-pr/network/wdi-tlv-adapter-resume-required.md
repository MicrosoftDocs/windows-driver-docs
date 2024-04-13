---
title: WDI_TLV_ADAPTER_RESUME_REQUIRED
ms.topic: reference
description: WDI_TLV_ADAPTER_RESUME_REQUIRED is a TLV that specifies if adapter resume is required.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ADAPTER_RESUME_REQUIRED Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ADAPTER\_RESUME\_REQUIRED


WDI\_TLV\_ADAPTER\_RESUME\_REQUIRED is a TLV that specifies if adapter resume is required.

## TLV Type


0xB7

## Length


The size (in bytes) of a UINT8.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT8</td>
<td>Specifies if adapter resume is required.
<p>Valid values are 0 (not required) and 1 (required). If set to 1, the firmware requires OS assistance to resume its context.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




