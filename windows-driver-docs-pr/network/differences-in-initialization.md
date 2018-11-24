---
title: Differences in Initialization
description: Differences in Initialization
ms.assetid: 1b19e30d-3c10-4b97-9bb4-3233f7f2a195
keywords:
- initializing connection-oriented protocols
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences in Initialization





A call manager is an NDIS protocol; therefore, it follows the initialization sequence for a connection-oriented protocol, but with one additional step. In its [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) handler, immediately after completing the initialization steps for a connection-oriented protocol, a call manager must register an address family by calling [**NdisCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561685). The call to **NdisCmRegisterAddressFamilyEx**, in which a call manager registers its call manager functions, identifies the protocol as a call manager. The call manager must register an address family for each NIC to which it binds itself.

An MCM driver is a miniport driver; therefore, it follows the initialization sequence for a connection-oriented miniport driver with the addition of the following step: an MCM driver must register an address family by calling [**NdisMCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff563554) in its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, immediately after completing the miniport driver initialization sequence . The call to **NdisMCmRegisterAddressFamilyEx**, in which an MCM driver registers its call manager functions, distinguishes the MCM driver from a regular connection-oriented miniport driver. Although an MCM driver registers its miniport driver handlers only once during initialization by calling [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654), it must call **NdisMCmRegisterAddressFamilyEx** once for each NIC that it controls.

 

 





