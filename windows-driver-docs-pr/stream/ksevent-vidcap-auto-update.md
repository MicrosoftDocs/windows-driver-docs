---
title: KSEVENT\_VIDCAP\_AUTO\_UPDATE
description: The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a property value changes.
ms.assetid: dd7e665f-104d-4276-94aa-62d64faba69d
keywords: ["KSEVENT_VIDCAP_AUTO_UPDATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDCAP_AUTO_UPDATE
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENT\_VIDCAP\_AUTO\_UPDATE


The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a property value changes.

## <span id="ddk_ksevent_vidcap_auto_update_ks"></span><span id="DDK_KSEVENT_VIDCAP_AUTO_UPDATE_KS"></span>


### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Clients might register for this event to be notified if a user flips a switch on the device, changing a property value. For this event to be available, the hardware implementation must provide support for this feature.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENT_VIDCAP_AUTO_UPDATE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




