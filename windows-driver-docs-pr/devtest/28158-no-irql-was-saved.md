---
title: C28158
description: Warning C28158 No IRQL was saved.
ms.assetid: f1ae0de8-e2c8-4aa5-b2db-8aecff68c872
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28158


warning C28158: No IRQL was saved

A **\_IRQL\_saves\_** annotation specifies that the current function will save an IRQL value in the specified variable, but there is at least one path in which the IRQL value is not saved in that variable.

 

 





