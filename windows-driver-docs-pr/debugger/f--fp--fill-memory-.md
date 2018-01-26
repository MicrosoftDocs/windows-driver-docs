---
title: f, fp (Fill Memory)
description: The f and fp commands fill the specified memory range with a repeating pattern.These commands should not be confused with the ~F (Freeze Thread) command.
ms.assetid: 9ef4eb88-dc6f-4f0f-ac01-a6b0bb42b33e
keywords: ["f, fp (Fill Memory) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- f, fp (Fill Memory)
api_type:
- NA
---

# f, fp (Fill Memory)


The **f** and **fp** commands fill the specified memory range with a repeating pattern.

These commands should not be confused with the [**~F (Freeze Thread)**](-f--freeze-thread-.md) command.

```
f Range Pattern 
fp [MemoryType] PhysicalRange Pattern
```

## <span id="ddk_cmd_fill_memory_dbg"></span><span id="DDK_CMD_FILL_MEMORY_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the range in virtual memory to fill. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______PhysicalRange______"></span><span id="_______physicalrange______"></span><span id="_______PHYSICALRANGE______"></span> *PhysicalRange*   
(Kernel mode only) Specifies the range in physical memory to fill. The syntax of *PhysicalRange* is the same as that of a virtual memory range, except that no symbol names are permitted.

<span id="_______MemoryType______"></span><span id="_______memorytype______"></span><span id="_______MEMORYTYPE______"></span> *MemoryType*   
(Kernel mode only) Specifies the type of physical memory, which can be one of the following:

<span id="_c_"></span><span id="_C_"></span>**\[c\]**  
Cached memory.

<span id="_uc_"></span><span id="_UC_"></span>**\[uc\]**  
Uncached memory.

<span id="_wc_"></span><span id="_WC_"></span>**\[wc\]**  
Write-combined memory.

<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Specifies one or more byte values with which to fill memory.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p></p>
<strong>f:</strong> user mode, kernel mode
<strong>fp:</strong> kernel mode only</td>
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

This command fills the memory area specified by *range* with the specified *pattern*, repeated as many times as necessary.

The *pattern* parameter must be input as a series of bytes. These can be entered as numeric or as ASCII characters.

Numeric values will be interpreted as numbers in the current radix (16, 10, or 8). To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command. The default radix can be overridden by specifying the **0x** prefix (hexadecimal), the **0n** prefix (decimal), the **0t** prefix (octal), or the **0y** prefix (binary).

**Note**   The default radix behaves differently when C++ expressions are being used. For more information, see the [Evaluating Expressions](evaluating-expressions.md) topic.

 

If ASCII characters are used, each character must be enclosed in single straight quotation marks. C-style escape characters (such as '\\0' or '\\n') may not be used.

If multiple bytes are specified, they must be separated by spaces.

If *pattern* has more values than the number of bytes in the range, the debugger ignores the extra values.

Here are some examples. Assuming the current radix is 16, the following command will fill memory locations 0012FF40 through 0012FF5F with the pattern "ABC", repeated several times:

```
0:000> f 0012ff40 L20 'A' 'B' 'C'
```

The following command has the exact same effect:

```
0:000> f 0012ff40 L20 41 42 43
```

The following examples show how you can use the physical memory types (**c**, **uc**, and **wc**) with the **fp** command in kernel mode:

```
kd> fp [c] 0012ff40 L20 'A' 'B' 'C'
```

```
kd> fp [uc] 0012ff40 L20 'A' 'B' 'C'
```

```
kd> fp [wc] 0012ff40 L20 'A' 'B' 'C'
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20f,%20fp%20%28Fill%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




