---
title: KSEVENT\_VOLUMELIMIT\_CHANGED
description: The KSEVENT\_VOLUMELIMIT\_CHANGED event indicates to the audio stack that the audio volume level limit for the audio device has changed.
ms.assetid: CC6A6027-03CA-4D2C-8AA2-155E1617E19B
keywords: ["KSEVENT_VOLUMELIMIT_CHANGED Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VOLUMELIMIT_CHANGED
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENT\_VOLUMELIMIT\_CHANGED


The KSEVENT\_VOLUMELIMIT\_CHANGED event indicates to the audio stack that the audio volume level limit for the audio device has changed.

### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span> Usage Summary Table

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target</th>
<th align="left">Event descriptor type</th>
<th align="left">Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td align="left"><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a **KSEVENTDATA** structure that specifies the notification method to use for this event.

Remarks
-------

For information about how to implement support for the KSEVENT\_PINCAPS\_VOLUMELIMITCHANGE event, see the **Remarks** section of [**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md).

Note that while KSEVENT\_PINCAPS\_FORMATCHANGE is implemented on the Wave filter (for miniport drivers that are linked to Portcls), the KSEVENT\_VOLUMELIMIT\_CHANGED event is implemented on the Topology filter.

## <span id="see_also"></span>See also


[**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744)

[**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSEVENT_VOLUMELIMIT_CHANGED%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





