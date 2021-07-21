---
title: OID_PD_CLOSE_PROVIDER
description: An NDIS protocol or filter driver sends an object identifier (OID) method request of OID_PD_CLOSE_PROVIDER to the PDPI provider to give up access to the PD capability in a PDPI provider object.
ms.date: 08/08/2017
keywords: 
 -OID_PD_CLOSE_PROVIDER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PD\_CLOSE\_PROVIDER


An NDIS protocol or filter driver sends an object identifier (OID) method request of OID\_PD\_CLOSE\_PROVIDER to the PDPI provider to give up access to the PD capability in a PDPI provider object.

An NDIS protocol or filter driver must call this OID when it receives an unbind notification, a pause indication, a low-power event, or a PD configuration change event that indicates the PD is disabled on the binding.

Before calling this OID, the NDIS protocol or filter driver must ensure that it has closed and freed all PD objects such as queues, counters, and filters that it created over the PD provider instance. The NDIS protocol or filter driver must guarantee that there are no in-progress calls to any of the PD provider dispatch table functions before issuing this OID.

## Requirements

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)

[**NDIS\_PD\_CLOSE\_PROVIDER\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_pd_close_provider_parameters)

[NDIS\_STATUS\_PD\_CURRENT\_CONFIG](./ndis-status-pd-current-config.md)

[OID\_PD\_OPEN\_PROVIDER](oid-pd-open-provider.md)

 

