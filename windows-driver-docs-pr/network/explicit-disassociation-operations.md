---
title: Explicit Disassociation Operations
description: Explicit Disassociation Operations
ms.assetid: 006946b6-39ee-4e71-9d4e-72ef64e74e86
keywords: ["disassociation operations WDK Native 802.11", "explicit disassociation operations WDK Native 802.11"]
---

# Explicit Disassociation Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver performs an explicit disassociation operation after the 802.11 station has successfully connected to a BSS network and one of the following occurs:

-   The access point (AP) or peer station with which the 802.11 station is associated sends an 802.11 frame to the station to end the association. Examples of the 802.11 frames that could end an association are:
    -   802.11 Disassociation frames.
    -   802.11 Deauthentication frames.
    -   Frames specific to proprietary or non-standard association algorithms developed by an independent hardware vendor (IHV).
-   The 802.11 station has not detected the presence of the AP or peer station within the basic service set (BSS) network to which the 802.11 station is connected. In this situation, the 802.11 station has not received any frames, including 802.11 Beacon frames, for more than the timeout threshold defined by the Extensible Station (ExtSTA) **msDot11UnreachableDetectionThreshold** management information base (MIB) object. For more information about this MIB object, see [OID\_DOT11\_UNREACHABLE\_DETECTION\_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569434).

-   The 802.11 station disconnects from the BSS network following a set request of [OID\_DOT11\_DISCONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569147) or a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409). In this situation, the miniport driver must perform an explicit disassociation operation with the access point (AP) or every independent BSS (IBSS) peer station with which it is currently associated.

    **Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).

     

The miniport driver must make an [NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334) indication when it disassociates with an AP or peer station. The miniport driver provides the following information regarding the disassociation operation within the indication:

-   A code that defined the reason for the disassociation.

-   The media access control (MAC) address of the AP or peer station with which the 802.11 station has disassociated.

-   The Reason Code field from the received 802.11 Deauthentication or Disassociation frame, if such a frame was the cause of the disassociation.

**Note**  The miniport driver must not make a status indication of NDIS\_STATUS\_MEDIA\_DISCONNECT when performing the disassociation operation.

 

If the authentication algorithm that was used on the association requires port authorization for network access, the operating system will delete the port that was used for network access after the miniport driver indicates [NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334). For more information about this process, see [Port-Based Network Access](port-based-network-access.md).

If the 802.11 station is connected to an IBSS network and receives an 802.11 Deauthentication frame from a peer station, the miniport driver must do the following:

-   Make an [NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334) indication, following the guidelines described above.

-   Delete the entry from the miniport driver's key-mapping and per-station key tables as referenced by the MAC address of the peer station. For more information about these types of keys, see [802.11 Cipher Key Types](802-11-cipher-key-types.md).

 

 





