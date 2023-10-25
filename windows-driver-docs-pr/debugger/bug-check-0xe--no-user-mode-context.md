---
title: Bug Check 0xE NO_USER_MODE_CONTEXT
description: The NO_USER_MODE_CONTEXT bug check has a value of 0x0000000E.This bug check appears very infrequently.
keywords: ["Bug Check 0xE NO_USER_MODE_CONTEXT", "NO_USER_MODE_CONTEXT"]
ms.date: 06/21/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- NO_USER_MODE_CONTEXT
api_type:
- NA
---

# Bug Check 0xE: NO\_USER\_MODE\_CONTEXT

The NO\_USER\_MODE\_CONTEXT bug check has a value of 0x0000000E.

In the process of starting a system thread, if control returns from the initial thread procedure, a bug check will occur.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Resolution
The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
