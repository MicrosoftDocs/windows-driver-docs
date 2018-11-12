---
title: C28625
description: Warning C28625 Function call used to clear sensitive data will be optimized away.
ms.assetid: 9ae44fbc-9a56-41e4-9972-d76d9b62033c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28625


warning C28625: Function call used to clear sensitive data will be optimized away

The current function call might be optimized during compilation, which could make sensitive data stay in memory. Use the **SecureZeroMemory** or **RtlSecureZeroMemory** functions instead. A heuristic looks for identifier names that contain items such as "key" or "pass" to trigger this warning.

 

 





