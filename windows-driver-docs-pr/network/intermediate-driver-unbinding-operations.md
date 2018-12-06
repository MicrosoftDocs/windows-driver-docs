---
title: Intermediate Driver Unbinding Operations
description: Intermediate Driver Unbinding Operations
ms.assetid: d316385a-9481-4708-9e09-06d0424acd8f
keywords:
- intermediate drivers WDK networking , binding
- NDIS intermediate drivers WDK , binding
- unbinding WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver Unbinding Operations





An intermediate driver unbinds from an underlying miniport driver by calling [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640) from its [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function. NDIS calls *ProtocolUnbindAdapterEx* if the underlying miniport adapter is no longer available.

An intermediate driver's *ProtocolUnbindAdapterEx* function might be called when the driver has an outstanding call to [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727). This situation occurs when NDIS has not yet called [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) to initialize the corresponding virtual miniports. In this case, the intermediate driver must call [**NdisIMCancelInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562719) to attempt to cancel the initialization of these virtual miniports.

If the binding that is being closed is mapped to a device exported by the intermediate driver, and if that device was initialized by calling [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727), the intermediate driver can call [**NdisIMDeInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562721) to close the device. The result is that the intermediate driver's virtual miniport becomes no longer available for sends or requests made by higher-level drivers.

If an NDIS intermediate driver calls the **NdisIMDeInitializeDeviceInstance** function, NDIS calls the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function for the affected virtual miniport. For information about handling the halt operation for virtual miniports, see [Halting a Virtual Miniport](halting-a-virtual-miniport.md).

After an intermediate driver calls **NdisCloseAdapterEx**, it should fail any send requests for that binding with an appropriate error status.

For additional information about intermediate driver unbinding operations, see [Unbinding from an Adapter](unbinding-from-an-adapter.md).

 

 





