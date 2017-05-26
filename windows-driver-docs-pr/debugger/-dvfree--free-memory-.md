---
title: .dvfree (Free Memory)
description: The .dvfree command frees a memory allocation owned by the target process.
ms.assetid: 46845a5c-6ec4-4ae4-b89d-886df367dc5e
keywords: [".dvfree (Free Memory) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .dvfree (Free Memory)
api_type:
- NA
---

# .dvfree (Free Memory)


The **.dvfree** command frees a memory allocation owned by the target process.

``` syntax
    .dvfree [/d] BaseAddress Size 
```

## <span id="ddk_meta_free_memory_dbg"></span><span id="DDK_META_FREE_MEMORY_DBG"></span>Parameters


<span id="________d______"></span><span id="________D______"></span> **/d**   
Decommits the allocation, but does not actually release the pages containing the allocation. If this option is used, the debugger calls **VirtualFreeEx** with the *dwFreeType* parameter equal to MEM\_DECOMMIT. If this option is not used, the value MEM\_RELEASE is used. See the Microsoft Windows SDK for details.

<span id="_______BaseAddress______"></span><span id="_______baseaddress______"></span><span id="_______BASEADDRESS______"></span> *BaseAddress*   
Specifies the virtual address of the beginning of the allocation.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Specifies the amount of memory to be freed, in bytes. The actual memory freed will always be a whole number of memory pages.

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

The **.dvfree** command calls **VirtualFreeEx** to free an existing memory allocation. Unless the **/d** option is specified, the pages containing this memory are released.

This command can be used to free an allocation made by [**.dvalloc (Allocate Memory)**](-dvalloc--allocate-memory-.md). It can also be used to free any block of memory owned by the target process, but freeing memory that was not acquired through **.dvalloc** will naturally pose risks to the stability of the target process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.dvfree%20%28Free%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




