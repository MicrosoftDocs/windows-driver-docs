---
title: CPSUI Message Handler
description: CPSUI Message Handler
ms.assetid: 4a6434e9-d65e-4ddd-836e-d6101532bbb8
keywords:
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CPSUI Message Handler





A CPSUI message handler is a callback function that is defined using the [**\_CPSUICALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff564313) function type. This type of [page event callback](page-event-callbacks.md) is recommended if you are using [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md).

When a user interacts with a property sheet page and causes an event to occur, CPSUI intercepts the event and calls the \_CPSUICALLBACK-typed function, supplying a [**CPSUICBPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff547088) structure that describes the reason the callback function is being called.

The callback function must handle the event, and then return a status value to CPSUI that indicates if the page needs to be redisplayed or reinitialized.

 

 




