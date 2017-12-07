---
title: Native 802.11 associaton status codes
author: windows-driver-content
description: This section describes Native 802.11 associaton status codes.
ms.assetid: d3942045-6bad-461e-bd79-ba129a5bd7de
keywords:
- Native 802.11 associaton status codes network drivers
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DOT11_ASSOC_STATUS status codes

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The DOT11_ASSOC_STATUS data type defines a range of values that the Native 802.11 miniport driver uses to specify the results of a connection, association, disassociation, or roaming network operation.

## Syntax

```c++
typedef ULONG DOT11_ASSOC_STATUS;
```

## Status codes

Available status codes are defined as follows:

**DOT11_ASSOC_STATUS_SUCCESS**  
The network operation completed successfully.

**DOT11_ASSOC_STATUS_FAILURE**  
The network operation completed with a failure.  
> [!NOTE]
> The Native 802.11 miniport driver must only specify **DOT11_ASSOC_STATUS_FAILURE** if other DOT11_ASSOC_STATUS values, which are defined below, are not appropriate.
 
**DOT11_ASSOC_STATUS_UNREACHABLE**  
The network operation failed because the 802.11 station determined that the peer station or access point (AP) is unresponsive due to one of the following reasons: 

- The 802.11 station did not receive an 802.11 Authentication frame from the peer station or AP during the association or roaming operation.
- The 802.11 station did not receive an 802.11-Association or Reassociation Response frame from the AP during the association or roaming operation.
- The 802.11 station did not receive an 802.11 Probe Response frame from the peer station or AP after the station sent an 802.11 Probe Request frame.
- The 802.11 station no longer receives 802.11 Beacon frames from the peer station or AP.
- The 802.11 station determines the peer station or AP to be unresponsive due to other proprietary methods specific to the implementation by the independent hardware vendor (IHV).

**DOT11_ASSOC_STATUS_RADIO_OFF**  
The network operation failed because the radio is turned off on the 802.11 station.

**DOT11_ASSOC_STATUS_PHY_DISABLED**  
The network operation failed because the PHY, which was being used for the operation, has been disabled.  
> [!NOTE]
> This status code is only applicable for PHYs that can be disabled on the 802.11 station through proprietary methods developed by the IHV.
 
**DOT11_ASSOC_STATUS_CANCELLED**  
A pending network operation failed because one of the following occurred: 

- The Native 802.11 miniport driver issued a set request of [OID_DOT11_RESET_REQUEST](oid-dot11-reset-request.md).
- The Native 802.11 miniport driver issued a set request of [OID_DOT11_DISCONNECT_REQUEST](oid-dot11-disconnect-request.md).

**DOT11_ASSOC_STATUS_CANDIDATE_LIST_EXHAUSTED**  
A pending connection or roaming operation failed because the 802.11 station could not successfully associate with any peer station or AP from its [BSS Network Candidate List](bss-network-candidate-list.md).

**DOT11_ASSOC_STATUS_DISASSOCIATED_BY_OS**  
If the 802.11 station is associated to a basic service set (BSS) network and is not performing a roaming operation, the Native 802.11 miniport driver uses this status code in its [NDIS_STATUS_DOT11_DISASSOCIATION](ndis-status-dot11-disassociation.md) status indication whenever one of the following OIDs is set: 

- [OID_DOT11_RESET_REQUEST](oid-dot11-reset-request.md) 
- [OID_DOT11_DISCONNECT_REQUEST](oid-dot11-disconnect-request.md)

**DOT11_ASSOC_STATUS_DISASSOCIATED_BY_ROAMING**  
This status code is reserved for use by the operating system for indications that it generates following an implicit disassociation operation performed by the Native 802.11 miniport driver. For more information about this operation, see [Implicit Disassociation Operations](implicit-disassociation-operations.md).

**DOT11_ASSOC_STATUS_DISASSOCIATED_BY_RESET**  
A pending network operation failed because the Native 802.11 miniport driver failed in a call to an NDIS API.

For example, the miniport driver would cancel the pending operation and return a status code of **DOT11_ASSOC_STATUS_DISASSOCIATED_BY_RESET** if the call to [NdisAllocateIoWorkItem](https://msdn.microsoft.com/library/windows/hardware/ff561604) failed.

If the 802.11 station is associated to a BSS network and is not performing a roaming operation, the Native 802.11 miniport driver uses this status code in its [NDIS_STATUS_DOT11_DISASSOCIATION](ndis-status-dot11-disassociation.md) status indication whenever one of the following OIDs is set:

- [OID_DOT11_RESET_REQUEST](oid-dot11-reset-request.md) 
- [OID_DOT11_DISCONNECT_REQUEST](oid-dot11-disconnect-request.md)

**DOT11_ASSOC_STATUS_ROAMING_BETTER_AP_FOUND**  
If a roaming operation is pending, the Native 802.11 miniport driver can cancel the operation and return this status code if the 802.11 station detects a better BSS candidate. In this situation, the driver must do the following: 

- Make an [NDIS_STATUS_DOT11_ROAMING_COMPLETION](ndis-status-dot11-roaming-completion.md) indication and set the **uStatus** member of the [DOT11_ROAMING_COMPLETION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff548762) structure to **DOT11_ASSOC_STATUS_ROAMING_BETTER_AP_FOUND**.
- Make an [NDIS_STATUS_DOT11_ROAMING_START](ndis-status-dot11-roaming-start.md) indication before attempting to roam to the new BSS candidate.

For more information about the roaming operation, see [Roaming Operations](roaming-operations.md).

**DOT11_ASSOC_STATUS_ROAMING_ASSOCIATION_LOST**  
If the 802.11 station is associated with a BSS network and receives either an 802.11 Disassociation or Deauthentication frame from the AP, the miniport driver makes an [NDIS_STATUS_DOT11_ROAMING_START](ndis-status-dot11-roaming-start.md) indication and sets the **uRoamingReason** member of the [DOT11_ROAMING_START_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff548764) structure to **DOT11_ASSOC_STATUS_ROAMING_ASSOCIATION_LOST**. 
> [!NOTE]
> **DOT11_ASSOC_STATUS_ROAMING_ASSOCIATION_LOST** is a generic status code that defines the reason for initiating a roaming operation after an association is lost. When making the [NDIS_STATUS_DOT11_ROAMING_START](ndis-status-dot11-roaming-start.md) indication following the receipt of an 802.11 Disassociation or Deauthentication frame, the miniport driver can use a more explicit status code. In this situation, the driver sets the **uRoamingReason** member of the [DOT11_ROAMING_START_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff548764) structure to the value used to set the **uRoamingReason** member of the [DOT11_DISASSOCIATION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff547682) structure when the driver made the [NDIS_STATUS_DOT11_DISASSOCIATION](ndis-status-dot11-disassociation.md) status indication.
 
**DOT11_ASSOC_STATUS_ROAMING_ADHOC**  
If the 802.11 station is associated with an independent BSS (IBSS) network, the miniport driver can roam to another IBSS network with the same service set identifier (SSID). In this situation, the driver roams from a smaller to a larger IBSS network. 

Before the 802.11 station performs the roaming operation, the miniport driver makes an [NDIS_STATUS_DOT11_ROAMING_START](ndis-status-dot11-roaming-start.md) status indication and sets the **uRoamingReason** member of the [DOT11_ROAMING_START_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff548764) structure to **DOT11_ASSOC_STATUS_ROAMING_ADHOC**.

**DOT11_ASSOC_STATUS_PEER_DEAUTHENTICATED**  
Specifies the status code related to BSS network deauthentication. The miniport driver returns the value of the Reason Code field from the 802.11 deauthentication frame through the following: 

( **DOT11_ASSOC_STATUS_PEER_DEAUTHENTICATED** | Reason Code)

The Native 802.11 miniport driver uses this status code when one of the following occurs:

- The 802.11 station is associated with a peer station or access point (AP), which sends the station an 802.11 deauthentication frame. In this situation, the miniport driver makes an [NDIS_STATUS_DOT11_DISASSOCIATION](ndis-status-dot11-disassociation.md) status indication and sets the **uReason** member of the [DOT11_DISASSOCIATION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff547682) structure to:

( **DOT11_ASSOC_STATUS_PEER_DEAUTHENTICATED** | Reason Code)

- The 802.11 station is associating with a peer station or AP, which sends the station an 802.11 deauthentication frame. In this situation, the miniport driver makes an [NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION](ndis-status-dot11-association-completion.md) status indication and sets the **uReason** member of the [DOT11_ASSOCIATION_COMPLETION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff547647) structure to:

( **DOT11_ASSOC_STATUS_PEER_DEAUTHENTICATED** | Reason Code)

For more information about the Reason Code field, refer to Clause 8.4.1.7 of the IEEE 802.11-2012 standard.

**DOT11_ASSOC_STATUS_PEER_DISASSOCIATED**  
Specifies the status code related to BSS network disassociation. The miniport driver returns the value of the Reason Code field from the 802.11 Disassociation frame through the following: 

( **DOT11_ASSOC_STATUS_PEER_DISASSOCIATED** | Reason Code)
The Native 802.11 miniport driver uses this status code when configured for IBSS network operations and one of the following occurs:

- The 802.11 station is associated with an AP, which sends the 802.11 station an 802.11 disassociation frame from the peer station. In this situation, the miniport driver makes an [NDIS_STATUS_DOT11_DISASSOCIATION](ndis-status-dot11-disassociation.md) status indication and sets the **uReason** member of the [DOT11_DISASSOCIATION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff547682) structure to:

( **DOT11_ASSOC_STATUS_PEER_DISASSOCIATED** | Reason Code)

- The 802.11 station is associating with an AP, which sends the station an 802.11 disassociation frame from the peer station. In this situation, the miniport driver makes an [NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION](ndis-status-dot11-association-completion.md) status indication and sets the **uReason** member of the [DOT11_ASSOCIATION_COMPLETION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff547647) structure to:

( **DOT11_ASSOC_STATUS_PEER_DISASSOCIATED** | Reason Code)

For more information about the Reason Code field, refer to Clause 8.4.1.7 of the IEEE 802.11-2012 standard.

**DOT11_ASSOC_STATUS_ASSOCIATION_RESPONSE**  
Specifies the status code related to BSS network association. The miniport driver returns the value of the Status Code field from either the 802.11 Association Response or Authentication frame through the following:

( **DOT11_ASSOC_STATUS_ASSOCIATION_RESPONSE** | Status Code)

The Native 802.11 miniport driver performs an association operation with an AP, which sends the station either an 802.11 Association Response or Authentication frame with a nonzero value for the Status Code field. In this situation, the miniport driver makes an [NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION](ndis-status-dot11-association-completion.md) status indication and sets the **uStatus** member of the [DOT11_ASSOCIATION_COMPLETION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff547647) structure to:

( **DOT11_ASSOC_STATUS_ASSOCIATION_RESPONSE** | Status Code)

For more information about the Status Code field, refer to Clause 8.4.1.9 of the IEEE 802.11-2012 standard.

**DOT11_ASSOC_STATUS_IHV_START**  
Specifies the start of the range of values that can be used by the IHV to define proprietary status codes for BSS network operations.

**DOT11_ASSOC_STATUS_IHV_END**  
Specifies the end of the range of values used for proprietary status codes for BSS network operations.

## Remarks

For more information about network operations performed by a Native 802.11 miniport driver, see [Native 802.11 Network Operations](native-802-11-network-operations.md).

## Requirements

|   |   |
| --- | --- |
| Version | Available in Windows Vista and later versions of the Windows operating systems. |
| Header | Windot11.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")