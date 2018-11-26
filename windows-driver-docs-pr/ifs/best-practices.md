---
title: Best Practices
description: Best Practices
ms.assetid: c01b3fd9-7f4e-4d1a-a726-b31b0eebf094
keywords:
- contexts WDK file system minifilter , best practices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Best Practices


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


If a minifilter driver creates only one minifilter driver instance per volume, it should use instance contexts rather than volume contexts for better performance.

A minifilter driver can also improve performance by storing a pointer to the minifilter driver instance context inside its stream or stream handle contexts.

 

 




