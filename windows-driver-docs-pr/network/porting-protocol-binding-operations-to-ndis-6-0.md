---
title: Porting Protocol Binding Operations to NDIS 6.0
description: Porting Protocol Binding Operations to NDIS 6.0
ms.assetid: 25e2d209-3256-4451-867f-a3c6c4ca7092
keywords:
- protocol drivers WDK networking , binding operations
- NDIS protocol drivers WDK , binding operations
- protocol bindings WDK networking
- binding operations WDK networking
- porting protocol drivers WDK networking , binding operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Binding Operations to NDIS 6.0





As with NDIS 5.*x*, NDIS 6.0 protocol drivers can support multiple protocol bindings. A protocol binding is a binding instance of a protocol driver. A protocol binding binds an NDIS protocol driver to a miniport adapter. To initialize a protocol binding, NDIS 5.*x* calls the protocol driver's [**ProtocolBindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff562465) function. In NDIS 6.0, the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function replaces *ProtocolBindAdapter*.

The following topics provide information about porting protocol binding operations to NDIS 6.0:

[Updating the ProtocolBindAdapter Function for an NDIS 6.0 Protocol Driver](updating-the-protocolbindadapter-function-for-an-ndis-6-0-protocol-dri.md)

[Opening an Adapter in an NDIS 6.0 Protocol Driver](opening-an-adapter-in-an-ndis-6-0-protocol-driver.md)

[Reading the Registry in an NDIS 6.0 Protocol Driver](reading-the-registry-in-an-ndis-6-0-protocol-driver.md)

[Allocating Memory in an NDIS 6.0 Protocol Driver](allocating-memory-in-an-ndis-6-0-protocol-driver.md)

 

 





