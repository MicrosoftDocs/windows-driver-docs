---
title: Lists (GPD language)
description: To assign a set of values to an attribute, use the LIST keyword.
keywords:
- GPD file entries WDK Unidrv , lists
- listing attributes WDK GPD files
- LIST keyword
ms.date: 01/27/2023
---

# Lists (GPD language)

[!include[Print Support Apps](../includes/print-support-apps.md)]

To assign a set of values to an attribute, use the LIST keyword. The format is:

**LIST** ( *Value1* , *Value2* , *Value3* , ..., *ValueN*)

where *Value1*, *Value2*, *Value3*, ..., *ValueN* represent a set of one or more values, all of the type specified for the attribute. For example, the order in which a printer's color plane data should be sent can be specified as follows:

```GPD
*ColorPlaneOrder: LIST(YELLOW, MAGENTA, CYAN, BLACK)
```
