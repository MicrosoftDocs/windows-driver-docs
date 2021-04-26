---
title: Bug Check 0x154 UNEXPECTED_STORE_EXCEPTION
description: The UNEXPECTED_STORE_EXCEPTION bug check has a value of 0x00000154. This indicates that the kernel memory store component caught an unexpected exception.
keywords: ["Bug Check 0x154 UNEXPECTED_STORE_EXCEPTION", "UNEXPECTED_STORE_EXCEPTION"]
ms.date: 02/27/2020
topic_type:
- apiref
api_name:
- UNEXPECTED_STORE_EXCEPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x154: UNEXPECTED\_STORE\_EXCEPTION

The UNEXPECTED\_STORE\_EXCEPTION bug check has a value of 0x00000154. This indicates that the kernel memory store component caught an unexpected exception.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## UNEXPECTED\_STORE\_EXCEPTION Parameters

| Parameter | Description                                  |
|-----------|----------------------------------------------|
| 1         | Pointer to the store context or data manager |
| 2         | Exception information                        |
| 3         | Reserved                                     |
| 4         | Reserved                                     |

## Resolution

Determining the cause of this issues typically requires the use of the debugger to gather additional information. Multiple dump files should be examined to see if this stop code has similar characteristics, such as if the same code is running when the stop code appears. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md), [Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md).

Once information about the source code in question is available,  set a breakpoint in the related code before this code is executed and single step forward through the code looking at the values of critical variables that are used to control the code flow.  Carefully examine this area of your code to look for false assumptions or other mistakes.

## Troubleshooting Tips

If you are not able to work with the underlying code that is causing this issue, these troubleshooting tips may be helpful.

- Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. To open Event Viewer select the keyboard shortcut Win+R, type `eventvwr.msc` and press the ENTER key. Look for critical errors in the system log that occurred in the same time window as the blue screen.

- Select Start, and type **"Windows Memory Diagnostics"** in the Search box, and then press Enter. Choose whether to restart the computer and run the tool immediately or schedule the tool to run at the next restart. Windows Memory Diagnostics runs automatically after the computer restarts and performs a standard memory test automatically. To run the extended test, press F1, and use the Up and Down arrow keys to set the Test Mix to Extended, and then press F10 to apply the desired settings and resume testing.

- Look in Device Manager to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

- Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

  `SFC /scannow`

   For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

