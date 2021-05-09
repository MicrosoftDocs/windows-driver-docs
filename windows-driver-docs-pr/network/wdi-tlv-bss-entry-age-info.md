---
title: WDI_TLV_BSS_ENTRY_AGE_INFO
description: WDI_TLV_BSS_ENTRY_AGE_INFO is a TLV that contains age information for a BSS entry.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BSS_ENTRY_AGE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY\_AGE\_INFO


WDI\_TLV\_BSS\_ENTRY\_AGE\_INFO is a TLV that contains age information for a BSS entry.

## TLV Type


0xBA

## Length


The sum (in bytes) of the sizes of all contained elements.

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
<td>UINT64</td>
<td>Timestamp of when this BSS entry was most recently discovered. The timestamp should be obtained with <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetcurrentsystemtime" data-raw-source="[&lt;strong&gt;NdisGetCurrentSystemTime&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetcurrentsystemtime)"><strong>NdisGetCurrentSystemTime</strong></a> or <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime" data-raw-source="[&lt;strong&gt;KeQuerySystemTime&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime)"><strong>KeQuerySystemTime</strong></a>.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether this information is live (found during a currently running scan) or is coming from the IHV component's BSS list cache.
<p>Valid values are 0 (live) or 1 (cached).</p></td>
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
