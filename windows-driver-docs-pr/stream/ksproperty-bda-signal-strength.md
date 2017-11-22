---
title: KSPROPERTY\_BDA\_SIGNAL\_STRENGTH
description: Clients use KSPROPERTY\_BDA\_SIGNAL\_STRENGTH to determine the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).
MS-HAID:
- 'bdaref\_429d1529-9bc3-461f-87d7-d6a32974a954.xml'
- 'stream.ksproperty\_bda\_signal\_strength'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b8b71135-cc0b-4a59-940a-dd766cab3305
keywords: ["KSPROPERTY_BDA_SIGNAL_STRENGTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_STRENGTH
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_BDA\_SIGNAL\_STRENGTH


Clients use KSPROPERTY\_BDA\_SIGNAL\_STRENGTH to determine the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).

## <span id="ddk_ksproperty_bda_signal_strength_ks"></span><span id="DDK_KSPROPERTY_BDA_SIGNAL_STRENGTH_KS"></span>


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
<td><p>Pin or Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value specifies the carrier strength of the signal in mDb.

A strength of 0 is nominal strength as expected for the given type of broadcast network. Subnominal strengths are reported as positive mDb. Super-nominal strengths are reported as negative mDb.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_BDA_SIGNAL_STRENGTH%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





