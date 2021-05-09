---
title: OID_GEN_PORT_STATE
description: As a query, overlying drivers use the OID_GEN_PORT_STATE OID to get the current state of the port that is specified in the PortNumber member of the NDIS_OID_REQUEST structure.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_PORT_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_PORT\_STATE


As a query, overlying drivers use the OID\_GEN\_PORT\_STATE OID to get the current state of the port that is specified in the **PortNumber** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

## Remarks

NDIS handles this OID and miniport drivers do not receive this OID query.

If the query succeeds, NDIS returns NDIS\_STATUS\_SUCCESS and returns the port state information in an [**NDIS\_PORT\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_state) structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_PORT\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_state)

 

