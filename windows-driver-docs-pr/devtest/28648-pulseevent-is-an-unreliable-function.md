---
title: C28648
description: Warning C28648 PulseEvent is an unreliable function.
ms.assetid: 6132e35c-f1ae-44cc-9a6c-b61d6e7f8c57
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28648


warning C28648: PulseEvent is an unreliable function

A thread waiting on a synchronization object can be momentarily removed from the wait state by a kernel-mode APC, and then returned to the wait state after the APC is complete. If the call to **PulseEvent** occurs during the period when the thread was removed from the wait state, the thread will not be released and will "hang" forever. This is because **PulseEvent** releases only those threads that are waiting at the moment it is called.

Some of the ways to fix the use of **PulseEvent**:

-   If only one of the threads waiting on the event needs to be released AND the event is a manual-reset event, change it to an auto-reset event and call **SetEvent** instead of **PulseEvent**.

-   If only one of the threads waiting on the event needs to be released AND the event is an auto-reset event, call **SetEvent** instead of **PulseEvent**.

-   If all threads waiting on the event need to be released AND the event is a manual-reset event, redesign your code to use a different kind of synchronization object (such as a semaphore).

-   If all threads waiting on the event need to be released AND the event is an auto-reset event, call **SetEvent** instead of **PulseEvent** (your original call to **PulseEvent** was releasing only one thread anyway).

 

 





