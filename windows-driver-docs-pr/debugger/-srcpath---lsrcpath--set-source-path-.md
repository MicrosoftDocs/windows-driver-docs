---
title: .srcpath, .lsrcpath (Set Source Path)
description: The .srcpath and .lsrcpath commands set or display the source file search path.
ms.assetid: 416c062f-cbf9-4134-aa2c-306147a466b5
keywords: [".srcpath, .lsrcpath (Set Source Path) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .srcpath, .lsrcpath (Set Source Path)
api_type:
- NA
ms.localizationpriority: medium
---

# .srcpath, .lsrcpath (Set Source Path)


The **.srcpath** and **.lsrcpath** commands set or display the source file search path.

```dbgcmd
.srcpath[+] [Directory [; ...]] 
.lsrcpath[+] [Directory [; ...]] 
```

## <span id="ddk_meta_set_source_path_dbg"></span><span id="DDK_META_SET_SOURCE_PATH_DBG"></span>Parameters


<span id="______________"></span> **+**   
Specifies that the new directories will be appended to (rather than replacing) the previous source file search path.

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If *Directory* is not specified, the current path is displayed. Separate multiple directories with semicolons.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

The **.srcpath** command is available on all debuggers. The **.lsrcpath** command is available only in WinDbg and cannot be used in script files.

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

For details and other ways to change this path, see [Source Path](source-path.md). For more information about commands that can be used while performing remote debugging through the debugger, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

Remarks
-------

If you include `srv*` in your source path, the debugger uses [SrcSrv](srcsrv.md) to retrieve source files from locations specified in the target modules' symbol files. For more information about using srv\* in a source path, see [Using a Source Server](using-a-source-server.md) and [**.srcfix**](-srcfix---lsrcfix--use-source-server-.md).

When this command is issued from a debugging client, **.srcpath** sets the source path on the debugging server, while **.lsrcpath** sets the source path on the local machine.

 

 





