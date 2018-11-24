---
title: MCM Drivers vs. Call Managers
description: MCM Drivers vs.
ms.assetid: 374716fb-c192-42fd-bef0-0097d622f791
keywords:
- connection-oriented NDIS WDK , call managers
- CoNDIS WDK networking , call managers
- connection-oriented NDIS WDK , MCM drivers
- CoNDIS WDK networking , MCM drivers
- MCM drivers WDK networking
- call managers WDK networking , vs. MCM drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MCM Drivers vs. Call Managers





An integrated MCM driver is a connection-oriented miniport driver that also provides call manager services to connection-oriented clients. As such, an MCM driver performs all the connection-oriented functions of both a connection-oriented miniport driver and a call manager. Like all miniport drivers, MCM drivers must use **Ndis*Xxx*** calls to communicate with the underlying NIC hardware.

An MCM driver differs from a call manager in two major ways:

-   A call manager is an NDIS connection-oriented *protocol driver* with added call manager functionality. An MCM driver is an NDIS connection-oriented *miniport driver* with added call manager functionality.

-   The interface between a call manager and a connection-oriented miniport driver is fully exposed to NDIS--that is, all communication between the call manager and the miniport driver passes through NDIS. Except for the activation and deactivation of client VCs (VCs used for transmitting outgoing or incoming client data), the interface between the call manager part of an MCM driver and the miniport driver part of an MCM driver is opaque to NDIS. The activation and deactivation of client VCs must be accomplished through NDIS because NDIS keeps track of client VCs.

The differences between an MCM driver and a call manager are further described in the following sections:

[Differences in Initialization](differences-in-initialization.md)

[Differences in Calls to NdisXxx Functions](differences-in-calls-to-ndisxxx-functions.md)

[Differences in Virtual Connections](differences-in-virtual-connections.md)

 

 





