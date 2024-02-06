---
title: C28730 Warning
description: Warning C28730 Possible assignment of '\\0' directly to a pointer.
ms.date: 04/20/2017
f1_keywords: 
  - "C28730"
---

# C28730


warning C28730: Possible assignment of '\\\\0' directly to a pointer.

This warning indicates a probable typographical error: a **nul** character is being assigned to a pointer; it is probably the case that the character is intended as a string terminator and should be assigned to the memory where the pointer is pointing.

