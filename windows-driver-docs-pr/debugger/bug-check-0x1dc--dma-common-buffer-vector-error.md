---
title: Bug Check 0x1DC DMA_COMMON_BUFFER_VECTOR_ERROR
description: The DMA_COMMON_BUFFER_VECTOR_ERROR bug check has a value of 0x000001DC. It indicates that driver has misused the DMA vectored common buffer APIs.
keywords: ["Bug Check 0x1DC DMA_COMMON_BUFFER_VECTOR_ERROR", "DMA_COMMON_BUFFER_VECTOR_ERROR"]
ms.date: 01/30/2019
topic_type:
- apiref
api_name:
- DMA_COMMON_BUFFER_VECTOR_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1DC: DMA\_COMMON\_BUFFER\_VECTOR\_ERROR

The DMA\_COMMON\_BUFFER\_VECTOR\_ERROR bug check has a value of 0x000001DC. It indicates that a driver has misused the DMA vectored common buffer APIs.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## DMA\_COMMON\_BUFFER\_VECTOR\_ERROR Parameters

|Parameter|Description|
|-------- |---------- |
|1| Indicates the type of failure. See values below.|
|2| See values below. |
|3| See values below. |
|4| See values below. |

**Type of Failure**

```text
0x01 : Wrong IRQL
    2 - Current IRQL.

x02 : Vector not empty.
    2 - Index of remaining buffer.
    3 - Virtual Address of remaining buffer.
    4 - Logical address of remaining buffer.

0x03 : Index out of bounds.
    2 - Number of available entries.
    3 - Index requested.

0x04 : Index freed.
    2 - Index requested.

0x05 : Common buffer leaked.
```

## ## Cause

A driver has misused the DMA vectored common buffer APIs. The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

