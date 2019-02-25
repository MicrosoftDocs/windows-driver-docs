---
title: WDI_TLV_DELETE_PORT_PARAMETERS
description: WDI_TLV_DELETE_PORT_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_DELETE_PORT.
ms.assetid: F3DDECDC-1A92-4022-9E2C-780ED480172C
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DELETE_PORT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DELETE\_PORT\_PARAMETERS


WDI\_TLV\_DELETE\_PORT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_DELETE\_PORT](https://msdn.microsoft.com/library/windows/hardware/dn925950).

## TLV Type


0x2A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                          |
|--------|--------------------------------------|
| UINT16 | Specifies the port number to delete. |

 

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

 

 




