---
title: Filter Engine
description: Filter Engine
keywords:
- filter engine WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Engine


The *filter engine* is a component of the Windows Filtering Platform that stores filters and performs filter arbitration. [Filters](filter.md) are added to the filter engine at designated [filtering layers](filtering-layer.md) so that the filter engine can perform the desired filtering action (permit, drop, or a callout). If a filter in the filter engine specifies a [callout](callout.md) for the filter's action, the filter engine calls the callout's [*classifyFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_classify_fn0) function so that the callout can process the network data.

 

