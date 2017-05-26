---
title: m (Move Memory)
description: The m command copies the contents of memory from one location to another. Do not confuse this command with the ~m (Resume Thread) command.
ms.assetid: afcac933-6bba-4566-ae07-bb9110f851d2
keywords: ["m (Move Memory) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- m (Move Memory)
api_type:
- NA
---

# m (Move Memory)


The **m** command copies the contents of memory from one location to another.

Do not confuse this command with the [**~m (Resume Thread)**](-m--resume-thread-.md) command.

```
    m Range Address 
```

## <span id="ddk_cmd_move_memory_dbg"></span><span id="DDK_CMD_MOVE_MEMORY_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory area to copy. For more information about the syntax of this parameter, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the starting address of the destination memory area. For more information about the syntax of this parameter, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

The memory area that *Address* specifies can be part of the memory area that *Range* specifies. Overlapping moves are handled correctly.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20m%20%28Move%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




