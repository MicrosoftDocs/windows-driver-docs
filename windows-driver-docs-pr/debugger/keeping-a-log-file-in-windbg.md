---
title: Keeping a Log File in WinDbg
description: Keeping a Log File in WinDbg
ms.assetid: 96CFF42B-CBBB-40F7-8CD3-1CF4A538A963
---

# Keeping a Log File in WinDbg


## <span id="ddk_keeping_a_log_file_dbg"></span><span id="DDK_KEEPING_A_LOG_FILE_DBG"></span>


WinDbg can write a log file that records the debugging session. This log file contains all of the contents of the [Debugger Command window](debugger-command-window.md), including the commands that you type and the responses from the debugger.

### <span id="opening_a_new_log_file"></span><span id="OPENING_A_NEW_LOG_FILE"></span>Opening a New Log File

To open a new log file, or to overwrite a previous log file, do one of the following:

-   Choose **Open/Close Log file** from the **Edit** menu.

-   When you start WinDbg in a Command Prompt window, use the **-logo** command-line option.

-   Enter the [**.logopen (Open Log File)**](-logopen--open-log-file-.md) command. If you use the **/t** option, the date and time are appended to your specified file name. If you use the **/u** option, the log file is written in Unicode instead of in ASCII.

### <span id="appending_to_an_existing_log_file"></span><span id="APPENDING_TO_AN_EXISTING_LOG_FILE"></span>Appending to an Existing Log File

To append command window text to a log file, do one of the following:

-   Choose **Open/Close Log file** from the **Edit** menu.

-   When you start WinDbg in a Command Prompt window, use the **-loga** command-line option.

-   Enter the [**.logappend (Append Log File)**](-logappend--append-log-file-.md) command. If you are appending to a Unicode log file, you must use the **/u** option.

### <span id="closing_a_log_file"></span><span id="CLOSING_A_LOG_FILE"></span>Closing a Log File

To close an open log file, do one of the following:

-   Choose **Open/Close Log file** from the **Edit** menu.

-   Enter the [**.logclose (Close Log File)**](-logclose--close-log-file-.md) command.

### <span id="checking_log_file_status"></span><span id="CHECKING_LOG_FILE_STATUS"></span>Checking Log File Status

To determine the log file status, do one of the following:

-   Choose **Open/Close Log file** from the **Edit** menu, and see whether a log file is listed.

-   Enter the [**.logfile (Display Log File Status)**](-logfile--display-log-file-status-.md) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Keeping%20a%20Log%20File%20in%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




