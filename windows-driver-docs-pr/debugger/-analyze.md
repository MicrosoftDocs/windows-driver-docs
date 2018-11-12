---
title: analyze
description: The analyze extension displays information about the current exception or bug check.
ms.assetid: dec760fb-0af6-4504-9855-8fe63c1c9783
keywords: ["analyze Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- analyze
api_type:
- NA
ms.localizationpriority: medium
---

# !analyze


The **!analyze** extension displays information about the current exception or bug check.

User-Mode

```dbgcmd
    !analyze [-v] [-f | -hang] [-D BucketID] 
    !analyze -c [-load KnownIssuesFile | -unload | -help ]
```

Kernel-Mode

```dbgcmd    
    !analyze [-v] [-f | -hang] [-D BucketID] 
    !analyze -c [-load KnownIssuesFile | -unload | -help ]
    !analyze -show BugCheckCode [BugParameters]
```

## <span id="ddk__analyze_dbg"></span><span id="DDK__ANALYZE_DBG"></span>Parameters


<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Displays verbose output.

<span id="-f"></span><span id="-F"></span>**-f**  
Generates the **!analyze** exception output. Use this parameter to see an exception analysis even when the debugger does not detect an exception.

<span id="-hang"></span><span id="-HANG"></span>**-hang**  
Generates **!analyze** hung-application output. Use this parameter when the target has experienced a bug check or exception, but an analysis of why an application hung is more relevant to your problem. In kernel mode, **!analyze** **-hang** investigates locks that the system holds and then scans the DPC queue chain. In user mode, **!analyze** **-hang** analyzes the thread stack to determine whether any threads are blocking other threads.

Before you run this extension in user mode, consider changing the current thread to the thread that you think has stopped responding (that is, hung), because the exception might have changed the current thread to a different one.

<span id="_______-D_______BucketID______"></span><span id="_______-d_______bucketid______"></span><span id="_______-D_______BUCKETID______"></span> **-D** *BucketID*   
Displays only those items that are relevant to the specified *BucketID*.

<span id="_______-show_______BugCheckCode___BugParameters_"></span><span id="_______-show_______bugcheckcode___bugparameters_"></span><span id="_______-SHOW_______BUGCHECKCODE___BUGPARAMETERS_"></span> **-show** *BugCheckCode* \[*BugParameters*\]  
Displays information about the bug check specified by *BugCheckCode*. *BugParameters* specifies up to four bug check parameters separated by spaces. These parameters enable you to further refine your search.

<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Continues execution when the debugger encounters a known issue. If the issue is not a "known" issue, the debugger remains broken into the target.

You can use the **-c** option with the following subparameters. These subparameters configure the list of known issues. They do not cause execution to occur by themselves. Until you run **!analyze** **-c** **** **-load** at least one time, **!analyze** **-c** has no effect.

<span id="-load_KnownIssuesFile"></span><span id="-load_knownissuesfile"></span><span id="-LOAD_KNOWNISSUESFILE"></span>**-load** *KnownIssuesFile*  
Loads the specified known-issues file. *KnownIssuesFile* specifies the path and file name of this file. This file must be in XML format. You can find a sample file in the sdk\\samples\\analyze\_continue subdirectory of the debugger installation directory. (You must have performed a full installation of Debugging Tools for Windows to have this file.)

The list of known issues in the *KnownIssuesFile* file is used for all later **-c** commands until you use **-c** **** **-unload**, or until you use **-c** **** **-load** again (at which point the new data replaces the old data).

<span id="-unload"></span><span id="-UNLOAD"></span>**-unload**  
Unloads the current list of known issues.

<span id="-help"></span><span id="-HELP"></span>**-help**  
Displays help for the **!analyze** **-c** extension commands extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

Ext.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For sample analysis of a user-mode exception and of a kernel-mode stop error (that is, crash), and for more information about how **!analyze** uses the triage.ini file, see [Using the !analyze Extension](using-the--analyze-extension.md).

Remarks
-------

In user mode, **!analyze** displays information about the current exception.

In kernel mode, **!analyze** displays information about the most recent bug check. If a bug check occurs, the **!analyze** display is automatically generated. You can use **!analyze** **-v** to show additional information. If you want to see only the basic bug check parameters, you can use the [**.bugcheck (Display Bug Check Data)**](-bugcheck--display-bug-check-data-.md) command.

For drivers that use User-Mode Driver Framework (UMDF) version 2.15 or later, **!analyze** provides information about UMDF verifier failures and unhandled exceptions. This functionality is available when performing live kernel-mode debugging, as well when analyzing a user-mode memory dump file. For UMDF driver crashes, **!analyze** attempts to identify the responsible driver.

 

 





