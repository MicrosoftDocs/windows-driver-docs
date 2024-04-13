---
title: "!wmitrace.searchpath"
description: "The !wmitrace.searchpath extension specifies the location of the trace message format files for messages in the trace buffers."
keywords: ["!wmitrace.searchpath Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wmitrace.searchpath
api_type:
- NA
---

# !wmitrace.searchpath

The **!wmitrace.searchpath** extension specifies the location of the trace message format files for messages in the trace buffers.

```dbgcmd
!wmitrace.searchpath [+] TMFPath 
!wmitrace.searchpath
```

## Parameters

<span id="______________"></span> **+**   
Causes *TMFPath* to be appended to the existing search path. If the plus (+) token is not used, *TMFPath* replaces the existing search path.

<span id="_______TMFPath______"></span><span id="_______tmfpath______"></span><span id="_______TMFPATH______"></span> *TMFPath*   
The path to the directory where the debugger should look for the trace message format files. Paths that contain spaces are not supported. If multiple paths are included, they should be separated by semicolons, and the entire string should be enclosed in quotation marks. If the path is in quotation marks, the backslash character must be preceded by an escape character ( `"c:\\debuggers;c:\\debuggers2"` ). When the **+** token is used, *TMFPath* will be appended to the existing path, with a semicolon automatically inserted between the existing path and the new path; however, if the **+** token is used, quotation marks cannot be used.

<span id="_____________"></span>   

## DLL

Wmitrace.dll

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

## Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about trace message format files, see the "Trace Message Format Files" topic in the Windows Driver Kit (WDK).

## Remarks

When used with no parameters, **!wmitrace.searchpath** displays the current search path.

The trace message format files (\*.tmf) contain instructions for formatting the binary trace messages that a trace provider generates.

The *TMFPath* parameter must contain only a path to a directory; it cannot include a file name. The name of a TMF file is a message GUID followed by the .tmf extension. When the system formats a message, it reads the message GUID on the message and searches recursively for a TMF file whose name matches the message GUID, beginning in the specified directory.

Windows needs a TMF file in order to format the binary trace messages in a buffer. Use **!wmitrace.searchpath** or [**!wmitrace.tmffile**](-wmitrace-tmffile.md) to specify the TMF file before using [**!wmitrace.dynamicprint**](-wmitrace-dynamicprint.md) or [**!wmitrace.logdump**](-wmitrace-logdump.md) to display trace buffer contents.

If you do not use either **!wmitrace.searchpath** or [**!wmitrace.tmffile**](-wmitrace-tmffile.md), the system uses the value of the TRACE\_FORMAT\_SEARCH\_PATH environment variable. If that variable is not present, it uses the default.tmf file, which is included in Windows. If the system cannot find any formatting information for a trace message, it writes a "No format information found" error message in place of the trace message content.
