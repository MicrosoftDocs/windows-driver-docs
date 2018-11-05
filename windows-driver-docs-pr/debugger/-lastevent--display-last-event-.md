---
title: .lastevent (Display Last Event)
description: The .lastevent command displays the most recent exception or event that occurred.
ms.assetid: 6f722c22-cb0f-4a10-b719-a168f7ba0943
keywords: [".lastevent (Display Last Event) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .lastevent (Display Last Event)
api_type:
- NA
ms.localizationpriority: medium
---

# .lastevent (Display Last Event)


The **.lastevent** command displays the most recent exception or event that occurred.

```dbgcmd
.lastevent 
```

## <span id="ddk_meta_display_last_event_dbg"></span><span id="DDK_META_DISPLAY_LAST_EVENT_DBG"></span>


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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about exceptions and events, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

Remarks
-------

Breaking into the debugger always creates an exception. There is always a *last event* when the debugger accepted command input. If you break into the debugger by using [**CTRL+C**](ctrl-c--break-.md), [CTRL+BREAK](debug---break.md), or Debug | Break, an exception code of 0x80000003 is created.

 

 





