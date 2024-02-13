---
title: C28639 Warning
description: Warning C28639 Calling close handle with string.
ms.date: 04/20/2017
f1_keywords: 
  - "C28639"
---

# C28639


warning C28639: Calling close handle with string

The function **CloseHandle** takes a **void \\*** parameter. It is possible to cast (among other things) a string pointer to a **void \\*** and pass it as an argument when the intention was to pass a handle opened using the string.

