---
title: Pairs
description: Pairs
ms.assetid: 156e6b10-74c2-4702-b0be-b9d209c02070
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

 

 




