---
title: Lists (GPD language)
description: To assign a set of values to an attribute, use the LIST keyword.
keywords:
- GPD file entries WDK Unidrv , lists
- listing attributes WDK GPD files
- LIST keyword
ms.date: 09/07/2021
ms.localizationpriority: medium
---

# Lists (GPD language)

To assign a set of values to an attribute, use the LIST keyword. The format is:

**LIST** ( *Value1* , *Value2* , *Value3* , ..., *ValueN*)

where *Value1*, *Value2*, *Value3*, ..., *ValueN* represent a set of one or more values, all of the type specified for the attribute. For example, the order in which a printer's color plane data should be sent can be specified as follows:

```cpp
*ColorPlaneOrder: LIST(YELLOW, MAGENTA, CYAN, BLACK)
```
