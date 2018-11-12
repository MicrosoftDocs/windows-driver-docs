---
title: .pagein (Page In Memory)
description: The .pagein command pages in the specified region of memory.
ms.assetid: 5fb8f9d2-d07a-49c3-b844-aade9bdba367
keywords: ["Page In Memory (.pagein) command", "memory, Page In Memory (.pagein) command", ".pagein (Page In Memory) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .pagein (Page In Memory)
api_type:
- NA
ms.localizationpriority: medium
---

# .pagein (Page In Memory)


The **.pagein** command pages in the specified region of memory.

```dbgcmd
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

 

 





