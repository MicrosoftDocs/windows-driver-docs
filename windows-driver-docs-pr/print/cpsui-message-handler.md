---
title: CPSUI Message Handler
author: windows-driver-content
description: CPSUI Message Handler
ms.assetid: 4a6434e9-d65e-4ddd-836e-d6101532bbb8
keywords:
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CPSUI Message Handler


## <a href="" id="ddk-cpsui-message-handler-gg"></a>


A CPSUI message handler is a callback function that is defined using the [**\_CPSUICALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff564313) function type. This type of [page event callback](page-event-callbacks.md) is recommended if you are using [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md).

When a user interacts with a property sheet page and causes an event to occur, CPSUI intercepts the event and calls the \_CPSUICALLBACK-typed function, supplying a [**CPSUICBPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff547088) structure that describes the reason the callback function is being called.

The callback function must handle the event, and then return a status value to CPSUI that indicates if the page needs to be redisplayed or reinitialized.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20CPSUI%20Message%20Handler%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


