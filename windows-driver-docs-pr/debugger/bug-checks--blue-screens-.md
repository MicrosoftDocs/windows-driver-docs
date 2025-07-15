---
title: Bug Checks (Blue Screens)
description: Review general information about bug check system halt errors or Blue Screens, and find troubleshooting tips.
keywords: bug check, blue screen, kernel error, stop error, stop code
ms.date: 07/15/2025
---

# Bug checks (Blue Screens)

This article provides general information about bug check system halt errors. The halt error condition is commonly referred to as a _Blue Screen_ because the error text usually displays on a screen with a blue background. The exact appearance of the Blue Screen depends on the cause of the error.

Depending on your scenario, you might be interested in another article:

- If you're a customer whose system is displaying a Blue Screen with a bug check code, see [Resolving Blue Screen errors in Windows](https://support.microsoft.com/windows/resolving-blue-screen-errors-in-windows-60b01860-58f2-be66-7516-5c45a66ae3c6).

- If you're an IT professional, you can find more information in [Advanced troubleshooting for stop code errors](/troubleshoot/windows-client/performance/stop-code-error-troubleshooting). 

- If you're a programmer looking for common bug check codes displayed on the blue bug check screen, see the [Bug check code reference](bug-check-code-reference2.md).

## Understand bug check system halts

When Windows encounters a condition that compromises safe system operation, the system halts. This condition is referred to as a *bug check*, or sometimes, a *system crash*, *kernel error*, or *stop error*. As mentioned earlier, the most common term for the condition is Blue Screen because of the blue background. However, if you're using an insider build of Windows, the text displays on a green background rather than blue. 

Here are some example scenarios related to a bug check system halt:

- If the operating system is allowed to continue to run after the integrity is compromised, data can be corrupted or the security of the system compromised.

- If crash dumps are enabled on the system, a crash dump file is created.

- If a kernel debugger is attached and active, the system causes a break so the debugger can be used to investigate the crash.

- If no debugger is attached, a Blue Screen displays with information about the error.

The following example illustrates a bug check system halt condition that displays a Blue Screen:

:::image type="content" source="images/bug-check-example-blue-screen-page-fault.png" alt-text="Screenshot of a Windows 10 Blue Screen displaying a bug check with a QR code.":::

The Blue Screen displays the stop code and also the module name of the currently executing code, when it's available. The example shows the [PAGE_FAULT_IN_NONPAGED_AREA](bug-check-0x50--page-fault-in-nonpaged-area.md) stop code and the name of the executing module, `AcmeVideo.sys`. The stop code hex value associated with each stop code is available in [Bug check code reference](bug-check-code-reference2.md).

If the system can generate a [kernel-mode dump file](kernel-mode-dump-files.md), you see a display showing the percent complete as the system writes the dump file.

## Troubleshoot bug checks (Blue Screens)

If your computer stops working and displays a Blue Screen, the computer shuts down abruptly to protect itself from data loss. A hardware device, its driver, or related software might cause the error. To learn more about the information displayed on the Blue Screen, such as the faulting driver name, see [Analyze bug check Blue Screen data](blue-screen-data.md).

The following table provides general troubleshooting tips for Windows bug check codes.

| Scenario | Troubleshooting tips |
|----------|----------------------|
| _New device drivers or system services_ | Remove or update any recently added device drivers or system services. Identify any recent system configuration changes that might cause a new bug check code. |
| _Faulty devices or drives_ | Open Windows **Device Manager** and check for devices marked with the exclamation point (**!**). Review the events log displayed in the driver properties. Look for any faulting driver and update the related driver. |
| _New hardware_ | Remove or replace any recently added hardware. Check with the manufacturer to see if any patches are available. |
| _Other hardware issues_ | Run the hardware diagnostics supplied by the system manufacturer. |
| _Critical errors in system log_ | Check the system log in the **Event Viewer** for error messages. Look for content that might help pinpoint the device or driver that's causing the error. Check for critical errors in the system log that occurred in the same time frame as the Blue Screen. |
| _Memory errors_ | Run the Windows **Memory Diagnostics** tool to test the memory. In the Window **Control Panel**, search for **Memory**, and then select **Diagnose your computer's memory problems**.‌ </br></br> After the test runs, use **Event Viewer** to see the results under the system log. Look for the **MemoryDiagnostics-Results** entry and view the results. |
| _Hardware incompatibility_ | Confirm any recently installed hardware is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications). |
| _Virus or system corruption_ | Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows. The resulting disk corruption can generate system bug check codes. Check the Master Boot Record for infections with the virus detection program. |
| _File system errors_ | Use the **Scan disk** utility to confirm there are no file system errors. Right-click the drive to scan and select **Properties** > **Tools** > **Check now**. |
| _Missing or corrupted files_ | Use the **System File Checker** tool to repair missing or corrupted system files. This Windows utility allows users to look for corruptions in Windows system files and then restore corrupted files. Use the `SFC /scannow` command to run the **System File Checker** tool (*SFC.exe*). </br></br>For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files-79aa86cb-ca52-166a-92a3-966e85d4094e). |
| _Insufficient free space_ | Confirm sufficient free space on the hard drive. The operating system and some applications require sufficient free space to create swap files and perform other functions. Based on the system configuration, the exact requirement varies, but it's a good idea to have 10% to 15% of free space available. |
| _Outdated software_ | Verify the system has the latest Service Pack installed. To detect which Service Pack is installed on your system, select **Start** > **Run**, enter _winver_, and select **OK**. The **About Windows** dialog opens showing the Windows version number and the version number of the Service Pack, if any is installed. |
| _Outdated BIOS or firmware_ | Check with the manufacturer to see if an updated system BIOS or Unified Extensible Firmware Interface (UEFI) firmware is available. |
| _Hardware connection problems_ | For computers, make sure all expansion boards are properly seated and all cables are properly connected. |

### Use Safe Mode

When you remove or disable any components during troubleshooting, it's a good practice to run in Safe Mode.

Safe Mode loads only the minimum required drivers and system services during the Windows startup. 

1. To enter Safe Mode, go to **Control Panel** > **Settings** and select **Update and Security**. 

1. To boot to maintenance mode, select **Recovery** > **Advanced startup**.

1. At the next menu, select **Troubleshoot** > **Advanced Options** > **Startup Settings** > **Restart**. 

1. After Windows restarts to the **Startup Settings** screen, select option 4, 5, or 6 to boot to Safe Mode.

Safe Mode might be available by pressing a function key on boot, for example **F8**. Refer to information from the manufacturer for specific startup options.
