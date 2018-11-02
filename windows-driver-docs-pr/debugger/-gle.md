---
title: gle
description: The gle extension displays the last error value for the current thread.
ms.assetid: bed3ce17-6860-421f-ae20-11faa50310ed
keywords: ["thread, error value", "error value", "gle Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gle
api_type:
- NA
ms.localizationpriority: medium
---

# !gle


The **!gle** extension displays the last error value for the current thread.

```dbgcmd
!gle [-all]
```

## <span id="ddk__gle_dbg"></span><span id="DDK__GLE_DBG"></span>Parameters


<span id="_______-all______"></span><span id="_______-ALL______"></span> **-all**   
Displays the last error for each user-mode thread on the target system. If you omit this parameter in user mode, the debugger displays the last error for the current thread. If you omit this parameter in kernel mode, the debugger displays the last error for the thread that the current [register context](changing-contexts.md#register-context) specifies.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Ext.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) routine, see the Micorosft Windows SDK documentation.

Remarks
-------

The **!gle** extension displays the value of [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) and tries to decode this value.

In kernel mode, the **!gle** extension work only if the debugger can read the thread environment block (TEB).

 

 





