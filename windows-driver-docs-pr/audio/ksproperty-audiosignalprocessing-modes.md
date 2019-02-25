---
title: KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES
description: The KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES property returns the list of audio signal processing modes supported by a pin factory.
ms.assetid: 95536F80-D4E0-48CB-8DB2-603C4CEF0053
keywords: ["KSPROPERTY_AUDIOSIGNALPROCESSING_MODES Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOSIGNALPROCESSING_MODES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES


The **KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES** property returns the list of audio signal processing modes supported by a pin factory.

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
<td align="left"><p>Pin factory (via Filter instance)</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722.aspx" data-raw-source="[KSP_PIN](https://msdn.microsoft.com/library/windows/hardware/ff566722.aspx)">KSP_PIN</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx" data-raw-source="[KSMULTIPLE_ITEM](https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)">KSMULTIPLE_ITEM</a></p></td>
</tr>
</tbody>
</table>

 

The property value is a structure, followed by zero (0) or more GUIDs.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES** returns a **KSMULTIPLE\_ITEM** followed by zero (0) or more GUIDS. The KSMULTIPLE\_ITEM.Count member contains the number of GUIDs. The KSMULTIPLE\_ITEM.Size member contains the total size of the property value. Each GUID identifies a signal processing mode supported by the audio driver for the Pin ID specified in the *PinId* member of the **KSP\_PIN** structure.

In Windows 8.1 there were two defined audio signal processing modes, AUDIO\_SIGNALPROCESSINGMODE\_DEFAULT and AUDIO\_SIGNALPROCESSINGMODE\_RAW.

In Windows 10, five additional mode are defined.

AUDIO\_SIGNALPROCESSINGMODE\_COMMUNICATIONS
AUDIO\_SIGNALPROCESSINGMODE\_SPEECH
AUDIO\_SIGNALPROCESSINGMODE\_MEDIA
AUDIO\_SIGNALPROCESSINGMODE\_MOVIE
AUDIO\_SIGNALPROCESSINGMODE\_NOTIFICATION
For more information, see [Audio Signal Processing Modes](https://msdn.microsoft.com/windows/hardware/drivers/audio/audio-signal-processing-modes).

Remarks
-------

The basic support handler for **KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES** should be handed a **KSP\_PIN** structure, and should advertise support only on non-loopback streaming pins. Audio drivers should support signal processing modes only on host and offload pins. For loopback or bridge pins the audio driver should still support the property, but return a **KSMULTIPLE\_ITEM** structure with its *Count* parameter set to zero (0).

Any audio miniport driver that is developed to work with the Microsoft audio port Class driver (Portcls) can implement the [**IMiniportAudioSignalProcessing::GetModes**](https://msdn.microsoft.com/library/windows/hardware/dn457660) method.

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
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IMiniportAudioSignalProcessing::GetModes**](https://msdn.microsoft.com/library/windows/hardware/dn457660)

[KSMULTIPLE\_ITEM](https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)

[KSP\_PIN](https://msdn.microsoft.com/library/windows/hardware/ff566722.aspx)

 

 






