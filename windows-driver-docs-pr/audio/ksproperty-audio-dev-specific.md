---
title: KSPROPERTY\_AUDIO\_DEV\_SPECIFIC
description: The KSPROPERTY\_AUDIO\_DEV\_SPECIFIC property is used to access a device-specific property in a device-specific node (KSNODETYPE\_DEV\_SPECIFIC).
ms.assetid: f3f2e340-7403-4c86-841f-7008afda28a5
keywords: ["KSPROPERTY_AUDIO_DEV_SPECIFIC Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_DEV_SPECIFIC
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_DEV\_SPECIFIC


The `KSPROPERTY_AUDIO_DEV_SPECIFIC` property is used to access a device-specific property in a device-specific node ([**KSNODETYPE\_DEV\_SPECIFIC**](ksnodetype-dev-specific.md)).

## <span id="ddk_ksproperty_audio_dev_specific_ks"></span><span id="DDK_KSPROPERTY_AUDIO_DEV_SPECIFIC_KS"></span>


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
<td align="left"><p>&lt;device-specific&gt;</p></td>
<td align="left"><p>&lt;device-specific&gt;</p></td>
<td align="left"><p>&lt;device-specific&gt;</p></td>
<td align="left"><p>&lt;device-specific&gt;</p></td>
<td align="left"><p>&lt;device-specific&gt;</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is expressed in a device-specific format.

Whether the property supports get- or set-property requests is also device-specific.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

This property returns either STATUS\_SUCCESS or a device specific value determined by the third-party provider of the audio driver.

Remarks
-------

In Windows Vista and later versions of Windows, an additional tab (labeled **Custom**) is provided in the **Sound** applet in **Control Panel**. The **Custom** tab displays controls for automatic gain control (AGC) and device-specific properties. The following table shows the controls that are exposed in the **Sound** applet for the various `KSPROPERTY_AUDIO_DEV_SPECIFIC` property and data type combinations.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">KSPROPERTY</th>
<th align="left">Data type</th>
<th align="left">Control</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="ksproperty-audio-agc.md" data-raw-source="[&lt;strong&gt;KSPROPERTY_AUDIO_AGC&lt;/strong&gt;](ksproperty-audio-agc.md)"><strong>KSPROPERTY_AUDIO_AGC</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
<td align="left"><p>Check box</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSPROPERTY_AUDIO_DEV_SPECIFIC</p></td>
<td align="left"><p>BOOL</p></td>
<td align="left"><p>Check box</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSPROPERTY_AUDIO_DEV_SPECIFIC</p></td>
<td align="left"><p>LONG</p></td>
<td align="left"><p>Slider</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSPROPERTY_AUDIO_DEV_SPECIFIC</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>Slider</p></td>
</tr>
</tbody>
</table>

 

**KSPROPERTY\_AUDIO\_AGC** must be used to expose actual AGC functionality in the device. Other device-specific functionality must be exposed by using `KSPROPERTY_AUDIO_DEV_SPECIFIC`.

To see the **Custom** tab, select an audio render or capture device in the **Sound** applet and then click *Properties*.

For an example of how to implement a property handler for the `KSPROPERTY_AUDIO_DEV_SPECIFIC` property, see the **CMiniportTopologyMSVAD::PropertyHandlerDevSpecific** method in the Basetopo.cpp file.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODETYPE\_DEV\_SPECIFIC**](ksnodetype-dev-specific.md)

[**KSPROPERTY\_AUDIO\_AGC**](ksproperty-audio-agc.md)

 

 






