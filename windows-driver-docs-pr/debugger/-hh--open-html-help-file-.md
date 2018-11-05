---
title: .hh (Open HTML Help File)
description: The .hh command opens the Debugging Tools for Windows documentation.
ms.assetid: 6c6d5b33-ad54-4325-93d7-ed63f9f012e8
keywords: [".hh (Open HTML Help File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .hh (Open HTML Help File)
api_type:
- NA
ms.localizationpriority: medium
---

# .hh (Open HTML Help File)


The **.hh** command opens the Debugging Tools for Windows documentation.

```dbgcmd
.hh [Text] 
```

## <span id="ddk_meta_open_html_help_file_dbg"></span><span id="DDK_META_OPEN_HTML_HELP_FILE_DBG"></span>Parameters


<span id="_______Text______"></span><span id="_______text______"></span><span id="_______TEXT______"></span> *Text*   
Specifies the text to find in the index of the Help documentation.

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

 

You cannot use this command when you are performing [remote debugging through Remote.exe](remote-debugging-through-remote-exe.md).

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the Help documentation, see [Using the Help File](using-the-help-documentation.md).

Remarks
-------

The **.hh** command opens the Debugging Tools for Windows documentation (Debugger.chm). If you specify *Text*, the debugger opens the **Index** pane in the documentation and searches for *Text* as a keyword in the index. If you do not specify *Text*, the debugger opens the **Contents** pane of the documentation.

 

 





