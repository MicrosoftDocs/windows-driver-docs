---
title: Introduction to WMI
description: Introduction to WMI
ms.assetid: 9ee0ecbb-05fc-42ab-8bad-7c647f30c82c
keywords: ["WMI WDK kernel , about Windows Management Instrumentation"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to WMI





By making your driver a WMI provider, you can:

-   Make custom data available to WMI consumers.

-   Permit WMI consumers to configure a device through a standard interface rather than a custom control panel application.

-   Notify WMI consumers of driver-defined events without requiring the consumer to poll or send IRPs.

-   Reduce driver overhead by collecting and sending only requested data to a single destination.

-   Annotate data and event blocks with descriptive driver-defined class names and optional descriptions that WMI clients can then enumerate and display to users.

 

 




