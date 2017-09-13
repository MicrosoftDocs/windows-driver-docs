---
title: Stopping a Device
author: windows-driver-content
description: Stopping a Device
ms.assetid: 65a47e7b-aabd-4b55-8fa6-c3482da1cc84
keywords: ["PnP WDK kernel , stopping devices", "Plug and Play WDK kernel , stopping devices", "stopping PnP devices", "stop IRPs WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stopping a Device


## <a href="" id="ddk-stopping-a-device-kg"></a>


The PnP manager directs drivers to stop a device in the following situations:

-   To rebalance the hardware resources being used by the device. Rebalancing is typically necessary when a new device is enumerated that requires a resource already in use.

-   To disable the device in response to a Device Manager request (Windows 98/Me only). Windows 2000 and later versions of Windows send remove IRPs in this situation; see [Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md).

-   After a failed [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request (Windows 98/Me only)

This section covers the following topics:

[Stopping a Device to Rebalance Resources](stopping-a-device-to-rebalance-resources.md)

[Stopping a Device to Disable It (Windows 98/Me)](stopping-a-device-to-disable-it--windows-98-me-.md)

[Stopping a Device after a Failed Start (Windows 98/Me)](stopping-a-device-after-a-failed-start--windows-98-me-.md)

[Handling Stop IRPs (Windows 2000 and Later)](handling-stop-irps--windows-2000-and-later-.md)

[Handling Stop IRPs (Windows 98/Me)](handling-stop-irps--windows-98-me-.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Stopping%20a%20Device%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


