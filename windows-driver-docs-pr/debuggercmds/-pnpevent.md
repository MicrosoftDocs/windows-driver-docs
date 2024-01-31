---
title: pnpevent (WinDbg)
description: The pnpevent extension displays the Plug and Play device event queue.
keywords: ["pnpevent Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pnpevent
api_type:
- NA
---

# !pnpevent


The **!pnpevent** extension displays the Plug and Play device event queue.

```dbgcmd
!pnpevent [DeviceEvent]
```

## <span id="ddk__pnpevent_dbg"></span><span id="DDK__PNPEVENT_DBG"></span>Parameters


<span id="_______DeviceEvent______"></span><span id="_______deviceevent______"></span><span id="_______DEVICEEVENT______"></span> *DeviceEvent*   
Specifies the address of a device event to display. If this is zero or omitted, the tree of all device events in the queue is displayed.

## DLL

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

 

### Additional Information

See [Plug and Play Debugging](../debugger/plug-and-play-debugging.md) for applications of this extension command. For information about Plug and Play drivers, see the Windows Driver Kit (WDK) documentation.

## <span id="see_also"></span>See also


[Plug and Play and Power Debugger Commands](../debugger/plug-and-play-and-power-debugger-commands.md)

 

 






