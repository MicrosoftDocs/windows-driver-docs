---
title: Interpreting a Bug Check Code
description: When Microsoft Windows encounters a condition that compromises safe system operation, the system halts.
ms.assetid: b5c8e18e-c2d3-47d9-b2bd-38aaaedcfde9
keywords:
- tools WDK , bug check codes
- driver development tools WDK , bug check codes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interpreting a Bug Check Code


When Microsoft Windows encounters a condition that compromises safe system operation, the system halts. This condition is called a *bug check*. It is also commonly referred to as a *system crash*, a *kernel error*, a *Stop error*, or *BSOD*. A hardware device, its driver, or related software might have caused this error.

If crash dumps are enabled on the system, a crash dump file is created.

If a kernel debugger is attached and active, the system causes a break so the debugger can be used to investigate the crash.

If no debugger is attached, a blue text screen appears with information about the error. This screen is called a *blue screen*, a *bug check screen*, a *Stop screen*, or *BSOD*.

## <span id="ddk_interpreting_bug_check_codes_tools"></span><span id="DDK_INTERPRETING_BUG_CHECK_CODES_TOOLS"></span>


The exact appearance of the bug check screen depends on the cause of the error. The following is an example of one possible bug check screen:

```
STOP: 0x00000079 (0x00000002, 0x00000001, 0x00000002, 0x00000000)

Mismatched kernel and hal image.

Beginning dump of physical memory
Physical memory dump complete. Contact your system administrator or
technical support group.
```

On the other hand, some blue screens look like this:

```
STOP: c000021a {Fatal System Error}

The Windows Logon Process system process terminated unexpectedly with
a status of 0x00000001 (0x00000000 0x00000000).
The system has been shut down.
```

### <span id="ddk_blue_screen_data_tools"></span><span id="DDK_BLUE_SCREEN_DATA_TOOLS"></span>

The hexadecimal number following the word "STOP" is called the *bug check code* or *Stop code*. This is the most important item on the screen.

Each bug check code has four associated parameters. In the first blue screen shown here, all four parameters are displayed after the bug check code. However, in the second kind of blue screen, these parameters have been rearranged within the explanatory text. Regardless of the amount of rearrangement, they will always appear sequentially. If fewer than four parameters appear, the remaining parameters can be assumed to be zero.

The remainder of the text on the blue screen gives additional information. For some bug checks, this may be an explanation of what happened or suggestions for how you can deal with the problem. If a kernel-mode dump file has been written, this will usually be indicated as well.

Under some conditions, Windows will display only the first line of the blue screen. This can occur if the vital services needed for the display have been affected by the error.

### <span id="bug_check_symbolic_names"></span><span id="BUG_CHECK_SYMBOLIC_NAMES"></span>Bug Check Symbolic Names

Each bug check code also has an associated symbolic name. These names usually do not appear on the blue screen. In these examples, the first screen shows [**bug check 0x79**](https://msdn.microsoft.com/library/windows/hardware/ff559209) (MISMATCHED\_HAL), while the second shows [**bug check 0xC000021A**](https://msdn.microsoft.com/library/windows/hardware/ff560177) (STATUS\_SYSTEM\_PROCESS\_TERMINATED).

You can deliberately cause a bug check from a kernel-mode driver by passing the bug check's symbolic name to [**KeBugCheck**](https://msdn.microsoft.com/library/windows/hardware/ff551948) or [**KeBugCheckEx**](https://msdn.microsoft.com/library/windows/hardware/ff551961). This should only be done in circumstances where no other option is available.

### <span id="reading_bug_check_information_from_the_debugger"></span><span id="READING_BUG_CHECK_INFORMATION_FROM_THE_DEBUGGER"></span>Reading Bug Check Information from the Debugger

If a debugger is attached, a bug check will cause the target computer to break into the debugger. In this case, the blue screen may not appear, or may appear with less text; the full details on this crash will be sent to the debugger and appear in the debugger window. For more information, see [Using a Debugger](using-a-debugger.md).

This reference section for the bug check codes can be found as part of [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063). See [Bug Check Code Reference](https://msdn.microsoft.com/library/windows/hardware/hh994433) for descriptions of the bug checks and parameters. Each reference page lists the bug check code, the text string, and the four additional parameters which are displayed with each bug check. It also describes how you can diagnose the fault that led to the bug check, and possible ways to deal with the error.

For a full list of bug check codes, see the Bugcodes.h file. This file can be found in the inc directory of the Microsoft Windows Driver Kit (WDK).

## <span id="related_topics"></span>Related topics


[Bug Check Code Reference](https://msdn.microsoft.com/library/windows/hardware/hh994433)

[Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063)

 

 






