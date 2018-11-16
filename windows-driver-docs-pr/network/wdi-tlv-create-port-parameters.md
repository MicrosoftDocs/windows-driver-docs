---
title: WDI_TLV_CREATE_PORT_PARAMETERS
description: WDI_TLV_CREATE_PORT_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_CREATE_PORT.
ms.assetid: CE0ACE11-5E7A-43E1-BE0B-8BA8F7FF8432
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CREATE_PORT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CREATE\_PORT\_PARAMETERS


WDI\_TLV\_CREATE\_PORT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_CREATE\_PORT](https://msdn.microsoft.com/library/windows/hardware/dn925949).

## TLV Type


0x28

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16 | A bitwise OR value of the operation modes the host may configure on the port being created. The operation modes are defined in [**WDI\_OPERATION\_MODE**](https://msdn.microsoft.com/library/windows/hardware/dn926085). |
| UINT32 | The NDIS\_PORT\_NUMBER that will be associated with the created port. Unless the adapter wants to handle non-WDI OIDs, it does not need to do anything with this field.                 |

 

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

 

 




