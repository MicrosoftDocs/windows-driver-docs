---
title: .pagein (Page In Memory)
description: The .pagein command pages in the specified region of memory.
ms.assetid: 5fb8f9d2-d07a-49c3-b844-aade9bdba367
keywords: ["Page In Memory (.pagein) command", "memory, Page In Memory (.pagein) command", ".pagein (Page In Memory) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .pagein (Page In Memory)
api_type:
- NA
---

# .pagein (Page In Memory)


The **.pagein** command pages in the specified region of memory.

```
.pagein [Options] Address
```

## <span id="ddk_meta_page_in_memory_dbg"></span><span id="DDK_META_PAGE_IN_MEMORY_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any of the following options:

<span id="_p_Process"></span><span id="_p_process"></span><span id="_P_PROCESS"></span>**/p** **** *Process*  
Specifies the address of the process that owns the memory that you want to page in. (More precisely, this parameter specifies the address of the EPROCESS block for the process.) If you omit *Process* or specify zero, the debugger uses the current process setting. For more information about the process setting, see [**.process (Set Process Context)**](-process--set-process-context-.md)

<span id="_f"></span><span id="_F"></span>**/f**  
Forces the memory to be paged in, even if the address is in kernel memory and the version of the Microsoft Windows operating system does not support this action.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address to page in.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only (but not during local kernel debugging)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

After you run the **.pagein** command, you must use the [**g (Go)**](g--go-.md) command to resume program execution. After a brief time, the target computer automatically breaks into the debugger again.

At this point, the address that you specify is paged in. If you use the **/p** option, the process context is also set to the specified process, exactly as if you used the [**.process /i Process**](-process--set-process-context-.md) command.

If the address is already paged in, the **.pagein** command still checks that the address is paged in and then breaks back into the debugger. If the address is invalid, this command only breaks back into the debugger.

In Windows Server 2003 and Windows XP, you can page in only user-mode addresses by using **.pagein**. You can override this restriction by using the **/f** switch, but we do not recommend that you use this switch. In Windows Vista, you can safely page in user-mode and kernel-mode memory.

**Warning**   If you use **.pagein** on an address in a kernel stack in Windows Server 2003 or Windows XP, a bug check might occur.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Supported in Windows XP and later versions of Windows.</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.pagein%20%28Page%20In%20Memory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




