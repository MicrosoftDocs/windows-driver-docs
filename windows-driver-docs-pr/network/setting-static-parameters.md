---
title: Setting Static Parameters
description: Setting Static Parameters
ms.assetid: 0a41d8b4-8dd8-4a6b-a9b9-d19d07acd083
keywords:
- add-registry-sections WDK networking , static parameters
- static parameters WDK networking
- parameters WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Static Parameters





An INF file sets a static parameter only once. This parameter cannot be reconfigured through a properties page in the user interface.

An *add-registry-section* adds a static parameter as a REG\_SZ value to a component's instance key as shown in the following example:

```INF
[a1.staticparams.reg]
HKR,, MediaType, 0, "1"
HKR,, InternalId, 0, "232"
```

An *add-registry-section* can add any vendor-defined static parameter to a component's instance key.

 

 





