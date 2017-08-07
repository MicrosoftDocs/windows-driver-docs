---
title: OID\_DOT11\_OPERATION\_MODE\_CAPABILITY
author: windows-driver-content
description: When queried, the OID\_DOT11\_OPERATION\_MODE\_CAPABILITY object identifier (OID) requests that the miniport driver return the Native 802.11 operation modes that it supports.
ms.assetid: d56151e0-8390-4639-bb2f-8fd27c3ddcf4
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_OPERATION_MODE_CAPABILITY Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_OPERATION_MODE_CAPABILITY%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


