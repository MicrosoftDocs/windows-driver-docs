---
title: KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY
description: Clients use KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY to inform the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the low-noise block (LNB) device to switch from using low-band local oscillator frequency (LOF) to using high-band LOF or vice versa when the LNB shifts the frequency of RF signals.
ms.assetid: a448bad1-40dc-4596-bc18-9522144e33a7
keywords: ["KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY


Clients use KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY to inform the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the low-noise block (LNB) device to switch from using low-band local oscillator frequency (LOF) to using high-band LOF or vice versa when the LNB shifts the frequency of RF signals.

## <span id="ddk_ksproperty_bda_lnb_switch_frequency_ks"></span><span id="DDK_KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY_KS"></span>


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
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the RF tuner node.

The property value specifies the frequency of incoming RF signals at which the LNB should switch from using low-band LOF to using high-band LOF.

If a client sends a KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY request to tune an RF tuner to a specific frequency and this frequency is greater than or equal to the switch frequency specified using KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY, then the RF tuner should send a command to the LNB to switch to the high-band LOF. The RF tuner should then expect that the LNB device shifts the frequency of the incoming RF signal by the high-band LOF amount, which was specified using KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND.

Likewise, if a client sends a KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY request to tune an RF tuner to a specific frequency and this frequency is less than the switch frequency, then the RF tuner should send a command to the LNB to switch to the low-band LOF. The RF tuner should then expect that the LNB device shifts the frequency of the incoming RF signal by the low-band LOF amount, which was specified using KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

[**KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND**](ksproperty-bda-lnb-lof-high-band.md)

[**KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND**](ksproperty-bda-lnb-lof-low-band.md)

[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





