---
title: NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT to indicate association results.
ms.assetid: dc025aec-30f4-4a78-b449-acc49d13b507
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT to indicate association results.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                     | Multiple TLV instances allowed | Optional | Description                    |
|--------------------------------------------------------------------------|--------------------------------|----------|--------------------------------|
| [**WDI\_TLV\_ASSOCIATION\_RESULT**](https://msdn.microsoft.com/library/windows/hardware/dn926140) | X                              |          | A list of association results. |

 

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


[OID\_WDI\_TASK\_CONNECT](oid-wdi-task-connect.md)

[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

 




