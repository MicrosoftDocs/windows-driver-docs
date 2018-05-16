---
title: Lists
author: windows-driver-content
description: Lists
ms.assetid: 69b928fa-8348-437a-ac4d-677f272615dd
keywords:
- GPD file entries WDK Unidrv , lists
- listing attributes WDK GPD files
- LIST keyword
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Lists


## <a href="" id="ddk-lists-gg"></a>


To assign a set of values to an attribute, use the LIST keyword. The format is:

**LIST** ( *Value1* , *Value2* , *Value3* , ..., *ValueN*)

where *Value1*, *Value2*, *Value3*, ..., *ValueN* represent a set of one or more values, all of the type specified for the attribute. For example, the order in which a printer's color plane data should be sent can be specified as follows:

```
*ColorPlaneOrder: LIST(YELLOW, MAGENTA, CYAN, BLACK)
```

 

 




