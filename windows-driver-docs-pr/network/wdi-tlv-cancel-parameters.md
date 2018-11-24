---
title: WDI_TLV_CANCEL_PARAMETERS
description: WDI_TLV_CANCEL_PARAMETERS is a TLV that contains parameters for OID_WDI_ABORT_TASK.
ms.assetid: 7C071743-5DF9-4CA8-873A-64B06C94388F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CANCEL_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CANCEL\_PARAMETERS


WDI\_TLV\_CANCEL\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_ABORT\_TASK](https://msdn.microsoft.com/library/windows/hardware/dn925835).

## TLV Type


0x2B

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                   | Description                                             |
|------------------------|---------------------------------------------------------|
| NDIS\_OID              | Specifies the OID from the original task being aborted. |
| UINT32                 | Specifies the transaction ID from the original task.    |
| WDI\_PORT\_ID (UINT16) | Specifies the port ID from the original task.           |

 

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

 

 




