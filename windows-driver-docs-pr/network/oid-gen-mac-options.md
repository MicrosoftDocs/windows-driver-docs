---
title: OID_GEN_MAC_OPTIONS
description: As a query, the OID_GEN_MAC_OPTIONS OID specifies a bitmask that defines optional properties of the underlying driver or a NIC.
ms.assetid: 2a093bcb-ae6f-491c-a596-03e6f47b0b86
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MAC_OPTIONS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MAC\_OPTIONS


As a query, the OID\_GEN\_MAC\_OPTIONS OID specifies a bitmask that defines optional properties of the underlying driver or a NIC.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS handles this OID for NDIS 6.0 and later miniport drivers.

A protocol that initiates this query can determine which of the flags the underlying driver sets, and can optionally take advantage of them.

The following flags are currently defined:

<a href="" id="ndis-mac-option-copy-lookahead-data"></a>NDIS\_MAC\_OPTION\_COPY\_LOOKAHEAD\_DATA  
The protocol driver is free to access indicated data by any means. Some fast-copy functions have trouble accessing on-board device memory. Miniport drivers that indicate data out of mapped device memory should never set this flag. If a miniport driver does set this flag, it relaxes the restriction on fast-copy functions.

<a href="" id="ndis-mac-option-receive-serialized"></a>NDIS\_MAC\_OPTION\_RECEIVE\_SERIALIZED  
The miniport driver indicates packets in a serial manner. That is, such a driver does not enter a new receive indication until the previous receive, if any, has been completed.

<a href="" id="ndis-mac-option-transfers-not-pend"></a>NDIS\_MAC\_OPTION\_TRANSFERS\_NOT\_PEND  
The miniport driver never completes receive indications asynchronously.

A miniport driver that indicates receive operations with the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function should set this flag.

<a href="" id="ndis-mac-option-no-loopback"></a>NDIS\_MAC\_OPTION\_NO\_LOOPBACK  
The NIC has no internal loopback support so NDIS will manage loopbacks on behalf of this driver. A miniport driver cannot provide its own software loopback as efficiently as NDIS, so every miniport driver should set this flag unless a NIC has hardware loopback support. WAN miniport drivers must set this flag.

<a href="" id="ndis-mac-option-full-duplex"></a>NDIS\_MAC\_OPTION\_FULL\_DUPLEX  
The miniport driver supports full-duplex transmits and indications on SMP platforms.

**Note**  This flag has been deprecated for use by NDIS 5.0 and later miniport drivers. NDIS 5.0 and later ignores this flag.

 

<a href="" id="ndis-mac-option-eotx-indication"></a>NDIS\_MAC\_OPTION\_EOTX\_INDICATION  
This flag is obsolete.

<a href="" id="ndis-mac-option-8021p-priority"></a>NDIS\_MAC\_OPTION\_8021P\_PRIORITY  
The NIC and its driver support 802.1p packet priority. For more information, see [Packet Priority](https://msdn.microsoft.com/library/windows/hardware/ff562331). Packet-priority values are received in [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures from higher-layer drivers. The appropriate information is generated in the MAC headers of packets and transmitted over the network. In addition, this NIC and its driver support extracting the appropriate information from the MAC headers of packets received from the network. This information is forwarded in NET\_BUFFER structures to higher-layer drivers.

**Note**  NDIS 6.0 and later and later and later miniport drivers must set the NDIS\_MAC\_OPTION\_8021P\_PRIORITY flag.

 

<a href="" id="ndis-mac-option-supports-mac-address-overwrite"></a>NDIS\_MAC\_OPTION\_SUPPORTS\_MAC\_ADDRESS\_OVERWRITE  
NDIS sets this flag when a miniport driver calls the [**NdisReadNetworkAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564512) function.

<a href="" id="ndis-mac-option-receive-at-dpc"></a>NDIS\_MAC\_OPTION\_RECEIVE\_AT\_DPC  
This flag is obsolete.

<a href="" id="ndis-mac-option-8021q-vlan"></a>NDIS\_MAC\_OPTION\_8021Q\_VLAN  
The miniport driver can assign and remove VLAN identifier (ID) marking in the MAC headers of packets. The driver maintains a configured VLAN ID for each NIC that the driver handles. The driver filters out incoming packets that do not belong to the VLAN to which a NIC is associated and marks outgoing packets with the VLAN ID. During the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function for a particular NIC, the driver initially sets the NIC's VLAN ID to zero. The driver's *MiniportInitializeEx* function then reads the following configuration parameter from the registry, and, if the parameter is present, sets the NIC's VLAN ID to the parameter's value.

```syntax
VlanId, REG_DWORD
```

<a href="" id="ndis-mac-option-reserved"></a>NDIS\_MAC\_OPTION\_RESERVED  
Reserved for NDIS internal use.

**Note**  A miniport driver that sets the NDIS\_MAC\_OPTION\_8021Q\_VLAN flag must also set the NDIS\_MAC\_OPTION\_8021P\_PRIORITY flag. In other words, a miniport driver that supports 802.1Q must also support 802.1p.

 

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

[**NdisReadNetworkAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564512)

[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

 

 




