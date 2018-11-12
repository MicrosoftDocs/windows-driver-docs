---
title: Porting Virtual Miniport Initialization to NDIS 6.0
description: Porting Virtual Miniport Initialization to NDIS 6.0
ms.assetid: 1706f3ae-fb8a-45d9-8bc5-1b460b9d3b97
keywords:
- intermediate drivers WDK networking , virtual miniports
- NDIS intermediate drivers WDK , virtual miniports
- virtual miniports WDK networking
- porting intermediate drivers WDK networking , virtual miniports
- initializing virtual miniports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Virtual Miniport Initialization to NDIS 6.0





Like NDIS 5.*x* intermediate drivers, NDIS 6.0 intermediate drivers usually starts virtual miniport initialization during the bind operation. In NDIS 6.0, the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function replaces the NDIS 5.*x*[**ProtocolBindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff562465) function.

To initialize a virtual miniport, NDIS 5.*x* calls the intermediate driver's [**MiniportInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff550472) function. In NDIS 6.0, the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function replaces *MiniportInitialize*.

To start initializing a virtual miniport, an intermediate driver calls the [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727) function. After the intermediate driver calls **NdisIMInitializeDeviceInstanceEx** and the Plug and Play manager requests NDIS to start the virtual device, NDIS calls the driver's *MiniportInitializeEx* function.

An intermediate driver calls the **NdisIMInitializeDeviceInstanceEx** function from its [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function one or more times to request initialization of one or more virtual miniports.

For more information about miniport adapter initialization, see [Porting Miniport Adapter Initialization to NDIS 6.0](porting-miniport-adapter-initialization-to-ndis-6-0.md).

For more information about binding operations, see [Porting Protocol Binding Operations to NDIS 6.0](porting-protocol-binding-operations-to-ndis-6-0.md).

For more information about initializing a virtual miniport, see [Initializing a Virtual Miniport](initializing-a-virtual-miniport.md).

NDIS 6.0 filter drivers do not require a virtual miniport. For more information about filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

 

 





