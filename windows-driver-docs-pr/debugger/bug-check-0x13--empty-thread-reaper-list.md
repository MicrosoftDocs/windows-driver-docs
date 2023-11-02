---
title: Bug Check 0x13 EMPTY_THREAD_REAPER_LIST
description: The EMPTY_THREAD_REAPER_LIST bug check has a value of 0x00000013.This bug check appears very infrequently.
keywords: ["Bug Check 0x13 EMPTY_THREAD_REAPER_LIST", "EMPTY_THREAD_REAPER_LIST"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- EMPTY_THREAD_REAPER_LIST
api_type:
- NA
---

# Bug Check 0x13: EMPTY\_THREAD\_REAPER\_LIST


The EMPTY\_THREAD\_REAPER\_LIST bug check has a value of 0x00000013.

This bug check **never** appears.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Cause

This bug check has only been in use during the early development stages of Windows NT. It has since been unused.

Upon terminating, Windows threads notify the thread reaper to clean up after them. Early in Windows NT development, this error would indicate that the thread reaper had received a cleanup request but not details of what to clean up. The design of Windows has since changed to mitigate this condition without generating a stop error.

## Resolution

All reports of this stop error are false. Examine the faulty source that generated the false positive.

## Citations

- Chen, Raymond. [“What Is the Thread Reaper?”](https://devblogs.microsoft.com/oldnewthing/20231031-00/?p=108944) _The Old New Thing_, Microsoft Corporation, 31 Oct. 2023.
