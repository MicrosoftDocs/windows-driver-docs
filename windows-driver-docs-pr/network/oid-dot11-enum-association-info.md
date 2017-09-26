---
title: OID\_DOT11\_ENUM\_ASSOCIATION\_INFO
author: windows-driver-content
description: When queried, the OID\_DOT11\_ASSOCIATION\_INFO object identifier (OID) requests that the miniport driver return a list of the access point (AP) (for infrastructure basic service set (BSS) networks) or all peer stations (for independent BSS (IBSS) networks) with which the 802.11 station is associated.
ms.assetid: 1aba29c6-bea9-41a1-b530-4df248f19821
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ENUM_ASSOCIATION_INFO Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ENUM\_ASSOCIATION\_INFO


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_ASSOCIATION\_INFO object identifier (OID) requests that the miniport driver return a list of the access point (AP) (for infrastructure basic service set (BSS) networks) or all peer stations (for independent BSS (IBSS) networks) with which the 802.11 station is associated.

The data type for this OID is the DOT11\_ASSOCIATION\_INFO\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_ASSOCIATION_INFO_LIST {
         NDIS_OBJECT_HEADER Header;
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_ASSOCIATION_INFO_EX dot11AssocInfo[1];
    } DOT11_ASSOCIATION_INFO_LIST,   *PDOT11_ASSOCIATION_INFO_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_ASSOCIATION\_INFO\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_ASSOCIATION\_INFO\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_ASSOCIATION\_INFO\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **dot11AssocInfo** array. A zero value for this member indicates an empty list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **dot11AssocInfo** array can contain.

<a href="" id="dot11associnfo"></a>**dot11AssocInfo**  
The association information list.

The data type for the entries in the **dot11AssocInfo** array is the DOT11\_ASSOCIATION\_INFO\_EX structure.

``` syntax
typedef struct DOT11_ASSOCIATION_INFO_EX {         
         DOT11_MAC_ADDRESS PeerMacAddress;
         DOT11_MAC_ADDRESS BSSID;
         USHORT usCapabilityInformation;
         USHORT usListenInterval;
         UCHAR ucPeerSupportedRates[MAX_NUM_SUPPORTED_RATES_V2];
         USHORT usAssociationID; 
         DOT11_ASSOCIATION_STATE dot11AssociationState;
         DOT11_POWER_MODE dot11PowerMode;
         LARGE_INTEGER liAssociationUpTime;
         ULONGLONG ullNumOfTxPacketSuccesses;
         ULONGLONG ullNumOfTxPacketFailures;
         ULONGLONG ullNumOfRxPacketSuccesses;
         ULONGLONG ullNumOfRxPacketFailures;  
     } DOT11_ASSOCIATION_INFO_EX, *PDOT11_ASSOCIATION_INFO_EX;
```

This structure includes the following members:

<a href="" id="peermacaddress"></a>**PeerMacAddress**  
The MAC address of the AP or peer station.

<a href="" id="bssid"></a>**BSSID**  
The BSS identifier (BSSID). The BSSID is one of the following:

-   The MAC address of the AP.

-   The BSSID of the IBSS network that the peer station is connected to.

<a href="" id="uscapabilityinformation"></a>**usCapabilityInformation**  
The 802.11 Capability Information field from the Beacon or Probe Response frames that the 802.11 station most recently received from the peer.

<a href="" id="uslisteninterval"></a>**usListenInterval**  
The 802.11 Listen Interval field from the Association Request or Reassociation Request frames the 802.11 station sent to the AP.

If the desired BSS type is **dot11\_BSS\_type\_independent**, the miniport driver must set this member to zero.

<a href="" id="ucpeersupportedrates"></a>**ucPeerSupportedRates**  
The data rates supported by the AP or peer station. These rates are based on the 802.11 Supported Rates IE from the Beacon or Probe Response frames that the 802.11 station most recently received from the peer.

Each entry in the **ucPeerSupportedRates** array is the value of an index within the table of data rates returned through a query of [OID\_DOT11\_DATA\_RATE\_MAPPING\_TABLE](oid-dot11-data-rate-mapping-table.md). The index value must be between 2 and 127.

<a href="" id="usassociationid"></a>**usAssociationID**  
The 802.11 Association ID field from the Association or Reassociation Response frames that the 802.11 station received from the AP.

If the desired BSS type is **dot11\_BSS\_type\_independent**, the miniport driver must set this member to zero.

<a href="" id="dot11associationstate"></a>**dot11AssociationState**  
The 802.11 authentication and association state of the peer. This member can have one of the values of the [**DOT11\_ASSOCIATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff547650) enumeration.

If the desired BSS type is **dot11\_BSS\_type\_independent**, the miniport driver must not set this member to **dot11\_assoc\_state\_auth\_assoc**. Since the 802.11 authentication procedure is optional for IBSSs, the miniport driver might set this member to **dot11\_assoc\_state\_unauth\_unassoc** even though it is connected to an IBSS network.

<a href="" id="dot11powermode"></a>**dot11PowerMode**  
Power management mode of the peer. For more information about this structure, see [**DOT11\_POWER\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff548755).

If the desired BSS type is **dot11\_BSS\_type\_infrastructure**, the miniport driver must set this member to **dot11\_power\_mode\_active**.

<a href="" id="liassociationuptime"></a>**liAssociationUpTime**  
The timestamp when the 802.11 association procedure successfully completed. The miniport driver calls [**NdisGetCurrentSystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff562629) to get the timestamp of the association completion.

If the desired BSS type is **dot11\_BSS\_type\_independent**, the miniport driver must set this member to zero.

<a href="" id="ullnumoftxpacketsuccesses"></a>**ullNumOfTxPacketSuccesses**  
The number of 802.11 MAC protocol data unit (MPDU), management MPDU (MMPDU), and control frames successfully transmitted to the peer.

<a href="" id="ullnumoftxpacketfailures"></a>**ullNumOfTxPacketFailures**  
The number of 802.11 MPDU, MMPDU, and control frames that failed during transmission to the peer.

<a href="" id="ullnumofrxpacketsuccesses"></a>**ullNumOfRxPacketSuccesses**  
The number of 802.11 MPDU, MMPDU, and control frames successfully received from the peer.

<a href="" id="ullnumofrxpacketfailures"></a>**ullNumOfRxPacketFailures**  
The number of 802.11 MPDU, MMPDU, and control frames that the 802.11 failed to receive from the peer. This counter must include packets that the 802.11 station received successfully but failed to decrypt.

If the desired BSS type is **dot11\_BSS\_type\_infrastructure**, the association information list must contain DOT11\_ASSOCIATION\_INFO\_EX data for only the AP with which the 802.11 station is associated. If the 802.11 station is not associated, the miniport driver must return an empty list and set the **uNumOfEntries** member to zero.

If the desired BSS type is **dot11\_BSS\_type\_independent**, the association information list must contain DOT11\_ASSOCIATION\_INFO\_EX data for every peer station in the IBSS with which the 802.11 station has connected.

When OID\_DOT11\_ASSOCIATION\_INFO is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_ASSOCIATION\_INFO\_LIST structure, including all entries in the **dot11AssocInfo** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_ASSOCIATION\_INFO\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **dot11AssocInfo** array.

        For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_ASSOCIATION\_INFO\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to than the length, in bytes, of the entire DOT11\_ASSOCIATION\_INFO\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_ASSOCIATION\_INFO\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **dot11AssocInfo** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_ASSOCIATION\_INFO\_LIST structure. The miniport driver must also copy the entire DOT11\_ASSOCIATION\_INFO\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_ENUM_ASSOCIATION_INFO%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


