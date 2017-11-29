---
title: KSPROPERTY\_TOPOLOGYNODE\_ENABLE
description: The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to turn on or off the topology nodes in an already built topology.
ms.assetid: 6b9f7a92-97dc-476b-962a-40ccf1987154
keywords: ["KSPROPERTY_TOPOLOGYNODE_ENABLE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TOPOLOGYNODE_ENABLE
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

# KSPROPERTY\_TOPOLOGYNODE\_ENABLE


The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to turn on or off the topology nodes in an already built topology.

## <span id="ddk_ksproperty_topologynode_enable_ks"></span><span id="DDK_KSPROPERTY_TOPOLOGYNODE_ENABLE_KS"></span>


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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>KSNODEPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537143)</p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL and specifies whether the node is turned on or off. A value of **TRUE** indicates that the node is turned on. **FALSE** indicates that the node is turned off.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_TOPOLOGYNODE\_ENABLE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

Enabling an already enabled node or disabling an already disabled node has no effect, but should not be treated as an error.

Disabling a node turns off the transformation that the node performs on the stream that passes through the node. In the case of an AEC, AGC, or noise-suppression node ([**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md), [**KSNODETYPE\_AGC**](ksnodetype-agc.md), or [**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)), for example, a disabled node operates in pass-through mode (that is, it performs no operation on the stream as it flows from the node's input pin to its output pin).

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


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)

[**KSNODETYPE\_AGC**](ksnodetype-agc.md)

[**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_TOPOLOGYNODE_ENABLE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





