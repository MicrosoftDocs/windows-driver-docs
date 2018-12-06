---
title: C28157
description: Warning C28157 The IRQL was never restored.
ms.assetid: 3c60253f-5d89-4bb7-9787-9a2aa42bf7fb
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28157


warning C28157: The IRQL was never restored

The current function has a **\_IRQL\_restores\_** annotation, which requires that when it completes, the driver should be executing at an IRQL that was restored from a previous IRQL value. However, there is at least one path in which the driver is executing at a different IRQL when the function completes.

 

 





