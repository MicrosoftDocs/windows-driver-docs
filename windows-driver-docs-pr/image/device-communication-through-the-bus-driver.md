---
title: Device Communication through the Bus Driver
description: Device Communication through the Bus Driver
ms.assetid: 093e95db-dc3e-467b-9163-e61d793c042e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Communication through the Bus Driver





The primary responsibility of the WIA minidriver is to communicate with the device. When a WIA application makes a call to the WIA service, that request is forwarded to the WIA minidriver's interface through the [IStiUSD](istiusd-com-interface.md) or [IWiaMiniDrv](https://msdn.microsoft.com/library/windows/hardware/ff545027) interface. In some cases, the WIA minidriver must query the physical device or perform some other action on the device. The minidriver's device communication layer is responsible for translating the request from the WIA service into a request that the device can understand, and then sending the request to the device through the bus driver stack. Similarly, when the device sends its response back up the bus driver stack, the device communication layer is responsible for translating the response from a device into a response that the WIA service understands.

All communication with the bus driver stack is performed by using calls to the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **ReadFile**, **WriteFile**, and **DeviceIoControl** functions, which are described in the Microsoft Windows SDK documentation. For more information about communicating with the bus driver stack, see [Accessing Kernel-Mode Drivers for Still Image Devices](accessing-kernel-mode-drivers-for-still-image-devices.md).

 

 




