---
title: C28157 Warning
description: Warning C28157 The IRQL was never restored.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28157"
---

# C28157


warning C28157: The IRQL was never restored

The current function has a **\_IRQL\_restores\_** annotation, which requires that when it completes, the driver should be executing at an IRQL that was restored from a previous IRQL value. However, there is at least one path in which the driver is executing at a different IRQL when the function completes.

