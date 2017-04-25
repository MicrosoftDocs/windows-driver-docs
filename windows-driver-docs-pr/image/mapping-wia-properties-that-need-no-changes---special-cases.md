---
title: Mapping WIA Properties That Need No Changes - Special Cases
author: windows-driver-content
description: Mapping WIA Properties That Need No Changes - Special Cases
ms.assetid: 4ed02c01-efe8-4728-a54a-26fe27aa403c
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mapping WIA Properties That Need No Changes - Special Cases


The cases where the compatibility layer might fail are:

-   Missing/corrupted Windows XP properties related to required Windows Vista properties might render the compatibility layer unavailable. In these cases, the current session will fail; the option to continue is not available because of differences in item structure and properties between Windows XP and Windows Vista drivers and applications (the application's COM proxy cannot function in such cases). The [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384) and [**WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551379) properties are a special case; if they are not supported by the Windows XP driver, only a FLATBED item will be translated for theWindows Vista application

-   Certain Windows XP root properties dependent on a specific context (FLATBED, FEEDER, or a property context) may be not available unless that specific context is set, or these properties might have different valid and current values for each context. WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT will be used to set the correct FEEDER/FLATBED context; it will be set to FEEDER (plus DUPLEX when necessary) or FLATBED on the root item of the Windows XP driver. In all other cases, the context should be set though the appropriate property. This is also the case when the Windows XP device supports both FEEDER and FLATBED, and all root properties could be translated to both the FLATBED and FEEDER items in Windows Vista.

-   For duplicate Windows Vista properties translated from/to unique Windows XP properties, the WIA service has to decide how to treat the case where the same property is set to different values from different Windows Vista items. The solution is to reinitialize all Windows XP A-AIT item properties every time the context is changed. This way separate sets of properties could be negotiated from a Windows XP application for the FEEDER and FLATBED items of the Windows Vista driver.

-   If the Windows Vista driver doesn't implement a FEEDER or FLATBED item (for example, the driver might implement just film/TPA(transparency adapter) and/or storage items), the compatibility layer will not be available. It is not safe to assume that a generic Windows XP child item can always be created for Windows Vista film/TPA and/or storage items. Further, even more complication could arise if the Windows Vista driver implements both a film/TPA and storage items. So, the compatibility layer won't work for Windows Vista drivers that do not implement at least a FLATBED or a FEEDER item.

-   If the Windows XP driver does not implement a correct Windows XP item structure (root plus child scan item), for example, if the driver partially implements support for the new Windows Vista item structure but fails to provide complete support for Windows Vista image transfers, the property/item compatibility layer will be disabled and the current session will fail.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20WIA%20Properties%20That%20Need%20No%20Changes%20-%20Special%20Cases%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


