---
title: CoNDIS Miniport Driver Status Indications
description: CoNDIS Miniport Driver Status Indications
keywords:
- miniport drivers WDK networking , CoNDIS
- NDIS miniport drivers WDK , CoNDIS
ms.date: 03/02/2023
---

# CoNDIS Miniport Driver Status Indications





Miniport drivers call the [**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex) function to report a change in the status of a miniport adapter. The miniport driver passes **NdisMCoIndicateStatusEx** a pointer to an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure that contains the status information.

The status indication includes information to identify the type of status and a reason for the status change.

The miniport driver should set the **SourceHandle** member of the NDIS\_STATUS\_INDICATION structure to the handle that NDIS passed to the *MiniportAdapterHandle* parameter of the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. If the status indication is associated with an OID request, the miniport driver can set the **DestinationHandle** and **RequestId** members of NDIS\_STATUS\_INDICATION so that NDIS can provide the status indication to a specific protocol binding. For more information about OID requests, see [CoNDIS Miniport Driver OID Requests](condis-miniport-driver-oid-requests.md).

 

