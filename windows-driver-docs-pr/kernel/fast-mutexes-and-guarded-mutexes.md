---
title: Fast Mutexes and Guarded Mutexes
description: Fast Mutexes and Guarded Mutexes
ms.assetid: 8c8014bf-6b81-4039-ae93-d4cedd6d6fed
keywords: ["synchronization WDK kernel , fast mutexes", "synchronization WDK kernel , guarded mutexes", "guarded mutexes WDK kernel", "fast mutexes WDK kernel", "mutexes WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Fast Mutexes and Guarded Mutexes


Starting with Windows 2000, drivers can use *fast mutexes* if they require a low-overhead form of mutual exclusion for code that runs at IRQL &lt;= APC\_LEVEL. A fast mutex can protect a code path that must be entered by only one thread at a time. To enter the protected code path, the thread *acquires* the mutex. If another thread has already acquired the mutex, execution of the current thread is suspended until the mutex is released. To exit the protected code path, the thread *releases* the mutex.

Starting with Windows Server 2003, drivers can also use *guarded mutexes*. Guarded mutexes are drop-in replacements for fast mutexes but provide better performance. Like a fast mutex, a guarded mutex can protect a code path that must be entered by only one thread at a time. However, code that uses guarded mutexes runs more quickly than code that uses fast mutexes.

In versions of Windows before Windows 8, guarded mutexes are implemented differently from fast mutexes. A code path that is protected by a fast mutex runs at IRQL = APC\_LEVEL. A code path that is protected by a guarded mutex runs at IRQL &lt;= APC\_LEVEL but with all APCs disabled. In these earlier versions of Windows, acquisition of a guarded mutex is a faster operation than acquisition of a fast mutex. However, these two types of mutex behave identically and are subject to the same restrictions. In particular, kernel routines that are illegal to call at IRQL = APC\_LEVEL should not be called from a code path that is protected by either a fast mutex or a guarded mutex.

Starting with Windows 8, guarded mutexes are implemented as fast mutexes. In a code path that is protected by a guarded mutex or a fast mutex, [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) treats calls to kernel routines as occurring at IRQL = APC\_LEVEL. As in earlier versions of Windows, calls that are illegal at APC\_LEVEL are illegal in a code path that is protected by a guarded mutex or a fast mutex.

### Fast Mutexes

A fast mutex is represented by a [**FAST\_MUTEX**](https://msdn.microsoft.com/library/windows/hardware/ff545715) structure. The driver allocates its own storage for a **FAST\_MUTEX** structure and then calls the [**ExInitializeFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff545293) routine to initialize the structure.

A thread acquires a fast mutex by doing one of the following:

-   Calling the [**ExAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff544337) routine. If the mutex has already been acquired by another thread, execution of the calling thread is suspended until the mutex becomes available.

-   Calling the [**ExTryToAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff545647) routine to try to acquire the fast mutex without suspending the current thread. The routine returns immediately, regardless of whether the mutex has been acquired. **ExTryToAcquireFastMutex** returns **TRUE** if it successfully acquired the mutex for the caller; otherwise, it returns **FALSE**.

A thread calls [**ExReleaseFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff545549) to release a fast mutex that was acquired by either **ExAcquireFastMutex** or **ExTryToAcquireFastMutex**.

A code path that is protected by a fast mutex runs at IRQL = APC\_LEVEL. **ExAcquireFastMutex** and **ExTryToAcquireFastMutex** raise the current IRQL to APC\_LEVEL, and **ExReleaseFastMutex** restores the original IRQL. Thus, all APCs are disabled while the thread holds a fast mutex.

If a code path is guaranteed to always run at APC\_LEVEL, the driver can instead call [**ExAcquireFastMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff544340) and [**ExReleaseFastMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff545567) to acquire and release a fast mutex. These routines do not change the current IRQL and can be used safely only when the current IRQL is APC\_LEVEL.

Fast mutexes cannot be acquired recursively. If a thread that is already holding a fast mutex tries to acquire it, that thread will deadlock. Fast mutexes can be used only in code that runs at IRQL &lt;= APC\_LEVEL.

### Guarded Mutexes

Guarded mutexes, which are available starting with Windows Server 2003, perform the same function as fast mutexes but with higher performance.

Starting with Windows 8, guarded mutexes and fast mutexes are implemented identically.

In versions of Windows before Windows 8, guarded mutexes are implemented differently from fast mutexes. Acquiring a fast mutex raises the current IRQL to APC\_LEVEL, while acquiring a guarded mutex enters a guarded region, which is a faster operation. For more information about guarded regions, see [Critical Regions and Guarded Regions](critical-regions-and-guarded-regions.md).

A guarded mutex is represented by a [**KGUARDED\_MUTEX**](https://msdn.microsoft.com/library/windows/hardware/ff554235) structure. The driver allocates its own storage for a **KGUARDED\_MUTEX** structure and then calls the [**KeInitializeGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff552144) routine to initialize the structure.

A thread acquires a guarded mutex by doing one of the following:

-   Calling [**KeAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff551892). If the mutex has already been acquired by another thread, execution of the calling thread is suspended until the mutex becomes available.

-   Calling [**KeTryToAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553307) to try to acquire the guarded mutex without suspending the current thread. The routine returns immediately, regardless of whether the mutex has been acquired. **KeTryToAcquireGuardedMutex** returns **TRUE** if it successfully acquired the mutex for the caller; otherwise, it returns **FALSE**.

A thread calls [**KeReleaseGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553124) to release a guarded mutex that was acquired by either **KeAcquireGuardedMutex** or **KeTryToAcquireGuardedMutex**.

A thread that holds a guarded mutex implicitly runs inside a guarded region. **KeAcquireGuardedMutex** and **KeTryToAcquireGuardedMutex** enter the guarded region, while **KeReleaseGuardedMutex** exits it. All APCs are disabled while the thread holds a guarded mutex.

If a code path is guaranteed to run with all APCs disabled, the driver can instead use [**KeAcquireGuardedMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff551894) and [**KeReleaseGuardedMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff553125) to acquire and release the guarded mutex. These routines do not enter or exit a guarded region and can be used only inside an already-existing guarded region or at IRQL = APC\_LEVEL.

Guarded mutexes cannot be acquired recursively. If a thread that is already holding a guarded mutex tries to acquire it, that thread will deadlock. Guarded mutexes can be used only in code that runs at IRQL &lt;= APC\_LEVEL.

 

 




