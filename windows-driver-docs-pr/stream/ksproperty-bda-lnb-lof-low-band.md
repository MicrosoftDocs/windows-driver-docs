---
title: KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND
description: Clients use KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming low-band RF signals.
MS-HAID:
- 'bdaref\_947d9fbf-a01e-4ac3-8cb7-8c40b95cc93b.xml'
- 'stream.ksproperty\_bda\_lnb\_lof\_low\_band'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 96880a70-5c3f-4391-a613-a6a90d1605b4
keywords: ["KSPROPERTY_BDA_LNB_LOF_LOW_BAND Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_LNB_LOF_LOW_BAND
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND


Clients use KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming low-band RF signals.

## <span id="ddk_ksproperty_bda_lnb_lof_low_band_ks"></span><span id="DDK_KSPROPERTY_BDA_LNB_LOF_LOW_BAND_KS"></span>


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

The property value specifies the LOF that is used by the LNB for low-band signals.

The LNB gathers the RF signal reflected by the satellite dish, shifts the frequency of the RF signal down by the low-band LOF amount, and sends the resulting signal to the RF tuner.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_BDA_LNB_LOF_LOW_BAND%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





