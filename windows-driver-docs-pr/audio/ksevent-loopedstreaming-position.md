---
title: KSEVENT\_LOOPEDSTREAMING\_POSITION
description: The KSEVENT\_LOOPEDSTREAMING\_POSITION event indicates that the audio stream has reached a specified position in a looped buffer.Usage Summary TableTargetEvent Descriptor TypeEvent Value TypePinKSEVENTLOOPEDSTREAMING\_POSITION\_EVENT\_DATA The event value type (operation data) is a LOOPEDSTREAMING\_POSITION\_EVENT\_DATA structure that contains the following information The type of notification that the system will send to the client when the position event occurs.The buffer position that triggers the event.
ms.assetid: 6609ddac-e506-4fab-b580-0def30be2e9c
keywords: ["KSEVENT_LOOPEDSTREAMING_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_LOOPEDSTREAMING_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENT\_LOOPEDSTREAMING\_POSITION


The KSEVENT\_LOOPEDSTREAMING\_POSITION event indicates that the audio stream has reached a specified position in a looped buffer.

**Usage Summary Table**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target</th>
<th align="left">Event Descriptor Type</th>
<th align="left">Event Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td align="left"><p>[<strong>LOOPEDSTREAMING_POSITION_EVENT_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537505)</p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a LOOPEDSTREAMING\_POSITION\_EVENT\_DATA structure that contains the following information:

-   The type of notification that the system will send to the client when the position event occurs.

-   The buffer position that triggers the event.

This event is intended only for internal use by the system.

Remarks
-------

In Windows Server 2003, Windows XP, Windows 2000, Windows Me, and Windows 98, the WavePci and WaveCyclic port drivers contain their own built-in handlers for KSEVENT\_LOOPEDSTREAMING\_POSITION events. WavePci and WaveCyclic miniport drivers should not implement handlers for these events.

In Windows Vista, none of the Wave*Xxx* port drivers implement event handlers or other support for KSEVENT\_LOOPEDSTREAMING\_POSITION events.

A looped buffer is a data buffer for an audio stream of type [**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff563381). When a play or record cursor reaches the end of a looped buffer, the cursor wraps around to the start of the buffer.

For more information about looped buffers, buffer positions, and play and record cursors, see [Audio Position Property](https://msdn.microsoft.com/library/windows/hardware/ff536211).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744)

[**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff563381)

[**LOOPEDSTREAMING\_POSITION\_EVENT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff537505)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSEVENT_LOOPEDSTREAMING_POSITION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





