---
title: .exr (Display Exception Record)
description: The .exr command displays the contents of an exception record.
ms.assetid: 786d7ee0-45d7-489c-b53b-28349ea10e36
keywords: ["Display Exception Record (.exr) command", "exception record", ".exr (Display Exception Record) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .exr (Display Exception Record)
api_type:
- NA
ms.localizationpriority: medium
---

# .exr (Display Exception Record)


The **.exr** command displays the contents of an exception record.

```dbgcmd
.exr Address 
.exr -1
```

## <span id="ddk_meta_display_exception_record_dbg"></span><span id="DDK_META_DISPLAY_EXCEPTION_RECORD_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the exception record. If you specify **-1** as the address, the debugger displays the most recent exception.

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

The **.exr** command displays information that is related to an exception that the debugger encountered on the target computer. The information that is displayed includes the exception address, the exception code, the exception flags, and a variable list of parameters to the exception.

You can usually obtain the *Address* by using the [**!pcr**](-pcr.md) extension.

The **.exr** command is often used to debug bug check 0x1E. For more information and an example, see [**Bug Check 0x1E**](bug-check-0x1e--kmode-exception-not-handled.md) (KMODE\_EXCEPTION\_NOT\_HANDLED).

 

 





