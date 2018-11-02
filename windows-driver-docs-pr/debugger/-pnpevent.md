---
title: pnpevent
description: The pnpevent extension displays the Plug and Play device event queue.
ms.assetid: 5f70fbf8-1313-4238-a917-c3fba8c80927
keywords: ["pnpevent Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pnpevent
api_type:
- NA
ms.localizationpriority: medium
---

# !pnpevent


The **!pnpevent** extension displays the Plug and Play device event queue.

```dbgcmd
!pnpevent [DeviceEvent]
```

## <span id="ddk__pnpevent_dbg"></span><span id="DDK__PNPEVENT_DBG"></span>Parameters


<span id="_______DeviceEvent______"></span><span id="_______deviceevent______"></span><span id="_______DEVICEEVENT______"></span> *DeviceEvent*   
Specifies the address of a device event to display. If this is zero or omitted, the tree of all device events in the queue is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about Plug and Play drivers, see the Windows Driver Kit (WDK) documentation.

## <span id="see_also"></span>See also


[Plug and Play and Power Debugger Commands](plug-and-play-and-power-debugger-commands.md)

 

 






