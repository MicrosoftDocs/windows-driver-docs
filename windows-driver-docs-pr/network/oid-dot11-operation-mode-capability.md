---
title: OID_DOT11_OPERATION_MODE_CAPABILITY
author: windows-driver-content
description: When queried, the OID_DOT11_OPERATION_MODE_CAPABILITY object identifier (OID) requests that the miniport driver return the Native 802.11 operation modes that it supports.
ms.assetid: d56151e0-8390-4639-bb2f-8fd27c3ddcf4
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_OPERATION_MODE_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_OPERATION\_MODE\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_OPERATION\_MODE\_CAPABILITY object identifier (OID) requests that the miniport driver return the Native 802.11 operation modes that it supports.

The data type for this OID is the DOT11\_OPERATION\_MODE\_CAPABILITY structure.

```ManagedCPlusPlus
    typedef struct _DOT11_OPERATION_MODE_CAPABILITY {
         ULONG uReserved;
         ULONG uMajorVersion;
         ULONG uMinorVersion;
         ULONG uNumOfTxBuffers;
         ULONG uNumOfRxBuffers;
         ULONG uOpModeCapability;
    } DOT11_OPERATION_MODE_CAPABILITY, *PDOT11_OPERATION_MODE_CAPABILITY;
  
```

This structure includes the following members:

<a href="" id="ureserved"></a>**uReserved**  
This member is reserved. The miniport driver must not modify the value of this member.

<a href="" id="umajorversion"></a>**uMajorVersion**  
The major version of the Native 802.11 framework that the miniport driver supports. For the Windows Vista operating system, the major version is two.

<a href="" id="uminorversion"></a>**uMinorVersion**  
The minor version of the Native 802.11 framework that the miniport driver supports. For the Windows Vista operating system, the minor version is zero.

<a href="" id="unumoftxbuffers"></a>**uNumOfTxBuffers**  
Maximum number of media access control (MAC) service data unit (MSDU) packets that the 802.11 station can hold in its transmit queue. The miniport driver must support a minimum transmit queue depth of 64.

The value of this member must not include the number of transmit buffers that the 802.11 station uses to send packets on its own, such as Beacon packets or 802.11 control packets.

<a href="" id="unumofrxbuffers"></a>**uNumOfRxBuffers**  
Maximum number of MSDU packets that the 802.11 station can buffer in its receive queue. The miniport driver must support a minimum receive queue depth of 64.

<a href="" id="uopmodecapability"></a>**uOpModeCapability**  
A bitmask of the miniport driver's supported operation modes. This bitmask is defined through the following:

<a href="" id="dot11-operation-mode-extensible-ap"></a>DOT11\_OPERATION\_MODE\_EXTENSIBLE\_AP  
Specifies that the miniport driver supports the Extensible Access Point (ExtAP) operation mode.

<a href="" id="dot11-operation-mode-extensible-station"></a>DOT11\_OPERATION\_MODE\_EXTENSIBLE\_STATION  
Specifies that the miniport driver supports the Extensible Station (ExtSTA) operation mode.

<a href="" id="dot11-operation-mode-network-monitor"></a>DOT11\_OPERATION\_MODE\_NETWORK\_MONITOR  
Specifies that the miniport driver supports the Network Monitor (NetMon) operation mode.

For more information about the operation modes of a Native 802.11 miniport driver, see [Native 802.11 Operation Modes](https://msdn.microsoft.com/library/windows/hardware/ff560671).

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

 

 




