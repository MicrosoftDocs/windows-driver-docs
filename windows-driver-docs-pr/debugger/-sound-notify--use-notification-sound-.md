---
title: .sound_notify (Use Notification Sound)
description: The .sound_notify command causes a sound to be played when WinDbg enters the wait-for-command state.
ms.assetid: 72ef33ea-1c75-4add-80eb-a0d824571948
keywords: [".sound_notify (Use Notification Sound) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .sound_notify (Use Notification Sound)
api_type:
- NA
ms.localizationpriority: medium
---

# .sound\_notify (Use Notification Sound)


The **.sound\_notify** command causes a sound to be played when WinDbg enters the wait-for-command state.

```dbgcmd
.sound_notify /ed 
.sound_notify /ef File 
.sound_notify /d 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________ed______"></span><span id="________ED______"></span> **/ed**   
Causes the default Windows alert sound to be played when WinDbg enters the wait-for-command state.

<span id="________ef_______File______"></span><span id="________ef_______file______"></span><span id="________EF_______FILE______"></span> **/ef** **** *File*   
Causes the sound contained in the specified file to be played when WinDbg enters the wait-for-command state.

<span id="________d"></span><span id="________D"></span> **/d**  
Disables the playing of sounds.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is available only in WinDbg and cannot be used in script files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

 

 





