---
title: .logappend (Append Log File)
description: The .logappend command appends a copy of the events and commands from the Debugger Command window to the specified log file.
ms.assetid: e1c58c34-1fc5-4ec3-bd37-6c7816735aec
keywords: ["Append Log File (.logappend) command", "log file, Append Log File (.logappend) command", ".logappend (Append Log File) Windows Debugging"]
topic_type:
- apiref
api_name:
- .logappend (Append Log File)
api_type:
- NA
---

# .logappend (Append Log File)


The **.logappend** command appends a copy of the events and commands from the [Debugger Command window](debugger-command-window.md) to the specified log file.

``` syntax
.logappend [/u] [FileName]
```

## <span id="ddk_meta_append_log_file_dbg"></span><span id="DDK_META_APPEND_LOG_FILE_DBG"></span>Parameters


<span id="________u______"></span><span id="________U______"></span> **/u**   
Writes the log file in Unicode format. If you omit this parameter, the debugger writes the log file in ASCII (ANSI) format.

**Note**   When you are appending to an existing log file, you should use the **/u** parameter only if you created the log file by using the **/u** option. Otherwise, your log file will contain ASCII and Unicode characters, which might make it more difficult to read.

 

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the log file. You can specify a full path or only the file name. If the file name contains spaces, enclose *FileName* in quotation marks. If you do not specify the path, the debugger uses the current directory. If you omit *FileName*, the debugger names the file Dbgeng.log.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If you already have a log file open when you run the **.logappend** command, the debugger closes the log file. If you specify the name of a file that already exists, the debugger appends new information to the file. If the file does not exist, the debugger creates it.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.logappend%20%28Append%20Log%20File%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




