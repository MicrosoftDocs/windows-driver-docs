---
title: How the Checked Build Indicates a Problem
description: How the Checked Build Indicates a Problem
ms.assetid: 373519e0-bca9-434e-8cc3-e11c2d4b42a4
keywords:
- checked builds WDK , problem notifications
- notifications WDK checked builds
- ASSERTs WDK checked builds
- breakpoints WDK
- debugger messages WDK
- messages WDK checked builds
- errors WDK checked builds
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How the Checked Build Indicates a Problem


## <span id="ddk_how_the_checked_build_indicates_a_problem_tools"></span><span id="DDK_HOW_THE_CHECKED_BUILD_INDICATES_A_PROBLEM_TOOLS"></span>


The checked build of the operating system uses a variety of methods to notify you of problems that it finds. These methods include ASSERT failures, breakpoints, and debugger messages. All of these methods result in output from a kernel debugger. Therefore, to be useful, you must run the checked build with a kernel-mode debugger (such as WinDbg or KD) connected.

For details on debugging, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

### <span id="assert_failures"></span><span id="ASSERT_FAILURES"></span>ASSERT Failures

Most of the checks that the checked build performs are implemented as [**ASSERT**](https://msdn.microsoft.com/library/windows/hardware/ff542107) statements. When the expression that is asserted evaluates to **FALSE**, the debugger displays a message that contains:

-   The text of the code expression that failed

-   The source code path, file name, and line number of the failed ASSERT routine

The following example shows the output that the debugger displays when an assert fails in the I/O Manager:

```
*** Assertion failed: Irp->IoStatus.Status != 0xffffffff
***   Source File: D:\nt\private\ntos\io\iosubs.c, line 3305

0:Break, Ignore, Terminate Process or Terminate Thread (bipt)? b
0:Execute &#39;!cxr BD94B918&#39; to dump context
Break instruction exception - code 80000003 (first chance)
ntkrnlmp!DbgBreakPoint:
804a3ce4 cc               int     3
```

As shown in the debugger output, the user is asked to "Break, Ignore, Terminate Process or Terminate Thread." The user answered by entering "b", which caused the debugger to stop system execution with a breakpoint. As a result, the user can now continue to debug the problem that was discovered.

The way in which a failed assert affects the system depends on a number of factors. In versions of Windows prior to Windows Vista, if debugging was enabled for the operating system during the system startup process, the system will break into the debugger (if connected), or hang waiting for a debugger to be connected. If debugging was not enabled, the system will crash with [**Bug Check 0x1E**](https://msdn.microsoft.com/library/windows/hardware/ff557408) (KMODE\_EXCEPTION\_NOT\_HANDLED) with a Parameter 1 value of 0x80000003. In Windows Vista and later, the system will break into the debugger only if the debugger is connected. If debugging is not enabled, or if debugging is enabled but the debugger is not connected, the failed assertion will not be reported (although assertion checking will still be performed). If you are developing a driver and want to deterministically break into the debugger if debugging is enabled but a debugger is not connected, you can use [**DbgBreakPoint**](https://msdn.microsoft.com/library/windows/hardware/ff543626) statements in your code.

Some [**ASSERT**](https://msdn.microsoft.com/library/windows/hardware/ff542107) failures are preceded by additional [**DbgPrint**](https://msdn.microsoft.com/library/windows/hardware/ff543632) output. One common example of this type of assert is the following [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro, which is defined in ntddk.h and wdm.h for use in the checked build of drivers:

```
#define PAGED_CODE() \
    if (KeGetCurrentIrql() > APC_LEVEL) { \
KdPrint(( "EX: Pageable code called at IRQL %d\n", KeGetCurrentIrql() )); \
        ASSERT(FALSE); \
        }
```

This macro is frequently used within the operating system to verify that pageable functions are called only at appropriate IRQLs.

You can typically examine the text of the failing code expression to determine the cause of an assert, including the driver's actions when the ASSERT occurred and the functions that were called. The **KB (Display Stack Trace)** debugger command is crucial to this analysis.

For a list of the most common ASSERT calls, see [Checked Build ASSERTs](checked-build-asserts.md).

### <span id="breakpoints"></span><span id="BREAKPOINTS"></span>Breakpoints

Checked builds can also use breakpoints to indicate a problem. Breakpoints are often preceded by [**DbgPrint**](https://msdn.microsoft.com/library/windows/hardware/ff543632) statements, which cause the debugger to display information about the problem that has been encountered. If a debugger is not connected to the system when a breakpoint occurs, the system crashes and all explanatory messages are lost.

Some of the most common messages that precede breakpoints in the checked build, and which are encountered by driver writers, are listed in [Checked Build Breakpoints and Messages](checked-build-breakpoints-and-messages.md).

The following example shows how a **DbgPrint** call and breakpoint appear in the debugger:

```
*** DPC routine > 1 sec --- This is not a break in KeUpdateSystemTime
Break instruction exception - code 80000003 (first chance)
NTOSKRNL!DbgBreakPoint:
804a3ce4 cc               int     3
```

This example shows a debugger message that indicates a single deferred procedure call (DPC) was running for longer than one second, and illustrates the type of checks implemented in the checked build. This breakpoint means that a driver has spent a long time in a DPC routine, which could indicate a serious driver problem. On the other hand, this breakpoint can also occur if the driver generates a large amount of debug output in its DPC routine, thereby extending the length of time required for the DPC to run. To discover the underlying cause of the problem, examine what the DPC routine is doing, and continue past the breakpoint once or twice.

In the rare situation when a breakpoint is encountered but no message is displayed, it is important to examine the kernel stack trace (using the **KB** debugger command) to determine where the breakpoint was encountered. Often, this will give a strong clue to the reason for the breakpoint.

The following example shows a common breakpoint that has been seen by many Windows driver developers, along with a stack trace:

```
Break instruction exception - code 80000003 (first chance)
ntkrnlmp!SpinLockSpinningForTooLong:
8069aafd cc               int     3
1: kd> kb
ChildEBP RetAddr  Args to Child              
f9f77c4c 80103a6c f9f77c84 00000005 fa20e7df ntkrnlmp!SpinLockSpinningForTooLong
f9f77c58 fa20e7df 81b34930 e1558bd0 00180016 halmps!KfAcquireSpinLock+0x3c
f9f77c7c 80742683 000000ff 81ba6000 00000000 nothing+0x7df
f9f77d54 80742893 0000046c 81ba6000 f9f77d80 ntkrnlmp!IopLoadDriver+0x785
f9f77d78 805f8d2d 00000000 00000000 81fa88b8 ntkrnlmp!IopLoadUnloadDriver+0x75
f9f77dac 807cd14f f7d59ce8 00000000 00000000 ntkrnlmp!ExpWorkerThread+0x129
f9f77ddc 8069bece 805f8c04 00000001 00000000 ntkrnlmp!PspSystemThreadStartup+0x4d
00000000 00000000 00000000 00000000 00000000 ntkrnlmp!KiThreadStartup+0x16
```

As you can see from this stack trace, the breakpoint was taken as a result of the call **KfAcquireSpinLock**. After you examine the wdm.h, you can see that this is the actual name of the function referred to by drivers as [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917). Even though no message was displayed prior to the breakpoint, you can see the location of the breakpoint at the top of the stack (**ntkrnlmp!SpinLockSpinningForTooLong**). This location indicates the reason for the breakpoint: A spin lock has been spinning, pending acquisition, for an unusually long time.

### <span id="debugger_messages"></span><span id="DEBUGGER_MESSAGES"></span>Debugger Messages

Checked builds can also use debugger messages to identify, or provide additional information about, errors that have occurred. The most common sources of debugger messages are errors that originate from non-kernel and non-HAL components, or from checked (debug) user-mode programs. The amount of output varies with each operating system release.

The following example shows output that might be displayed by an installation of the full checked build. This output was generated by a prerelease version of Windows XP, and thus is even more voluminous than is usually seen on a fully checked build.

```
0:Attempting to load winsock
0:Checking for presence of ws2_32
0:Looking in ws2_32 for getaddrinfo
0:AudioSrv: 1:CreateSessionUserSid: GetCurrentUserTokenW failed, LastError=1245
1:AudioSrv: RegOpenConsoleUser: no console sid
0:(s: 0 0xc4.d0 winlogon.exe) USRK-[Wrn=170] CloseDesktop: Desktop 0X81CEAF78 still in use by thread 0XE16F3EA0
0:GetWinStationUserToken: Error 1702 getting UserToken LogonId 0
1:AudioSrv: InitializeForNewConsoleUser: User SID S-1-5-21-329068152-1292428093-1547161642-500
1:(s: 0 0x240.3a8 spoolsv.exe) USRK-[Wrn=1400] ValidateHwnd: Invalid hwnd (0X0000FFFF)
0:(s: 0 0x240.3a8 spoolsv.exe) USRK-[Wrn=1400] ValidateHwnd: Invalid hwnd (0X0000FFFF)
0:bReadUserSystemEUDCRegistry():fail NtStatus - c0000000
0:GDI: GDISRV:Fail to read system wide eudc
0:
1:TERMSRV : Not Personal Workstation
0:(s: 0 0x260.3c4 Explorer.EXE) USER-[Wrn=1400] HMValidateHandle: Invalid:00000000 Type:0x1
0:(s: 0 0x260.3c4 Explorer.EXE) USER-[Wrn=1400] HMValidateHandle: Invalid:00000000 Type:0x1
0:(s: 0 0x260.3c4 Explorer.EXE) USER-[Wrn=1400] HMValidateHandle: Invalid:00000000 Type:0x1
```

Some of the most common messages that the checked build can display during driver debugging are listed in [Checked Build Breakpoints and Messages](checked-build-breakpoints-and-messages.md).

Enabling additional trace or informational messages in various system components can also cause debugger messages without subsequent breakpoints or ASSERT failures.

 

 





