---
title: Bug Check 0xF SPIN_LOCK_ALREADY_OWNED
description: The SPIN_LOCK_ALREADY_OWNED bug check has a value of 0x0000000F. This indicates that a request for a spin lock has been initiated when the spin lock was already owned.
keywords: ["Bug Check 0xF SPIN_LOCK_ALREADY_OWNED", "SPIN_LOCK_ALREADY_OWNED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- SPIN_LOCK_ALREADY_OWNED
api_type:
- NA
---

# Bug Check 0xF: SPIN\_LOCK\_ALREADY\_OWNED


The SPIN\_LOCK\_ALREADY\_OWNED bug check has a value of 0x0000000F. This indicates that a request for a spin lock has been initiated when the spin lock was already owned.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SPIN\_LOCK\_ALREADY\_OWNED Parameters


None

## Cause

Typically, this error is caused by a recursive request for a spin lock. It can also occur if something similar to a recursive request for a spin lock has been initiated--for example, when a spin lock has been acquired by a thread, and then that same thread calls a function, which also tries to acquire a spin lock. The second attempt to acquire a spin lock is not blocked in this case because doing so would result in an unrecoverable deadlock. If the calls are made on more than one processor, then one processor will be blocked until the other processor releases the lock.

This error can also occur, without explicit recursion, when all threads and all spin locks are assigned an IRQL. Spin lock IRQLs are always greater than or equal to DPC level, but this is not true for threads. However, a thread that is holding a spin lock must maintain an IRQL greater than or equal to that of the spin lock. Decreasing the thread IRQL below the IRQL level of the spin lock that it is holding allows another thread to be scheduled on the processor. This new thread could then attempt to acquire the same spin lock.

## Resolution

Ensure that you are not recursively acquiring the lock. And, for threads that hold a spin lock, ensure that you are not decreasing the thread IRQL to a level below the IRQL of the spin lock that it is holding.

 

 




