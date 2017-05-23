---
title: Logger Restrictions and Limitations
description: Logger Restrictions and Limitations
ms.assetid: cb16c193-5420-4900-bf07-44b49859e296
keywords: ["Logger, restrictions", "Logger, limitations"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Logger Restrictions and Limitations


## <span id="ddk_logger_restrictions_and_limitations_dtoolq"></span><span id="DDK_LOGGER_RESTRICTIONS_AND_LIMITATIONS_DTOOLQ"></span>


Logger increases stack consumption for a process because it introduces an additional "wrapping" function before the actual function call.

This can expose bugs in applications that are usually related to uninitialized variables. Since Logger alters stack usage, a local variable declared in a function call might take a different initial value than it does without the presence of Logger. If the program uses this variable without initializing it, the program might crash or otherwise behave differently than if Logger was not present.

Unfortunately, there is no easy way around such problems. The only workaround is to try disabling categories of functions in an attempt to isolate the area that is causing the problem.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Logger%20Restrictions%20and%20Limitations%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




