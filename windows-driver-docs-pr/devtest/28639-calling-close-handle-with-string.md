---
title: C28639
description: Warning C28639 Calling close handle with string.
ms.assetid: 346b9798-3719-4b8e-8edd-f8ee3b751cef
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28639


warning C28639: Calling close handle with string

The function **CloseHandle** takes a **void \\*** parameter. It is possible to cast (among other things) a string pointer to a **void \\*** and pass it as an argument when the intention was to pass a handle opened using the string.

 

 





