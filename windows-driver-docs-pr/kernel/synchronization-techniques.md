---
title: Synchronization Techniques
author: windows-driver-content
description: Synchronization Techniques
ms.assetid: dfee2240-44df-43bc-8804-271203480664
keywords: ["synchronization WDK kernel", "kernel-mode drivers WDK , synchronization", "thread synchronization WDK kernel", "simultaneous access protection WDK kernel", "data integrity WDK kernel", "integrity WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Synchronization Techniques


## <a href="" id="ddk-synchronization-techniques-kg"></a>


This section provides information about the techniques you can use to synchronize driver activities in a multiprocessor-safe manner. The following topics are discussed:

[Kernel Dispatcher Objects](kernel-dispatcher-objects.md)

[Callback Objects](callback-objects.md)

[Spin Locks](spin-locks.md)

[Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md)

[ERESOURCE Structures](eresource-structures.md)

[Additional Timers and Counters](additional-timers-and-counters.md)

[Asynchronous Procedure Calls](asynchronous-procedure-calls.md)

[Acquire and Release Semantics](acquire-and-release-semantics.md)

[Run-Down Protection](run-down-protection.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronization%20Techniques%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


