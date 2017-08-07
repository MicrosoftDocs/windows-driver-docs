---
title: OID\_GEN\_VLAN\_ID
author: windows-driver-content
description: As a query, the OID\_GEN\_VLAN\_ID OID reports the configured VLAN identifier (ID) for a NIC.
ms.assetid: 4e024951-a578-4f69-873d-879aecc96e68
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_GEN_VLAN_ID Network Drivers Starting with Windows Vista
---

# OID\_GEN\_VLAN\_ID


As a query, the OID\_GEN\_VLAN\_ID OID reports the configured VLAN identifier (ID) for a NIC.

As a set, the OID\_GEN\_VLAN\_ID OID specifies the configured VLAN identifier (ID) for an NIC that the miniport driver handles.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Optional.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

Remarks
-------

The information buffer passed in this request contains an NDIS\_VLAN\_ID data type. This NDIS\_VLAN\_ID value contains the VLAN ID in the 12 least significant bits per the IEEE 802.1Q-2005 standard. Higher order bits of the NDIS\_VLAN\_ID value are reserved and must be set to 0. Note that NDIS defines NDIS\_VLAN\_ID as a ULONG.

When a transport uses OID\_GEN\_VLAN\_ID in a query, the miniport driver returns the current configured VLAN ID for the NIC. When used in a set, the miniport driver sets the NIC's current configured VLAN ID to the specified value.

During the miniport driver's [*MiniportInitializeEx*](miniportinitializeex.md) function for a particular NIC, the driver initially sets the NIC's VLAN ID to zero. The driver's *MiniportInitializeEx* function then reads the following configuration parameter from the registry, and, if the parameter is present, sets the NIC's VLAN ID to the parameter's value.

```
VlanId, REG_DWORD
```

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


[*MiniportInitializeEx*](miniportinitializeex.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_VLAN_ID%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


