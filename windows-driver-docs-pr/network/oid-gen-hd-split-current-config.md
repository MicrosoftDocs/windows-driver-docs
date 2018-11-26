---
title: OID_GEN_HD_SPLIT_CURRENT_CONFIG
description: As a query, overlying drivers or administrative utilities can use the OID_GEN_HD_SPLIT_CURRENT_CONFIG OID to determine the current header-data split configuration of a miniport adapter.
ms.assetid: fc363227-1040-45bc-8c76-2ac61606d777
ms.date: 08/08/2017
keywords: 
 -OID_GEN_HD_SPLIT_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG


As a query, overlying drivers or administrative utilities can use the OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG OID to determine the current header-data split configuration of a miniport adapter. A system administrator can use the GUID that is associated with this OID through the WMI interface.

Remarks
-------

NDIS handles this OID on behalf of the miniport driver. NDIS maintains the current header-data split configuration information based on the miniport driver initialization attributes and the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567370) status indication.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696) structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567370)

 

 




