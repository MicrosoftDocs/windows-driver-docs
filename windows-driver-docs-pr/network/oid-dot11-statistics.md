---
title: OID_DOT11_STATISTICS
author: windows-driver-content
description: When queried, the OID\_DOT11\_STATISTICS object identifier (OID) requests that the miniport driver return the statistics for the IEEE 802.11 interface, including
ms.assetid: 631f29fb-c59f-4ecf-9d63-cde348270315
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_STATISTICS Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_STATISTICS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_STATISTICS object identifier (OID) requests that the miniport driver return the statistics for the IEEE 802.11 interface, including:

-   Statistics for the IEEE media access control (MAC) layer of the 802.11 station.

-   Statistics for the IEEE PHY layer of the 802.11 station for each supported PHY.

The data type for this OID is the DOT11\_STATISTICS structure.

```ManagedCPlusPlus
    typedef struct DOT11_STATISTICS {
         NDIS_OBJECT_HEADER Header;
         ULONGLONG ullFourWayHandshakeFailures;
         ULONGLONG ullTKIPCounterMeasuresInvoked;
         ULONGLONG ullReserved;
         DOT11_MAC_FRAME_STATISTICS MacUcastCounters;
         DOT11_MAC_FRAME_STATISTICS MacMcastCounters;
         DOT11_PHY_FRAME_STATISTICS PhyCounters[];
    } DOT11_STATISTICS, *PDOT11_STATISTICS;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_STATISTICS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_STATISTICS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_STATISTICS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="ullfourwayhandshakefailures"></a>**ullFourWayHandshakeFailures**  
The number of four-way handshake failures that the 802.11 station encountered during Wi-Fi Protected Access (WPA) or Robust Security Network Association (RSNA) authentication.

If the 802.11 station is not performing the WPA or RSNA authentication, it must not write to this member.

<a href="" id="ulltkipcountermeasuresinvoked"></a>**ullTKIPCounterMeasuresInvoked**  
The number of times that the 802.11 station invoked countermeasures following a message integrity code (MIC) failure.

If the 802.11 station is not performing TKIP countermeasures, it must not write to this member.

<a href="" id="ullreserved"></a>**ullReserved**  
This member is reserved for use by the operating system. The miniport driver must not write to this member.

<a href="" id="macucastcounters"></a>**MacUcastCounters**  
The MAC layer counters based on unicast packets sent or received by the 802.11 station. The data structure for this member is the DOT11\_MAC\_FRAME\_STATISTICS structure.

**Note**  The miniport driver must increment counters for received unicast packets only for those packets with a destination MAC address in the 802.11 MAC header that matches the 802.11 station's MAC address.

 

<a href="" id="macmcastcounters"></a>**MacMcastCounters**  
The MAC layer counters based on multicast or broadcast packets sent or received by the 802.11 station. The data structure for this member is the DOT11\_MAC\_FRAME\_STATISTICS structure.

**Note**  The miniport driver must increment counters for received multicast packets if the MAC address in the 802.11 MAC header matches an entry in the multicast address list of the 802.11 station. For more information about the multicast address list, see [OID\_DOT11\_MULTICAST\_LIST](oid-dot11-multicast-list.md). The driver must increment counters on receipt of broadcast packets that match the currently configured packet filter. For more information about packet filters, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md).

 

<a href="" id="phycounters"></a>**PhyCounters**  
An array of PHY layer counters. Each entry in this array is formatted as a DOT11\_PHY\_FRAME\_STATISTICS structure.

The driver must maintain separate copies of the DOT11\_PHY\_FRAME\_STATISTICS structure for each supported PHY.

The miniport driver returns the list of supported PHYs when queried by [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

When OID\_DOT11\_STATISTICS is queried, the miniport driver must return an entry in the **PhyCounters** array for each supported PHY.

The data type for the **MacUcastCounters** and **MacMcastCounters** members is the DOT11\_MAC\_FRAME\_STATISTICS structure.

``` syntax
typedef struct DOT11_MAC_FRAME_STATISTICS {         
         ULONGLONG ullTransmittedFrameCount;
         ULONGLONG ullReceivedFrameCount;
         ULONGLONG ullWEPExcludedCount;
         ULONGLONG ullTKIPLocalMICFailures;
         ULONGLONG ullTKIPReplays;
         ULONGLONG ullTKIPICVErrorCount;
         ULONGLONG ullCCMPFormatErrors;
         ULONGLONG ullCCMPReplays;         
         ULONGLONG ullCCMPDecryptErrors;
         ULONGLONG ullWEPUndecryptableCount;
         ULONGLONG ullWEPICVErrorCount;         
         ULONGLONG ullDecryptSuccessCount;
         ULONGLONG ullDecryptFailureCount;   
     } DOT11_MAC_STATISTICS, * PDOT11_MAC_STATISTICS;
```

The members of this structure are used to record MAC-level statistics for:

-   MAC service data unit (MSDU) packets.

-   MAC protocol data unit (MPDU) frames.

    MPDU frame counters must include all MPDU fragments sent for an MSDU packet.

-   Management MPDU (MMPDU) frames.

This structure includes the following members:

<a href="" id="ulltransmittedframecount"></a>**ullTransmittedFrameCount**  
The number of MSDU packets and MMPDU frames that the IEEE MAC layer of the 802.11 station successfully transmitted.

<a href="" id="ullreceivedframecount"></a>**ullReceivedFrameCount**  
The number of MSDU packets and MMPDU frames that the IEEE MAC layer of the 802.11 station successfully received. This member should not be incremented for received packets that failed cipher decryption or MIC validation.

<a href="" id="ullwepexcludedcount"></a>**ullWEPExcludedCount**  
The number of unencrypted received MPDU frames that the MAC layer discarded when the IEEE 802.11 **dot11ExcludeUnencrypted** management information base (MIB) object is enabled. For more information about this MIB object, see [OID\_DOT11\_EXCLUDE\_UNENCRYPTED](oid-dot11-exclude-unencrypted.md).

MPDU frames are considered unencrypted when the Protected Frame subfield of the Frame Control field in the IEEE 802.11 MAC header is set to zero.

<a href="" id="ulltkiplocalmicfailures"></a>**ullTKIPLocalMICFailures**  
The number of received MSDU packets that the 802.11 station discarded because of MIC failures.

<a href="" id="ulltkipreplays"></a>**ullTKIPReplays**  
The number of received MPDU frames that the 802.11 station discarded because of the TKIP replay protection procedure.

<a href="" id="ulltkipicverrorcount"></a>**ullTKIPICVErrorCount**  
The number of encrypted MPDU frames that the 802.11 station failed to decrypt because of a TKIP ICV error.

<a href="" id="ullccmpformaterrors"></a>**ullCCMPFormatErrors**  
The number of received MPDU frames that the 802.11 discarded because of an invalid AES-CCMP format.

<a href="" id="ullccmpreplays"></a>**ullCCMPReplays**  
The number of received MPDU frames that the 802.11 station discarded because of the AES-CCMP replay protection procedure.

<a href="" id="ullccmpdecrypterrors"></a>**ullCCMPDecryptErrors**  
The number of received MPDU frames that the 802.11 station discarded because of errors detected by the AES-CCMP decryption algorithm.

<a href="" id="ullwepundecryptablecount"></a>**ullWEPUndecryptableCount**  
The number of encrypted MPDU frames received for which a WEP decryption key was not available on the 802.11 station.

<a href="" id="ullwepicverrorcount"></a>**ullWEPICVErrorCount**  
The number of encrypted MPDU frames that the 802.11 station failed to decrypt because of a WEP ICV error.

<a href="" id="ulldecryptsuccesscount"></a>**ullDecryptSuccessCount**  
The number of received encrypted packets that the 802.11 station successfully decrypted.

For the WEP and TKIP cipher algorithms, the miniport driver must increment this counter for each received encrypted MPDU that was successfully decrypted. For the AES-CCMP cipher algorithm, the miniport driver must increment this counter on each received encrypted MSDU packet that was successfully decrypted.

<a href="" id="ulldecryptfailurecount"></a>**ullDecryptFailureCount**  
The number of encrypted packets that the 802.11 station failed to decrypt.

For the WEP and TKIP cipher algorithms, the miniport driver must increment this counter for each received encrypted MPDU that was not successfully decrypted. For the AES-CCMP cipher algorithm, the miniport driver must increment this counter on each received encrypted MSDU packet that was not successfully decrypted.

The miniport driver must not increment this counter for packets that are decrypted successfully, but are discarded for other reasons. For example, the miniport driver must not increment this counter for packets discarded because of TKIP MIC failures or TKIP/CCMP replays.

The data type for the elements of the **PhyCounters** array is the DOT11\_PHY\_FRAME\_STATISTICS structure.

``` syntax
typedef struct DOT11_PHY_FRAME_STATISTICS {         
         ULONGLONG ullTransmittedFrameCount;
         ULONGLONG ullMulticastTransmittedFrameCount;
         ULONGLONG ullFailedCount;
         ULONGLONG ullRetryCount;
         ULONGLONG ullMultipleRetryCount;         
         ULONGLONG ullMaxTXLifetimeExceededCount;
         ULONGLONG ullTransmittedFragmentCount;
         ULONGLONG ullRTSSuccessCount;
         ULONGLONG ullRTSFailureCount;
         ULONGLONG ullACKFailureCount;
         ULONGLONG ullReceivedFrameCount;         
         ULONGLONG ullMulticastReceivedFrameCount;
         ULONGLONG ullPromiscuousReceivedFrameCount;         
         ULONGLONG ullMaxRXLifetimeExceededCount;
         ULONGLONG ullFrameDuplicateCount;         
         ULONGLONG ullReceivedFragmentCount;
         ULONGLONG ullPromiscuousReceivedFragmentCount;         
         ULONGLONG ullFCSErrorCount;   
     } DOT11_PHY_FRAME_STATISTICS,  *PDOT11_PHY_FRAME_STATISTICS;
```

The members of this structure are used to record PHY-level statistics for:

-   MAC service data unit (MSDU) packets.

-   MAC protocol data unit (MPDU) frames.

    MPDU frame counters must include all MPDU fragments sent for an MSDU packet.

-   Management MPDU (MMPDU) frames.

This structure includes the following members:

<a href="" id="ulltransmittedframecount"></a>**ullTransmittedFrameCount**  
The number of MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has successfully transmitted.

<a href="" id="ullmulticasttransmittedframecount"></a>**ullMulticastTransmittedFrameCount**  
The number of multicast or broadcast MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has successfully transmitted.

<a href="" id="ullfailedcount"></a>**ullFailedCount**  
The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit after exceeding the retry limits defined by the 802.11 IEEE **dot11ShortRetryLimit** or **dot11LongRetryLimit** MIB counters. For more information about these MIB counters, see [OID\_DOT11\_SHORT\_RETRY\_LIMIT](oid-dot11-short-retry-limit.md) or [OID\_DOT11\_LONG\_RETRY\_LIMIT](oid-dot11-long-retry-limit.md).

<a href="" id="ullretrycount"></a>**ullRetryCount**  
The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after one or more attempts.

<a href="" id="ullmultipleretrycount"></a>**ullMultipleRetryCount**  
The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after more than one retransmission attempt.

For MSDU packets, the miniport driver must increment this counter for each packet that was transmitted successfully after one or more of its MPDU fragments required retransmission.

<a href="" id="ullmaxtxlifetimeexceededcount"></a>**ullMaxTXLifetimeExceededCount**  
The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit because of a timeout as defined by the IEEE 802.11 **dot11MaxTransmitMSDULifetime** MIB object. For more information about this MIB object, see [OID\_DOT11\_MAX\_TRANSMIT\_MSDU\_LIFETIME](oid-dot11-max-transmit-msdu-lifetime.md).

<a href="" id="ulltransmittedfragmentcount"></a>**ullTransmittedFragmentCount**  
The number of MPDU frames that the 802.11 station transmitted and acknowledged through a received 802.11 ACK frame.

<a href="" id="ullrtssuccesscount"></a>**ullRTSSuccessCount**  
The number of times that the 802.11 station received a Clear To Send (CTS) frame in response to a Request To Send (RTS) frame.

<a href="" id="ullrtsfailurecount"></a>**ullRTSFailureCount**  
The number of times that the 802.11 station did not receive a CTS frame in response to an RTS frame.

<a href="" id="ullackfailurecount"></a>**ullACKFailureCount**  
The number of times that the 802.11 station expected and did not receive an Acknowledgement (ACK) frame.

<a href="" id="ullreceivedframecount"></a>**ullReceivedFrameCount**  
The number of MSDU packets and MMPDU frames that the 802.11 station has successfully received.

For MSDU packets, the miniport driver must increment this counter for each packet whose MPDU fragments were received and passed frame check sequence (FCS) verification and replay detection. The miniport driver must increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer cipher decryption.

<a href="" id="ullmulticastreceivedframecount"></a>**ullMulticastReceivedFrameCount**  
The number of multicast or broadcast MSDU packets and MMPDU frames that the 802.11 station has successfully received.

For MSDU packets, the miniport driver must increment this counter for each packet whose MPDU fragments were received and passed FCS verification and replay detection. The miniport driver must increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer cipher decryption.

<a href="" id="ullpromiscuousreceivedframecount"></a>**ullPromiscuousReceivedFrameCount**  
The number of MSDU packets or MMPDU frames received by the 802.11 station when a promiscuous packet filter is enabled. For more information about packet filters, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md).

If a promiscuous packet filter is enabled, the miniport driver must only increment this counter for received MSDU packets or MMPDU frames that would have been rejected if the filter was not enabled. The driver must not increment this counter for:

-   Unicast MSDU packets or MMPDU frames with a destination MAC address that matches the 802.11 station's MAC address.

-   Multicast or broadcast MSDU packets or MMPDU frames with a destination MAC address that matches an entry in the multicast address list of the 802.11 station. For more information about the multicast address list, see [OID\_DOT11\_MULTICAST\_LIST](oid-dot11-multicast-list.md).

<a href="" id="ullmaxrxlifetimeexceededcount"></a>**ullMaxRXLifetimeExceededCount**  
The number if MSDU packets and MMPDU frames that the 802.11 station discarded because of a timeout as defined by the IEEE 802.11 **dot11MaxReceiveLifetime** MIB object. For more information about this MIB object, see [OID\_DOT11\_MAX\_RECEIVE\_LIFETIME](oid-dot11-max-receive-lifetime.md).

<a href="" id="ullframeduplicatecount"></a>**ullFrameDuplicateCount**  
The number of duplicate MPDU frames that the 802.11 station received. The 802.11 station determines duplicate frames through the Sequence Control field of the 802.11 MAC header.

<a href="" id="ullreceivedfragmentcount"></a>**ullReceivedFragmentCount**  
The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames.

<a href="" id="ullpromiscuousreceivedfragmentcount"></a>**ullPromiscuousReceivedFragmentCount**  
The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames when a promiscuous packet filter was enabled. For more information about packet filters, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md).

If a promiscuous packet filter is enabled, the miniport driver must only increment this counter for received MPDU frames that would have been rejected if the filter was not enabled. The driver must not increment this counter for:

-   Unicast MPDU frames with a destination MAC address that matches the 802.11 station's MAC address.

-   Multicast or broadcast MPDU frames with a destination MAC address that matches an entry in the multicast address list of the 802.11 station. For more information about the multicast address list, see [OID\_DOT11\_MULTICAST\_LIST](oid-dot11-multicast-list.md).

<a href="" id="ullfcserrorcount"></a>**ullFCSErrorCount**  
The number of MPDU frames that the 802.11 station received with FCS errors.

The miniport driver must unconditionally set all of the counters in the DOT11\_STATISTICS structure to zero, including MAC-layer and PHY-layer counters, when one of the following occurs:

-   The driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   The driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function is called with a method request of the [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) OID, regardless of the type of reset operation specified in the set request.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_STATISTICS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


