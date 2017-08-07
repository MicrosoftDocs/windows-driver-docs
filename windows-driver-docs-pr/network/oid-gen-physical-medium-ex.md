---
title: OID\_GEN\_PHYSICAL\_MEDIUM\_EX
author: windows-driver-content
description: As a query, the OID\_GEN\_PHYSICAL\_MEDIUM\_EX OID specifies the types of physical media that a miniport adapter supports.
ms.assetid: cbac8c9b-d7fe-4588-8a64-599d04a77a72
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_GEN_PHYSICAL_MEDIUM_EX Network Drivers Starting with Windows Vista
---

# OID\_GEN\_PHYSICAL\_MEDIUM\_EX


As a query, the OID\_GEN\_PHYSICAL\_MEDIUM\_EX OID specifies the types of physical media that a miniport adapter supports.

Remarks
-------

NDIS handles this OID for NDIS 6.0 and later miniport drivers. The miniport driver supplies the physical medium value during initialization.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains an NDIS\_PHYSICAL\_MEDIUM enumeration value.

**Note**  The difference between OID\_GEN\_PHYSICAL\_MEDIUM\_EX and [OID\_GEN\_PHYSICAL\_MEDIUM](oid-gen-physical-medium.md) is that the OID\_GEN\_PHYSICAL\_MEDIUM\_EX version does not override the **NdisPhysicalMedium802\_3** type as **NdisPhysicalMediumUnspecified** whereas OID\_GEN\_PHYSICAL\_MEDIUM still does. We recommend that all 6.x drivers use the EX version. OID\_GEN\_PHYSICAL\_MEDIUM\_EX is exposed through a WMI GUID.

 

Miniport drivers report a physical media type to differentiate their physical media from media that they declared to support in the [OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md) OID query.

NDIS supports the OID\_GEN\_PHYSICAL\_MEDIUM\_EX OID for miniport adapters that support newer networks, even though those networks transfer packets that appear to the operating system and to NDIS as standard, well-known media types.

Newer networks transfer packets that might appear like standard media, but that might have new features or slight differences from the standard. This OID exists so upper-layer drivers and applications can determine the actual networks to which a NIC connects. After retrieving information about underlying networks, upper-layer drivers and applications can use this information to modify how such drivers and applications behave.

To clearly distinguish an 802.3 NIC from an emulated 802.3 NIC for which there is no physical medium type defined, NDIS 6.0 and later and later versions require 802.3 miniport drivers to report an **NdisPhysicalMedium802\_3** media type.

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
<td><p>Supported in NDIS 6.20 and later. Not requested for miniport drivers. (See Remarks section.)</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md)

[OID\_GEN\_PHYSICAL\_MEDIUM](oid-gen-physical-medium.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_PHYSICAL_MEDIUM_EX%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


