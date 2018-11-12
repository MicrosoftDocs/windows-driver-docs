---
title: kuser
description: The kuser extension displays the shared user-mode page (KUSER_SHARED_DATA).
ms.assetid: 352a2f96-ff66-41be-94ee-045edbb1f81f
keywords: ["kuser Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- kuser
api_type:
- NA
ms.localizationpriority: medium
---

# !kuser


The **!kuser** extension displays the shared user-mode page (KUSER\_SHARED\_DATA).

```dbgcmd
!kuser 
```

## <span id="ddk__kuser_dbg"></span><span id="DDK__KUSER_DBG"></span>


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
Kdextx86.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The KUSER\_SHARED\_DATA page gives resource and other information about the user who is currently logged on.

Here is an example. Note that, in this example, the tick count is displayed in both its raw form and in a more user-friendly form, which is in parentheses. The user-friendly display is available only in Windows XP and later.

```dbgcmd
kd> !kuser
_KUSER_SHARED_DATA at 7ffe0000
TickCount:    fa00000 * 00482006 (0:20:30:56.093)
TimeZone Id: 2
ImageNumber Range: [14c .. 14c]
Crypto Exponent: 0
SystemRoot: 'F:\WINDOWS'
```

 

 





