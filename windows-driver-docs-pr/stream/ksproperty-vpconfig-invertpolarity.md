---
title: KSPROPERTY\_VPCONFIG\_INVERTPOLARITY
description: The KSPROPERTY\_VPCONFIG\_INVERTPOLARITY property toggles the global polarity flag, forcing the video port to be inverted.
MS-HAID:
- 'dvdref\_bfe1d273-f7ed-4a9f-90ef-002f639ab4d0.xml'
- 'stream.ksproperty\_vpconfig\_invertpolarity'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c0b69aa4-0f81-42b4-9a69-5afcf702f5f1
keywords: ["KSPROPERTY_VPCONFIG_INVERTPOLARITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_INVERTPOLARITY
api_location:
- ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_VPCONFIG\_INVERTPOLARITY


The KSPROPERTY\_VPCONFIG\_INVERTPOLARITY property toggles the global polarity flag, forcing the video port to be inverted.

## <span id="ddk_ksproperty_vpconfig_invertpolarity_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_INVERTPOLARITY_KS"></span>


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
<td><p>Boolean</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a Boolean. Specify **TRUE** to invert the polarity, or specify **FALSE** to prevent inverting the polarity.

Remarks
-------

KSPROPERTY\_VPCONFIG\_INVERTPOLARITY property requests return STATUS\_SUCCESS to indicate successful completion. Otherwise, requests return an appropriate error status code.

Because this feature is hardware dependent, models that do not use this feature must return STATUS\_NOT\_IMPLEMENTED.

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

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_VPCONFIG_INVERTPOLARITY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





