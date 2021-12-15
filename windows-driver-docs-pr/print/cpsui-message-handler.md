---
title: CPSUI Message Handler
description: CPSUI Message Handler
keywords:
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
ms.date: 04/20/2017
---

# CPSUI Message Handler





A CPSUI message handler is a callback function that is defined using the [**\_CPSUICALLBACK**](/windows-hardware/drivers/ddi/compstui/nc-compstui-_cpsuicallback) function type. This type of [page event callback](page-event-callbacks.md) is recommended if you are using [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md).

When a user interacts with a property sheet page and causes an event to occur, CPSUI intercepts the event and calls the \_CPSUICALLBACK-typed function, supplying a [**CPSUICBPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_cpsuicbparam) structure that describes the reason the callback function is being called.

The callback function must handle the event, and then return a status value to CPSUI that indicates if the page needs to be redisplayed or reinitialized.

 

