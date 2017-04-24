---
title: Performing Explicit Scan Operations
description: Performing Explicit Scan Operations
ms.assetid: b86acf15-5321-4fa3-bcf8-5ccd87c3db71
keywords:
- explicit scan operations WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing Explicit Scan Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The 802.11 station performs the explicit scan operation following an OID set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). The parameters for the scan operation are defined through the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure, which accompanies the set request.

Following the OID set request of the [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) object identifier (OID), the miniport driver invokes the 802.11 station's media access control (MAC) layer management entity (MLME) MLME-SCAN.request service primitive. For more information about this service primitive, refer to Clause 6.3.3 of the IEEE 802.11-2012 standard.

When performing the implicit scan operation, the miniport driver and 802.11 station must follow these guidelines::

-   The miniport driver must initiate the explicit scan request by the 802.11 station and complete the OID set request of the [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) OID. The miniport driver must not wait for the scan operation to finish before completing the set request. The miniport driver must return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function after initiating the scan operation.

-   The 802.11 station must cancel any implicit scan operations that it is currently performing. The miniport driver must restrict the 802.11 station from performing implicit scan operations while the explicit scan operation is in progress.

-   The 802.11 station must perform only one explicit scan operation for each OID set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). The miniport driver cannot initiate another explicit scan operation by the 802.11 station until the operating system issues another OID set request of OID\_DOT11\_SCAN\_REQUEST.

-   If the miniport driver is operating in Extensible Station (ExtSTA) mode, retain its basic service set (BSS) network cache. The miniport driver must only clear the cache when [OID\_DOT11\_FLUSH\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569367) is set.

-   If an explicit scan operation is in progress when a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made or the [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function is called, cancel the scan operation.

If the 802.11 station performs an active scan, it must transmit an 802.11 Probe Request frame on every channel that it scans. The 802.11 station prepares each Probe Request frame in the following way:

-   The BSS identifier (BSSID) field of the 802.11 MAC header is set to the value of the **dot11BSSID** member of the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure. If this member has a value of zero, the BSSID field must be set to the wildcard BSSID value of 0xFFFFFFFFFFFF.

-   The SSID IE is set to an entry from the SSID list that is defined through the **udot11SSIDsOffset** and **uNumOfdot11SSIDs** members of the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure. The 802.11 station must send a Probe Request frame for each SSID entry in the list.

-   If the list is empty (as indicated by a zero value for the **uNumOfdot11SSIDs** member), the station must send a single Probe Request frame and set the SSID IE to the wildcard zero-length SSID.

-   If the IEEE 802.11d **dot11MultiDomainCapabilityEnabled** management information base (MIB) object is set to **TRUE** and the **bUseRequestIE** member of the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure is set to **TRUE**, the 802.11 station must prepare an 802.11d Request information element (IE) at the end of the Probe Request frame. The station must set the Length subfield of the IE to the value of the **uNumOfRequestIDs** member and must copy the list of Request IDs after the Length subfield. For more information about the **dot11MultiDomainCapabilityEnabled** MIB object, see [OID\_DOT11\_MULTI\_DOMAIN\_CAPABILITY\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390).

    The 802.11 station can add entries to the list of Request IDs, but must insert each Request ID in the Request IE in order of increasing element ID.

    For more information about the 802.1d Request IE and Request IDs, refer to clause 7.3.2.15 of the IEEE 802.11d-2001 standard.

-   If the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure defines a list of information elements (IEs), the 802.11 station must copy the list of IEs to the end of the Probe Response frame. The list of IEs is defined through the **uIEsOffset** and **uIEsLength** members.

If the miniport driver's current packet filter has enabled the NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_MGMT or NDIS\_PACKET\_TYPE\_802\_11\_BROADCAST\_MGMT filter settings, the miniport driver must call [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) for all 802.11 Beacon and Probe Response frames received by the 802.11 station. When performing the scan operation, the miniport driver must indicate these frames regardless of whether the 802.11 station received the frames as part of the scan operation. For more information about the 802.11 packet filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

The 802.11 station completes the explicit scan operation when one of the following occurs:

-   The 802.11 station has scanned all specified channels for each PHY specified in the [**DOT11\_SCAN\_REQUEST\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548767) structure.

-   The scan operation is canceled through a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) or a call to the miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function.

-   The scan operation is canceled whenever all PHYs that are used for the scan operation are turned off through either an OID set request of [OID\_DOT11\_NIC\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392) or through some proprietary object identifier (OID) or hardware switch developed by the independent hardware vendor (IHV). In this situation, the miniport driver must set the **ndisStatus** member of the [NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM](https://msdn.microsoft.com/library/windows/hardware/ff567364) indication to NDIS\_STATUS\_UNSUPPORTED\_MEDIA.

After the scan operation completes, the miniport driver must make a media-specific [NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM](https://msdn.microsoft.com/library/windows/hardware/ff567364) indication. The miniport driver must also make this indication when the scan operation is canceled through a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) or a call to the miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function.

If the miniport driver is operating in ExtSTA mode, a method request of [OID\_DOT11\_ENUM\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360) can be made to return a list of BSS networks detected during the scan operation. The OID\_DOT11\_ENUM\_BSS\_LIST OID returns the cached list regardless of the scan state and should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE.

 

 





