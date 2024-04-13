---
title: Differences in Initialization
description: Differences in Initialization
keywords:
- initializing connection-oriented protocols
ms.date: 04/20/2017
---

# Differences in Initialization





A call manager is an NDIS protocol; therefore, it follows the initialization sequence for a connection-oriented protocol, but with one additional step. In its [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) handler, immediately after completing the initialization steps for a connection-oriented protocol, a call manager must register an address family by calling [**NdisCmRegisterAddressFamilyEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmregisteraddressfamilyex). The call to **NdisCmRegisterAddressFamilyEx**, in which a call manager registers its call manager functions, identifies the protocol as a call manager. The call manager must register an address family for each NIC to which it binds itself.

An MCM driver is a miniport driver; therefore, it follows the initialization sequence for a connection-oriented miniport driver with the addition of the following step: an MCM driver must register an address family by calling [**NdisMCmRegisterAddressFamilyEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmregisteraddressfamilyex) in its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, immediately after completing the miniport driver initialization sequence . The call to **NdisMCmRegisterAddressFamilyEx**, in which an MCM driver registers its call manager functions, distinguishes the MCM driver from a regular connection-oriented miniport driver. Although an MCM driver registers its miniport driver handlers only once during initialization by calling [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver), it must call **NdisMCmRegisterAddressFamilyEx** once for each NIC that it controls.

 

