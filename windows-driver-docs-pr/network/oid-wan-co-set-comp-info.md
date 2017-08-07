---
title: OID\_WAN\_CO\_SET\_COMP\_INFO
author: windows-driver-content
description: The OID\_WAN\_CO\_SET\_COMP\_INFO OID notifies the miniport driver of the PPP compression scheme selected by a protocol to which the miniport driver already returned information with a OID\_WAN\_CO\_GET\_COMP\_INFO query.
ms.assetid: f3b6b846-fa8c-425b-ba05-45927e744d66
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WAN_CO_SET_COMP_INFO Network Drivers Starting with Windows Vista
---

# OID\_WAN\_CO\_SET\_COMP\_INFO


The OID\_WAN\_CO\_SET\_COMP\_INFO OID notifies the miniport driver of the PPP compression scheme selected by a protocol to which the miniport driver already returned information with a [OID\_WAN\_CO\_GET\_COMP\_INFO](oid-wan-co-get-comp-info.md) query. This PPP compression scheme is specific to a virtual connection (VC).

The protocol supplies a specification for the PPP compression scheme it selected in an NDIS\_WAN\_CO\_SET\_COMP\_INFO structure, defined as follows:

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_SET_COMP_INFO {
         IN NDIS_WAN_COMPRESS_INFO SendCapabilities;
         IN NDIS_WAN_COMPRESS_INFO RecvCapabilities;
    } NDIS_WAN_CO_SET_COMP_INFO,   *PNDIS_WAN_CO_SET_COMP_INFO;
  
```

## <a href="" id="ddk-oid-wan-co-set-comp-info-nr"></a>


The members of this structure contain the following information:

<a href="" id="sendcapabilities"></a>**SendCapabilities**  
Specifies a structure containing information about compression capabilities for sending data.

<a href="" id="recvcapabilities"></a>**RecvCapabilities**  
Specifies a structure containing information about compression capabilities for receiving data.

Remarks
-------

For specifics of the NDIS\_WAN\_COMPRESS\_INFO structure, see [OID\_WAN\_GET\_COMP\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff561202).

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
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_WAN\_CO\_GET\_COMP\_INFO](oid-wan-co-get-comp-info.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WAN_CO_SET_COMP_INFO%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


