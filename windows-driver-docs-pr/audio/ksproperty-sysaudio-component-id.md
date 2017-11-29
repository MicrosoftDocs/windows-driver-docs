---
title: KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID
description: The KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID property retrieves the component ID from the wave-rendering device that the specified virtual audio device uses.
ms.assetid: ef4a940f-dfef-43ed-8895-d318fb603e5c
keywords: ["KSPROPERTY_SYSAUDIO_COMPONENT_ID Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_COMPONENT_ID
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

# KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID


The KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID property retrieves the component ID from the wave-rendering device that the specified virtual audio device uses.

## <span id="ddk_ksproperty_sysaudio_component_id_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_COMPONENT_ID_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)+ULONG</p></td>
<td align="left"><p>[<strong>KSCOMPONENTID</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561027)</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a structure of type KSPROPERTY followed by a ULONG variable containing a device ID that identifies a virtual audio device. If SysAudio enumerates *n* virtual audio devices (see [**KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT**](ksproperty-sysaudio-device-count.md)), then valid device IDs range from 0 to *n*-1.

The property value (operation data) is a structure of type KSCOMPONENTID that specifies the manufacturer, product, and other hardware-specific information about the wave-rendering device that is used by the specified virtual audio device.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

DirectSound does not communicate directly with the miniport driver for the audio hardware that underlies each of SysAudio's virtual audio devices. Thus, DirectSound is unable to query the wave-rendering device directly for its component-ID information. The KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID property provides a means for DirectSound to obtain this information indirectly through SysAudio.

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


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSCOMPONENTID**](https://msdn.microsoft.com/library/windows/hardware/ff561027)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT**](ksproperty-sysaudio-device-count.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_SYSAUDIO_COMPONENT_ID%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





