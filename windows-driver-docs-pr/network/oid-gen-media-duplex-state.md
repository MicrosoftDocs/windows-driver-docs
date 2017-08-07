---
title: OID\_GEN\_MEDIA\_DUPLEX\_STATE
author: windows-driver-content
description: As a query, the OID\_GEN\_MEDIA\_DUPLEX\_STATE OID returns the duplex state of an interface. Version Information Windows Vista and laterSupported. NDIS 6.0 and later miniport driversNot requested. For NDIS interface providers only.
ms.assetid: 63776227-dc48-4506-888f-c4b944837c4c
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_GEN_MEDIA_DUPLEX_STATE Network Drivers Starting with Windows Vista
---

# OID\_GEN\_MEDIA\_DUPLEX\_STATE


As a query, the OID\_GEN\_MEDIA\_DUPLEX\_STATE OID returns the duplex state of an interface.

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

NDIS uses this OID to query the duplex state of an [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) provider. Only NDIS interface providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query can be one of the values in the [**NET\_IF\_MEDIA\_DUPLEX\_STATE**](net-if-media-duplex-state.md) enumeration.

Miniport drivers supply the media duplex state during initialization and provide updates with status indications.

To specify the duplex state in a miniport driver, set the **MediaDuplexState** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](ndis-miniport-adapter-general-attributes.md) structure that the miniport driver passes to the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function.

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](ndis-miniport-adapter-general-attributes.md)

[**NET\_IF\_MEDIA\_DUPLEX\_STATE**](net-if-media-duplex-state.md)

[**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md)

[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_MEDIA_DUPLEX_STATE%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


