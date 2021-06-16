---
title: Filter Module Status Indications
description: Filter Module Status Indications
keywords:
- filter modules WDK networking , status indications
- filter drivers WDK networking , status indications
- NDIS filter drivers WDK , status indications
- status indications WDK networking , filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module Status Indications





Filter drivers can supply a [*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status) function that NDIS calls when an underlying driver reports status. Filter drivers can also initiate status indications.

The following figure illustrates a filtered status indication.

![diagram illustrating a filtered status indication.](images/statusfilter.png)

NDIS calls a filter driver's [*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status) function, after an underlying driver calls a status indication function ([**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) or [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus)). For more information about how to indicate status from a miniport driver, see [Adapter Status Indications](miniport-adapter-status-indications.md).

A filter driver calls **NdisFIndicateStatus** in its [*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status) function, to pass on a filtered status indication to overlying drivers. A filter driver can filter out status indications (by not calling [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus)) or modify the indicated status before it calls **NdisFIndicateStatus**.

To originate status indications, filter drivers call [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus) without a prior call to [*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status).

In this case, the filter driver should set the **SourceHandle** member to the handle that NDIS passed to the *NdisFilterHandle* parameter of the [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function. If the status indication is associated with an OID request, the filter driver can set the **DestinationHandle** and **RequestId** members so that NDIS can provide the status indication to a specific protocol binding.

After a filter driver calls [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus), NDIS calls the status function ([**ProtocolStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex) or *FilterStatus*) of the next overlying driver.

 

