---
title: KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST
description: The KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST property specifies whether a channel on a mute node (KSNODETYPE\_MUTE) is muted or not.
keywords: ["KSPROPERTY_AUDIOEFFECTSDISCOVERY_EFFECTSLIST Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOEFFECTSDISCOVERY_EFFECTSLIST
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/30/2020
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST

The **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST** property is a filter property whose value is a list of audio effect types that are applied to a particular KS pin factory, for a particular audio signal processing path.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

### Usage Summary Table

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
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
<td><p>Pin factory (via Filter instance)</p></td>
<td><p>KSP_PIN</p></td>
<td><a href="/windows/win32/api/msapofxproxy/ns-msapofxproxy-ksp_pinmode"><strong>KSP_PINMODE</strong></a></td>
</tr>
</tbody>
</table>

The property value is an array of zero or more audio effect type GUIDs (for example, AUDIO\_EFFECT\_TYPE\_ACOUSTIC\_ECHO\_CANCELLATION) that are in the pin’s signal processing path identified by the **KSP\_PINMODE** structure.

**Note**  The KSPROPERTY\_TYPE\_TOPOLOGY flag bit must not be set for this property.

### Return Value

The **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST** property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, this property request returns an appropriate error status code.

## Remarks

If an audio driver uses Microsoft’s generic proxy APO to retrieve the audio effects that are included in the different signal processing paths for a KS pin, then it must support this property. The generic proxy APO is contained in the *msapofxproxy.dll* file. Audio drivers can use this generic proxy APO when all signal processing is done in the audio driver, or in the corresponding digital signal processor (DSP) hardware component, with no processing being done in an APO. In this case, the APO’s only function is to report the signal processing effects to the audio system.

The generic proxy APO receives **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST** from the audio driver and uses it to report the effects to the audio system. The generic proxy APO assumes that the list of effects does not change while the KS pin’s filter interface is enabled.

If the property descriptor specifies a KS pin that does not support **KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST**, then the driver must return STATUS\_NOT\_SUPPORTED.

If the property descriptor specifies an *AudioProcessingMode* value that the driver does not support, then the driver must return STATUS\_INVALID\_PARAMETER. Note that an audio driver must support the [**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](ksproperty-audiosignalprocessing-modes.md) property to be able to indicate its supported audio signal processing modes.

## Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Msapofxproxy.h</td>
</tr>
</tbody>
</table>

## See also

[**KSP\_PINMODE**](/windows/win32/api/msapofxproxy/ns-msapofxproxy-ksp_pinmode)

[**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](ksproperty-audiosignalprocessing-modes.md)
