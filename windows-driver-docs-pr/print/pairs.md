---
title: Pairs (GPD language)
description: To assign a pair of values to an attribute, use the PAIR keyword.
keywords:
- GPD file entries WDK Unidrv , pairs
- pairs WDK GPD files
ms.date: 01/30/2023
---

# Pairs (GPD language)

[!include[Print Support Apps](../includes/print-support-apps.md)]

To assign a pair of values to an attribute, use the PAIR keyword. The format is:

**PAIR** ( *Value1* , *Value2* )

where *Value1* and *Value2* are [numeric values](numeric-values.md). For example, the cursor origin position can be specified in [master units](master-units.md) as follows:

```GPD
*CursorOrigin: PAIR(120, 100)
```
