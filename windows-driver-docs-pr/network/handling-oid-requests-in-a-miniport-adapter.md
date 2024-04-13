---
title: Handling OID Requests In a Miniport Adapter
description: Handling OID Requests In a Miniport Adapter
keywords:
- miniport drivers WDK networking , OID requests
- OIDs WDK networking , miniport drivers
ms.date: 04/20/2017
---

# Handling OID Requests In a Miniport Adapter





NDIS calls a miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function to submit an OID request to query or set information in the driver. NDIS calls the *MiniportOidRequest* function either on its own behalf or on behalf of an overlying driver that called the [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) or [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) function.

NDIS passes *MiniportOidRequest* a pointer to an [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure that contains the request information. The request structure contains an OID\_Xxx identifier that indicates the type of request and other members to define the request data.

The **Timeout** member specifies a time-out, in seconds, for the request. NDIS can reset the driver or cancel the request if the time-out expires before the driver completes the request.

The **RequestId** member specifies an optional identifier for the request. Miniport drivers can set the **RequestId** member of a status indication to the value obtained from the **RequestId** member of an associated OID request. Typically, miniport drivers can ignore this member. If a driver must set this member, the reference page for the particular OID provides the required values. For more information about status indications, see [Adapter Status Indications](miniport-adapter-status-indications.md).

A miniport driver that successfully handles an OID set request must set the **SupportedRevision** member in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure upon return from the OID set request. The **SupportedRevision** member notifies the initiator of the request of the revision that the driver supported. For example, a miniport driver can create an Xxx\_REVISION\_2 structure, supply values that are appropriate for an Xxx\_REVISION\_1 structure, and fill the rest of the structure with zeros. The miniport driver would report Xxx\_REVISION\_1 in the **SupportedRevision** member. In this case, a protocol driver that can support an Xxx\_REVISION\_2 will use Xxx\_REVISION\_1 information that the miniport driver supported. For more information about version information in NDIS structures, see [Specifying NDIS Version Information](specifying-ndis-version-information.md).

A miniport driver can complete an OID request synchronously by returning a success or failure status.

A miniport driver can complete an OID request asynchronously by returning NDIS\_STATUS\_PENDING. In this case, the miniport driver must call the [**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete) function to complete the operation.

If *MiniportOidRequest* returns NDIS\_STATUS\_PENDING, NDIS will not call *MiniportOidRequest* with another request for the adapter until the pending request is completed.

NDIS can call a miniport driver's [*MiniportCancelOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_oid_request) function to cancel an OID request.

 

