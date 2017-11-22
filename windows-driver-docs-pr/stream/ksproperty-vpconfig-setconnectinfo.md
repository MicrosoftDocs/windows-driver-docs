---
title: KSPROPERTY\_VPCONFIG\_SETCONNECTINFO
description: The KSPROPERTY\_VPCONFIG\_SETCONNECTINFO property sets the video port configuration with user-defined connection information. It is a pointer to an array of DDVIDEOPORTCONNECT structures as returned by the KSPROPERTY\_VPCONFIG\_GETCONNECTINFO property.
MS-HAID:
- 'dvdref\_dbf4d289-4500-4edd-94ff-51583c050aad.xml'
- 'stream.ksproperty\_vpconfig\_setconnectinfo'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 120f6889-cd67-4c05-b4b8-adab3efd7f2c
keywords: ["KSPROPERTY_VPCONFIG_SETCONNECTINFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_SETCONNECTINFO
api_location:
- ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_VPCONFIG\_SETCONNECTINFO


The KSPROPERTY\_VPCONFIG\_SETCONNECTINFO property sets the video port configuration with user-defined connection information. It is a pointer to an array of [**DDVIDEOPORTCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff550388) structures as returned by the KSPROPERTY\_VPCONFIG\_GETCONNECTINFO property.

## <span id="ddk_ksproperty_vpconfig_setconnectinfo_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SETCONNECTINFO_KS"></span>


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
<td><p>[<strong>DDVIDEOPORTCONNECT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550388)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DDVIDEOPORTCONNECT structure that describes the configuration of a video port connection.

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


[**DDVIDEOPORTCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff550388)

[**KSPROPERTY\_VPCONFIG\_GETCONNECTINFO**](ksproperty-vpconfig-getconnectinfo.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_VPCONFIG_SETCONNECTINFO%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





