---
title: Bug Check 0xE NO_USER_MODE_CONTEXT
description: The NO_USER_MODE_CONTEXT bug check has a value of 0x0000000E.This bug check appears very infrequently.
ms.assetid: 0c3b3da9-c9e6-443d-9087-9bee9aa1e41a
keywords: ["Bug Check 0xE NO_USER_MODE_CONTEXT", "NO_USER_MODE_CONTEXT"]
ms.date: 06/21/2019
topic_type:
- apiref
api_name:
- NO_USER_MODE_CONTEXT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE: NO\_USER\_MODE\_CONTEXT

The NO\_USER\_MODE\_CONTEXT bug check has a value of 0x0000000E.

In the process of starting a system thread, if control returns from the initial thread procedure, a bug check will occur.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Resolution
The [**!analyze**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be helpful in determining the root cause.
