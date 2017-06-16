---
title: Accessing Device Configuration Space
author: windows-driver-content
description: Accessing Device Configuration Space
ms.assetid: 082500ae-9df2-4f8b-8be3-ff2b95067a12
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "resource information WDK I/O", "driver stacks WDK configuration info"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing Device Configuration Space


## <a href="" id="ddk-accessing-device-configuration-space-kg"></a>


Some buses provide a way of accessing a special configuration space for each device attached to the bus. This section explains how a driver can get information from a target device's configuration space, provided the driver is loaded in the same driver stack as the driver for the target device, either as a function driver or a filter driver.

In Microsoft Windows NT 4.0, drivers get information from a target device's configuration space by scanning the bus and calling the [**HalGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff546599) and [**HalGetBusDataByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546606) routines. In Windows 2000 and later operating systems, the hardware buses are controlled by their respective bus drivers and not by HAL. Therefore, all of the HAL routines that used to help drivers retrieve bus-related information are obsolete in Windows 2000.

The configuration space for a device contains a description of the device and its resource requirements. On Windows 2000 and later operating systems, a driver does not need to query a device to find resources. The driver gets the resources from the Plug and Play (PnP) manager in its [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. Typically, a well-written driver would not require any of this information to function correctly. If, for some reason, the driver requires this information, the code sample in the [Obtaining Device Configuration Information at IRQL = PASSIVE\_LEVEL](obtaining-device-configuration-information-at-irql---passive-level.md) section shows how to get the resources. The driver must be part of the target device's driver stack, because it requires the underlying physical device objects (PDO) of the target device to send the appropriate PnP request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Accessing%20Device%20Configuration%20Space%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


