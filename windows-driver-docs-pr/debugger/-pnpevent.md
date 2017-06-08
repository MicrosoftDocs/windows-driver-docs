---
title: pnpevent
description: The pnpevent extension displays the Plug and Play device event queue.
ms.assetid: 5f70fbf8-1313-4238-a917-c3fba8c80927
keywords: ["pnpevent Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- pnpevent
api_type:
- NA
---

# !pnpevent


The **!pnpevent** extension displays the Plug and Play device event queue.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!pnpevent%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





