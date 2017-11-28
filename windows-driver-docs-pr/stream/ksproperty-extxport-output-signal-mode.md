---
title: KSPROPERTY\_EXTXPORT\_OUTPUT\_SIGNAL\_MODE
description: The KSPROPERTY\_EXTXPORT\_OUTPUT\_SIGNAL\_MODE property sets or gets an external device's output signal mode. For example DV-SD/NTSC/PAL, DV-SL/NTSC/PAL, MPEG2-TS, etc.
ms.assetid: 9cd1bf2a-c241-491a-af22-5cf7b654169d
keywords: ["KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE
api_location:
- ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_EXTXPORT\_OUTPUT\_SIGNAL\_MODE


The KSPROPERTY\_EXTXPORT\_OUTPUT\_SIGNAL\_MODE property sets or gets an external device's output signal mode. For example DV-SD/NTSC/PAL, DV-SL/NTSC/PAL, MPEG2-TS, etc.

## <span id="ddk_ksproperty_extxport_output_signal_mode_ks"></span><span id="DDK_KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Device</p></td>
<td><p>[<strong>KSPROPERTY_EXTXPORT_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565167)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the current output signal mode of the external transport.

Remarks
-------

The **SignalMode** member of the KSPROPERTY\_EXTXPORT\_S structure specifies the output signal mode.

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

[**KSPROPERTY\_EXTXPORT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565167)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





