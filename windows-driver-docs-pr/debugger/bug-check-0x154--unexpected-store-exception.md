---
title: Bug Check 0x154 UNEXPECTED_STORE_EXCEPTION
description: Learn about the UNEXPECTED_STORE_EXCEPTION bug check, which indicates that the kernel memory store component caught an unexpected exception.
keywords: ["Bug Check 0x154 UNEXPECTED_STORE_EXCEPTION", "UNEXPECTED_STORE_EXCEPTION"]
ms.date: 12/12/2022
topic_type:
- apiref
api_name:
- UNEXPECTED_STORE_EXCEPTION
api_type:
- NA
---

# Bug Check 0x154: UNEXPECTED_STORE_EXCEPTION

The UNEXPECTED_STORE_EXCEPTION bug check has a value of 0x00000154. This bug check indicates that the kernel memory store component caught an unexpected exception.

> [!IMPORTANT]
> This topic is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## UNEXPECTED_STORE_EXCEPTION parameters

| Parameter | Description                                  |
|-----------|----------------------------------------------|
| 1         | Pointer to the store context or data manager |
| 2         | Exception information                        |
| 3         | Reserved                                     |
| 4         | Reserved                                     |

## Resolution

To determine the cause of the issue, use the debugger to gather additional information. Examine multiple dump files to see if this stop code has similar characteristics, such as the same code running when the stop code appears. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md), [Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](-analyze.md).

After information about the source code in question is available, set a breakpoint in the related code before this code is executed. Single step forward through the code, looking at the values of critical variables that are used to control the code flow. Carefully examine this area of your code to look for false assumptions or other mistakes.

## Troubleshooting tips

If you're not able to work with the underlying code that's causing the issue, these troubleshooting tips might be helpful.

- Check the System Log in Event Viewer for other error messages to help pinpoint the device or driver that's causing the error. To open Event Viewer, select the keyboard shortcut Win+R, enter `eventvwr.msc` and press the ENTER key. Look for critical errors in the system log that occurred in the same time frame as the blue screen.

- Select Start, enter **"Windows Memory Diagnostics"** in the Search box, and then press Enter. Choose whether to restart the computer and run the tool immediately or schedule the tool to run at the next restart. Windows Memory Diagnostics runs automatically after the computer restarts and performs a standard memory test automatically. To run the extended test, press F1 and use the Up and Down arrow keys to set the Test Mix to Extended. Press F10 to apply the desired settings and resume testing.

- Look in Device Manager to see if any devices are marked with the exclamation point (!). Review the events log displayed in the driver properties for any faulting driver. Try updating the related driver.

- Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the `SFC /scannow` command to run the System File Checker tool. For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

## See also

[Bug Check code reference](bug-check-code-reference2.md)
