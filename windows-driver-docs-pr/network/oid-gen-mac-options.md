---
title: OID_GEN_MAC_OPTIONS
author: windows-driver-content
description: As a query, the OID\_GEN\_MAC\_OPTIONS OID specifies a bitmask that defines optional properties of the underlying driver or a NIC.
ms.assetid: 2a093bcb-ae6f-491c-a596-03e6f47b0b86
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_MAC_OPTIONS Network Drivers Starting with Windows Vista
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_MAC_OPTIONS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


