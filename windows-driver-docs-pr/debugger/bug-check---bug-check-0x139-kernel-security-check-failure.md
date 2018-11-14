---
title: Bug Check 0x139 KERNEL_SECURITY_CHECK_FAILURE
description: The KERNEL_SECURITY_CHECK_FAILURE bug check has a value of 0x00000139. This bug check indicates that the kernel has detected the corruption of a critical data structure.
ms.assetid: C0E5C625-13DB-4B3A-8080-69CEB963A299
keywords: ["Bug Check 0x139 KERNEL_SECURITY_CHECK_FAILURE", "Bug Check 0x139 KERNEL_SECURITY_CHECK_FAILURE"]
ms.author: domars
ms.date: 06/27/2018
topic_type:
- apiref
api_name:
- Bug Check 0x139 KERNEL_SECURITY_CHECK_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x139: KERNEL\_SECURITY\_CHECK\_FAILURE


The KERNEL\_SECURITY\_CHECK\_FAILURE bug check has a value of 0x00000139. This bug check indicates that the kernel has detected the corruption of a critical data structure.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## Bug Check 0x139 KERNEL\_SECURITY\_CHECK\_FAILURE Parameters


| Parameter | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 1         | The type of corruption. For more information, see the following table.      |
| 2         | Address of the trap frame for the exception that caused the bug check       |
| 3         | Address of the exception record for the exception that caused the bug check |
| 4         | Reserved                                                                    |

 

The following table describes possible values for Parameter 1.

| Parameter 1 | Description                                                                                                                                                                                                                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 | A stack-based buffer has been overrun (legacy /GS violation).                                                                                                                                                                                                                                                     |
| 1  |  VTGuard instrumentation code detected an attempt to use an illegal virtual function table. Typically, a C++ object was corrupted, and then a virtual method call was attempted using the corrupted object's **this** pointer.                                                                                     |
| 2  |  Stack cookie instrumentation code detected a stack-based buffer overrun (/GS violation).                                                                                                                                                                                                                          |
| 3  |  A LIST\_ENTRY was corrupted (for example, a double remove). For more information, see the following Cause section.                                                                                                                                                                                                |
| 4  |  Reserved                                                                                                                                                                                                                                                                                                          |
| 5  |  An invalid parameter was passed to a function that considers invalid parameters fatal.                                                                                                                                                                                                                            |
| 6  |  The stack cookie security cookie was not properly initialized by the loader. This may be caused by building a driver to run only on Windows 8 and attempting to load the driver image on an earlier version of Windows. To avoid this problem, you must build the driver to run on an earlier version of Windows. |
| 7  |  A fatal program exit was requested.                                                                                                                                                                                                                                                                               |
| 8  |  A array bounds check inserted by the compiler detected an illegal array indexing operation.                                                                                                                                                                                                                       |
| 9  |  A call to **RtlQueryRegistryValues** was made specifying RTL\_QUERY\_REGISTRY\_DIRECT without RTL\_QUERY\_REGISTRY\_TYPECHECK, and the target value was not in a trusted system hive.                                                                                                                             |
|   10 |  Indirect call guard check detected invalid control transfer. |
|   11 | Write guard check detected invalid memory write. |
|   12 | An attempt was made to switch to an invalid fiber context. |
|   13 | An attempt was made to assign an invalid register context. |
|   14 | The reference count for an object is invalid. |
|   18 | An attempt was made to switch to an invalid jmp_buf context. |
|   19 | An unsafe modification was made to read-only data. |
|   20 | A cryptographic self-test failed. |
|   21 | An invalid exception chain was detected. |
|   22 | A cryptographic library error occurred. |
|   23 | An invalid call was made from within DllMain. |
|   24 | An invalid image base address was detected. |
|   25 | An unrecoverable failure was encountered while protecting a delay load import. |
|   26 | A call was made to an unsafe extension. |
|   27 | A deprecated service was invoked. |
|   28 | An out of bounds buffer access was detected. |
|   29 | An RTL_BALANCED_NODE RBTree entry has been corrupted. |
|   37 | An out of range switch jumptable entry was invoked. |
|   38 | A longjmp was attempted to an invalid target. |
|   39 | An export suppressed call target couldn't be made a valid call target. |
 

Cause
-----

Using the parameter 1 table, and a dump file, it is possible to narrow down the cause for many bug checks of this type.

LIST\_ENTRY corruption can be difficult to track down and this bug check, indicates that an inconsistency has been introduced into a doubly-linked list (detected when an individual list entry element is added to or removed from the list). Unfortunately, the inconsistency is not necessarily detected at the time when the corruption occurred, so some detective work may be necessary to identify the root cause.

Common causes of list entry corruption include:

-   A driver has corrupted a kernel synchronization object, such as a KEVENT (for example double initializing a KEVENT while a thread was still waiting on that same KEVENT, or allowing a stack-based KEVENT to go out of scope while another thread was using that KEVENT). This type of bug check typically occurs in nt!Ke\* or nt!Ki\* code. It can happen when a thread finishes waiting on a synchronization object or when code attempts to put a synchronization object in the signaled state. Usually, the synchronization object being signaled is the one that has been corrupted. Sometimes, Driver Verifier with special pool can help track down the culprit (if the corrupted synchronization object is in a pool block that has already been freed).
-   A driver has corrupted a periodic KTIMER. This type of bug check typically occurs in nt!Ke\* or nt!Ki\* code and involves signaling a timer, or inserting or removing a timer from a timer table. The timer being manipulated may be the corrupted one, but it might be necessary to inspect the timer table with [**!timer**](-timer.md) (or manually walking the timer list links) to identify which timer has been corrupted. Sometimes, Driver Verifier with special pool can help track down the culprit (if the corrupted KTIMER is in a pool block that has already been freed).
-   A driver has mismanaged an internal LIST\_ENTRY-style linked list. A typical example would be calling **RemoveEntryList** twice on the same list entry without reinserting the list entry between the two **RemoveEntryList** calls. Other variations are possible, such as double inserting an entry into the same list.
-   A driver has freed a data structure that contains a LIST\_ENTRY without removing the data structure from its corresponding list, causing corruption to be detected later when the list is examined after the old pool block has been reused.
-   A driver has used a LIST\_ENTRY-style list in a concurrent fashion without proper synchronization, resulting in a torn update to the list.

In most cases, you can identify the corrupted data structure by walking the linked list both forward and backwards (the [**dl**](dl--display-linked-list-.md) and **dlb** commands are useful for this purpose) and comparing the results. Where the list is inconsistent between a forward and backward walk is typically the location of the corruption. Since a linked list update operation can modify the list links of a neighboring element, you should look at the neighbors of a corrupted list entry closely, as they may be the underlying culprit.

Because many system components internally utilize LIST\_ENTRY lists, various types of resource mismanagement by a driver using system APIs might cause linked list corruption in a system-managed linked list.

Resolution
----------

Determining the cause of this issues typically requires the use of the debugger to gather additional information. Multiple dump files should be examined to see if this stop code has similar characteristics, such as the code that is running when the stop code appears.

For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md), [Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md).

Use the event log to see if there are higher level events that occur leading up to this stop code.

These general troubleshooting tips may be helpful.

-   If you recently added hardware to the system, try removing or replacing it. Or check with the manufacturer to see if any patches are available.

-   If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

-   Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows, and resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

## <span id="see_also"></span>See also


[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

 

 




