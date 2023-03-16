---
title: Bug Check 0x20001 HYPERVISOR_ERROR
description: The HYPERVISOR_ERROR bug check has a value of 0x00020001. This indicates that the hypervisor has encountered a fatal error.
keywords: ["Bug Check 0x20001 HYPERVISOR_ERROR", "HYPERVISOR_ERROR"]
ms.date: 05/15/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- HYPERVISOR_ERROR
api_type:
- NA
---

# Bug Check 0x20001: HYPERVISOR\_ERROR

The HYPERVISOR\_ERROR bug check has a value of 0x00020001. This indicates that the hypervisor has encountered a fatal error.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## HYPERVISOR\_ERROR Parameters


| Parameter | Description |
|-----------|-------------|
| 1         | Reserved    |
| 2         | Reserved    |
| 3         | Reserved    |
| 4         | Reserved    |

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
