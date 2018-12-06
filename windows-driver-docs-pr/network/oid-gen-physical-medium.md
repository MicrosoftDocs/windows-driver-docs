---
title: OID_GEN_PHYSICAL_MEDIUM
description: As a query, the OID_GEN_PHYSICAL_MEDIUM OID specifies the types of physical media that the NIC supports.
ms.assetid: 84d7231b-8af2-4bdb-8df5-37088767f708
ms.date: 08/08/2017
keywords: 
 -OID_GEN_PHYSICAL_MEDIUM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_PHYSICAL\_MEDIUM


As a query, the OID\_GEN\_PHYSICAL\_MEDIUM OID specifies the types of physical media that the NIC supports. This OID is essentially an extension of [OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md).

**Version Information**

**Note**  This OID is supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use [OID\_GEN\_PHYSICAL\_MEDIUM\_EX](oid-gen-physical-medium-ex.md).

 

Remarks
-------

NDIS handles this OID for miniport drivers. The miniport driver supplies the physical medium value during initialization.

Miniport drivers report a physical media type to differentiate their physical media from media that they declared to support in the [OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md) OID query. These media types are listed as a proper subset of the following system-defined values from the **NDIS\_PHYSICAL\_MEDIUM** enumeration:

**NdisPhysicalMediumUnspecified**
The physical medium is none of the preceding mediums. For example, a one-way satellite feed is an unspecified physical medium.

**NdisPhysicalMediumWirelessLan**
Packets are transferred over a wireless LAN network through a miniport driver that conforms to the 802.11 interface. For more information about this interface, see. [802.11 Wireless LAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543933)

**NdisPhysicalMediumCableModem**
Packets are transferred over a DOCSIS-based cable network.

**NdisPhysicalMediumPhoneLine**
Packets are transferred over standard phone lines.
Includes, for example, HomePNA media.
**NdisPhysicalMediumPowerLine**
Packets are transferred over wiring that is connected to a power distribution system.

**NdisPhysicalMediumDSL**
Packets are transferred over a Digital Subscriber Line (DSL) network.
Includes, for example, ADSL and UADSL (G.Lite).
**NdisPhysicalMediumFibreChannel**
Packets are transferred over a Fibre Channel interconnect.

**NdisPhysicalMedium1394**
Packets are transferred over an IEEE 1394 bus.

**NdisPhysicalMediumWirelessWan**
Packets are transferred over a Wireless WAN link. Includes, for example, CDPD, CDMA, and GPRS.

<a href="" id="ndisphysicalmediumnative802-11"></a>**NdisPhysicalMediumNative802\_11**
Packets are transferred over a wireless LAN network through a miniport driver that conforms to the Native 802.11 interface. For more information about this interface, see [Native 802.11 Wireless LAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff560648).

**Note**  The Native 802.11 interface is supported in NDIS 6.0 and later and later and later versions.

 

**NdisPhysicalMediumBluetooth**
Packets are transferred over a Bluetooth network. Bluetooth is a short-range wireless technology that uses the 2.4 GHz spectrum.

**NdisPhysicalMediumInfiniband**
The Infiniband physical medium. Packets are transferred over an infiniband interconnect.

**NdisPhysicalMediumUWB**
The Ultra Wideband (UWB) physical medium. Packets are transferred over a UWB network. UWB is a radio frequency platform that personal area networks can use to wirelessly communicate over short distances at high speeds.

<a href="" id="ndisphysicalmedium802-3"></a>**NdisPhysicalMedium802\_3**
The Ethernet (802.3) physical medium. Packets are transferred over a wired LAN through a miniport driver that conforms to the 802.3 interface specification. This medium type does not include devices that emulate 802.3.

<a href="" id="ndisphysicalmedium802-5"></a>**NdisPhysicalMedium802\_5**
The Token Ring physical medium. (802.5 is not supported in NDIS 6.0 and later and later drivers.) Packets are transferred over a Token Ring network through a miniport driver that conforms to the 802.5 interface specification.

**NdisPhysicalMediumIrda**
The infrared (IrDA) physical medium. Packets are transferred over a nonvisible, infrared light spectrum IrDA network.

**NdisPhysicalMediumWiredWAN**
The wired, wide area network (WAN) physical medium. Packets are transferred over a wired WAN.

**NdisPhysicalMediumWiredCoWan**
The wired, connection-oriented WAN physical medium. Packets are transferred over a wired WAN in a connection-oriented environment.

**NdisPhysicalMediumOther**
The physical medium is none of the preceding mediums. **NdisPhysicalMediumOther** specifies a new physical medium type that is not present in the NDIS\_PHYSICAL\_MEDIUM enumeration.

NDIS supports the OID\_GEN\_PHYSICAL\_MEDIUM OID for miniport adapters that support newer networks, even though those networks transfer packets that appear to the operating system and to NDIS as standard and well known media types.

Newer networks transfer packets that might appear like standard media but that might have new features or slight differences from the standard. This OID was developed so upper-layer drivers and applications could determine the actual networks to which a NIC connects. After retrieving information about underlying networks, upper-layer drivers and applications could use this information to modify how such drivers and applications behave.

To clearly distinguish an 802.3 NIC from an emulated 802.3 NIC for which there is no physical medium type defined, NDIS 6.0 and later and later and later versions require 802.3 miniport drivers to report **NdisPhysicalMedium802\_3**.

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
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="oid-gen-physical-medium-ex.md" data-raw-source="[OID_GEN_PHYSICAL_MEDIUM_EX](oid-gen-physical-medium-ex.md)">OID_GEN_PHYSICAL_MEDIUM_EX</a> instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md)

[OID\_GEN\_PHYSICAL\_MEDIUM\_EX](oid-gen-physical-medium-ex.md)

 

 




