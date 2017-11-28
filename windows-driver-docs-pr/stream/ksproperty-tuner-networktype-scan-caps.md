---
title: KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS
description: The KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS property describes the scanning capabilities of a particular broadcast network type that the tuning device supports. This property can be implemented optionally.
ms.assetid: 89f66812-9192-4d1d-ac8c-38396fc6be8e
keywords: ["KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS


The KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS property describes the scanning capabilities of a particular broadcast network type that the tuning device supports. This property can be implemented optionally.

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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565885)</p></td>
<td><p>KSPROPERTY_TUNER_NETWORKTYPE</p>
<p>_SCAN_CAPS_S</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S structure that specifies the scanning capabilities for a network type.

Remarks
-------

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565885)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





