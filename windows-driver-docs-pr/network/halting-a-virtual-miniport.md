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





If an NDIS intermediate driver calls the [**NdisIMDeinitializeDeviceInstance**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisimdeinitializedeviceinstance) function, NDIS calls the [*MiniportHaltEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function for the affected virtual miniport. An intermediate driver usually calls **NdisIMDeInitializeDeviceInstance** from its [*ProtocolUnbindAdapterEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex) function.

NDIS sets the *HaltAction* parameter to **NdisHaltDeviceInstanceDeInitialized** to indicate that NDIS is halting the adapter in response to an intermediate driver's call to the **NdisIMDeInitializeDeviceInstance** function.

The intermediate driver's [*MiniportHaltEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function must release all driver-allocated resources that are associated with a virtual miniport.

 

 





