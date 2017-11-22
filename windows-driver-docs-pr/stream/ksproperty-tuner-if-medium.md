---
title: KSPROPERTY\_TUNER\_IF\_MEDIUM
description: KSPROPERTY\_TUNER\_IF\_MEDIUM describes the medium for the intermediate frequency pin for devices that support digital TV tuning. This property is optional.
MS-HAID:
- 'vidcapprop\_3e9195da-3c4b-469f-bc62-1a37252ef717.xml'
- 'stream.ksproperty\_tuner\_if\_medium'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1144777c-e81c-4b8f-a634-411591c71356
keywords: ["KSPROPERTY_TUNER_IF_MEDIUM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_IF_MEDIUM
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_TUNER\_IF\_MEDIUM


KSPROPERTY\_TUNER\_IF\_MEDIUM describes the medium for the intermediate frequency pin for devices that support digital TV tuning. This property is optional.

## <span id="ddk_ksproperty_tuner_if_medium_ks"></span><span id="DDK_KSPROPERTY_TUNER_IF_MEDIUM_KS"></span>


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
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_TUNER_IF_MEDIUM_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565848)</p></td>
<td><p>[<strong>KSPIN_MEDIUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563538)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPIN\_MEDIUM structure that specifies the Medium GUID for the pin that is capable of supporting tuning to an intermediate frequency.

Remarks
-------

The **IFMedium** member of the KSPROPERTY\_TUNER\_IF\_MEDIUM\_S structure specifies the Medium GUID of the intermediate frequency pin.

If the video capture minidriver supports KSPROPERTY\_TUNER\_IF\_MEDIUM, then *kstvtune.ax* creates an additional pin that represents the hardware-based MPEG-2 transport stream originating at the tuner. This pin is used solely to define graph topology. Data samples flowing through the user-mode stream from this pin on *kstvtune.ax* consist of [**KS\_TVTUNER\_CHANGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567691) structures.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_TUNER\_IF\_MEDIUM\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565848)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_TUNER_IF_MEDIUM%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





