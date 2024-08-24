---
title: Bug Checks (Blue Screens)
description: This topic covers bug checks (Blue Screens)
keywords: bug check, blue screen, kernel error, stop error, stop code
ms.date: 08/23/2024
---

# Bug Checks (Blue Screens)

**Note**   If you are an IT professional or support agent, see this article for additional information, [Troubleshoot "blue screen" or Stop error problems before you contact Microsoft Support](https://support.microsoft.com/help/3106831/). If you are a customer whose system has displayed a blue screen with a bug check code, see [Troubleshoot blue screen errors](https://support.microsoft.com/sbs/windows/troubleshoot-blue-screen-errors-5c62726c-6489-52da-a372-3f73142c14ad).

## Bug Check System Halt

When Microsoft Windows encounters a condition that compromises safe system operation, the system halts. This condition is called a *bug check*. It's also referred to as a *system crash*, a *kernel error*, or a *stop error*.  

Examples of situations that could occur are:

- If the OS is allowed to continue to run after the operating system integrity is compromised, it could corrupt data or compromise the security of the system.

- If crash dumps are enabled on the system, a crash dump file is created.

- If a kernel debugger is attached and active, the system causes a break so that the debugger can be used to investigate the crash.

- If no debugger is attached, a blue text screen appears with information about the error. This screen is called a *blue screen*, a *bug check screen*, or a *stop screen*.

If you're using an insider build of Windows, the text is displayed on a green background. The exact appearance of the blue screen depends on the cause of the error.
The following example shows a possible blue screen:

:::image type="content" source="images/bug-check-example-blue-screen-page-fault.png" alt-text="Screenshot of a Windows 10 blue screen displaying a bug check with a QR code.":::

The stop code is displayed, such as [PAGE_FAULT_IN_NONPAGED_AREA](bug-check-0x50--page-fault-in-nonpaged-area.md). When it's available, the module name of the code that was being executed is also displayed, such as **AcmeVideo.sys**.

If a [kernel-mode dump file](kernel-mode-dump-files.md) has been written, it's indicated with a percentage complete count down as the dump is being written.

There's a stop code hex value associated with each stop code as listed in [Bug check code reference](bug-check-code-reference2.md).

## General Tips for Bug Check (Blue Screens)

If your computer stops working and displays a blue screen, the computer has shut down abruptly to protect itself from data loss. A hardware device, its driver, or related software might have caused this error. To learn more about the information that is displayed, such as the faulting driver name, see [Analyze Bug Check Blue Screen Data](blue-screen-data.md).

For general troubleshooting of Windows bug check codes, follow these suggestions:

- If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

- Look in the **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in the driver properties for any faulting driver. Try updating the related driver.

- If you recently added hardware to the system, try removing or replacing it. Or you can check with the manufacturer to see if any patches are available.

- You can try running the hardware diagnostics supplied by the system manufacturer.

- Check the system log in Event Viewer for other error messages that might help pinpoint the device or driver that's causing the error. For more information, see [Open Event Viewer](/microsoft-365/security/defender-endpoint/event-error-codes). Look for critical errors in the system log that occurred in the same time frame as the blue screen.

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

- Check with the manufacturer to see if an updated system BIOS or UEFI firmware is available.

- For PCs, make sure that all expansion boards are properly seated and all cables are completely connected.

- **Use Safe Mode**

    Consider using Safe Mode when removing or disabling components. Using Safe Mode loads only the minimum required drivers and system services during the Windows startup. 
    1. To enter Safe Mode, go to Settings and select **Update and Security**. 
    1. Select **Recovery** > **Advanced startup** to boot to maintenance mode. 
    1. At the resulting menu, select **Troubleshoot** > **Advanced Options** > **Startup Settings** > **Restart**. 
    1. After Windows restarts to the **Startup Settings** screen, select option 4, 5, or 6 to boot to Safe Mode.

    Safe Mode might be available by pressing a function key on boot, for example F8. Refer to information from the manufacturer for specific startup options.


