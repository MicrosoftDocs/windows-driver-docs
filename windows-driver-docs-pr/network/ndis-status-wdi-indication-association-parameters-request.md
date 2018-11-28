---
title: NDIS_STATUS_WDI_INDICATION_ASSOCIATION_PARAMETERS_REQUEST
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_ASSOCIATION_PARAMETERS_REQUEST to request association parameters for a set of BSSIDs from the host.
ms.assetid: 2c8aef86-bb4a-47c6-a839-eb14eb430a31
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_ASSOCIATION_PARAMETERS_REQUEST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_PARAMETERS\_REQUEST


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_PARAMETERS\_REQUEST to request association parameters for a set of BSSIDs from the host.

| Object |
|--------|
| Port   |

 

This indication can be sent by the adapter when it finds a BSS entry that is a candidate for association based on the current settings. Upon receiving this indication, the host checks if the association parameters are available, and if so, sends them with [OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS](oid-wdi-set-association-parameters.md).

## Payload data


| Type                                                                                                             | Multiple TLV instances allowed | Optional | Description                                   |
|------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------|
| [**WDI\_TLV\_ASSOCIATION\_PARAMETERS\_REQUESTED\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926131) |                                |          | The list of requested association parameters. |
| [**WDI\_TLV\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926162)                                                           | X                              | X        | The list of BSSIDs.                           |

 

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

 

 




