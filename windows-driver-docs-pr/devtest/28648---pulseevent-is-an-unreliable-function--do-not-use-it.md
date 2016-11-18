---
title: C28648
description: Warning C28648 PulseEvent is an unreliable function.
ms.assetid: 6132e35c-f1ae-44cc-9a6c-b61d6e7f8c57
---

# C28648


warning C28648: PulseEvent is an unreliable function

A thread waiting on a synchronization object can be momentarily removed from the wait state by a kernel-mode APC, and then returned to the wait state after the APC is complete. If the call to **PulseEvent** occurs during the period when the thread was removed from the wait state, the thread will not be released and will "hang" forever. This is because **PulseEvent** releases only those threads that are waiting at the moment it is called.

Some of the ways to fix the use of **PulseEvent**:

-   If only one of the threads waiting on the event needs to be released AND the event is a manual-reset event, change it to an auto-reset event and call **SetEvent** instead of **PulseEvent**.

-   If only one of the threads waiting on the event needs to be released AND the event is an auto-reset event, call **SetEvent** instead of **PulseEvent**.

-   If all threads waiting on the event need to be released AND the event is a manual-reset event, redesign your code to use a different kind of synchronization object (such as a semaphore).

-   If all threads waiting on the event need to be released AND the event is an auto-reset event, call **SetEvent** instead of **PulseEvent** (your original call to **PulseEvent** was releasing only one thread anyway).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28648%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




