---
title: NDIS_STATUS_PD_CURRENT_CONFIG
description: This status indication is a notification that the NDIS_PD_CONFIG structure has changed.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PD_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PD\_CURRENT\_CONFIG


This status indication is a notification that the [**NDIS\_PD\_CONFIG**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pd_config) structure has changed.

A PacketDirect-capable miniport driver must make an NDIS\_STATUS\_PD\_CURRENT\_CONFIG status indication after an [OID\_PD\_CLOSE\_PROVIDER](./oid-pd-close-provider.md) or [OID\_PD\_OPEN\_PROVIDER](./oid-pd-open-provider.md) request.

The miniport driver calls [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) to make the status indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **SourceHandle** must be set to the handle that the miniport received in the *MiniportAdapterHandle* parameter of the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

-   **StatusCode** must be set to NDIS\_STATUS\_PD\_CURRENT\_CONFIG.

-   **StatusBuffer** must be set to the address of a ULONG variable, which stores the appropriate NDIS\_STATUS\_xxxx code for the result of the scan operation.

-   **StatusBufferSize** must be set to **sizeof**(ULONG).

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)

[OID\_PD\_CLOSE\_PROVIDER](./oid-pd-close-provider.md)

[OID\_PD\_OPEN\_PROVIDER](./oid-pd-open-provider.md)

 

