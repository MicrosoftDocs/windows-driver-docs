---
title: Pairs (GPD language)
description: To assign a pair of values to an attribute, use the PAIR keyword.
keywords:
- GPD file entries WDK Unidrv , pairs
- pairs WDK GPD files
ms.date: 09/08/2021
ms.localizationpriority: medium
---

# Pairs (GPD language)

To assign a pair of values to an attribute, use the PAIR keyword. The format is:

**PAIR** ( *Value1* , *Value2* )

where *Value1* and *Value2* are [numeric values](numeric-values.md). For example, the cursor origin position can be specified in [master units](master-units.md) as follows:

```cpp
*CursorOrigin: PAIR(120, 100)
```
