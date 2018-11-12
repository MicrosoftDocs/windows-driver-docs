---
title: envvar
description: The envvar extension displays the value of the specified environment variable.
ms.assetid: 7a6e1796-08e0-414e-a092-326b30c8ce8f
keywords: ["envvar Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- envvar
api_type:
- NA
ms.localizationpriority: medium
---

# !envvar


The **!envvar** extension displays the value of the specified environment variable.

```dbgcmd
!envvar Variable
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Variable______"></span><span id="_______variable______"></span><span id="_______VARIABLE______"></span> *Variable*   
Specifies the environment variable whose value is displayed. *Variable* is not case sensitive.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about environment variables, see [Environment Variables](environment-variables.md) and the Microsoft Windows SDK documentation.

Remarks
-------

The **!envvar** extension works both in user mode and in kernel mode. However, in kernel mode, when you set the idle thread as the current process, the pointer to the Process Environment Block (PEB) is **NULL**, so it fails. In kernel mode, the **!envvar** extension displays the environment variables on the target computer, as the following example shows.

```dbgcmd
0:000> !envvar _nt_symbol_path
        _nt_symbol_path = srv*C:\mysyms*https://msdl.microsoft.com/download/symbols
```

 

 





