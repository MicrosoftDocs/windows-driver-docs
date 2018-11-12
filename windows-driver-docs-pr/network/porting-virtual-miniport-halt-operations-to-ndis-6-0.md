---
title: Porting Virtual Miniport Halt Operations to NDIS 6.0
description: Porting Virtual Miniport Halt Operations to NDIS 6.0
ms.assetid: 2188eb52-9baa-4b7c-9d58-67a0bd7e27be
keywords:
- intermediate drivers WDK networking , virtual miniports
- NDIS intermediate drivers WDK , virtual miniports
- virtual miniports WDK networking
- porting intermediate drivers WDK networking , virtual miniports
- halting virtual miniports
- stopping virtual
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Virtual Miniport Halt Operations to NDIS 6.0





Like NDIS 5.*x* intermediate drivers, NDIS 6.0 intermediate drivers usually halt virtual miniports during the unbind operation. In NDIS 6.0, the [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function replaces the NDIS 5.*x*[**ProtocolUnbindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff563260) function.

To halt a virtual miniport, NDIS 5.*x* calls the intermediate driver's [**MiniportHalt**](https://msdn.microsoft.com/library/windows/hardware/ff549451) function. In NDIS 6.0, the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function replaces *MiniportHalt*.

If an NDIS 6.0 intermediate driver calls the [**NdisIMDeInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562721) function, NDIS calls the *MiniportHaltEx* function for the affected virtual miniport. An intermediate driver usually calls **NdisIMDeInitializeDeviceInstance** from its [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function.

For more information about halting a miniport adapter, see [Porting Miniport Adapter Halt Operations to NDIS 6.0](porting-miniport-adapter-halt-operations-to-ndis-6-0.md).

For more information about unbinding operations, see [Porting Protocol Unbinding Operations to NDIS 6.0](porting-protocol-unbinding-operations-to-ndis-6-0.md).

For more information about halting a virtual miniport, see [Halting a Virtual Miniport](halting-a-virtual-miniport.md).

NDIS 6.0 filter drivers do not require a virtual miniport. For more information about filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

 

 





