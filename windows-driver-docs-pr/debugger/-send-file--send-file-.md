---
title: .send_file (Send File)
description: The .send_file command copies files. If you are performing remote debugging through a process server, it sends a file from the smart client's computer to the process server's computer.
ms.assetid: ad12ec46-79a3-458a-acdc-c2ccb06f8c96
keywords: [".send_file (Send File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .send_file (Send File)
api_type:
- NA
---

# .send\_file (Send File)


The **.send\_file** command copies files. If you are performing remote debugging through a process server, it sends a file from the smart client's computer to the process server's computer.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.send_file%20%28Send%20File%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




