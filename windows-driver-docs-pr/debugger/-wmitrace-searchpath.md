---
title: wmitrace.searchpath
description: The wmitrace.searchpath extension specifies the location of the trace message format files for messages in the trace buffers.
ms.assetid: 528c997c-007c-4046-92cc-169c7720b3fe
keywords: ["wmitrace.searchpath Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wmitrace.searchpath
api_type:
- NA
---

# !wmitrace.searchpath


The **!wmitrace.searchpath** extension specifies the location of the trace message format files for messages in the trace buffers.

```
!wmitrace.searchpath [+] TMFPath 
!wmitrace.searchpath
```

## <span id="ddk__wmitrace_searchpath_dbg"></span><span id="DDK__WMITRACE_SEARCHPATH_DBG"></span>Parameters


<span id="______________"></span> **+**   
Causes *TMFPath* to be appended to the existing search path. If the plus (+) token is not used, *TMFPath* replaces the existing search path.

<span id="_______TMFPath______"></span><span id="_______tmfpath______"></span><span id="_______TMFPATH______"></span> *TMFPath*   
The path to the directory where the debugger should look for the trace message format files. Paths that contain spaces are not supported. If multiple paths are included, they should be separated by semicolons, and the entire string should be enclosed in quotation marks. If the path is in quotation marks, the backslash character must be preceded by an escape character ( `"c:\\debuggers;c:\\debuggers2"` ). When the **+** token is used, *TMFPath* will be appended to the existing path, with a semicolon automatically inserted between the existing path and the new path; however, if the **+** token is used, quotation marks cannot be used.

<span id="_____________"></span>   

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about trace message format files, see the "Trace Message Format Files" topic in the Windows Driver Kit (WDK).

Remarks
-------

When used with no parameters, **!wmitrace.searchpath** displays the current search path.

The trace message format files (\*.tmf) contain instructions for formatting the binary trace messages that a trace provider generates.

The *TMFPath* parameter must contain only a path to a directory; it cannot include a file name. The name of a TMF file is a message GUID followed by the .tmf extension. When the system formats a message, it reads the message GUID on the message and searches recursively for a TMF file whose name matches the message GUID, beginning in the specified directory.

Windows needs a TMF file in order to format the binary trace messages in a buffer. Use **!wmitrace.searchpath** or [**!wmitrace.tmffile**](-wmitrace-tmffile.md) to specify the TMF file before using [**!wmitrace.dynamicprint**](-wmitrace-dynamicprint.md) or [**!wmitrace.logdump**](-wmitrace-logdump.md) to display trace buffer contents.

If you do not use either **!wmitrace.searchpath** or [**!wmitrace.tmffile**](-wmitrace-tmffile.md), the system uses the value of the TRACE\_FORMAT\_SEARCH\_PATH environment variable. If that variable is not present, it uses the default.tmf file, which is included in Windows. If the system cannot find any formatting information for a trace message, it writes a "No format information found" error message in place of the trace message content.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wmitrace.searchpath%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




