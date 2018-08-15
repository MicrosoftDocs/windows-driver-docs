---
title: KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING
description: In the stream class model, clients use the KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING property to determine framing requirements for a pin.
ms.assetid: 02cacade-938b-4fab-928f-75f790692324
keywords: ["KSPROPERTY_CONNECTION_ALLOCATORFRAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_ALLOCATORFRAMING
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING


In the stream class model, clients use the KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING property to determine framing requirements for a pin.

## <span id="ddk_ksproperty_connection_allocatorframing_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_ALLOCATORFRAMING_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSALLOCATOR_FRAMING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560979)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979), which describes the framing requirements for the pin. For example, the **FrameSize** member specifies the frame size of data on the pin.

AVStream minidrivers should use [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX**](ksproperty-connection-allocatorframing-ex.md).

See [KS Allocators](https://msdn.microsoft.com/library/windows/hardware/ff567257). and [AVStream Allocators](https://msdn.microsoft.com/library/windows/hardware/ff554202).

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

## <span id="see_also"></span>See also


[**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979)

 

 






