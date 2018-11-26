---
title: OID_WDI_GET_NEXT_ACTION_FRAME_DIALOG_TOKEN
description: OID_WDI_GET_NEXT_ACTION_FRAME_DIALOG_TOKEN requests the DialogToken to be used in the next Action frame.
ms.assetid: EB5F6077-1566-41AE-B414-9ECF24BAE982
ms.date: 07/18/2017
keywords:
 - OID_WDI_GET_NEXT_ACTION_FRAME_DIALOG_TOKEN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN


OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN requests the DialogToken to be used in the next Action frame.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                     | Multiple TLV instances allowed | Optional | Description     |
|-------------------------------------------------------------------------|--------------------------------|----------|-----------------|
| [**WDI\_TLV\_NEXT\_DIALOG\_TOKEN**](https://msdn.microsoft.com/library/windows/hardware/dn897854) |                                |          | A dialog token. |

 

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

 

 




