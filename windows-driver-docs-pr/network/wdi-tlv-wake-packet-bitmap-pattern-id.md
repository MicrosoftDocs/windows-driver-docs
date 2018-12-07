---
title: WDI_TLV_WAKE_PACKET_BITMAP_PATTERN_ID
description: WDI_TLV_WAKE_PACKET_BITMAP_PATTERN_ID is a TLV that contains a wake-on-LAN pattern ID.
ms.assetid: 78807D91-189B-4E66-B3DC-500E9A59AEF2
ms.date: 07/18/2017
keywords:
 - WDI_TLV_WAKE_PACKET_BITMAP_PATTERN_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN\_ID


WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN\_ID is a TLV that contains a wake-on-LAN pattern ID.

The pattern ID is an OS-provided value that identifies the wake-on-LAN pattern and is set to a value that is unique among the wake-on-LAN patterns on a network adapter. The pattern ID is set before the OS sends an add to the underlying drivers or completes the request to the overlying driver.

## TLV Type


0xE3

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                 |
|--------|-----------------------------|
| UINT32 | The wake-on-LAN pattern ID. |

 

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

## See also


[OID\_WDI\_SET\_ADD\_WOL\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/dn925858)

 

 




