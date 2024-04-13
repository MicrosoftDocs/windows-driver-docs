---
title: WDI_TLV_SET_POWER_DX_REASON
ms.topic: reference
description: WDI_TLV_SET_POWER_DX_REASON is a TLV that contains the reason for a set power Dx.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SET_POWER_DX_REASON Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SET\_POWER\_DX\_REASON


WDI\_TLV\_SET\_POWER\_DX\_REASON is a TLV that contains the reason for a set power Dx.

## TLV Type


0x103

## Length


The size (in bytes) of a UINT32.

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
<td>UINT32</td>
<td>The reason for a set power Dx.
<p>Valid values are:</p>
<ul>
<li><p>WDI_SET_POWER_DX_REASON_SELETIVE_SUSPEND (1)</p>
<p>When this value is set, it implies waking on any interesting external events without explicit <a href="wdi-tlv-enable-wake-events.md" data-raw-source="[&lt;strong&gt;WDI_TLV_ENABLE_WAKE_EVENTS&lt;/strong&gt;](wdi-tlv-enable-wake-events.md)"><strong>WDI_TLV_ENABLE_WAKE_EVENTS</strong></a>. This is an idle low power where the device functions transparently to end users as if it were in D0. See <a href="/windows-hardware/drivers/network/wdi-usb-remote-wake-sequence" data-raw-source="[WDI USB remote wake sequence](./wdi-usb-remote-wake-sequence.md)">WDI USB remote wake sequence</a> for more information.</p></li>
</ul></td>
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

