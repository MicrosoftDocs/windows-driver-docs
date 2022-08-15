---
title: C28751 warning
description: Warning C28751 Banned usage of ExAllocatePool and its variants.
ms.date: 04/20/2017
f1_keywords: 
  - "C28751"
---

# C28751


**Warning C28751: Banned API Usage ExAllocatePool (BANNED_API_USAGE_EXALLOCATEPOOL)**\
Example output: ```Banned usage of ExAllocatePool and its variants: ExAllocatePool is a banned API for improved error handling purposes.```

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement. This specific warning indicates the use of ExAllocatePool or one of its variants, which are deprecated. See [Updating Deprecated ExAllocatePool Calls to ExAllocatePool2 and ExAllocatePool3](../kernel/updating-deprecated-exallocatepool-calls.md) for further information. A list of all banned functions covered by this error and recommended replacements can be found below: 

## Banned Functions 
| Banned API | Replacement Function(s) |
| -----------|----------------|
|```ExAllocatePool```| ```ExAllocatePool2``` |
|```ExAllocatePoolWithTag```| ```ExAllocatePool2```|
|```ExAllocatePoolWithQuota```| ```ExAllocatePool2```|
|```ExAllocatePoolWithQuotaTag```| ```ExAllocatePool2```|
|```ExAllocatePoolWithTagPriority```| ```ExAllocatePool3```|