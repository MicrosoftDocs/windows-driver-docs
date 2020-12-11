---
title: Pairs
description: Pairs
keywords:
- GPD file entries WDK Unidrv , pairs
- pairs WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pairs





To assign a pair of values to an attribute, use the PAIR keyword. The format is:

**PAIR** ( *Value1* , *Value2* )

where *Value1* and *Value2* are [numeric values](numeric-values.md). For example, the cursor origin position can be specified in [master units](master-units.md) as follows:

```cpp
*CursorOrigin: PAIR(120, 100)
```

 

 




