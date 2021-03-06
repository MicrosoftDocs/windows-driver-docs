---
title: Managing an NDIS Port
description: Managing an NDIS Port
keywords:
- ports WDK NDIS , managing
- NDIS ports WDK , managing
- port states WDK NDIS
- port numbers WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing an NDIS Port





Interested NDIS drivers and user-mode applications can manage NDIS ports. NDIS provides services to help manage ports.

NDIS notifies the interested NDIS drivers and user mode applications of port state changes by issuing the associated status indications, and PnP events.

The port number that is passed to send and receive functions identifies the target port of a send operation or the source port of a receive indication. Similarly, the port number in the associated structures identifies the port for status indications, OID requests, and PnP events. For more information about port numbers, see [NDIS Ports Introduction](overview-of-ndis-ports.md).

To help manage NDIS ports, the following structures include the port number:

<a href="" id="ndis-oid-request"></a>[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)  
Describes OID requests.

<a href="" id="ndis-status-indication"></a>[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)  
Describes NDIS status indications.

<a href="" id="net-pnp-event-notification"></a>[**NET\_PNP\_EVENT\_NOTIFICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event_notification)  
Describes PnP event notifications.

This section includes:

[NDIS Port Send and Receive Operations](ndis-port-send-and-receive-operations.md)

[NDIS Port OID Requests](ndis-port-oid-requests.md)

[Handling NDIS Ports Status Indications](handling-ndis-ports-status-indications.md)

[Handling NDIS Ports PnP Event Notifications](handling-ndis-ports-pnp-event-notifications.md)

 

