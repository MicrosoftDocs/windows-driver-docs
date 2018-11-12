---
title: .srcfix, .lsrcfix (Use Source Server)
description: The .srcfix and .lsrcfix commands automatically set the source path to indicate that a source server will be used.
ms.assetid: e4cc3031-7990-4339-9dc2-f2c5a219a771
keywords: [".srcfix, .lsrcfix (Use Source Server) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .srcfix, .lsrcfix (Use Source Server)
api_type:
- NA
ms.localizationpriority: medium
---

# .srcfix, .lsrcfix (Use Source Server)


The **.srcfix** and **.lsrcfix** commands automatically set the source path to indicate that a source server will be used.

```dbgcmd
.srcfix[+] [Paths] 
.lsrcfix[+] [Paths] 
```

## <span id="ddk_meta_use_source_server_dbg"></span><span id="DDK_META_USE_SOURCE_SERVER_DBG"></span>Parameters


<span id="______________"></span> **+**   
Causes the existing source path to be preserved, and **; srv\\*** to be appended to the end. If the **+** is not used, the existing source path is replaced.

<span id="_______Paths______"></span><span id="_______paths______"></span><span id="_______PATHS______"></span> *Paths*   
Specifies one or more additional paths to append to the end of the new source path.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

The **.srcfix** command is available on all debuggers. The **.lsrcfix** command is available only in WinDbg and cannot be used in script files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information on setting the local source path for a remote client, see [**WinDbg Command-Line Options**](windbg-command-line-options.md). For details about [SrcSrv](srcsrv.md), see [Using a Source Server](using-a-source-server.md). For details on the source path and the local source path, see [Source Path](source-path.md). For more information about commands that can be used while performing remote debugging through the debugger, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

Remarks
-------

When you add `srv*` to the source path, the debugger uses [SrcSrv](srcsrv.md) to retrieve source files from locations specified in the target modules' symbol files. Using `srv*` in the source path is fundamentally different from using `srv*` in the symbol path. In the symbol path, you can specify a symbol server location along with the `srv*` (for example, `.sympath SRV*https://msdl.microsoft.com/download/symbols`). In the source path, srv\* stands alone, separated from all other elements by semicolons.

When this command is issued from a debugging client, **.srcfix** sets the source path to use a source server on the debugging server, while **.lsrcfix** does the same on the local machine.

These commands are the same as the [**.srcpath (Set Source Path)**](-srcpath---lsrcpath--set-source-path-.md) and **.lsrcpath (Set Local Source Path)** commands followed by the **srv\\*** source path element. Thus, the following two commands are equivalent:

```dbgcmd
.srcfix[+] [Paths] 
.srcpath[+] srv*[;Paths] 
```

Similarly, the following two commands are equivalent:

```dbgcmd
.lsrcfix[+] [Paths] 
.lsrcpath[+] srv*[;Paths] 
```

 

 





