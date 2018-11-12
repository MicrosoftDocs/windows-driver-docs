---
title: Keeping a Log File in CDB
description: Keeping a Log File in CDB
ms.assetid: 02164ABF-BF57-4E1D-BD4B-CEEE60E0D7D0
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Keeping a Log File in CDB


## <span id="ddk_keeping_a_log_file_dbg"></span><span id="DDK_KEEPING_A_LOG_FILE_DBG"></span>


CDB can write a log file that records the debugging session. This log file contains all of the commands that you type and the responses from the debugger.

### <span id="opening_a_new_log_file"></span><span id="OPENING_A_NEW_LOG_FILE"></span>Opening a New Log File

To open a new log file, or to overwrite a previous log file, do one of the following:

-   Before you start the debugger, set the \_NT\_DEBUG\_LOG\_FILE\_OPEN [environment variable](environment-variables.md).

-   When you start the debugger, use the **-logo** command-line option.

-   Enter the [**.logopen (Open Log File)**](-logopen--open-log-file-.md) command. If you use the **/t** option, the date and time are appended to your specified file name. If you use the **/u** option, the log file is written in Unicode instead of in ASCII.

### <span id="appending_to_an_existing_log_file"></span><span id="APPENDING_TO_AN_EXISTING_LOG_FILE"></span>Appending to an Existing Log File

To append command window text to a log file, do one of the following:

-   Before you start the debugger, set the \_NT\_DEBUG\_LOG\_FILE\_APPEND [environment variable](environment-variables.md).

-   When you start the debugger, use the **-loga** command-line option.

-   Enter the [**.logappend (Append Log File)**](-logappend--append-log-file-.md) command. If you are appending to a Unicode log file, you must use the **/u** option.

### <span id="closing_a_log_file"></span><span id="CLOSING_A_LOG_FILE"></span>Closing a Log File

To close an open log file, do the following:

-   Enter the [**.logclose (Close Log File)**](-logclose--close-log-file-.md) command.

### <span id="checking_log_file_status"></span><span id="CHECKING_LOG_FILE_STATUS"></span>Checking Log File Status

To determine the log file status, do the following:

-   Enter the [**.logfile (Display Log File Status)**](-logfile--display-log-file-status-.md) command.

 

 





