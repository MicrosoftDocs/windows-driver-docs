---
title: C28751 Warning
description: Warning C28751 Banned usage of ExAllocatePool and its variants.
ms.date: 08/22/2022
f1_keywords: ["C28751", "BANNED_API_USAGE_EXALLOCATEPOOL", "__WARNING_BANNED_API_USAGE_EXALLOCATEPOOL"]
ms.topic: reference
---
# Warning C28751

> Banned usage of ExAllocatePool and its variants: ExAllocatePool is a banned API for improved error handling purposes.

This warning indicates the use of `ExAllocatePool` or one of its variants, which are deprecated. These APIs should be substituted with their more robust and secure replacements `ExAllocatePool2`/`ExAllocatePool3`.

The new API should be used even if you are already zero-ing your memory because there is too many ways to misuse the banned APIs. If performance is a concern the new APIs provides a flag (`POOl_FLAG_UNINITIALIZED`) that can be used to opt-out of zero-ing your memory. If you do so you will need to take the steps necessary to ensure the your memory is correctly initialized.

## Remarks

See [Updating Deprecated ExAllocatePool Calls to ExAllocatePool2 and ExAllocatePool3](../kernel/updating-deprecated-exallocatepool-calls.md) for further information. A list of all banned functions covered by this error and recommended replacements can be found below.

Code analysis name: BANNED_API_USAGE_EXALLOCATEPOOL

## Banned Functions 

| Banned API | Replacement Function(s) |
| -----------|----------------|
|```ExAllocatePool```| ```ExAllocatePool2``` |
|```ExAllocatePoolWithTag```| ```ExAllocatePool2```|
|```ExAllocatePoolWithQuota```| ```ExAllocatePool2```|
|```ExAllocatePoolWithQuotaTag```| ```ExAllocatePool2```|
|```ExAllocatePoolWithTagPriority```| ```ExAllocatePool3```|
