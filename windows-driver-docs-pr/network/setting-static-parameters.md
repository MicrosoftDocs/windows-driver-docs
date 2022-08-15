---
title: Setting Static Parameters
description: Setting Static Parameters
keywords:
- add-registry-sections WDK networking , static parameters
- static parameters WDK networking
- parameters WDK networking
ms.date: 04/20/2017
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

 

 





