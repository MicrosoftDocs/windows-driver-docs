---
title: .writemem (Write Memory to File)
description: The .writemem command writes a section of memory to a file.
ms.assetid: 928e9452-d9b4-49fa-a5fa-cdc3832d7349
keywords: [".writemem (Write Memory to File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .writemem (Write Memory to File)
api_type:
- NA
---

# .writemem (Write Memory to File)


The **.writemem** command writes a section of memory to a file.

```
.writemem FileName Range 
```

## <span id="ddk_meta_write_memory_to_file_dbg"></span><span id="DDK_META_WRITE_MEMORY_TO_FILE_DBG"></span>Parameters


<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the file to be created. You can specify a full path and file name, or just the file name. If the file name contains spaces, *FileName* should be enclosed in quotation marks. If no path is specified, the current directory is used.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range to be written to the file. For syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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

The memory is copied literally to the file. It is not parsed in any way.

The **.writemem** command is the opposite of the [**.readmem (Read Memory from File)**](-readmem--read-memory-from-file-.md) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.writemem%20%28Write%20Memory%20to%20File%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




