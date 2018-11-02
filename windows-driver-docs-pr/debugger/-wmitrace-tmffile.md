---
title: wmitrace.tmffile
description: The wmitrace.tmffile extension specifies a trace message format (TMF) file. The file specified by this extension is used to format trace messages displayed or written by other WMI tracing extensions.
ms.assetid: 37ad335b-7604-466b-b328-7aebbc2fb5c1
keywords: ["wmitrace.tmffile Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.tmffile
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.tmffile


The **!wmitrace.tmffile** extension specifies a trace message format (TMF) file. The file specified by this extension is used to format trace messages displayed or written by other WMI tracing extensions.

```dbgcmd
!wmitrace.tmffile TMFFile 
```

## <span id="ddk__wmitrace_tmffile_dbg"></span><span id="DDK__WMITRACE_TMFFILE_DBG"></span>Parameters


<span id="_______TMFFile______"></span><span id="_______tmffile______"></span><span id="_______TMFFILE______"></span> *TMFFile*   
Specifies a trace message format file.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about trace message format files, see the "Trace Message Format File" topic in the Windows Driver Kit (WDK).

Remarks
-------

*Trace message format files* (.tmf) are structured text files that are created during Windows software trace preprocessor (WPP) software tracing. These files contain instructions for formatting trace binary trace messages so that they can be displayed in human-readable form.

In order to display the trace message in a trace buffer ([**!wmitrace.logdump**](-wmitrace-logdump.md)) or write them to a file [**(!wmitrace.logsave**](-wmitrace-logsave.md)), you must first identify the TMF files for the trace messages.

You can use [**!wmitrace.searchpath**](-wmitrace-searchpath.md) to specify a directory in which TMF files are stored. The system then searches the directory for a TMF file that contains instructions for the messages that it is formatting. (It uses the message GUID to associate the message with the correct TMF file.)

However, you can use **!wmitrace.tmffile** to specify a particular TMF file. You must use **!wmitrace.tmffile** if the TMF file name is not a message GUID followed by the .tmf extension. Otherwise, the system will not find it.

If you do not use either [**!wmitrace.searchpath**](-wmitrace-searchpath.md) or **!wmitrace.tmffile**, the system uses the value of the TRACE\_FORMAT\_SEARCH\_PATH environment variable. If that variable is not present, it uses the default.tmf file. If the system cannot find formatting information for a trace message, it writes a "No format information found" error message, instead of the trace message content.

**Note**  If your driver uses UMDF version 1.11 or later, you do not need to use [**!wmitrace.searchpath**](-wmitrace-searchpath.md) or **!wmitrace.tmffile**.

 

This extension is only useful during WPP software tracing, and earlier (legacy) methods of Event Tracing for Windows. Trace events that are produced by other manifested providers do not use trace message format (TMF) files, and therefore this extension cannot be used with them.

 

 





