---
title: KSPROPERTY\_AUDIO\_EQ\_BANDS
description: The KSPROPERTY\_AUDIO\_EQ\_BANDS property specifies the set of frequency bands from an equalization table. This is a get-only property of a channel in an EQ node (KSNODETYPE\_EQUALIZER).
ms.assetid: 64304cad-cf07-4bdb-96d5-7dd594380725
keywords: ["KSPROPERTY_AUDIO_EQ_BANDS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_EQ_BANDS
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

# KSPROPERTY\_AUDIO\_EQ\_BANDS


The KSPROPERTY\_AUDIO\_EQ\_BANDS property specifies the set of frequency bands from an equalization table. This is a get-only property of a channel in an EQ node ([**KSNODETYPE\_EQUALIZER**](ksnodetype-equalizer.md)).

## <span id="ddk_ksproperty_audio_eq_bands_ks"></span><span id="DDK_KSPROPERTY_AUDIO_EQ_BANDS_KS"></span>


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
<td align="left"><p>[<strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537145)</p></td>
<td align="left"><p>ULONG array</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is an array of ULONG elements:

```
  ULONG  CenterFreqVal[N];
```

If the channel's equalization table contains entries for N frequency bands, the array contains N elements and each array element specifies the center frequency of the corresponding band. The miniport driver writes into each element an integer frequency value that is expressed in hertz (Hz). The assignment of equalization bands to array elements is shown in the following table.

Array Element
Description
CenterFreqVal\[0\]

The center frequency (in Hz) for equalization band 0.

CenterFreqVal\[1\]

The center frequency (in Hz) for equalization band 1.

...

CenterFreqVal\[N-1\]

The center frequency (in Hz) for equalization band N-1.

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_EQ\_BANDS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The number of equalization bands can be determined by first submitting a [**KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS**](ksproperty-audio-num-eq-bands.md) request.

The equalization levels for the frequency bands are specified by the [**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md) property.

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


[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145)

[**KSNODETYPE\_EQUALIZER**](ksnodetype-equalizer.md)

[**KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS**](ksproperty-audio-num-eq-bands.md)

[**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_EQ_BANDS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





