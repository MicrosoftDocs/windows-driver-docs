---
title: WDI_TLV_P2P_CHANNEL_INDICATE_REASON
description: WDI_TLV_P2P_CHANNEL_INDICATE_REASON is a TLV that contains a reason for sending an indication.
ms.assetid: DD746492-82C5-4458-94A2-778F7F0F30B4
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_CHANNEL_INDICATE_REASON Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON


WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON is a TLV that contains a reason for sending an indication.

## TLV Type


0x102

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The reason for sending an indication. See [**WDI\_P2P\_CHANNEL\_INDICATE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/dn926090) for possible reasons. |

 

Requirements
------------

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

 

 




