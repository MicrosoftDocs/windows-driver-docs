---
title: WDI_TLV_INTERFACE_ATTRIBUTES
ms.topic: reference
description: WDI_TLV_INTERFACE_ATTRIBUTES is a TLV that contains the attributes of an interface.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INTERFACE_ATTRIBUTES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INTERFACE\_ATTRIBUTES


WDI\_TLV\_INTERFACE\_ATTRIBUTES is a TLV that contains the attributes of an interface.

## TLV Type


0x21

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                     |
|------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_INTERFACE\_CAPABILITIES**](wdi-tlv-interface-capabilities.md)  |                                |          | The capabilities of the interface.                                                                                                                                                              |
| [**WDI\_TLV\_FIRMWARE\_VERSION**](wdi-tlv-firmware-version.md)              |                                |          | An ASCII string that specifies the firmware version.                                                                                                                                            |
| [**WDI\_TLV\_IHV\_NON\_WDI\_OIDS\_LIST**](wdi-tlv-ihv-non-wdi-oids-list.md) |                                | X        | List of non-WDI OIDs that the adapter wants to advertise to the operating system. The adapter should not assume that the operating system has already filtered non-WDI OIDs to match this list. |

 

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

 

 




