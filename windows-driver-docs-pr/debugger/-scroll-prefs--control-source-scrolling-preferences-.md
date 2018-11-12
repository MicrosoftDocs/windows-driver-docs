---
title: .scroll_prefs (Control Source Scrolling Preferences)
description: The .scroll_prefs command controls the positioning of the source in a Source window when scrolling to a line.
ms.assetid: 08978751-c4b7-491a-9e1f-de21d74a10a8
keywords: [".scroll_prefs (Control Source Scrolling Preferences) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .scroll_prefs (Control Source Scrolling Preferences)
api_type:
- NA
ms.localizationpriority: medium
---

# .scroll\_prefs (Control Source Scrolling Preferences)


The **.scroll\_prefs** command controls the positioning of the source in a Source window when scrolling to a line.

```dbgcmd
.scroll_prefs Before After 
.scroll_prefs 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Before______"></span><span id="_______before______"></span><span id="_______BEFORE______"></span> *Before*   
Specifies how many source lines before the line you are scrolling to should be visible in the Source window.

<span id="_______After______"></span><span id="_______after______"></span><span id="_______AFTER______"></span> *After*   
Specifies how many source lines after the line you are scrolling to should be visible in the Source window.

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
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When this command is used with no parameters, the current source scrolling preferences are displayed.

 

 





