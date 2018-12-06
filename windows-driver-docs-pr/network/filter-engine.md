---
title: Filter Engine
description: Filter Engine
ms.assetid: 87bf23c7-4086-4016-b712-a083d3d69bbe
keywords:
- filter engine WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Engine


The *filter engine* is a component of the Windows Filtering Platform that stores filters and performs filter arbitration. [Filters](filter.md) are added to the filter engine at designated [filtering layers](filtering-layer.md) so that the filter engine can perform the desired filtering action (permit, drop, or a callout). If a filter in the filter engine specifies a [callout](callout.md) for the filter's action, the filter engine calls the callout's [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) function so that the callout can process the network data.

 

 





