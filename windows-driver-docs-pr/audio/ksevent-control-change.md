---
title: KSEVENT\_CONTROL\_CHANGE
description: The KSEVENT\_CONTROL\_CHANGE event indicates that a change in control value has occurred at a node that represents a hardware volume-control knob, mute switch, or other type of manual control.Usage Summary TableTargetEvent Descriptor TypeEvent Value TypePinKSE\_NODEKSEVENTDATA The event value type (operation data) is a KSEVENTDATA structure that specifies the type of notification to use for an event.
ms.assetid: 32d8e14c-f21d-4bac-8d98-8aca40e30b60
keywords: ["KSEVENT_CONTROL_CHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CONTROL_CHANGE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSEVENT\_CONTROL\_CHANGE


The KSEVENT\_CONTROL\_CHANGE event indicates that a change in control value has occurred at a node that represents a hardware volume-control knob, mute switch, or other type of manual control.

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
<td align="left"><p>[<strong>KSE_NODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561937)</p></td>
<td align="left"><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a KSEVENTDATA structure that specifies the type of notification to use for an event.

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


[**KSE\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff561937)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

[**PCEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537692)

[**PCEVENT\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537693)

[IPortEvents](https://msdn.microsoft.com/library/windows/hardware/ff536884)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSEVENT_CONTROL_CHANGE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





