---
title: Device-Specific Contexts
description: Device-Specific Contexts
ms.assetid: 29e0d451-57fb-4943-9508-022adffa4650
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device-Specific Contexts





Minidrivers can optionally make use of a private context for storing device-specific information. This device-specific context can reduce the number of times that a minidriver must call the device to obtain device information. There can be only one device-specific context for each driver item of a particular minidriver. When the driver item is no longer needed, the WIA service calls the minidriver's [**IWiaMiniDrv::drvFreeDrvItemContext**](https://msdn.microsoft.com/library/windows/hardware/ff543972) method to free all of the resources that are attached to the device-specific context.

For example, when a camera driver retrieves thumbnail data from the device, it usually caches the data in the driver context associated with the appropriate driver item. Note that the WIA service frees the context. The driver's responsibility is simply to free any resources held by their context. If the thumbnail data of the previous example was stored in memory allocated on the device-specific context, the memory holding that cached data should be freed here, but not the context itself.

 

 




