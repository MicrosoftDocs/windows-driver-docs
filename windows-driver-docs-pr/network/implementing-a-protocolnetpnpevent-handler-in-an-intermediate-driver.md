---
title: Implementing an intermediate driver ProtocolNetPnPEvent handler
description: Implementing a ProtocolNetPnPEvent Handler in an Intermediate Driver
ms.assetid: 1d0475c4-631d-4b8a-ab26-5b8b9425bfe6
keywords:
- ProtocolNetPnPEvent
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a ProtocolNetPnPEvent Handler in an Intermediate Driver





The implementation of a [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function in intermediate drivers is nearly identical to the implementation in protocol drivers. For more information about implementing a *ProtocolNetPnPEvent* handler in an intermediate driver, see [Handling PnP Events and PM Events in a Protocol Driver](handling-pnp-events-and-power-management-events-in-a-protocol-driver.md).

NDIS intermediate drivers pass on PnP events to higher layer drivers by calling the [**NdisMNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff563616) function.

 

 





