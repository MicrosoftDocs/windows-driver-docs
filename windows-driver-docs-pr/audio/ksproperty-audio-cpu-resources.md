---
title: KSPROPERTY\_AUDIO\_CPU\_RESOURCES
description: The KSPROPERTY\_AUDIO\_CPU\_RESOURCES property specifies whether a node's functionality is implemented in hardware or is emulated in software that runs on the host CPU.
ms.assetid: 4379aa05-9661-44cd-8f10-0fb37009a4f3
keywords: ["KSPROPERTY_AUDIO_CPU_RESOURCES Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_CPU_RESOURCES
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

# KSPROPERTY\_AUDIO\_CPU\_RESOURCES


The KSPROPERTY\_AUDIO\_CPU\_RESOURCES property specifies whether a node's functionality is implemented in hardware or is emulated in software that runs on the host CPU.

## <span id="ddk_ksproperty_audio_cpu_resources_ks"></span><span id="DDK_KSPROPERTY_AUDIO_CPU_RESOURCES_KS"></span>


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
<td align="left"><p>[<strong>KSNODEPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537143)</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and indicates whether the node's functionality is implemented in hardware or software. The miniport driver sets this value to one of the following two constants from header file Ksmedia.h:

<span id="KSAUDIO_CPU_RESOURCES_HOST_CPU"></span><span id="ksaudio_cpu_resources_host_cpu"></span>KSAUDIO\_CPU\_RESOURCES\_HOST\_CPU  
This node implements its functionality in software that runs on the host CPU.

<span id="KSAUDIO_CPU_RESOURCES_NOT_HOST_CPU"></span><span id="ksaudio_cpu_resources_not_host_cpu"></span>KSAUDIO\_CPU\_RESOURCES\_NOT\_HOST\_CPU  
This node implements its functionality in hardware.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_CPU\_RESOURCES property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This property is used to determine whether the following node types are implemented in hardware or software:

-   AEC node ([**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md))

-   Noise-suppression node ([**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md))

-   Peakmeter node ([**KSNODETYPE\_PEAKMETER**](ksnodetype-peakmeter.md))

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


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)

[**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)

[**KSNODETYPE\_PEAKMETER**](ksnodetype-peakmeter.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_CPU_RESOURCES%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





