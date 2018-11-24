---
title: CoNDIS WAN Is More Flexible
description: CoNDIS WAN Is More Flexible
ms.assetid: 01f4d5cc-3ecc-4d2f-bc19-67b8d0fda52f
keywords:
- CoNDIS WAN drivers WDK networking , benefits
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS WAN Is More Flexible





In the CoNDIS model, major functions (such as call management and data transfer) are compartmentalized into discrete components or subcomponents. This organization enables you to use system-supplied and third-party components and update functionality more easily.

The CoNDIS model provides four types of drivers:

-   Connection-oriented client drivers

-   Call managers

-   Connection-oriented miniport drivers

-   Integrated miniport call managers (MCMs)

For more information about CoNDIS drivers, see [Connection-Oriented NDIS](connection-oriented-ndis.md).

The separation of call manager and miniport driver components enables you to update the miniport driver to support new hardware while the call manager remains unchanged. In many cases, the call manager might require upgrades only to correct defects.

The separation of architectural components remains clearly defined in an MCM. The call manager subcomponent of the MCM handles the signaling aspects of connections, and the CoNDIS WAN miniport driver subcomponent handles the NIC hardware.

You can use a system-supplied call manager. If the system does not provide a call manager for your media type (as with, for example, ISDN), you can write one or possibly obtain one from a third party.

The Microsoft Windows operating system includes a PPP CoNDIS client, and CoNDIS WAN miniport drivers are available for many devices. You can write CoNDIS WAN clients to extend the system to support other protocol drivers in addition to PPP.

The CoNDIS WAN model is not restricted to PPP data. You can implement a custom WAN client driver and miniport driver to handle, for example, raw data streaming or proprietary encryption.

 

 





