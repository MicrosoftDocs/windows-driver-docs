---
title: OID_WDI_SET_CLEAR_RECEIVE_COALESCING
description: OID_WDI_SET_CLEAR_RECEIVE_COALESCING is used by the host to remove a packet filter for packet coalescing.
ms.assetid: 1c2848c4-c412-4f33-9fc6-bf900a89c65d
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_CLEAR_RECEIVE_COALESCING Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING


OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING is used by the host to remove a packet filter for packet coalescing.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                            | Multiple TLV instances allowed | Optional | Description                         |
|------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_SET\_CLEAR\_RECEIVE\_COALESCING**](https://msdn.microsoft.com/library/windows/hardware/dn898057) |                                |          | The packet filter ID to be removed. |

 

## Set property results


No additional data. The data in the header is sufficient.
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

## See also


[OID\_WDI\_SET\_RECEIVE\_COALESCING](oid-wdi-set-receive-coalescing.md)

 

 




