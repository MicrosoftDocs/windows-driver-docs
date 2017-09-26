---
title: OID\_DOT11\_QOS\_PARAMS
author: windows-driver-content
description: When set, the OID\_DOT11\_QOS\_PARAMS object identifier (OID) requests that the miniport driver set quality of service (QoS) parameters for the 802.11 station.
ms.assetid: c7f767bb-95ff-4d66-b0ca-0a658c31dbb0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_QOS_PARAMS Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_QOS\_PARAMS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_QOS\_PARAMS object identifier (OID) requests that the miniport driver set quality of service (QoS) parameters for the 802.11 station.

The data type for OID\_DOT11\_QOS\_PARAMS is the DOT11\_QOS\_PARAMS structure.

```ManagedCPlusPlus
    typedef struct DOT11_QOS_PARAMS {
         NDIS_OBJECT_HEADER Header;
         UCHAR ucEnabledQoSProtocolFlags;
      } DOT11_QOS_PARAMS, *PDOT11_QOS_PARAMS;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_QOS\_PARAMS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_QOS\_PARAMS\_REVISION\_1

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(OID\_DOT11\_QOS\_PARAMS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="ucenabledqosprotocolflags"></a>**ucEnabledQoSProtocolFlags**  
A set of flags that specify the quality of service (QoS) protocols enabled on the NIC. This member is either zero or a bitwise OR combination of the following flags:

<a href="" id="dot11-qos-protocol-flag-wmm"></a>DOT11\_QOS\_PROTOCOL\_FLAG\_WMM  
If the NIC supports the 802.11 WMM standard and this flag is set, the 802.11 WMM QoS protocol is enabled. Otherwise, the 802.11 WMM QoS protocol is disabled.

<a href="" id="dot11-qos-protocol-flag-11e"></a>DOT11\_QOS\_PROTOCOL\_FLAG\_11E  
If the NIC supports the 802.11e standard and this flag is set, the 802.11e QoS protocol is enabled. Otherwise, the 802.11e QoS protocol is disabled.

The default value of **ucEnabledQoSProtocolFlags** is the **ucSupportedQoSProtocolFlags** member of the [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688) structure.

The miniport driver must fail a set request with error code NDIS\_STATUS\_INVALID\_STATE if the 802.11 station is in any state except the initialization (INIT) state.

When queried, OID\_DOT11\_QOS\_PARAMS requests that the miniport driver return the value of the **msDot11QoSParams** MIB object.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_QOS_PARAMS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


