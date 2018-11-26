---
title: WDI_TLV_COMMUNICATION_CONFIGURATION_ATTRIBUTES
description: WDI_TLV_COMMUNICATION_CONFIGURATION_ATTRIBUTES is a TLV that contains the host-adapter communication protocol configuration attributes.
ms.assetid: A779FA2D-D3E0-4FC9-9A8A-09B6E3CFF758
ms.date: 07/18/2017
keywords:
 - WDI_TLV_COMMUNICATION_CONFIGURATION_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_COMMUNICATION\_CONFIGURATION\_ATTRIBUTES


WDI\_TLV\_COMMUNICATION\_CONFIGURATION\_ATTRIBUTES is a TLV that contains the host-adapter communication protocol configuration attributes.

## TLV Type


0x20

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                | Multiple TLV instances allowed | Optional | Description                     |
|-------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------|
| [**WDI\_TLV\_COMMUNICATION\_CAPABILITIES**](wdi-tlv-communication-capabilities.md) |                                | X        | The communication capabilities. |

 

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

 

 




