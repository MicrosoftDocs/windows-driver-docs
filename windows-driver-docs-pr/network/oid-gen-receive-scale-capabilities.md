---
title: OID_GEN_RECEIVE_SCALE_CAPABILITIES
description: As a query, overlying drivers can use the OID_GEN_RECEIVE_SCALE_CAPABILITIES OID to query the receive side scaling (RSS) capabilities of a NIC and its miniport driver.
ms.assetid: b7640ec3-248c-4db2-818d-3976df2dcb9b
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RECEIVE_SCALE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_RECEIVE\_SCALE\_CAPABILITIES


As a query, overlying drivers can use the OID\_GEN\_RECEIVE\_SCALE\_CAPABILITIES OID to query the receive side scaling (RSS) capabilities of a NIC and its miniport driver.

Remarks
-------

NDIS miniport drivers do not receive this OID request. NDIS handles the query for miniport drivers.

The miniport driver returns the RSS capabilities in an [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567220) structure.

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567220)

 

 




