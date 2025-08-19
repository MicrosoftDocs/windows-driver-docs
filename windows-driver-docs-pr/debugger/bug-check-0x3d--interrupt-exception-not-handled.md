---
title: Bug Check 0x3D INTERRUPT_EXCEPTION_NOT_HANDLED
description: The INTERRUPT_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000003D.
keywords: ["Bug Check 0x3D INTERRUPT_EXCEPTION_NOT_HANDLED", "INTERRUPT_EXCEPTION_NOT_HANDLED"]
ms.date: 10/18/2021
topic_type:
- apiref
ms.topic: reference
api_name:
- INTERRUPT_EXCEPTION_NOT_HANDLED
api_type:
- NA
---

# Bug Check 0x3D: INTERRUPT\_EXCEPTION\_NOT\_HANDLED

The INTERRUPT\_EXCEPTION\_NOT\_HANDLED bug check has a value of 0x0000003D. This indicates that the exception handler for the kernel interrupt object interrupt management was not able to handle the generated exception.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## INTERRUPT\_EXCEPTION\_NOT\_HANDLED Parameters

| Parameter | Description                       |
|-----------|-----------------------------------|
| 1         | Exception Record (When Available) |
| 2         | Context Record  (When Available)  |
| 3         | 0                                 |
| 4         | 0                                 |

## Resolution
 
The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 

