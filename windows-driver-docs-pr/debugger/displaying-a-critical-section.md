---
title: Displaying a Critical Section
description: Displaying a Critical Section
ms.assetid: d55971f6-9112-417d-8fb6-e299c7fc90a7
keywords: ["critical section", "critical section, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Displaying a Critical Section


## <span id="ddk_displaying_a_critical_section_dbg"></span><span id="DDK_DISPLAYING_A_CRITICAL_SECTION_DBG"></span>


Critical sections can be displayed in user mode by a variety of different methods. The exact meaning of each field depends on the version of Microsoft Windows version you are using.

### <span id="displaying_critical_sections"></span><span id="DISPLAYING_CRITICAL_SECTIONS"></span>Displaying Critical Sections

Critical sections can be displayed by the **!ntsdexts.locks** extension, the **!critsec** extension, the **!cs** extension, and the **dt (Display Type)** command.

The [**!ntsdexts.locks**](-locks---ntsdexts-locks-.md) extension displays a list of critical sections associated with the current process. If the **-v** option is used, all critical sections are displayed. Here is an example:

```dbgcmd
0:000> !locks

CritSec ntdll!FastPebLock+0 at 77FC49E0
LockCount          0
RecursionCount     1
OwningThread       c78
EntryCount         0
ContentionCount    0
*** Locked

....
Scanned 37 critical sections
```

If you know the address of the critical section you wish to display, you can use the [**!critsec**](-critsec.md) extension. This displays the same collection of information as **!ntsdexts.locks**. For example:

```dbgcmd
0:000> !critsec 77fc49e0

CritSec ntdll!FastPebLock+0 at 77FC49E0
LockCount          0
RecursionCount     1
OwningThread       c78
EntryCount         0
ContentionCount    0
*** Locked
```

The [**!cs**](-cs.md) extension can display a critical section based on its address, search an address range for critical sections, and even display the stack trace associated with each critical section. Some of these features require full Windows symbols to work properly. If Application Verifier is active, **!cs -t** can be used to display the critical section tree. See the **!cs** reference page for details and examples.

The information displayed by **!cs** is slightly different than that shown by **!ntsdexts.locks** and **!critsec**. For example:

```dbgcmd
## 0:000> !cs 77fc49e0

Critical section   = 0x77fc49e0 (ntdll!FastPebLock+0x0)
DebugInfo          = 0x77fc3e00
LOCKED
LockCount          = 0x0
OwningThread       = 0x00000c78
RecursionCount     = 0x1
LockSemaphore      = 0x0
SpinCount          = 0x00000000
```

The [**dt (Display Type)**](dt--display-type-.md) command can be used to display the literal contents of the RTL\_CRITICAL\_SECTION structure. For example:

```dbgcmd
0:000> dt RTL_CRITICAL_SECTION 77fc49e0
   +0x000 DebugInfo        : 0x77fc3e00 
   +0x004 LockCount        : 0
   +0x008 RecursionCount   : 1
   +0x00c OwningThread     : 0x00000c78 
   +0x010 LockSemaphore    : (null) 
   +0x014 SpinCount        : 0
```

### <span id="interpreting_critical_section_fields_in_windows_xp_and_windows_2000"></span><span id="INTERPRETING_CRITICAL_SECTION_FIELDS_IN_WINDOWS_XP_AND_WINDOWS_2000"></span>Interpreting Critical Section Fields in Windows XP and Windows 2000

The most important fields of the critical section structure are as follows:

-   In Microsoft Windows 2000, and Windows XP, the **LockCount** field indicates the number of times that any thread has called the **EnterCriticalSection** routine for this critical section, minus one. This field starts at -1 for an unlocked critical section. Each call of **EnterCriticalSection** increments this value; each call of **LeaveCriticalSection** decrements it. For example, if **LockCount** is 5, this critical section is locked, one thread has acquired it, and five additional threads are waiting for this lock.

-   The **RecursionCount** field indicates the number of times that the owning thread has called **EnterCriticalSection** for this critical section.

-   The **EntryCount** field indicates the number of times that a thread other than the owning thread has called **EnterCriticalSection** for this critical section.

A newly initialized critical section looks like this:

```dbgcmd
0:000> !critsec 433e60
CritSec mymodule!cs+0 at 00433E60
LockCount          NOT LOCKED 
RecursionCount     0
OwningThread       0
EntryCount         0
ContentionCount    0
```

The debugger displays "NOT LOCKED" as the value for **LockCount**. The actual value of this field for an unlocked critical section is -1. You can verify this with the **dt (Display Type)** command:

```dbgcmd
0:000> dt RTL_CRITICAL_SECTION 433e60
   +0x000 DebugInfo        : 0x77fcec80
   +0x004 LockCount        : -1
   +0x008 RecursionCount   : 0
   +0x00c OwningThread     : (null) 
   +0x010 LockSemaphore    : (null) 
   +0x014 SpinCount        : 0
```

When the first thread calls the **EnterCriticalSection** routine, the critical section's **LockCount**, **RecursionCount**, **EntryCount** and **ContentionCount** fields are all incremented by one, and **OwningThread** becomes the thread ID of the caller. **EntryCount** and **ContentionCount** are never decremented. For example:

```dbgcmd
0:000> !critsec 433e60
CritSec mymodule!cs+0 at 00433E60
LockCount          0
RecursionCount     1
OwningThread       4d0
EntryCount         0
ContentionCount    0
```

At this point, four different things can happen.

1.  The owning thread calls **EnterCriticalSection** again. This will increment **LockCount** and **RecursionCount**. **EntryCount** is not incremented.

    ```dbgcmd
    0:000> !critsec 433e60
    CritSec mymodule!cs+0 at 00433E60
    LockCount          1
    RecursionCount     2
    OwningThread       4d0
    EntryCount         0
    ContentionCount    0
    ```

2.  A different thread calls **EnterCriticalSection**. This will increment **LockCount** and **EntryCount**. **RecursionCount** is not incremented.

    ```dbgcmd
    0:000> !critsec 433e60
    CritSec mymodule!cs+0 at 00433E60
    LockCount          1
    RecursionCount     1
    OwningThread       4d0
    EntryCount         1
    ContentionCount    1
    ```

3.  The owning thread calls **LeaveCriticalSection**. This will decrement **LockCount** (to -1) and **RecursionCount** (to 0), and will reset **OwningThread** to 0.

    ```dbgcmd
    0:000> !critsec 433e60
    CritSec mymodule!cs+0 at 00433E60
    LockCount          NOT LOCKED 
    RecursionCount     0
    OwningThread       0
    EntryCount         0
    ContentionCount    0
    ```

4.  Another thread calls **LeaveCriticalSection**. This produces the same results as the owning thread calling **LeaveCriticalSection** -- it will decrement **LockCount** (to -1) and **RecursionCount** (to 0), and will reset **OwningThread** to 0.

When any thread calls **LeaveCriticalSection**, Windows decrements **LockCount** and **RecursionCount**. This feature has both good and bad aspects. It allows a device driver to enter a critical section on one thread and leave the critical section on another thread. However, it also makes it possible to accidentally call **LeaveCriticalSection** on the wrong thread, or to call **LeaveCriticalSection** too many times and cause **LockCount** to reach values lower than -1. This corrupts the critical section and causes all threads to wait indefinitely on the critical section.

### <span id="interpreting_critical_section_fields_in_windows_server_2003_sp1_and_la"></span><span id="INTERPRETING_CRITICAL_SECTION_FIELDS_IN_WINDOWS_SERVER_2003_SP1_AND_LA"></span>Interpreting Critical Section Fields in Windows Server 2003 SP1 and Later

In Microsoft Windows Server 2003 Service Pack 1 and later versions of Windows, the **LockCount** field is parsed as follows:

-   The lowest bit shows the lock status. If this bit is 0, the critical section is locked; if it is 1, the critical section is not locked.

-   The next bit shows whether a thread has been woken for this lock. If this bit is 0, then a thread has been woken for this lock; if it is 1, no thread has been woken.

-   The remaining bits are the ones-complement of the number of threads waiting for the lock.

As an example, suppose the **LockCount** is -22. The lowest bit can be determined in this way:

```dbgcmd
0:009> ? 0x1 & (-0n22)
Evaluate expression: 0 = 00000000
```

The next-lowest bit can be determined in this way:

```dbgcmd
0:009> ? (0x2 & (-0n22)) >> 1
Evaluate expression: 1 = 00000001
```

The ones-complement of the remaining bits can be determined in this way:

```dbgcmd
0:009> ? ((-1) - (-0n22)) >> 2
Evaluate expression: 5 = 00000005
```

In this example, the first bit is 0 and therefore the critical section is locked. The second bit is 1, and so no thread has been woken for this lock. The complement of the remaining bits is 5, and so there are five threads waiting for this lock.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about how to debug critical section time outs, see [Critical Section Time Outs](critical-section-time-outs.md). For general information about critical sections, see the Microsoft Windows SDK, the Windows Driver Kit (WDK), or *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

 

 





