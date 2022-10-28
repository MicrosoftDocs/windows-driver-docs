---
title: Bug Check 0x1ED HANDLE_ERROR_ON_CRITICAL_THREAD
description: The HANDLE_ERROR_ON_CRITICAL_THREAD bug check has a value of 0x000001ED. This indicates that an invalid handle access problem was detected in kernel mode on a system-critical thread.
keywords: ["Bug Check 0x1ED HANDLE_ERROR_ON_CRITICAL_THREAD", "HANDLE_ERROR_ON_CRITICAL_THREAD"]
ms.date: 09/13/2022
topic_type:
- apiref
api_name:
- HANDLE_ERROR_ON_CRITICAL_THREAD
api_type:
- NA
---

# Bug Check 0x1ED: HANDLE\_ERROR\_ON\_CRITICAL\_THREAD

The HANDLE\_ERROR\_ON\_CRITICAL\_THREAD bug check has a value of 0x000001ED. This indicates that an invalid handle access problem was detected in kernel mode on a system-critical thread.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## HANDLE\_ERROR\_ON\_CRITICAL\_THREAD Parameters

| Parameter | Description |
|-----------|-------------|
| 1         | Reserved    |
| 2         | Reserved    |
| 3         | Reserved    |
| 4         | Reserved    |
 

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

 ## See also

[Bug Check Code Reference](bug-check-code-reference2.md)
 
