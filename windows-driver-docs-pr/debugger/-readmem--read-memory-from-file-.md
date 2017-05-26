---
title: .readmem (Read Memory from File)
description: The .readmem command reads raw binary data from the specified file and copies the data to the target computer's memory.
ms.assetid: 128cbea1-5fb5-4685-8587-f814f94cc658
keywords: [".readmem (Read Memory from File) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .readmem (Read Memory from File)
api_type:
- NA
---

# .readmem (Read Memory from File)


The **.readmem** command reads raw binary data from the specified file and copies the data to the target computer's memory.

```
    .readmem FileName Range 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the file to read. You can specify a full path or only the file name. If the file name contains spaces, enclose *FileName* in quotation marks. If you do not specify a path, the debugger uses the current directory.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the address range for putting the data in memory. This parameter can contain a starting and ending address or a starting address and an object count. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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

The memory data is copied literally to the target computer. The debugger does not parse the data in any way. For example, the **.readmem myfile 1000 10** command copies 10 bytes from the Myfile file and stores them in the target computer's memory, starting at address 1000.

The **.readmem** command is the opposite of the [**.writemem (Write Memory to File)**](-writemem--write-memory-to-file-.md) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.readmem%20%28Read%20Memory%20from%20File%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




