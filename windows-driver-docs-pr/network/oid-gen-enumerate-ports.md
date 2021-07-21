---
title: OID_GEN_ENUMERATE_PORTS
description: As a query, NDIS and overlying drivers use the OID_GEN_ENUMERATE_PORTS OID to determine the characteristics of the active NDIS ports that are associated with an underlying miniport adapter.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_ENUMERATE_PORTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_ENUMERATE\_PORTS


As a query, NDIS and overlying drivers use the OID\_GEN\_ENUMERATE\_PORTS OID to determine the characteristics of the active NDIS ports that are associated with an underlying miniport adapter.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

## Remarks

NDIS handles this OID and miniport drivers do not receive this OID query.

If the query succeeds, NDIS returns NDIS\_STATUS\_SUCCESS and provides the results of the query in an [**NDIS\_PORT\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_array) structure. The **NumberOfPorts** member of NDIS\_PORT\_ARRAY contains the number of active ports that are associated with the miniport adapter. The **Ports** member of NDIS\_PORT\_ARRAY contains a list of pointers to [**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics) structures. Each NDIS\_PORT\_CHARACTERISTICS structure defines the characteristics of a single NDIDS port.

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


[**NDIS\_PORT\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_array)

[**NDIS\_PORT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_characteristics)

 

