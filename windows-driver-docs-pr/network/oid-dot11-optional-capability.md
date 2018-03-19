---
title: OID_DOT11_OPTIONAL_CAPABILITY
author: windows-driver-content
description: When queried, the OID_DOT11_OPTIONAL_CAPABILITY object identifier (OID) requests that the miniport driver return the optional capabilities that the 802.11 station supports.
ms.assetid: ad6573ed-8c27-4075-975f-1b7673c564d8
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_OPTIONAL_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_OPTIONAL\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_OPTIONAL\_CAPABILITY object identifier (OID) requests that the miniport driver return the optional capabilities that the 802.11 station supports.

The data type for this OID is the DOT11\_OPTIONAL\_CAPABILITY structure.

```ManagedCPlusPlus
    typedef struct _DOT11_OPTIONAL_CAPABILITY {
         ULONG uReserved;
         BOOLEAN bDot11PCF;
         BOOLEAN bDot11PCFMPDUTransferToPC;
         BOOLEAN bStrictlyOrderedServiceClass;
    } DOT11_OPTIONAL_CAPABILITY,   *PDOT11_OPTIONAL_CAPABILITY;
  
```

This structure includes the following members:

<a href="" id="ureserved"></a>**uReserved**  
This member is reserved. The miniport driver must not modify the value of this member.

<a href="" id="bdot11pcf"></a>**bDot11PCF**  
Specifies whether the 802.11 station supports the Point Coordination Function (PCF). For more information about PCF, refer to Clauses 9.2.3 and 9.4 of the IEEE 802.11-2012 standard.

<a href="" id="bdot11pcfmpdutransfertopc"></a>**bDot11PCFMPDUTransferToPC**  
Specifies whether the 802.11 station supports the delivery of received PCF MAC protocol data unit (MPDU)frames to the operating system.

**Note**  If the miniport driver sets this member to **TRUE**, it must set the **bDot11PCF** member to **TRUE**.

 

<a href="" id="bstrictlyorderedserviceclass"></a>**bStrictlyOrderedServiceClass**  
Specifies whether the 802.11 station supports the StrictlyOrdered service class for MAC service data unit (MSDU) ordering. For more information about the StrictlyOrdered service class, refer to clause 5.1.3 of the IEEE 802.11-2012 standard.

If the miniport driver sets the **bDot11PCF** member to **TRUE**, the 802.11 station must support the following PCF operations:

-   Maintenance of the contention-free period (CFP) structure and timing.

-   Deliveries of PCF MPDU frames from the operating system for transmit.

When [OID\_DOT11\_CURRENT\_OPTIONAL\_CAPABILITY](oid-dot11-current-optional-capability.md) is queried, the miniport driver specifies the status of these optional capabilities.

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

 

 




