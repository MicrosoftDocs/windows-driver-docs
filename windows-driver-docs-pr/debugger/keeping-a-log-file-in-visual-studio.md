---
title: Keeping a Log File in Visual Studio
description: The Windows Debugger can write a log file that records the debugging session.
ms.assetid: 6A7588D0-A477-4BE9-874F-3AFB52561903
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# Keeping a Log File in Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>


The Windows Debugger can write a log file that records the debugging session. This log file contains all of the commands that you type and the responses from the debugger. In Microsoft Visual Studio, you can open, append, and close log files by entering commands in the Debugger Immediate Window.

The procedures shown in this topic require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Development](https://msdn.microsoft.com/library/windows/hardware/ff557573).

## <span id="ddk_keeping_a_log_file_dbg"></span><span id="DDK_KEEPING_A_LOG_FILE_DBG"></span>


If the Debugger Immediate Window is not already open, from the **Debug** menu, choose **Windows&gt;Immediate**.

### <span id="opening_a_new_log_file"></span><span id="OPENING_A_NEW_LOG_FILE"></span>Opening a New Log File

To open a new log file, enter the [**.logopen (Open Log File)**](-logopen--open-log-file-.md) command. If you use the **/t** option, the date and time are appended to your specified file name. If you use the **/u** option, the log file is written in Unicode instead of in ASCII.

### <span id="appending_to_an_existing_log_file"></span><span id="APPENDING_TO_AN_EXISTING_LOG_FILE"></span>Appending to an Existing Log File

To append text to an existing log file, enter the [**.logappend (Append Log File)**](-logappend--append-log-file-.md) command. If you are appending to a Unicode log file, you must use the **/u** option.

### <span id="closing_a_log_file"></span><span id="CLOSING_A_LOG_FILE"></span>Closing a Log File

To close an open log file, enter the [**.logclose (Close Log File)**](-logclose--close-log-file-.md) command.

### <span id="checking_log_file_status"></span><span id="CHECKING_LOG_FILE_STATUS"></span>Checking Log File Status

To determine the log file status, enter the [**.logfile (Display Log File Status)**](-logfile--display-log-file-status-.md) command.

 

 





