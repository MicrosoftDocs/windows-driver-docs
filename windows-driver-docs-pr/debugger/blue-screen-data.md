---
title: Blue screen data
description: Learn about bug checks, which provide information when Microsoft Windows encounters a condition that compromises safe system operation and the system halts.
keywords: ["Blue Screen Data Windows Debugging"]
ms.date: 12/14/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- Blue Screen Data
api_type:
- NA
---

# Blue screen data

> [!NOTE]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://support.microsoft.com/help/14238/windows-10-troubleshoot-blue-screen-errors).

> [!NOTE]
> If you're an IT professional or support agent, see [Advanced troubleshooting for stop or blue screen errors](https://support.microsoft.com/help/3106831/) for more information.

When Microsoft Windows encounters a condition that compromises safe system operation, the system halts. This condition is called a *bug check*. It's also referred to as a *system crash*, a *kernel error*, or a *stop error*.  
 Examples of situations that could occur are:

- If the OS is allowed to continue to run after the operating system integrity is compromised, it could corrupt data or compromise the security of the system.

- If crash dumps are enabled on the system, a crash dump file is created.

- If a kernel debugger is attached and active, the system causes a break so that the debugger can be used to investigate the crash.

- If no debugger is attached, a blue text screen appears with information about the error. This screen is called a *blue screen*, a *bug check screen*, or a *stop screen*.

If you're using an insider build of Windows, the text is displayed on a green background. The exact appearance of the blue screen depends on the cause of the error.
The following example shows a possible blue screen:

![Screenshot showing a bug check Windows 10 blue screen with a QR code.](images/bug-check-example-blue-screen-page-fault.png)

The stop code is displayed, such as [PAGE_FAULT_IN_NONPAGED_AREA](bug-check-0x50--page-fault-in-nonpaged-area.md). When it's available, the module name of the code that was being executed is also displayed, such as **AcmeVideo.sys**.

If a [kernel-mode dump file](kernel-mode-dump-files.md) has been written, it's indicated with a percentage complete count down as the dump is being written.

There's a stop code hex value associated with each stop code as listed in [Bug check code reference](bug-check-code-reference2.md).

## Gather the stop code parameters

Each bug check code has four associated parameters that provide information. The parameters are described in [Bug check code reference](bug-check-code-reference2.md) for each stop code.

There are multiple ways to gather the four stop code parameters.

- Examine the Windows system log in the Event Viewer. The event properties for the bug check will list the four stop code parameters. For more information, see [Open Event Viewer](/microsoft-365/security/defender-endpoint/event-error-codes).

- Load the generated dump file and use the [!analyze](../debuggercmds/-analyze.md) command with the debugger attached. For more information, see [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md).

- Attach a kernel debugger to the faulting PC. When the stop code occurs, the debugger output will include the four parameters after the stop code hex value.

    ```dbgcmd
    *******************************************************************************
    *                                                                             *
    *                        Bugcheck Analysis                                    *
    *                                                                             *
    *******************************************************************************

    Use !analyze -v to get detailed debugging information.

    BugCheck 9F, {3, ffffe000f38c06a0, fffff803c596cad0, ffffe000f46a1010}

    Implicit thread is now ffffe000`f4ca3040
    Probably caused by : hidusb.sys
    ```

### Bug check symbolic names

[DRIVER_POWER_STATE_FAILURE](bug-check-0x9f--driver-power-state-failure.md) is the bug check symbolic name, with an associated bug check code of 9F. The stop code hex value associated with the bug check symbolic name is listed in the [Bug check code reference](bug-check-code-reference2.md).

### Read bug check information from the debugger

If a debugger is attached, and debugging is enabled on the PC, a bug check will cause the target computer to break into the debugger. In this case, the blue screen might not appear immediately. The full details on this crash will be sent to the debugger and appear in the debugger window. To see this information a second time, use the [.bugcheck (Display bug check data)](../debuggercmds/-bugcheck--display-bug-check-data-.md) command or the [!analyze](../debuggercmds/-analyze.md) extension command. For information on enabling debugging see, [Getting started with WinDbg (Kernel-Mode)](getting-started-with-windbg--kernel-mode-.md).

## Kernel debugging and crash dump analysis

Kernel debugging is especially useful when other troubleshooting techniques fail, or for a recurring problem. Remember to capture the exact text in the bug check information section of the error message. To isolate a complex problem and develop a viable workaround, it's useful to record the exact actions that lead to the failure.

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

For more information, see the following articles:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](../debuggercmds/-analyze.md)

[The Defrag Tools shows](/shows/defrag-tools/)

## Use Driver Verifier to gather information

It's estimated that about three quarters of blue screens are caused by faulting drivers. Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it finds errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, enter **Verifier** at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try to verify the smallest number of drivers as possible. For more information, see [Driver Verifier](../devtest/driver-verifier.md).

## Tips for software engineers

When a bug check occurs as a result of code you've written, you should use the kernel debugger to analyze the problem, and then fix the bugs in your code. For full details, see the individual bug check code in the [Bug check code reference](bug-check-code-reference2.md) section.

However, you might also encounter bug checks that aren't caused by your own code. In this case, you probably won't be able to fix the actual cause of the problem, so your goal should be to work around the problem. If possible, isolate and remove the hardware or software component that's at fault.

Many problems can be resolved through basic troubleshooting procedures, such as verifying instructions, reinstalling key components, and verifying file dates. Also, the Event Viewer, the Sysinternals diagnostic tools, and network monitoring tools might isolate and resolve these issues.

For general troubleshooting of Windows bug check codes, follow these suggestions:

- If you recently added hardware to the system, try removing or replacing it. Or you can check with the manufacturer to see if any patches are available.

- If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

- Look in the **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in the driver properties for any faulting driver. Try updating the related driver.

- Check the system log in Event Viewer for other error messages that might help pinpoint the device or driver that's causing the error. For more information, see [Open Event Viewer](/microsoft-365/security/defender-endpoint/event-error-codes). Look for critical errors in the system log that occurred in the same time frame as the blue screen.

- You can try running the hardware diagnostics supplied by the system manufacturer.

- Run the Windows Memory Diagnostics tool to test the memory. In the Control Panel search box, type **Memory**, and then select **Diagnose your computer's memory problems**.‌ After the test is run, use Event Viewer to view the results under the system log. Look for the *MemoryDiagnostics-Results* entry to view the results.

- Confirm that any new hardware that's installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications).

- Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows, and resulting disk corruption can generate system bug check codes. Check the Master Boot Record for infections with the virus detection program.

- Use the scan disk utility to confirm that there are no file system errors. Select and hold (or right-click) on the drive you want to scan and select **Properties** > **Tools** > **Check now**.

- Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

- Confirm that there's sufficient free space on the hard drive. The operating system and some applications require sufficient free space to create swap files and perform other functions. Based on the system configuration, the exact requirement varies, but it's a good idea to have 10% to 15% of free space available.

- Verify that the system has the latest Service Pack installed. To detect which Service Pack, if any, is installed on your system, select **Start**, select **Run**, enter **winver**, and then select ENTER. The **About Windows** dialog displays the Windows version number and the version number of the Service Pack, if one has been installed.

- Check with the manufacturer to see if an updated system BIOS or firmware is available.

- Disable BIOS memory options, such as caching or shadowing.

- For PCs, make sure that all expansion boards are properly seated and all cables are completely connected.

- **Use Safe Mode**

    Consider using Safe Mode when removing or disabling components. Using Safe Mode loads only the minimum required drivers and system services during the Windows startup. 
    1. To enter Safe Mode, go to Settings and select **Update and Security**. 
    1. Select **Recovery** > **Advanced startup** to boot to maintenance mode. 
    1. At the resulting menu, select **Troubleshoot** > **Advanced Options** > **Startup Settings** > **Restart**. 
    1. After Windows restarts to the **Startup Settings** screen, select option 4, 5, or 6 to boot to Safe Mode.

    Safe Mode might be available by pressing a function key on boot, for example F8. Refer to information from the manufacturer for specific startup options.

## See also

- [Bug check code reference](bug-check-code-reference2.md)

- [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

- [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](../debuggercmds/-analyze.md)
