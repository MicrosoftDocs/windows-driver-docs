---
title: Association Operation Guidelines for Extensible Access Point (ExtAP) Mode
description: Association Operation Guidelines for Extensible Access Point (ExtAP) Mode
ms.assetid: 6fd31cb7-dbef-4885-9ee2-131f65b6f8f7
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Association Operation Guidelines for Extensible Access Point (ExtAP) Mode


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When an 802.11 station is in Extensible Access Point (ExtAP) mode, the miniport driver and 802.11 station must follow the guidelines defined in [General Association Operation Guidelines](general-association-operation-guidelines.md) and [Association Operation Guidelines for Infrastructure BSS Networks](association-operation-guidelines-for-infrastructure-bss-networks.md).

In addition, the miniport driver and 802.11 station must follow these guidelines when associating with a peer station:

1.  The NIC issues an [NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_REQUEST\_RECEIVED](https://msdn.microsoft.com/library/windows/hardware/ff567339) indication to the operating system.

2.  After the operating system receives the association request indication, if it decides to make the association it calls the direct OID [OID\_DOT11\_INCOMING\_ASSOCIATION\_DECISION](https://msdn.microsoft.com/library/windows/hardware/ff569379). The operating system can optionally specify additional information elements (IEs) that the NIC must add to the association response frame. The operating system does this by setting values for the **uAssocResponseIEsOffset** and **uAssocResponseIEsLength** members of the [**DOT11\_INCOMING\_ASSOC\_DECISION**](https://msdn.microsoft.com/library/windows/hardware/ff548654) structure. The operating system will only make this OID call after it receives an NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_REQUEST\_RECEIVED indication.

3.  The NIC should accept the association request only if both it and the operating system decide to accept the association request. If so, the NIC should send an association response packet that indicates that it accepts the association request. Otherwise, the NIC should send an association response packet that indicates that it does not accept the association request.

4.  The NIC makes an [NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567338) status indication when it completes the association with the peer station, whether or not the association is successful. If the association is successful, the 802.11 miniport driver should indicate all data related to the association in the corresponding [**DOT11\_INCOMING\_ASSOC\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548650) structure. This data includes the current authentication and cipher algorithms ( **AuthAlgo**, **UnicastCipher**, and **MulticastCipher** ), and the latest Beacon frame data ( **uBeaconOffset** and **uBeaconSize**).

For each successful association, a port authorization procedure can be performed by the operating system. In this procedure, the operating system adds encryption keys and/or message integrity keys, as described in [Native 802.11 Authentication Operations](native-802-11-authentication-operations.md). After a previously associated client is disassociated, the miniport driver should remove the pair-wise key for that client from the [key table](key-mapping-keys.md).

 

 





