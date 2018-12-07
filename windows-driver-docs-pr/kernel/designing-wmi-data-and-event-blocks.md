---
title: Designing WMI Data and Event Blocks
description: Designing WMI Data and Event Blocks
ms.assetid: 3235accd-2bec-430e-ab00-1c5d0ef46045
keywords: ["WMI WDK kernel , event blocks", "event blocks WDK WMI", "data blocks WDK WMI", "WMI WDK kernel , data blocks", "blocks WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Designing WMI Data and Event Blocks





For best performance and ease of use by WMI clients, a driver should support standard data blocks, and driver writers should follow certain guidelines in designing custom WMI data and event blocks. In particular, driver writers should be aware of performance tradeoffs in choosing static versus dynamic instance names for data blocks. The topics in this section discuss issues and guidelines for designing WMI data and event blocks.

 

 




