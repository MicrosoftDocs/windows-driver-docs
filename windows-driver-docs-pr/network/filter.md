---
title: Filter
description: Filter
ms.assetid: eb8f0e55-eefd-48bb-abaa-0658bc977b5f
keywords:
- filters WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter


A *filter* defines several filtering conditions for filtering TCP/IP network data and an action that is to be taken on the data if all the filtering conditions are true. If a filter requires additional processing of the network data, it can specify a [callout](callout.md) for the filter's action. If the filtering conditions for such a filter are all true, the [filter engine](filter-engine.md) passes the network data to the specified callout for additional processing.

 

 





