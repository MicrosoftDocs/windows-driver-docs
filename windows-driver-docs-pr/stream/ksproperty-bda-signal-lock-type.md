---
title: KSPROPERTY\_BDA\_SIGNAL\_LOCK\_TYPE
description: Clients use KSPROPERTY\_BDA\_SIGNAL\_LOCK\_TYPE to determine the current lock type of a signal.
ms.assetid: 2ddf49c4-f0d1-4918-b564-719c695a83ac
keywords: ["KSPROPERTY_BDA_SIGNAL_LOCK_TYPE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_LOCK_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_SIGNAL\_LOCK\_TYPE


Clients use KSPROPERTY\_BDA\_SIGNAL\_LOCK\_TYPE to determine the current lock type of a signal.

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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin or Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556526" data-raw-source="[&lt;strong&gt;BDA_LockType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556526)"><strong>BDA_LockType</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the control node or is set to −1 to specify a pin.

The returned [**BDA\_LockType**](https://msdn.microsoft.com/library/windows/hardware/ff556526)-typed value identifies the current lock type.

The RF tuner node should provide this indication.

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

## See also


[**BDA\_LockType**](https://msdn.microsoft.com/library/windows/hardware/ff556526)

[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

[**KSPROPERTY\_BDA\_SIGNAL\_LOCK\_CAPS**](ksproperty-bda-signal-lock-caps.md)

 

 






