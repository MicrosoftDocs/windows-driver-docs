---
title: Device-Specific Contexts
author: windows-driver-content
description: Device-Specific Contexts
ms.assetid: 29e0d451-57fb-4943-9508-022adffa4650
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device-Specific Contexts


## <a href="" id="ddk-device-specific-contexts-si"></a>


Minidrivers can optionally make use of a private context for storing device-specific information. This device-specific context can reduce the number of times that a minidriver must call the device to obtain device information. There can be only one device-specific context for each driver item of a particular minidriver. When the driver item is no longer needed, the WIA service calls the minidriver's [**IWiaMiniDrv::drvFreeDrvItemContext**](https://msdn.microsoft.com/library/windows/hardware/ff543972) method to free all of the resources that are attached to the device-specific context.

For example, when a camera driver retrieves thumbnail data from the device, it usually caches the data in the driver context associated with the appropriate driver item. Note that the WIA service frees the context. The driver's responsibility is simply to free any resources held by their context. If the thumbnail data of the previous example was stored in memory allocated on the device-specific context, the memory holding that cached data should be freed here, but not the context itself.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Device-Specific%20Contexts%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


