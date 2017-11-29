---
title: KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON
description: The KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON property enables or disables the display of the subpicture.
ms.assetid: f9dcf8ca-44fb-45e2-9993-813439c742ef
keywords: ["KSPROPERTY_DVDSUBPIC_COMPOSIT_ON Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_COMPOSIT_ON
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON


The KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON property enables or disables the display of the subpicture.

## <span id="ddk_ksproperty_dvdsubpic_composit_on_ks"></span><span id="DDK_KSPROPERTY_DVDSUBPIC_COMPOSIT_ON_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>KSPROPERTY_COMPOSIT_ON</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_COMPOSIT\_ON (a type-defined Boolean). Specify **TRUE** to turn on the subpicture display, or specify **FALSE** to turn off the subpicture display.

Remarks
-------

If subpicture display is disabled then the decoder must still decode the subpicture data but not display it. This facilitates instant display when a subpicture-enable command is received.

There is a force-display subpicture command in the subpicture data command stream that can override the KSPROPERTY\_DVDSUBPIC\_COMPOSIT\_ON property.

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
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_DVDSUBPIC_COMPOSIT_ON%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




