---
title: .dvalloc (Allocate Memory)
description: The .dvalloc command causes Windows to allocate additional memory to the target process.
ms.assetid: 5bb0660e-0c88-4100-91ae-cd89834174f6
keywords: [".dvalloc (Allocate Memory) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .dvalloc (Allocate Memory)
api_type:
- NA
---

# .dvalloc (Allocate Memory)


The **.dvalloc** command causes Windows to allocate additional memory to the target process.

```
.dvalloc [Options] Size 
```

## <span id="ddk_meta_allocate_memory_dbg"></span><span id="DDK_META_ALLOCATE_MEMORY_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any number of the following options:

<span id="_b_BaseAddress"></span><span id="_b_baseaddress"></span><span id="_B_BASEADDRESS"></span>**/b** **** *BaseAddress*  
Specifies the virtual address of the beginning of the allocation.

<span id="_r"></span><span id="_R"></span>**/r**  
Reserves the memory in the virtual address space but does not actually allocate any physical memory. If this option is used, the debugger calls **VirtualAllocEx** with the *flAllocationType* parameter equal to MEM\_RESERVE. If this option is not used, the value MEM\_COMMIT | MEM\_RESERVE is used. See the Microsoft Windows SDK for details.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Specifies the amount of memory to be allocated, in bytes. The amount of memory available to the program will equal *Size*. The amount of memory actually used may be slightly larger, since it is always a whole number of pages.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.dvalloc** command calls **VirtualAllocEx** to allocate new memory for the target process. The allocated memory permits reading, writing, and execution.

To free this memory, use [**.dvfree (Free Memory)**](-dvfree--free-memory-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.dvalloc%20%28Allocate%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




