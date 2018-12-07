---
title: KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL
description: KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL
ms.assetid: 5f70b9ad-d569-404a-bf6d-01be689e2d56
keywords: ["KSNODETYPE_ACOUSTIC_ECHO_CANCEL Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_ACOUSTIC_ECHO_CANCEL
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL


## <span id="ddk_ksnodetype_acoustic_echo_cancel_ks"></span><span id="DDK_KSNODETYPE_ACOUSTIC_ECHO_CANCEL_KS"></span>


The KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL node represents an AEC (acoustic echo cancellation) control. An AEC node has connections for two input streams and two output streams. One input/output pair is used for the capture stream, and the other input/output pair is used for the render stream. The capture-output and render-input streams have the same format. The capture-input and render-output streams can have a different number of channels and different sample rates. However, in a typical implementation, the two streams either have the same sample rate or a combination, such as 16 kHz and 48 kHz or 11.025 kHz and 44.1 kHz, in which one sample rate is an integer multiple of the other.

An AEC node should number its logical pins with the pin IDs from header file Ksmedia.h, which are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Pin ID Parameter</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSNODEPIN_AEC_RENDER_IN</p></td>
<td align="left"><p>Sink pin (node input) for render stream.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSNODEPIN_AEC_RENDER_OUT</p></td>
<td align="left"><p>Source pin (node output) for render stream.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSNODEPIN_AEC_CAPTURE_IN</p></td>
<td align="left"><p>Sink pin (node input) for capture stream.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSNODEPIN_AEC_CAPTURE_OUT</p></td>
<td align="left"><p>Source pin (node output) for capture stream.</p></td>
</tr>
</tbody>
</table>

 

Note that the pins in the preceding table are logical pins on the node, which are used solely to specify connections internal to the filter, rather than external pins on the filter, which are used to connect to other filters. For more information, see [**PCCONNECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537688).

For information about how a filter containing an AEC node can provide support for full-duplex DirectSound applications, see [DirectSound Capture Effects](https://msdn.microsoft.com/library/windows/hardware/ff536327).

When a filter containing an AEC node is created or the node is reset, the node is initially configured to operate in pass-through mode.

A KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL node should support the following properties in order to enable hardware acceleration:

[**KSPROPERTY\_AUDIO\_CPU\_RESOURCES**](ksproperty-audio-cpu-resources.md)

[**KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE**](ksproperty-audio-algorithm-instance.md)

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to enable and disable an AEC node. When disabled, the node operates in pass-through mode; that is, it allows the render and capture streams to pass through the node without modification.

A KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL node can also support the following optional properties in order to provide additional control and monitoring capabilities:

[**KSPROPERTY\_AEC\_MODE**](ksproperty-aec-mode.md)

[**KSPROPERTY\_AEC\_NOISE\_FILL\_ENABLE**](ksproperty-aec-noise-fill-enable.md)

[**KSPROPERTY\_AEC\_STATUS**](ksproperty-aec-status.md)

 

 





