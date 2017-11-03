---
title: OID_DOT11_PORT_STATE_NOTIFICATION
author: windows-driver-content
description: When set, the OID_DOT11_PORT_STATE_NOTIFICATION object identifier (OID) indicates the status of the data port used for network access to the access point (AP) (for infrastructure BSS networks) or peer station (for independent BSS networks) with which the 802.11 station is associated.
ms.assetid: 2696f8a4-d9dd-4b17-86a2-02d9855f9b87
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_PORT_STATE_NOTIFICATION Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_PORT\_STATE\_NOTIFICATION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_PORT\_STATE\_NOTIFICATION object identifier (OID) indicates the status of the data port used for network access to the access point (AP) (for infrastructure BSS networks) or peer station (for independent BSS networks) with which the 802.11 station is associated.

The data type for OID\_DOT11\_PORT\_STATE\_NOTIFICATION is the DOT11\_PORT\_STATE\_NOTIFICATION structure.

```ManagedCPlusPlus
    typedef struct DOT11_PORT_STATE_NOTIFICATION {
         NDIS_OBJECT_HEADER Header;
         DOT11_MAC_ADDRESS PeerMac;
         BOOLEAN bOpen;
    } DOT11_PORT_STATE_NOTIFICATION, *PDOT11_PORT_STATE_NOTIFICATION;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_PORT\_STATE\_NOTIFICATION structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_PORT\_STATE\_NOTIFICATION\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_PORT\_STATE\_NOTIFICATION).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="peermac"></a>**PeerMac**  
The media access control (MAC) address of the AP or peer station with which the 802.11 station is associated.

<a href="" id="bopen"></a>**bOpen**  
The data port state. If **bOpen** is **TRUE**, the port is open for sending and receiving data packets.

The actions performed by the miniport driver following the set request of OID\_DOT11\_PORT\_STATE\_NOTIFICATION are specific to the implementation by the independent hardware vendor (IHV).

For more information about port-based network access, see [Port Access Management](https://msdn.microsoft.com/library/windows/hardware/ff570184).

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_PORT_STATE_NOTIFICATION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


