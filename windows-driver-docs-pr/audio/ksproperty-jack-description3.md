---
title: KSPROPERTY\_JACK\_DESCRIPTION3
description: The KSPROPERTY\_JACK\_DESCRIPTION3 property is implemented as a pin-wise property that is accessed by using the filter handle.
keywords: ["KSPROPERTY_JACK_DESCRIPTION3 Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_JACK_DESCRIPTION3
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/26/2022
---

# KSPROPERTY\_JACK\_DESCRIPTION3

The **KSPROPERTY\_JACK\_DESCRIPTION3** property is implemented as a pin-wise property that is accessed by using the filter handle.

In version 22H2 and later Windows operating systems, the associated [**KSJACK\_DESCRIPTION3**](ksjack-description3.md) structure can be used to specify and change the current configuration of the jack.

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
<td align="left"><p>Pin factory (via filter handle)</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)"><strong>KSP_PIN</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)"><strong>KSMULTIPLE_ITEM</strong></a> followed by an array of <a href="ksjack-description3.md" data-raw-source="[&lt;strong&gt;KSJACK_DESCRIPTION3&lt;/strong&gt;](ksjack-description3.md)"><strong>KSJACK_DESCRIPTION3</strong></a> structures</p></td>
</tr>
</tbody>
</table>

The property value (instance data) is a KSMULTIPLE\_ITEM, followed by an array of KSJACK\_DESCRIPTION3 structures.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_JACK\_DESCRIPTION3 property request returns a KSMULTIPLE\_ITEM followed by an array of *N* KSJACK\_DESCRIPTION3 structures, where *N* = the number of jacks that are associated with the specified bridge pin. The following list shows the items that are returned by the property request.

KSMULTIPLE\_ITEM.Size = sizeof(KSMULTIPLE\_ITEM) + N \* sizeof(KSJACK\_DESCRIPTION3)

KSMULTIPLE\_ITEM.Count = N

KSJACK\_DESCRIPTION3\[0\]

...

KSJACK\_DESCRIPTION3\[N-1\]

## Remarks

### Communicating audio device changes using KSJACK_DESCRIPTION3 and KSPROPERTY_JACK_DESCRIPTION3 

The Windows audio system caches audio device capabilities during audio endpoint creation. These cached values are for capabilities such as the presence of a HW audio engine, format support, container ID, buffer size characteristics, etc. These cached values are retained for the life of the windows installation. They are refreshed only when the audio driver is updated or during an OS upgrade. 

With [**KSJACK_DESCRIPTION3**](ksjack-description3.md), the Windows audio system provides a mechanism for the audio driver to request all cached values be discarded and refreshed. The request can be triggered by changes in the audio device capabilities such as resource constraints. 

Whenever the driver changes the contents of KSJACK\_DESCRIPTION3 at runtime, the driver will trigger the existing [KSEVENT_PINCAPS_JACKINFOCHANGE](ksproperty-jack-description3.md) event. 

The Windows audio system maintains the last reported *ConfigId* value cached on the audio endpoint. The *ConfigId* value is retrieved in response to [KSEVENT_PINCAPS_JACKINFOCHANGE](ksproperty-jack-description3.md) event and during normal processing of the audio endpoint at system boot, Audio Endpoint Builder service restart, audio driver update, or interface state changes for the endpoint. 

If the retrieved *ConfigId* value differs from the previously stored value, the Windows audio system will discard all previously cached endpoint capabilities and refresh them. 

The recommended usage is to define multiple audio endpoint configurations within the driver that is controlled by the *ConfigId* (bitmask or enum) value. For example, *ConfigId* of 1 may indicate the presence of an audio engine node, whereas *ConfigId* 2 would not report an audio engine node. The *ConfigId* in use by the driver is shared with the Windows audio system through KSPROPERTY_JACK_DESCRIPTION3 and acts to synchronize the endpoint with the capabilities cached by the Windows audio system. 

The value of the *ConfigId* is opaque to Windows. The audio driver could use a timestamp or incrementing value chosen at run time in place of a bitmask or enum as suggested above. This strategy is not recommended as it may result in unnecessary endpoint refreshes during boot up or interface changes to synchronize the last stored *ConfigId* value to the newly reported value, even when the endpoint capabilities are unchanged. This approach may also increase the chances of the driver and Windows becoming out of sync, which can result in audio playback failures. 

The mechanism used to refresh the cached values on the endpoint when the *ConfigId* changes is the same as used for Operating System Upgrades and Driver Updates. A new endpoint with a different ID is created which will contain the refreshed cached values that match the new *ConfigId* settings for the endpoint, user settings are then copied from the old endpoint to the new endpoint, and finally the old endpoint is deleted. For more information, on the audio endpoint migration process in OS upgrades, see [Operating System Upgrades](operating-system-upgrades.md). 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Available in version 22H2 and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSJACK\_DESCRIPTION3**](ksjack-description3.md)

[KSMULTIPLE\_ITEM](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[Operating System Upgrades](operating-system-upgrades.md)
