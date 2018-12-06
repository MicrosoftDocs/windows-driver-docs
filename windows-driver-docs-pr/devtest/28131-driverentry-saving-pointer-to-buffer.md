---
title: C28131
description: Warning C28131 The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer.
ms.assetid: 9661f17e-a19a-4230-a848-8233f635db09
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28131


warning C28131: The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer

The driver's *DriverEntry* routine is saving a copy of the pointer to the buffer instead of saving a copy of the buffer. Because the buffer is freed when the *DriverEntry* routine returns, the pointer to the buffer will soon be invalid.

 

 





