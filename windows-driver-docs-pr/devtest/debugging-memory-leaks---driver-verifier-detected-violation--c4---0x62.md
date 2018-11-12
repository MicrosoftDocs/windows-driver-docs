---
title: Debugging memory leaks - DRIVER_VERIFIER_DETECTED_VIOLATION (C4) 0x62
description: Driver Verifier generates Bug Check 0xC4 DRIVER_VERIFIER_DETECTED_VIOLATION with a parameter 1 value of 0x62 when a driver unloads without first freeing all of its pool allocations.
ms.assetid: CDBE9A18-4126-4AD7-8E53-6D75DCA8B022
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging memory leaks - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4): 0x62


[Driver Verifier](driver-verifier.md) generates [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) with a parameter 1 value of 0x62 when a driver unloads without first freeing all of its pool allocations. Unfreed memory allocations (also called memory leaks) are a common cause of lowered operating system performance. These can fragment the system pools and eventually cause system crashes.

When you have a kernel debugger connected to a test computer running [Driver Verifier](driver-verifier.md), if Driver Verifier detects a violation, Windows breaks into the debugger and displays a brief description of the error.

## >Debugging memory leaks at driver unload


-   [Use !analyze to display information about the bug check](#use-analyze-to-display-information-about-the-bug-check)
-   [Use the !verifier 3 extension command to find out about the pool allocations](#use-the-verifier-3-extension-command-to-find-out-about-the-pool-allocations)
-   [If you have symbols you can locate where in the source files the memory allocations occurred](#if-you-have-symbols-you-can-locate-where-in-the-source-files-the-memory-allocations-occurred)
-   [Examine the log for memory allocations](#examine-the-log-for-memory-allocations)
-   [Fixing memory leaks](#fixing-memory-leaks)

### Use !analyze to display information about the bug check

As with any bug check that occurs, once you have control of the debugger, the best first step is to run the [**!analyze -v**](https://msdn.microsoft.com/library/windows/hardware/ff562112) command.

```
kd> !analyze -v
Connected to Windows 8 9600 x86 compatible target
Loading Kernel Symbols
.................................................................................
Loading User Symbols
.......................
Loading unloaded module list
........
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

DRIVER_VERIFIER_DETECTED_VIOLATION (c4)
A device driver attempting to corrupt the system has been caught.  This is
because the driver was specified in the registry as being suspect (by the
administrator) and the kernel has enabled substantial checking of this driver.
If the driver attempts to corrupt the system, bugchecks 0xC4, 0xC1 and 0xA will
be among the most commonly seen crashes.
Arguments:
Arg1: 00000062, A driver has forgotten to free its pool allocations prior to unloading.
Arg2: 9707712c, name of the driver having the issue.
Arg3: 9c1faf70, verifier internal structure with driver information.
Arg4: 00000003, total # of (paged+nonpaged) allocations that weren't freed.
    Type !verifier 3 drivername.sys for info on the allocations
    that were leaked that caused the bugcheck.
```

A [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) with a parameter 1 (Arg1) value of 0x62 is described as follows:

DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4)
Arg1
Arg2
Arg3
Arg4
Cause
Driver Verifier flags
0x62
Name of the driver.
Reserved
Total number of allocations that were not freed, including both paged and non-paged pool.
The driver is unloading without first freeing its pool allocations. In Windows 8.1, this bug check will also occur if the driver unloaded without first freeing any work items ([**IO\_WORKITEM**](https://msdn.microsoft.com/library/windows/hardware/ff550679)) it had allocated with [**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276). A bug check with this parameter occurs only when the [Pool Tracking](pool-tracking.md) option is active.
Specify [Pool Tracking](pool-tracking.md) (**verifier /flags 0x8**). The Pool Tracking option is enabled with Standard Flags (**verifier /standard** ).
 

### Use the !verifier 3 extension command to find out about the pool allocations

For this particular bug check, the information provided in parameter 4 (Arg4) is the most important. Arg4 shows number of allocations that weren’t freed. The output of the [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112) command also shows the [**!verifier**](https://msdn.microsoft.com/library/windows/hardware/ff565591) debugger extension command that you can use to display what those allocations were. The full output of **!verifier 3 MyDriver.sys** command is shown in the following example:

```
kd> !verifier 3 Mydriver.sys

Verify Flags Level 0x000209bb

  STANDARD FLAGS:
    [X] (0x00000000) Automatic Checks
    [X] (0x00000001) Special pool
    [X] (0x00000002) Force IRQL checking
    [X] (0x00000008) Pool tracking
    [X] (0x00000010) I/O verification
    [X] (0x00000020) Deadlock detection
    [X] (0x00000080) DMA checking
    [X] (0x00000100) Security checks
    [X] (0x00000800) Miscellaneous checks
    [X] (0x00020000) DDI compliance checking

  ADDITIONAL FLAGS:
    [ ] (0x00000004) Randomized low resources simulation
    [ ] (0x00000200) Force pending I/O requests
    [ ] (0x00000400) IRP logging
    [ ] (0x00002000) Invariant MDL checking for stack
    [ ] (0x00004000) Invariant MDL checking for driver
    [ ] (0x00008000) Power framework delay fuzzing
    [ ] (0x00040000) Systematic low resources simulation
    [ ] (0x00080000) DDI compliance checking (additional)
    [ ] (0x00200000) NDIS/WIFI verification
    [ ] (0x00800000) Kernel synchronization delay fuzzing
    [ ] (0x01000000) VM switch verification

    [X] Indicates flag is enabled


Summary of All Verifier Statistics

  RaiseIrqls           0x0
  AcquireSpinLocks     0x0
  Synch Executions     0x0
  Trims                0x0

  Pool Allocations Attempted             0x2db1a
  Pool Allocations Succeeded             0x2db1a
  Pool Allocations Succeeded SpecialPool 0x2db1a
  Pool Allocations With NO TAG           0x0
  Pool Allocations Failed                0x0

  Current paged pool allocations         0x0 for 00000000 bytes
  Peak paged pool allocations            0x0 for 00000000 bytes
  Current nonpaged pool allocations      0x3 for 00001058 bytes
  Peak nonpaged pool allocations         0x13 for 0004A4A0 bytes

## Driver Verification List


  MODULE: 0x84226b28 MyDriver.sys (Loaded)

    Pool Allocation Statistics: ( NonPagedPool / PagedPool )

      Current Pool Allocations: ( 0x00000003 / 0x00000000 )
      Current Pool Bytes:       ( 0x00001058 / 0x00000000 )
      Peak Pool Allocations:    ( 0x00000013 / 0x00000000 )
      Peak Pool Bytes:          ( 0x0004A4A0 / 0x00000000 )
      Contiguous Memory Bytes:       0x00000000
      Peak Contiguous Memory Bytes:  0x00000000

    Pool Allocations:

      Address     Length      Tag   Caller    
      ----------  ----------  ----  ----------
      0x982a8fe0  0x00000020  VMdl  0x9a3bf6ac  MyDriver!DeviceControlDispatch
      0x8645a000  0x00001008  mdrv  0x9a3bf687  MyDriver!DeviceControlDispatch
      0x9a836fd0  0x00000030  Vfwi  0x9a3bf6ed  MyDriver!GetNecessaryObjects
```

In example, the driver, MyDriver.sys, has two memory allocations and one I/O work item that have not been properly freed. Each listing shows the address of the current allocation, the size, the pool tag used, and the address in the driver code where the request for an allocation was made. If symbols are loaded for the driver in question, it will also show the name of the function next to the caller address.

Of the tags displayed, only one (for the allocation at address 0x8645a000) was supplied by the driver itself (**mdrv**). The tag **VMdl** is used whenever a driver being verified by Driver Verifier makes calls [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263). Similarly, the tag **Vfwi** is used whenever a driver being verified by Driver Verifier makes a request to allocate a work item using [**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276).

### If you have symbols you can locate where in the source files the memory allocations occurred

When symbols are loaded for the driver, if those symbols contain the line number information, you can use the **ln** *CallerAddress* command to show the line where the call was made. This output will also show the offset in the function that made the allocation.

```
kd> ln 0x9a3bf6ac  
d:\coding\wdmdrivers\mydriver\handleioctl.c(50)+0x15
(9a3bf660)   MyDriver!DeviceControlDispatch+0x4c   |  (9a3bf6d0)   MyDriver!DeviceControlDispatch

kd> ln 0x9a3bf687  
d:\coding\wdmdrivers\mydriver\handleioctl.c(38)+0x12
(9a3bf660)   MyDriver!DeviceControlDispatch+0x27   |  (9a3bf6d0)   MyDriver!DeviceControlDispatch

kd> ln 0x9a3bf6ed  
d:\coding\wdmdrivers\mydriver\handleioctl.c(72)+0xa
(9a3bf6d0)   MyDriver!GetNecessaryObjects+0x1d   |  (9a3bf71c)   MyDriver!GetNecessaryObjects
```

### Examine the log for memory allocations

Driver Verifier also keeps a circular log of all memory allocations made in kernel space when pool tracking is enabled. By default, the most recent 65,536 (0x10000) allocations are kept. As a new allocation is made, the oldest allocation in the log is overwritten. If the allocations were made recently before the crash, it may be possible to get additional information about the allocation than shown above, specifically the thread address and frames of the kernel stack at the time of the allocation.

This log can be accessed by using the command **!verifier 0x80** *AddressOfPoolAllocation*. Note that this will list all of the allocations and frees in the log for this particular address. To cancel or stop display of the log history, use the keyboard shortcuts: **Ctrl + Break** with WinDbg and **Ctrl + C** with KD.

```
kd> !verifier 0x80 0x982a8fe0

Log of recent kernel pool Allocate and Free operations:

There are up to 0x10000 entries in the log.

Parsing 0x00010000 log entries, searching for address 0x982a8fe0.

# 

Pool block 982a8fe0, Size 00000020, Thread 9c158bc0
81b250cd nt!IovAllocateMdl+0x3d
8060e41d VerifierExt!IoAllocateMdl_internal_wrapper+0x35
81b29388 nt!VerifierIoAllocateMdl+0x22
9a3bf6ac MyDriver!DeviceControlDispatch+0x4c
9a3bf611 MyDriver!NonPNPIRPDispatch0x51
9a3bf05a MyDriver!AllIRPDispatch+0x1a
80611710 VerifierExt!xdv_IRP_MJ_DEVICE_CONTROL_wrapper+0xd0
81b3b635 nt!ViGenericDispatchHandler+0x2d
81b3b784 nt!ViGenericDeviceControl+0x18
81b24b4d nt!IovCallDriver+0x2cc
81703772 nt!IofCallDriver+0x62
8191165e nt!IopSynchronousServiceTail+0x16e
81915518 nt!IopXxxControlFile+0x3e8

kd> !verifier 0x80 0x8645a000

Log of recent kernel pool Allocate and Free operations:

There are up to 0x10000 entries in the log.

Parsing 0x00010000 log entries, searching for address 0x8645a000.

# 

Pool block 8645a000, Size 00001000, Thread 9c158bc0
8060ee4f VerifierExt!ExAllocatePoolWithTagPriority_internal_wrapper+0x5b
81b2619e nt!VerifierExAllocatePoolWithTag+0x24
9a3bf687 MyDriver!DeviceControlDispatch+0x27
9a3bf611 MyDriver!NonPNPIRPDispatch0x51
9a3bf05a MyDriver!AllIRPDispatch+0x1a
80611710 VerifierExt!xdv_IRP_MJ_DEVICE_CONTROL_wrapper+0xd0
81b3b635 nt!ViGenericDispatchHandler+0x2d
81b3b784 nt!ViGenericDeviceControl+0x18
81b24b4d nt!IovCallDriver+0x2cc
81703772 nt!IofCallDriver+0x62
8191165e nt!IopSynchronousServiceTail+0x16e
81915518 nt!IopXxxControlFile+0x3e8
81914516 nt!NtDeviceIoControlFile+0x2a

kd> !verifier 0x80 0x9a836fd0  

Log of recent kernel pool Allocate and Free operations:

There are up to 0x10000 entries in the log.

Parsing 0x00010000 log entries, searching for address 0x9a836fd0.

# 

Pool block 9a836fd0, Size 00000030, Thread 88758740
8151713d nt!IovAllocateWorkItem+0x1b
84a133d9 VerifierExt!IoAllocateWorkItem_internal_wrapper+0x29
8151b3a7 nt!VerifierIoAllocateWorkItem+0x16
9a3bf6ed MyDriver!GetNecessaryObjects+0x1d
9a3bf620 MyDriver!NonPNPIRPDispatch0x51
9a3bf05a MyDriver!AllIRPDispatch+0x1a
84a16710 VerifierExt!xdv_IRP_MJ_DEVICE_CONTROL_wrapper+0xd0
8152d635 nt!ViGenericDispatchHandler+0x2d
8152d784 nt!ViGenericDeviceControl+0x18
81516b4d nt!IovCallDriver+0x2cc
810f5772 nt!IofCallDriver+0x62
8130365e nt!IopSynchronousServiceTail+0x16e
81307518 nt!IopXxxControlFile+0x3e8
```

### Fixing memory leaks

This Driver Verifier bug check is designed to prevent the driver from leaking kernel memory. In each case, the proper fix is to identify any existing code paths where the allocated objects are not freed and ensure they’re freed properly.

[Static Driver Verifier](static-driver-verifier.md) is a tool that scans Windows driver source code and reports on possible issues by simulating the exercising of various code paths. Static Driver Verifier is an excellent development-time utility to help identify these kinds of issues.

For other techniques you can use, including scenarios where Driver Verifier is not involved, see [Finding a Kernel-Mode Memory Leak](https://msdn.microsoft.com/library/windows/hardware/ff545403).

## Related topics


[Finding a Kernel-Mode Memory Leak](https://msdn.microsoft.com/library/windows/hardware/ff545403)

[Static Driver Verifier](static-driver-verifier.md)

[Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063)

[Handling a Bug Check When Driver Verifier is Enabled](https://msdn.microsoft.com/library/windows/hardware/hh450984)

 

 






