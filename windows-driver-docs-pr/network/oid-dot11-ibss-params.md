---
title: OID\_DOT11\_IBSS\_PARAMS
author: windows-driver-content
description: When set, the OID\_DOT11\_IBSS\_PARAMS object identifier (OID) requests that the miniport driver set parameters to be used when connecting to an independent basic service set (IBSS) network.Note  IBSS (Ad hoc) and SoftAP are deprecated.
ms.assetid: 5b0500ed-40c1-4e23-8610-e299bfe692db
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_IBSS_PARAMS Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_IBSS\_PARAMS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_IBSS\_PARAMS object identifier (OID) requests that the miniport driver set parameters to be used when connecting to an independent basic service set (IBSS) network.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](https://msdn.microsoft.com/library/windows/hardware/hh440289).

 

When queried, this OID requests that the miniport driver return the IBSS network connection parameters.

If the IEEE **dot11DesiredBSSType** management information base (MIB) object is set to **dot11\_BSS\_type\_independent**, the 802.11 station uses the IBSS network parameters when performing a connection operation to an IBSS network. Connection operations are initiated through a set of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md).

For more information about the **dot11DesiredBSSType** MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

The data type for OID\_DOT11\_IBSS\_PARAMS is the DOT11\_IBSS\_PARAMS structure.

```ManagedCPlusPlus
    typedef struct DOT11_IBSS_PARAMS {
         NDIS_OBJECT_HEADER Header;
         BOOLEAN bJoinOnly;
         ULONG uIEsOffset;
         ULONG uIEsLength;
    } DOT11_IBSS_PARAMS, *PDOT11_IBSS_PARAMS;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_IBSS\_PARAMS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_IBSS\_PARAMS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_IBSS\_PARAMS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="bjoinonly"></a>**bJoinOnly**  
Specifies whether the 802.11 station should only join an existing IBSS network or start a new IBSS network during the connection operation.

If **bJoinOnly** is **FALSE**, the 802.11 station must join an existing IBSS network if the station detects one. If the 802.11 station does not detect an IBSS network, the station must start a new one.

If **bJoinOnly** is **TRUE**, the 802.11 station must only join an existing IBSS network. If the 802.11 station does not detect an IBSS network, the station must continue searching for an IBSS network to join until either a set request of [OID\_DOT11\_DISCONNECT\_REQUEST](oid-dot11-disconnect-request.md) or a set request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made.

<a href="" id="uiesoffset"></a>**uIEsOffset**  
Offset in the **InformationBuffer** member of the NDIS\_OID\_REQUEST structure where additional 802.11 Information Elements (IE) are stored.

The 802.11 station must append these additional IEs to the end of every transmitted 802.11 Beacon or Probe Response frames. If adding the additional IEs causes the size of the frames to exceed the maximum length for 802.11 media access control (MAC) management protocol data unit (MMPDU) frames, the 802.11 station must not append the additional IEs.

**Note**  If it cannot append the additional IEs, the 802.11 station must remain connected to the IBSS network.

 

**uIEsOffset** is calculated from the beginning of the DOT11\_IBSS\_PARAMS structure.

<a href="" id="uieslength"></a>**uIEsLength**  
Length of the additional 802.11 IEs. If **uIEsLength** is zero, no additional IEs are stored.

The 802.11 station must follow these guidelines when **bJoinOnly** is set to **TRUE**.

-   After joining an existing IBSS network, the 802.11 station cannot perform a roaming operation to a new IBSS network until it is the only station within the IBSS network with which it is joined. If it is the only station within the IBSS network with which it is joined, it should stop sending Beacon frames and must continue searching for an IBSS network to join until either a set request of [OID\_DOT11\_DISCONNECT\_REQUEST](oid-dot11-disconnect-request.md) or a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made.

-   If the 802.11 station supports 802.11h for IBSS networks, the station must not enter the DFS owner recovery mode as defined in Clause 11.6.7.2 of the IEEE 802.11h-2003 standard. Instead, the 802.11 station must disassociate from all the existing peer stations within the IBSS network and perform a roaming operation to another IBSS network.

    If the 802.11 station does not detect another IBSS network, the station must continue searching for an IBSS network to join until either a set request of [OID\_DOT11\_DISCONNECT\_REQUEST](oid-dot11-disconnect-request.md) or a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made.

The default values for the members of the DOT11\_IBSS\_PARAMS structure are defined in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>DOT11_IBSS_PARAMS member</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>bJoinOnly</strong></p></td>
<td><p><strong>FALSE</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>uIEsOffset</strong></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>uIEsLength</strong></p></td>
<td><p>0</p></td>
</tr>
</tbody>
</table>

 

The miniport driver must set the members of the DOT11\_IBSS\_PARAMS structure to the default values if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_IBSS_PARAMS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


