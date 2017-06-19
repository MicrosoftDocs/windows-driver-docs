---
title: Introduction to WMI
author: windows-driver-content
description: Introduction to WMI
ms.assetid: 9ee0ecbb-05fc-42ab-8bad-7c647f30c82c
keywords: ["WMI WDK kernel , about Windows Management Instrumentation"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to WMI


## <a href="" id="ddk-introduction-to-wmi-kg"></a>


By making your driver a WMI provider, you can:

-   Make custom data available to WMI consumers.

-   Permit WMI consumers to configure a device through a standard interface rather than a custom control panel application.

-   Notify WMI consumers of driver-defined events without requiring the consumer to poll or send IRPs.

-   Reduce driver overhead by collecting and sending only requested data to a single destination.

-   Annotate data and event blocks with descriptive driver-defined class names and optional descriptions that WMI clients can then enumerate and display to users.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20WMI%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


