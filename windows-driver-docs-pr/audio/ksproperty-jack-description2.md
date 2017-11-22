---
title: KSPROPERTY\_JACK\_DESCRIPTION2
description: The KSPROPERTY\_JACK\_DESCRIPTION2 property is implemented as a pin-wise property that is accessed by using the filter handle.
ms.assetid: 6856060b-f735-4ed8-99bd-5896c87d581f
keywords: ["KSPROPERTY_JACK_DESCRIPTION2 Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_JACK_DESCRIPTION2
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_JACK\_DESCRIPTION2


The KSPROPERTY\_JACK\_DESCRIPTION2 property is implemented as a pin-wise property that is accessed by using the filter handle.

In Windows 7 and later Windows operating systems, this property can be supported on any bridge pin that is associated with one or more physical jacks. KSPROPERTY\_JACK\_DESCRIPTION2 is used to get the state and the jack-related capabilities of the device.

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
<td align="left"><p>KS_PIN</p></td>
<td align="left"><p>[KSMULTIPLE_ITEM](http://msdn.microsoft.com/library/windows/hardware/ff563441.aspx) followed by an array of [<strong>KSJACK_DESCRIPTION2</strong>](ksjack-description2.md) structures</p></td>
</tr>
</tbody>
</table>

 

The property value (instance data) is a KSMULTIPLE\_ITEM, followed by an array of KSJACK\_DESCRIPTION2 structures.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_JACK\_DESCRIPTION2 property request returns a KSMULTIPLE\_ITEM followed by an array of *N* KSJACK\_DESCRIPTION2 structures, where *N* = the number of jacks that are associated with the specified bridge pin. The following list shows the items that are returned by the property request.

KSMULTIPLE\_ITEM.Size = sizeof(KSMULTIPLE\_ITEM) + N \* sizeof(KSJACK\_DESCRIPTION2)

KSMULTIPLE\_ITEM.Count = N

KSJACK\_DESCRIPTION2\[0\]

...

KSJACK\_DESCRIPTION2\[N-1\]

Remarks
-------

Each KSJACK\_DESCRIPTION2 structure must only contain information about one jack.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 7</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2008</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSJACK\_DESCRIPTION2**](ksjack-description2.md)

[KSMULTIPLE\_ITEM](http://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_JACK_DESCRIPTION2%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





