---
title: Extract information from a dump file
description: Learn how to debug a dump file to determine certain kinds of information, such as the name of the target computer.
keywords: ["extracting information from a dump file", "dump file, extracting various information", "machine name (determining from a dump file)", "computer name (determining from a dump file)", "IP address (determining from a dump file)"]
ms.date: 12/14/2022
---

# Extract information from a dump file

Some information, such as the name of the target computer, is easily available during live debugging. You can also debug a dump file to determine the information. This article explains how to extract information from a dump file.

## Find the computer name in a kernel-mode dump file

Use the [!peb](-peb.md) extension if you need to determine the name of the computer on which the crash dump was made. Look for the value of COMPUTERNAME in its output.

## Find the IP address in a kernel-mode dump file

To determine the IP address of the computer on which the crash dump was made, find a thread stack that shows some send or receive network activity. Open one of the send or receive packets. The IP address is visible in that packet.

## Find the process ID in a user-mode dump file

To determine the process ID of the target application from a user-mode dump file, use the [| (Process status)](---process-status-.md) command. This command displays all the processes being debugged at the time the dump was written. The process marked with a period (.) is the current process. Its process ID is given in hexadecimal after the **id:** notation.

## Integrate WER into applications

[Windows error reporting (WER)](/windows/desktop/wer/windows-error-reporting) information can be integrated into applications to provide other crash dump information. For more information, see [Using WER](/windows/desktop/wer/using-wer).

## See also

- [Advanced driver debugging [336 KB] [PPT]](https://download.microsoft.com/download/f/0/5/f05a42ce-575b-4c60-82d6-208d3754b2d6/adv-drv_debug.ppt)

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)

- [Driver debugging basics [WinHEC 2007; 633 KB] [PPT]](https://download.microsoft.com/download/a/f/d/afdfd50d-6eb9-425e-84e1-b4085a80e34e/dvr-t410_wh07.pptx)

- [How to read the small memory dump file that is created by Windows if a crash occurs](https://support.microsoft.com/help/315263/how-to-read-the-small-memory-dump-file-that-is-created-by-windows-if-a)

- [Resource-definition statements](/windows/desktop/menurc/resource-definition-statements)

- [Windows error reporting](/windows/desktop/wer/windows-error-reporting)

- [VERSIONINFO resource](/windows/desktop/menurc/versioninfo-resource)

 

 





