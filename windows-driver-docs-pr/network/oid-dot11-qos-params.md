---
title: OID_DOT11_QOS_PARAMS
author: windows-driver-content
description: When set, the OID_DOT11_QOS_PARAMS object identifier (OID) requests that the miniport driver set quality of service (QoS) parameters for the 802.11 station.
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

 

 




