---
title: KSPROPERTY\_PIN\_COMMUNICATION
description: The KSPROPERTY\_PIN\_COMMUNICATION property specifies the direction of IRP flow on pins instantiated by the pin factory.
ms.assetid: d5f62731-39de-4ec4-83d5-f4253373aaa4
keywords: ["KSPROPERTY_PIN_COMMUNICATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_COMMUNICATION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_COMMUNICATION


The KSPROPERTY\_PIN\_COMMUNICATION property specifies the direction of IRP flow on pins instantiated by the pin factory.

## <span id="ddk_ksproperty_pin_communication_ks"></span><span id="DDK_KSPROPERTY_PIN_COMMUNICATION_KS"></span>


### Usage Summary Table

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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></p></td>
<td><p>KSPIN_COMMUNICATION</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The KS filter returns one of the following values, which specifies the communication direction of a pin instantiated by this pin factory:

<span id="KSPIN_COMMUNICATION_NONE"></span><span id="kspin_communication_none"></span>KSPIN\_COMMUNICATION\_NONE  
The pin factory does not instantiate any pins.

<span id="KSPIN_COMMUNICATION_SINK"></span><span id="kspin_communication_sink"></span>KSPIN\_COMMUNICATION\_SINK  
The pin factory instantiates IRP sink pins. Such pins can only be connected to IRP source pins.

<span id="KSPIN_COMMUNICATION_SOURCE"></span><span id="kspin_communication_source"></span>KSPIN\_COMMUNICATION\_SOURCE  
The pin factory instantiates IRP source pins. Such pins can only be connected to IRP sink pins.

<span id="KSPIN_COMMUNICATION_BOTH"></span><span id="kspin_communication_both"></span>KSPIN\_COMMUNICATION\_BOTH  
The pin factory instantiates pins that are both IRP sinks and IRP sources.

<span id="KSPIN_COMMUNICATION_BRIDGE"></span><span id="kspin_communication_bridge"></span>KSPIN\_COMMUNICATION\_BRIDGE  
This pin cannot connect to other pins, but instances can be created on it to receive non-KS I/O requests.

Source pins send IRPs to sink pins. A source pin may read or write data, and a sink pin may have data read to it or written from it. For more information, see [**KSPROPERTY\_PIN\_DATAFLOW**](ksproperty-pin-dataflow.md).

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using Stream Request Blocks to query for more information where necessary.

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
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY\_PIN\_DATAFLOW**](ksproperty-pin-dataflow.md)

 

 






