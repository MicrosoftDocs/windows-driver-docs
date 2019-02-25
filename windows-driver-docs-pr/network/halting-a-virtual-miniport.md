---
title: Halting a Virtual Miniport
description: Halting a Virtual Miniport
ms.assetid: f53040b1-cbbc-4b13-9bc7-8fae9eb38391
keywords:
- halting virtual miniports
- virtual miniports WDK networking
- NDIS intermediate drivers WDK , virtual miniports
- intermediate drivers WDK networking , virtual miniports
- stopping virtual miniports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Halting a Virtual Miniport





If an NDIS intermediate driver calls the [**NdisIMDeinitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562721) function, NDIS calls the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function for the affected virtual miniport. An intermediate driver usually calls **NdisIMDeInitializeDeviceInstance** from its [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function.

NDIS sets the *HaltAction* parameter to **NdisHaltDeviceInstanceDeInitialized** to indicate that NDIS is halting the adapter in response to an intermediate driver's call to the **NdisIMDeInitializeDeviceInstance** function.

The intermediate driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function must release all driver-allocated resources that are associated with a virtual miniport.

 

 





