---
title: OID_WDI_IHV_REQUEST
description: OID_WDI_IHV_REQUEST is used to forward information that an IHV extensibility module has sent to the miniport.
ms.assetid: d5639def-ddde-4972-b331-46c0f768d155
ms.date: 07/18/2017
keywords:
 - OID_WDI_IHV_REQUEST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_IHV\_REQUEST


OID\_WDI\_IHV\_REQUEST is used to forward information that an IHV extensibility module has sent to the miniport.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command is not serialized with any tasks. It is serialized with other properties and with the M1-M3 of a task.

## Command parameter


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                        |
|------------------------------------------------------|--------------------------------|----------|----------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn926312) |                                | X        | The information from the IHV extensibility module. |

 

## Response result


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                 |
|------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn926312) |                                | X        | The response to be sent to the IHV extensibility module. The data value is forwarded as-is to the IHV extensibility module. |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




