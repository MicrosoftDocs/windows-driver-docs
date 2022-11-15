---
title: Extracting Information from a Dump File
description: Extracting Information from a Dump File
keywords: ["extracting information from a dump file", "dump file, extracting various information", "machine name (determining from a dump file)", "computer name (determining from a dump file)", "IP address (determining from a dump file)"]
ms.date: 11/09/2022
---

# Extracting Information from a Dump File

Certain kinds of information, such as the name of the target computer, are easily available during live debugging. When debugging a dump file it takes a little more work to determine this information.

### Finding the Computer Name in a Kernel-Mode Dump File

If you need to determine the name of the computer on which the crash dump was made, you can use the [**!peb**](-peb.md) extension and look for the value of COMPUTERNAME it its output.

### Finding the IP Address in a Kernel-Mode Dump File

To determine the IP address of the computer on which the crash dump was made, find a thread stack that shows some send/receive network activity. Open one of the send packets or receive packets. The IP address will be visible in that packet.

### Finding the Process ID in a User-Mode Dump File

To determine the process ID of the target application from a user-mode dump file, use the [**| (Process Status)**](---process-status-.md) command. This will display all the processes being debugged at the time the dump was written. The process marked with a period (**.**) is the current process. Its process ID is given in hexadecimal after the **id:** notation.

## Integrate WER into applications

[Windows Error Reporting (WER)](/windows/desktop/wer/windows-error-reporting) information can be integrated into applications to provide additional crash dump information. For more information, see [Using WER](/windows/desktop/wer/using-wer).

## Related topics

[Advanced Driver Debugging \[336 KB\] \[PPT\]](https://download.microsoft.com/download/f/0/5/f05a42ce-575b-4c60-82d6-208d3754b2d6/adv-drv_debug.ppt)

[WDK and WinDbg downloads](../download-the-wdk.md)

[Driver Debugging Basics \[WinHEC 2007; 633 KB\] \[PPT\]](https://download.microsoft.com/download/a/f/d/afdfd50d-6eb9-425e-84e1-b4085a80e34e/dvr-t410_wh07.pptx)

[How to read the small memory dump file that is created by Windows if a crash occurs](https://support.microsoft.com/help/315263/how-to-read-the-small-memory-dump-file-that-is-created-by-windows-if-a)

[Resource-Definition Statements](/windows/desktop/menurc/resource-definition-statements)

[Windows Error Reporting](/windows/desktop/wer/windows-error-reporting)

[VERSIONINFO resource](/windows/desktop/menurc/versioninfo-resource)

 

 





