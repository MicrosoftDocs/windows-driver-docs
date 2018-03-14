---
title: OID_DOT11_CURRENT_OPTIONAL_CAPABILITY
author: windows-driver-content
description: When queried, the OID_DOT11_CURRENT_OPTIONAL_CAPABILITY object identifier (OID) requests that the miniport driver return the state of the optional wireless LAN (WLAN) capabilities supported by the 802.11 station.
ms.assetid: e029712c-b34f-447c-9e43-48e5a72ad6ad
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_OPTIONAL_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_OPTIONAL\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_CURRENT\_OPTIONAL\_CAPABILITY object identifier (OID) requests that the miniport driver return the state of the optional wireless LAN (WLAN) capabilities supported by the 802.11 station.

Optional WLAN capabilities are not required for the 802.11 station to operate within a basic service set (BSS) network. However, once enabled, these capabilities could provide better performance within the BSS network. When [OID\_DOT11\_OPTIONAL\_CAPABILITY](oid-dot11-optional-capability.md) is queried, the miniport driver specifies the types of optional WLAN capabilities supported by the 802.11 station.

The data type for OID\_DOT11\_CURRENT\_OPTIONAL\_CAPABILITY is the DOT11\_CURRENT\_OPTIONAL\_CAPABILITY structure.

```ManagedCPlusPlus
    typedef struct _DOT11_CURRENT_OPTIONAL_CAPABILITY {
         ULONG uReserved;
         BOOLEAN bDot11CFPollable;
         BOOLEAN bDot11PCF;
         BOOLEAN bDot11PCFMPDUTransferToPC;
         BOOLEAN bStrictlyOrderedServiceClass;
    } DOT11_CURRENT_OPTIONAL_CAPABILITY,   *PDOT11_CURRENT_OPTIONAL_CAPABILITY;
  
```

This structure includes the following members:

<a href="" id="ureserved"></a>**uReserved**  
This member is reserved. The miniport driver must not modify the value of this member.

<a href="" id="bdot11cfpollable"></a>**bDot11CFPollable**  
Specifies whether the 802.11 station can respond to an 802.11 CF-Poll frame. The miniport driver should return the value of the IEEE 802.11 **dot11CFPollable** management information base (MIB) object. For more information about this MIB object, see [OID\_DOT11\_CF\_POLLABLE](oid-dot11-cf-pollable.md).

<a href="" id="bdot11pcf"></a>**bDot11PCF**  
Specifies whether the 802.11 station has enabled the Point Coordination Function (PCF). For more information about PCF, refer to clauses 9.2.3 and 9.4 of the IEEE 802.11-2012 standard.

<a href="" id="bdot11pcfmpdutransfertopc"></a>**bDot11PCFMPDUTransferToPC**  
Specifies whether the 802.11 station has enabled delivery of received PCF MAC protocol data unit (MPDU) frames to the operating system.

**Note**  
If the miniport driver sets this member to **TRUE**, the miniport driver must also set the **bDot11PCF** member to **TRUE**.

 

<a href="" id="bstrictlyorderedserviceclass"></a>**bStrictlyOrderedServiceClass**  
Specifies whether the 802.11 station has enabled the StrictlyOrdered service class for MSDU packet ordering. For more information about the StrictlyOrdered service class, refer to clause 5.1.3 of the IEEE 802.11-2012 standard.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, OID\_DOT11\_CURRENT\_OPTIONAL\_CAPABILITY is a query-only OID and cannot be used to enable or disable the optional WLAN capabilities supported by the 802.11 station. However, the independent hardware vendor (IHV) can define a proprietary NIC-specific extension to change the optional WLAN capabilities. After its been defined, a service supplied by the IHV can issue the NIC-specific extension to the miniport driver. For more information about NIC-specific extensions, see [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](oid-dot11-nic-specific-extension.md).

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




