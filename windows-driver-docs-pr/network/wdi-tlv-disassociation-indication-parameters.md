---
title: WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS
description: WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS is a TLV that contains disassociation indication parameters for NDIS_STATUS_WDI_INDICATION_DISASSOCIATION.
ms.assetid: AD799DAA-B89D-4015-8DC5-53057C4DA43E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS


WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS is a TLV that contains disassociation indication parameters for [NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/dn925631).

## TLV Type


0xBC

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                         | Description                                                                |
|--------------------------------------------------------------|----------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)            | The MAC address of the peer associated with the disassociation indication. |
| [**WDI\_ASSOC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/dn897725) (UINT32) | The trigger for the disassociation indication.                             |

 

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

 

 




