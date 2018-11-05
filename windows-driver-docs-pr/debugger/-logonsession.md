---
title: logonsession
description: The logonsession extension displays information about a specified logon session.
ms.assetid: 95746bc0-ab36-43a7-83ad-9f6fdbb15b39
keywords: ["logon session", "logonsession Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- logonsession
api_type:
- NA
ms.localizationpriority: medium
---

# !logonsession


The **!logonsession** extension displays information about a specified logon session.

Free Build Syntax

```dbgcmd
!logonsession LUID
```

Checked Build Syntax

```dbgcmd
!logonsession LUID [InfoLevel]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______LUID______"></span><span id="_______luid______"></span> *LUID*   
Specifies the locally unique identifier (LUID) of a logon session to display. If *LUID*is 0, information about all logon sessions is displayed.

To display information about the system session and all system tokens in a checked build, enter **!logonsession 3e7 1**.

<span id="_______InfoLevel______"></span><span id="_______infolevel______"></span><span id="_______INFOLEVEL______"></span> *InfoLevel*   
(Checked Build Only) Specifies how much token information is displayed. The *InfoLevel* parameter can take values from 0 to 4, with 0 representing the least information and 4 representing the most information.

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about logon sessions, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Here is an example of the output from this extension on a free build:

```dbgcmd
kd> !logonsession 0

Dumping all logon sessions.

** Session   0 = 0x0
   LogonId     = {0x0 0x0}
   References  = 0
** Session   1 = 0x8ebb50
 LogonId     = {0xe9f1 0x0}
   References  = 21
** Session   2 = 0x6e31e0
   LogonId     = {0x94d1 0x0}
   References  = 1
** Session   3 = 0x8ecd60
   LogonId     = {0x6b31 0x0}
   References  = 0
** Session   4 = 0xe0000106
   LogonId     = {0x0 0x0}
   References  = 0
** Session   5 = 0x0
   LogonId     = {0x0 0x0}
   References  = 0
** Session   6 = 0x8e9720
   LogonId     = {0x3e4 0x0}
   References  = 6
** Session   7 = 0xe0000106
   LogonId     = {0x0 0x0}
   References  = 0
** Session   8 = 0xa2e160
   LogonId     = {0x3e5 0x0}
   References  = 3
** Session   9 = 0xe0000106
   LogonId     = {0x0 0x0}
   References  = 0
** Session  10 = 0x3ca0
   LogonId     = {0x3e6 0x0}
   References  = 2
** Session  11 = 0xe0000106
   LogonId     = {0x0 0x0}
   References  = 0
** Session  12 = 0x1cd0
   LogonId     = {0x3e7 0x0}
   References  = 33
** Session  13 = 0xe0000106
 LogonId     = {0x0 0x0}
 References  = 0
14 sessions in the system.
```

You can stop execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





