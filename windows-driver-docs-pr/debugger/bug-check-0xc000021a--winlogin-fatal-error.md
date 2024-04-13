---
title: Bug Check 0xC000021A WINLOGON_FATAL_ERROR
description: The WINLOGON_FATAL_ERROR bug check has a value of 0xC000021A. This means that the Winlogon process terminated unexpectedly.
keywords: ["Bug Check 0xC000021A WINLOGON_FATAL_ERROR", "WINLOGON_FATAL_ERROR"]
ms.date: 09/12/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- WINLOGON_FATAL_ERROR
api_type:
- NA
---

# Bug Check 0xC000021A: WINLOGON\_FATAL\_ERROR

The WINLOGON\_FATAL\_ERROR bug check has a value of 0xC000021A. This means that the Winlogon process terminated unexpectedly.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## WINLOGON\_FATAL\_ERROR Parameters

<table>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>A string that identifies the problem</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The error code</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

## Cause

This error occurs when a user-mode subsystem, such as WinLogon or the Client Server Run-Time Subsystem (CSRSS), has been fatally compromised and security can no longer be guaranteed. In response, the operating system switches to kernel mode. Microsoft Windows cannot run without WinLogon or CSRSS. Therefore, this is one of the few cases where the failure of a user-mode service can shut down the system.

Mismatched system files can also cause this error. This mismatch can occur if you have restored your hard disk from a backup. Some backup programs might skip restoring system files that they determine are in use.

## Resolution

Running the kernel debugger may not be useful in this situation because the actual error occurred in a user-mode process.

### Resolving an error in a user-mode device driver, system service, or third-party application

Because bug check 0xC000021A occurs in a user-mode process, the most common culprits are third-party applications. If the error occurred after the installation of a new or updated device driver, system service, or third-party application, the new software should be removed or disabled to isolate the cause. Contact the manufacturer of the software about a possible update.

### Resolving a mismatched system file problem

If you have recently restored your hard disk from a backup, check if there is an updated version of the backup/restore program available from the manufacturer.

- Look at the most recently installed applications. To do this navigate to "Uninstall or change a program" in control panel and sort the installed applications by install date.

- Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://support.microsoft.com/hub/4338813/windows-help#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. Look for critical errors in the system log that occurred in the same time window as the blue screen.

## Remarks

- Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

-   Run a virus detection program. Viruses can infect all types of hard disks that are formatted for Windows, and the resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

-   Verify that the system has the latest updates installed. To detect which version is installed on your system, select **Start**, select **Run**, type **winver**, and then press ENTER. The **About Windows** dialog box displays the Windows version number (and the version number of the service pack, if one is installed).

### Using Safe Mode

Consider using Safe Mode to isolate elements for troubleshooting and, if necessary, to use Windows. Using Safe Mode loads only the minimum required drivers and system services during the Windows startup.

To enter Safe Mode, use **Update and Security** in Settings. Select **Recovery**&nbsp;&gt; **Advanced startup** to boot to maintenance mode. At the resulting menu, choose **Troubleshoot**&nbsp;&gt; **Advanced Options**&nbsp;&gt; **Startup Settings**&nbsp;&gt; **Restart**. After Windows restarts and displays the **Startup Settings** screen, select option 4, 5, or 6 to boot to Safe Mode.

Safe Mode may also be available by pressing a function key on boot, for example F8. Refer to information from the computer's manufacturer for specific startup options.
