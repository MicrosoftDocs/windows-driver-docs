---
title: KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID
description: The KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID property is used to inform a GFX filter of the Plug and Play device ID of the audio device that is the source of the capture stream.
ms.assetid: df4505c5-f9ff-4f8a-8521-90031c0b23e4
keywords: ["KSPROPERTY_AUDIOGFX_CAPTURETARGETDEVICEID Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOGFX_CAPTURETARGETDEVICEID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID


The KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID property is used to inform a GFX filter of the Plug and Play device ID of the audio device that is the source of the capture stream.

## <span id="ddk_ksproperty_audiogfx_capturetargetdeviceid_ks"></span><span id="DDK_KSPROPERTY_AUDIOGFX_CAPTURETARGETDEVICEID_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>WCHAR array</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a WCHAR array that contains the device ID. The device ID is a null-terminated string of Unicode characters.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The target for this set-only property request is a GFX filter that is configured for use as either a capture- or render/capture-GFX filter.

To determine the size of the buffer needed to hold the property value, see [Basic Support Queries for Audio Properties](https://msdn.microsoft.com/library/windows/hardware/ff536225).

For additional information about GFX filters and device IDs, see [GFX Filters](https://msdn.microsoft.com/library/windows/hardware/ff536403) and [Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIOGFX_CAPTURETARGETDEVICEID%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





