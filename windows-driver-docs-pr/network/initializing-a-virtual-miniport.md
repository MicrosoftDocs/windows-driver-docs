---
title: Initializing a Virtual Miniport
description: Initializing a Virtual Miniport
ms.assetid: 5f2e23a9-375b-4b0d-95d2-5a3af1acb3be
keywords:
- initializing virtual miniports
- virtual miniports WDK networking
- NDIS intermediate drivers WDK , virtual miniports
- intermediate drivers WDK networking , virtual miniports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Virtual Miniport





To initiate the initialization of a virtual miniport, an intermediate driver calls the [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727) function. The intermediate driver usually makes this call from its [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function. After the intermediate driver calls **NdisIMInitializeDeviceInstanceEx** and the Plug an Play manager requests NDIS to start the virtual device, NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

The call to *MiniportInitializeEx* can be in the context of **NdisIMInitializeDeviceInstanceEx** if the Plug and Play manager starts the virtual device before **NdisIMInitializeDeviceInstanceEx** returns. If the intermediate driver provides more than one virtual miniport, the driver must call **NdisIMInitializeDeviceInstanceEx** for each virtual miniport that it makes available.

NDIS passes initialization parameters to *MiniportInitializeEx* in an [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565972) structure at *MiniportInitParameters* . The **IMDeviceInstanceContext** member of the structure specifies a pointer to the context area for a virtual device. The driver passed this pointer to the [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727) function at the *DeviceContext* parameter.

In *MiniportInitializeEx*, the intermediate driver performs the operations required to initialize a virtual miniport. This initialization is similar to the initialization of any other miniport adapter.

 

 





