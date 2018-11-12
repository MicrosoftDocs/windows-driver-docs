---
title: .send_file (Send File)
description: The .send_file command copies files. If you are performing remote debugging through a process server, it sends a file from the smart client's computer to the process server's computer.
ms.assetid: ad12ec46-79a3-458a-acdc-c2ccb06f8c96
keywords: [".send_file (Send File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .send_file (Send File)
api_type:
- NA
ms.localizationpriority: medium
---

# .send\_file (Send File)


The **.send\_file** command copies files. If you are performing remote debugging through a process server, it sends a file from the smart client's computer to the process server's computer.

```dbgcmd
.send_file [-f] Source Destination 
.send_file [-f] -s Destination 
```

## <span id="ddk_meta_send_file_dbg"></span><span id="DDK_META_SEND_FILE_DBG"></span>Parameters


<span id="_______-f______"></span><span id="_______-F______"></span> **-f**   
Forces file creation. By default, **.send\_file** will not overwrite any existing files. If the -f switch is used, the destination file will always be created, and any existing file with the same name will be overwritten.

<span id="_______Source______"></span><span id="_______source______"></span><span id="_______SOURCE______"></span> *Source*   
Specifies the full path and filename of the file to be sent. If you are debugging through a process server, this file must be located on the computer where the smart client is running.

<span id="_______Destination______"></span><span id="_______destination______"></span><span id="_______DESTINATION______"></span> *Destination*   
Specifies the directory where the file is to be written. If you are debugging through a process server, this directory name is evaluated on the computer where the process server is running.

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Causes the debugger to copy all loaded symbol files.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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

 

Remarks
-------

This command is particularly useful when you have been performing remote debugging through a process server, but wish to begin debugging locally instead. In this case you can use the .send\_file -s command to copy all the symbol files that the debugger has been using to the process server. These symbol files can then be used by a debugger running on the local computer.

 

 





