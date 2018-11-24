---
title: Miscellaneous Checks
description: Miscellaneous Checks
ms.assetid: 4d7b14ae-5a3a-49b4-9678-6527cbacc4d4
keywords:
- Miscellaneous Checks option WDK Driver Verifier
- lookasides WDK Driver Verifier
- freed memory WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miscellaneous Checks


The Miscellaneous Checks option of Driver Verifier monitors the driver for common errors that cause the driver or system to crash, such as freeing memory that still contains active kernel objects.

Specifically, the Miscellaneous Checks option looks for the following improper driver behavior:

-   **Active work items in freed memory.** The driver calls [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) to free a pool block that contains work items that were queued by using [**IoQueueWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549466).. (This check is enabled by default in the checked build of Windows Server 2003.)

-   **Active resources in freed memory.** The driver calls [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) to free a pool block that contains active [ERESOURCE structures](https://msdn.microsoft.com/library/windows/hardware/ff544281). The driver should call [**ExDeleteResource**](https://msdn.microsoft.com/library/windows/hardware/ff544572) to delete ERESOURCE objects before calling **ExFreePool**.

-   **Active lookaside lists in freed memory.** The driver calls [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) to free a pool block that still contains active lookaside lists ([**NPAGED\_LOOKASIDE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff556431) or [**PAGED\_LOOKASIDE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff558775) structures. The driver should call [**ExDeleteNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544566) or [**ExDeletePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544570) to delete the lookaside lists before calling **ExFreePool**.

-   **Windows Management Instrumentation (WMI) and Event Tracing for Windows (ETW) registration issues.** Such issues detected by Driver Verifier include:
    -   A driver that attempts to unload without unregistering its WMI callback.
    -   A driver that attempts to delete a device object that has not been unregistered from WMI.
    -   A driver that attempts to unload without unregistering its ETW kernel-mode providers.
    -   A driver that attempts to unregister a provider that is already unregistered.
-   **Kernel handle errors.** (Windows Vista and later versions) Enabling the Miscellaneous Checks option will also enable handle tracing for the system process to aid in investigating kernel handle leaks and [**Bug Check 0x93: INVALID\_KERNEL\_HANDLE**](https://msdn.microsoft.com/library/windows/hardware/ff559292). With handle tracing enabled, the kernel will collect stack traces for recent handle open and close operations. The stack traces can be displayed in the kernel debugger using the **!htrace** debugger extension. For more information about **!htrace**, see the Debugging Tools for Windows documentation.

-   **User-mode handle with kernel mode access** Starting with Windows 7, when you select the Miscellaneous Checks option, Driver Verifier also checks on calls to [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679). You cannot pass a user-mode handle with kernel mode access. If such an operation occurs, Driver Verifier issues Bug Check 0xC4, with a parameter 1 value of 0xF6.

-   **UserMode Wait for Synchronization Objects Allocated on the Kernel Stack**

    Starting with Windows 7, Driver Verifier can detect additional ways that drivers can incorrectly use the multithreading synchronization mechanisms that the operating system provides.

    Allocating synchronization objects, such as KEVENT structures, as local variables on the kernel stack is a common practice. While a process is loaded in memory, the kernel stacks of its threads are never trimmed from the working set or paged out to the disk. Allocating synchronization objects in such nonpageable memory is correct.

    However, when drivers call APIs such as [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) or [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) to wait for an object that is allocated on the stack, they must specify the **KernelMode** value for the API’s *WaitMode* parameter. When all threads of a process are waiting in **UserMode** mode, that process becomes eligible to be swapped out to the disk. Therefore, if a driver specified **UserMode** as the *WaitMode* parameter, the operating system can swap out the current process as long as every other thread in the same process is waiting as **UserMode**, too. Swapping an entire process out to the disk includes paging out its kernel stacks. Waiting on a synchronization object that the operating system has swapped out is incorrect. At some point a thread must come along and signal the synchronization object. Signaling a synchronization object involves the Windows kernel manipulating the object at IRQL = DISPATCH\_LEVEL or above. Touching paged out or swapped out memory at DISPATCH\_LEVEL or above results in a system crash.

    Starting in Windows 7, when you select the Miscellaneous Checks option, Driver Verifier checks that the synchronization objects that the verified driver uses for waiting in **UserMode** are not allocated on the current thread’s kernel stack. When Driver Verifier detects such an incorrect wait, it issues a [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), with a parameter 1 value of 0x123.

-   **Incorrect Kernel Handle References**

    Each Windows process has a handle table. You can view the handle table as an array of handle entries. Each valid handle value refers to a valid entry in this array.

    A *kernel handle* as a handle that is valid for the System process’s handle table. A *user handle* as a handle that is valid for any process except the System process.

    In Windows 7, Driver Verifier detects tries to reference kernel handle values that are incorrect. These driver defects are reported as a [**Bug Check 0x93: INVALID\_KERNEL\_HANDLE**](https://msdn.microsoft.com/library/windows/hardware/ff559292) if the Driver Verifier Miscellaneous Checks option is enabled. Usually this kind of incorrect handle reference means that the driver has closed that handle already but is trying to continue using it. This kind of defect can result in unpredictable problems for the system because the handle value that is being referenced might have been reused already by another unrelated driver.

    If a kernel driver has recently closed a kernel handle and later references the closed handle, Driver Verifier forces the bug check as described previously. In this case the output of the [**!htrace**](https://msdn.microsoft.com/library/windows/hardware/ff563208) debugger extension provides the stack trace for the code path that closed this handle. Use the address of the System process as a parameter for **!htrace**. To find the address of the System process, use the **!process 4 0** command.

    Starting in Windows 7, Driver Verifier adds a check to [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679). It is now prohibited to pass a user-space handle with KernelMode access. If such a combination is detected, Driver Verifier issues [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), with a parameter 1 value of 0xF6.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Miscellaneous Checks option for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line**

    At the command line, the Miscellaneous Checks option is represented by **Bit 11 (0x800)**. To activate Miscellaneous Checks, use a flag value of 0x800 or add 0x800 to the flag value. For example:

    ```
    verifier /flags 0x800 /driver MyDriver.sys
    ```

    The option will be active after the next boot.

    On Windows Vista and later versions of Windows, you can also activate and deactivate Miscellaneous Checks without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x800 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The Miscellaneous Checks option is also included in the standard settings. For example:

    ```
    verifier  /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)**, and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select **Miscellaneous Checks**.

    The Miscellaneous Checks feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

### <span id="viewing_the_results"></span><span id="VIEWING_THE_RESULTS"></span>Viewing the Results

To view the results of the Miscellaneous Checks option, use the **!verifier** extension in the kernel debugger. (For information about **!verifier**, see the *Debugging Tools for Windows* documentation.)

In the following example, the Miscellaneous Checks option detected an active ERESOURCE structure in memory that the driver was trying to free, resulting in [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187). The Bug Check 0xC4 display includes the address of the ERESOURCE and the affected memory.

```
1: kd> !verifier 1

Verify Level 800 ... enabled options are:
 Miscellaneous checks enabled

Summary of All Verifier Statistics

RaiseIrqls                             0x0
AcquireSpinLocks                       0x0
Synch Executions                       0x0
Trims                                  0x0

Pool Allocations Attempted             0x1
Pool Allocations Succeeded             0x1
Pool Allocations Succeeded SpecialPool 0x0
Pool Allocations With NO TAG           0x0
Pool Allocations Failed                0x0
Resource Allocations Failed Deliberately   0x0

Current paged pool allocations         0x0 for 00000000 bytes
Peak paged pool allocations            0x0 for 00000000 bytes
Current nonpaged pool allocations      0x0 for 00000000 bytes
Peak nonpaged pool allocations         0x0 for 00000000 bytes

Driver Verification List

Entry     State           NonPagedPool   PagedPool   Module

8459ca50 Loaded           00000000       00000000    buggy.sys



*** Fatal System Error: 0x000000c4
 (0x000000D2,0x9655D4A8,0x9655D468,0x000000B0)


        0xD2 : Freeing pool allocation that contains active ERESOURCE.
               2 -  ERESOURCE address.
               3 -  Pool allocation start address.
               4 -  Pool allocation size.
```

To investigate the pool allocation, use the [**!pool**](https://msdn.microsoft.com/library/windows/hardware/ff564691) debugger extension with the starting address of the pool allocation, 9655D468. (The *2* flag displays header information only for the pool that contains the specified address. Header information for other pools is suppressed.)

```
1: kd> !pool 9655d468  2
Pool page 9655d468 region is Paged pool
*9655d468 size:   b0 previous size:    8  (Allocated) *Bug_
```

To find information about the ERESOURCE, use the [**!locks (!kdext\*.locks)**](https://msdn.microsoft.com/library/windows/hardware/ff563980) debugger extension with the address of the structure.

```
1: kd> !locks 0x9655D4A8     <<<<<- ERESOURCE @0x9655D4A8 lives inside the pool block being freed

Resource @ 0x9655d4a8    Available
1 total locks
```

You can also use the **kb** debugger command to display a stack trace of the calls that led to the failure. The following example shows the stack, including the call to **ExFreePoolWithTag** that Driver Verifier intercepted.

```
1: kd> kb
ChildEBP RetAddr  Args to Child
92f6374c 82c2c95a 00000003 92f68cdc 00000000 nt!RtlpBreakWithStatusInstruction 
92f6379c 82c2d345 00000003 9655d468 000000c4 nt!KiBugCheckDebugBreak+0x1c 
92f63b48 82c2c804 000000c4 000000d2 9655d4a8 nt!KeBugCheck2+0x5a9 
92f63b6c 82e73bae 000000c4 000000d2 9655d4a8 nt!KeBugCheckEx+0x1e 
92f63b88 82e78c32 9655d4a8 9655d468 000000b0 nt!VerifierBugCheckIfAppropriate+0x3c 
92f63ba4 82ca7dcb 9655d468 000000b0 00000000 nt!VfCheckForResource+0x52 
92f63bc8 82e7fb2d 000000b0 00000190 9655d470 nt!ExpCheckForResource+0x21 
92f63be4 82e6dc6c 9655d470 92f63c18 89b6c58c nt!ExFreePoolSanityChecks+0x1fb 
92f63bf0 89b6c58c 9655d470 00000000 89b74194 nt!VerifierExFreePoolWithTag+0x28 
92f63c00 89b6c0f6 846550c8 846550c8 846e2200 buggy!MmTestProbeLockForEverStress+0x2e 
92f63c18 82e6c5f1 846e2200 846550c8 85362e30 buggy!TdDeviceControl+0xc4 
92f63c38 82c1fd81 82d4d148 846550c8 846e2200 nt!IovCallDriver+0x251 
92f63c4c 82d4d148 85362e30 846550c8 84655138 nt!IofCallDriver+0x1b 
92f63c6c 82d4df9e 846e2200 85362e30 00000000 nt!IopSynchronousServiceTail+0x1e6 
92f63d00 82d527be 00000001 846550c8 00000000 nt!IopXxxControlFile+0x684 
92f63d34 82cb9efc 0000004c 00000000 00000000 nt!NtDeviceIoControlFile+0x2a 
92f63d34 6a22b204 0000004c 00000000 00000000 nt!KiFastCallEntry+0x12c 
```

 

 





