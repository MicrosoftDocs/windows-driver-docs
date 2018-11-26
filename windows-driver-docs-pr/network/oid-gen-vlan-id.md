---
title: OID_GEN_VLAN_ID
description: As a query, the OID_GEN_VLAN_ID OID reports the configured VLAN identifier (ID) for a NIC.
ms.assetid: 4e024951-a578-4f69-873d-879aecc96e68
ms.date: 08/08/2017
keywords: 
 -OID_GEN_VLAN_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

During the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function for a particular NIC, the driver initially sets the NIC's VLAN ID to zero. The driver's *MiniportInitializeEx* function then reads the following configuration parameter from the registry, and, if the parameter is present, sets the NIC's VLAN ID to the parameter's value.

```syntax
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


[*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389)

 

 




