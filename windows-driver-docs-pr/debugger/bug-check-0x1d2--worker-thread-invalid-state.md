---
title: Bug Check 0x1D2 WORKER_THREAD_INVALID_STATE  
description: The WORKER_THREAD_INVALID_STATE bug check has a value of 0x000001D2.
keywords: ["Bug Check 0x1D2 WORKER_THREAD_INVALID_STATE", "WORKER_THREAD_INVALID_STATE"]
ms.date: 05/23/2018
topic_type:
- apiref
api_name:
- WORKER_THREAD_INVALID_STATE
api_type:
- NA
---

# Bug Check 0x1D2: WORKER\_THREAD\_INVALID\_STATE 

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


The WORKER\_THREAD\_INVALID\_STATE  bug check has a value of 0x000001D2. 

This error indicates that an executive worker thread is in an invalid state.

## WORKER\_THREAD\_INVALID\_STATE Parameters

Parameter | Description 
|---------|--------------|
1 | Type of failure
2 | Address of the worker thread
3 | Reserved
4 | Reserved



**Parameter 1 Values**

  0x0 : A worker thread in the process of terminating has outstanding I/O
  
  2 - Address of the worker thread
  
  3 - Reserved
  
  4 - Reserved
