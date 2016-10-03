---
title: Extensible Station Operation Mode
description: Extensible Station Operation Mode
ms.assetid: c38a7b82-7584-4b86-8ca9-b0d86de034c4
keywords: ["operation modes WDK Native 802.11", "Extensible Station operation modes WDK Native 802.11", "ExtSTA operation modes WDK Native 802.11"]
---

# Extensible Station Operation Mode


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

In the Extensible Station (ExtSTA) operation mode, the 802.11 station operates as a wireless LAN (WLAN) mobile station and is responsible for the following:

-   The 802.11 station must process all media access control (MAC) frame formats for the 802.11 protocols that it supports.

    The 802.11 station processes all received MAC protocol data units (MPDU) and MAC management protocol data unit (MMPDU) frames. However, depending on the 802.11 filter settings in the packet filter, the miniport driver can indicate these frames to NDIS through a call to [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). For example, if the packet filter has the NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_MGMT bit set, the miniport driver must indicate any directed or unicast 802.11 MMPDU frames that the station receives.

    For more information about the 802.11 packet filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

-   The 802.11 station must implement all required MAC functions, as specified in Clause 9 of the IEEE 802.11-2012 standard. The 802.11 station can also support the optional point coordination function (PCF), as defined in Clause 9.4 of the IEEE 802.11-2012 standard.

-   The 802.11 station must implement all MAC-layer management entity (MLME) services, as specified in Clause 6.3 of the IEEE 802.11-2012 standard. The operating system configures the MAC and invokes an MLME service through Native 802.11 object identifiers (OIDs) that are processed by the miniport driver.

    For more information about Native 802.11 objects, see [Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691).

-   The 802.11 station must implement all physical-layer management entity (PLME) services, as specified in Clause 6.5 of the IEEE 802.11-2012 standard. The operating system configures the PHY and invokes a PLME service through Native 802.11 OIDs that are processed by the miniport driver.

-   The 802.11 station must perform all data encryption and fragmentation for each MAC service data unit (MSDU) packet or MMPDU frame delivered to the miniport driver for transmission. For more information about this process, see [Native 802.11 Send Operations](native-802-11-send-operations.md).

    In addition, the 802.11 station must perform all data encryption and fragmentation for all MMPDU sent by the station itself.

-   The 802.11 station must perform all data decryption, payload verification, and fragment reassembly for each MAC service data unit (MSDU) packet indicated by the miniport driver for reception. For more information about these processes, see [Native 802.11 Receive Operations](native-802-11-receive-operations.md).

The ExtSTA operation mode requires the miniport driver to support the Native 802.11 NDIS object identifier (OID) interface for the configuration of 802.11 MAC/PHY MIB attributes. Because the 802.11 MAC protocols are processed by the 802.11 station, the ExtSTA operation mode also requires the miniport driver to support a Native 802.11 NDIS OID interface for the configuration of basic service set (BSS) network parameters, such as BSS type and service set identifier (SSID). For more information about the Native 802.11 NDIS OID interface, see [Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691). For more information about ExtSTA OIDs, see [Native 802.11 Extensible Station OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560602).

The IHV can support proprietary or non-standard 802.11 extensions through a miniport driver that operates in ExtSTA mode. For more information about this, see [Extending Native 802.11 Functionality](extending-native-802-11-functionality.md).

 

 





