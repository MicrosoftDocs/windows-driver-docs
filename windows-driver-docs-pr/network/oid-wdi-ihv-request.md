---
title: OID_WDI_IHV_REQUEST
ms.topic: reference
description: OID_WDI_IHV_REQUEST is used to forward information that an IHV extensibility module has sent to the miniport.
ms.date: 03/02/2023
keywords:
 - OID_WDI_IHV_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_WDI\_IHV\_REQUEST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_IHV\_REQUEST is used to forward information that an IHV extensibility module has sent to the miniport.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command is not serialized with any tasks. It is serialized with other properties and with the M1-M3 of a task.

## Command parameter


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                        |
|------------------------------------------------------|--------------------------------|----------|----------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](./wdi-tlv-ihv-data.md) |                                | X        | The information from the IHV extensibility module. |

 

## Response result


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                 |
|------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](./wdi-tlv-ihv-data.md) |                                | X        | The response to be sent to the IHV extensibility module. The data value is forwarded as-is to the IHV extensibility module. |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

