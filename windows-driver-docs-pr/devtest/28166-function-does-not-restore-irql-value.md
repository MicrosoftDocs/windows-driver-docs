---
title: C28166
description: Warning C28166 The function does not restore the IRQL to the value that was current at function entry and is required to do so.
ms.assetid: 5835b2e7-0a66-474c-ba1b-40618403075d
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28166


warning C28166: The function does not restore the IRQL to the value that was current at function entry and is required to do so.

This warning indicates that a function has the **\_IRQL\_requires\_same\_** annotation and there is at least one path through the function that does not, by function exit, restore the IRQL to the IRQL at which the driver was running at function entry.

Typically, the **\_IRQL\_requires\_same\_** annotation is used on callback functions.

To avoid this warning, the driver must properly save the initial IRQL value and restore the same IRQL value at function exit, which is what the **\_IRQL\_requires\_same\_** annotation asserts.

 

 





