---
title: Writing NDIS Protocol Drivers
description: Writing NDIS Protocol Drivers
ms.assetid: 30d27b9b-e6b9-4548-ab83-f240e60d5393
keywords:
- protocol drivers WDK networking , about protocol drivers
- NDIS protocol drivers WDK , about NDIS protocol drivers
- NDIS protocol drivers WDK , writing
- protocol drivers WDK networking , writing
- writing NDIS protocol drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing NDIS Protocol Drivers





This documentation provides an overview of protocol driver operations for NDIS 6.0 and later. NDIS protocol drivers provide *ProtocolXxx* functions that NDIS calls to initiate operations. NDIS provides **Ndis*Xxx*** functions that protocol drivers call to perform operations.

The following topics describe the relationship between binding states and operations, and include overviews of some protocol driver operations:

-   [Initializing a Protocol Driver](initializing-a-protocol-driver.md)
-   [Protocol Binding States and Operations](protocol-binding-states-and-operations.md)
-   [Binding to an Adapter](binding-to-an-adapter.md)
-   [Unbinding from an Adapter](unbinding-from-an-adapter.md)
-   [Starting and Pausing a Binding](starting-and-pausing-a-binding.md)
-   [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md)
-   [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md)
-   [Protocol Driver OID Requests](protocol-driver-oid-requests.md)
-   [Handling Status Indications in a Protocol Driver](handling-status-indications-in-a-protocol-driver.md)
-   [Handling PnP Event Notifications in a Protocol Driver](handling-pnp-event-notifications-in-a-protocol-driver.md)

 

 





