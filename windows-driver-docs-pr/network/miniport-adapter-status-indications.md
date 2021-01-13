---
title: Miniport Adapter Status Indications
description: Miniport Adapter Status Indications
keywords:
- status indications WDK networking , miniport adapters
- miniport adapters WDK networking , status indications
- adapters WDK networking , status indications
- NdisMIndicateStatusEx
- NDIS_STATUS_INDICATION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Adapter Status Indications





Miniport drivers call the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) function to report a change in the status of a miniport adapter. The miniport driver passes **NdisMIndicateStatusEx** a pointer to an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure that contains the status information.

The status indication includes information to identify the type of status and a reason for the status change.

The miniport driver should set the **SourceHandle** member to the handle that NDIS passed to the *MiniportAdapterHandle* parameter of the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. If the status indication is associated with an OID request, the miniport driver can set the **DestinationHandle** and **RequestId** members so that NDIS can provide the status indication to a specific protocol binding.

 

