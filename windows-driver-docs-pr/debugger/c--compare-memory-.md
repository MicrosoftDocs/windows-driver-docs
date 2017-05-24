---
title: c (Compare Memory)
description: The c command compares the values held in two memory areas.
ms.assetid: caa02ec3-35d6-4d41-a777-daa264b0dd18
keywords: ["c (Compare Memory) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- c (Compare Memory)
api_type:
- NA
---

# c (Compare Memory)


The **c** command compares the values held in two memory areas.

``` syntax
c Range Address 
```

## <span id="ddk_cmd_compare_memory_dbg"></span><span id="DDK_CMD_COMPARE_MEMORY_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
The first of the two memory ranges to be compared. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The starting address of the second memory range to be compared. The size of this range will be the same as that specified for the first range. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

If the two areas are not identical, the debugger will display all memory addresses in the first range where they do not agree.

As an example, consider the following code:

```
void main()
{
    char rgBuf1[100];
    char rgBuf2[100];

    memset(rgBuf1, 0xCC, sizeof(rgBuf1));
    memset(rgBuf2, 0xCC, sizeof(rgBuf2));

    rgBuf1[42] = 0xFF;
}
```

To compare **rgBuf1** and **rgBuf2**, use either of the following commands:

```
0:000> c rgBuf1 (rgBuf1+0n100) rgBuf2

0:000> c rgBuf1 L 0n100 rgBuf2
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20c%20%28Compare%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




