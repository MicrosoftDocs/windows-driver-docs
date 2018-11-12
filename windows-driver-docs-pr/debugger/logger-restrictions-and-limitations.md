---
title: Logger Restrictions and Limitations
description: Logger Restrictions and Limitations
ms.assetid: cb16c193-5420-4900-bf07-44b49859e296
keywords: ["Logger, restrictions", "Logger, limitations"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Logger Restrictions and Limitations


## <span id="ddk_logger_restrictions_and_limitations_dtoolq"></span><span id="DDK_LOGGER_RESTRICTIONS_AND_LIMITATIONS_DTOOLQ"></span>


Logger increases stack consumption for a process because it introduces an additional "wrapping" function before the actual function call.

This can expose bugs in applications that are usually related to uninitialized variables. Since Logger alters stack usage, a local variable declared in a function call might take a different initial value than it does without the presence of Logger. If the program uses this variable without initializing it, the program might crash or otherwise behave differently than if Logger was not present.

Unfortunately, there is no easy way around such problems. The only workaround is to try disabling categories of functions in an attempt to isolate the area that is causing the problem.

 

 





