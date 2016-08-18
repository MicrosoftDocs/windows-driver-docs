---
title: Device Communication through the Bus Driver
author: windows-driver-content
description: Device Communication through the Bus Driver
MS-HAID:
- 'WIA\_arch\_6fd02bbf-cfc0-4893-aaa7-619d7f0f8f22.xml'
- 'image.device\_communication\_through\_the\_bus\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 093e95db-dc3e-467b-9163-e61d793c042e
---

# Device Communication through the Bus Driver


## <a href="" id="ddk-device-communication-through-the-bus-driver-si"></a>


The primary responsibility of the WIA minidriver is to communicate with the device. When a WIA application makes a call to the WIA service, that request is forwarded to the WIA minidriver's interface through the [IStiUSD](istiusd-com-interface.md) or [IWiaMiniDrv](https://msdn.microsoft.com/library/windows/hardware/ff545027) interface. In some cases, the WIA minidriver must query the physical device or perform some other action on the device. The minidriver's device communication layer is responsible for translating the request from the WIA service into a request that the device can understand, and then sending the request to the device through the bus driver stack. Similarly, when the device sends its response back up the bus driver stack, the device communication layer is responsible for translating the response from a device into a response that the WIA service understands.

All communication with the bus driver stack is performed by using calls to the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **ReadFile**, **WriteFile**, and **DeviceIoControl** functions, which are described in the Microsoft Windows SDK documentation. For more information about communicating with the bus driver stack, see [Accessing Kernel-Mode Drivers for Still Image Devices](accessing-kernel-mode-drivers-for-still-image-devices.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Device%20Communication%20through%20the%20Bus%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


