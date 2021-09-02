---
title: C28158 warning
description: Warning C28158 No IRQL was saved.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28158"
---

# C28158


warning C28158: No IRQL was saved

A **\_IRQL\_saves\_** annotation specifies that the current function will save an IRQL value in the specified variable, but there is at least one path in which the IRQL value is not saved in that variable.

 

 





