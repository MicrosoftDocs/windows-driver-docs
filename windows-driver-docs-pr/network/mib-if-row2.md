---
title: MIB_IF_ROW2 structure (Windows Drivers)
description: Learn more about the MIB_IF_ROW2 structure.
keywords:
- MIB_IF_ROW2
- PMIB_IF_ROW2
- netioapi/MIB_IF_ROW2
- netioapi/PMIB_IF_ROW2
ms.date: 10/25/2022
---

# MIB\_IF\_ROW2 structure

The MIB\_IF\_ROW2 structure stores information about a particular interface.

## Syntax

``` c++
typedef struct _MIB_IF_ROW2 {
  NET_LUID                   InterfaceLuid;
  NET_IFINDEX                InterfaceIndex;
  GUID                       InterfaceGuid;
  WCHAR                      Alias[IF_MAX_STRING_SIZE + 1];
  WCHAR                      Description[IF_MAX_STRING_SIZE + 1];
  ULONG                      PhysicalAddressLength;
  UCHAR                      PhysicalAddress[IF_MAX_PHYS_ADDRESS_LENGTH];
  UCHAR                      PermanentPhysicalAddress[IF_MAX_PHYS_ADDRESS_LENGTH];
  ULONG                      Mtu;
  IFTYPE                     Type;
  TUNNEL_TYPE                TunnelType;
  NDIS_MEDIUM                MediaType;
  NDIS_PHYSICAL_MEDIUM       PhysicalMediumType;
  NET_IF_ACCESS_TYPE         AccessType;
  NET_IF_DIRECTION_TYPE      DirectionType;
  struct {
    BOOLEAN HardwareInterface  :1;
    BOOLEAN FilterInterface  :1;
    BOOLEAN ConnectorPresent  :1;
    BOOLEAN NotAuthenticated  :1;
    BOOLEAN NotMediaConnected  :1;
    BOOLEAN Paused  :1;
    BOOLEAN LowPower  :1;
    BOOLEAN EndPointInterface  :1;
  } InterfaceAndOperStatusFlags;
  IF_OPER_STATUS             OperStatus;
  NET_IF_ADMIN_STATUS        AdminStatus;
  NET_IF_MEDIA_CONNECT_STATE MediaConnectState;
  NET_IF_NETWORK_GUID        NetworkGuid;
  NET_IF_CONNECTION_TYPE     ConnectionType;
  ULONG64                    TransmitLinkSpeed;
  ULONG64                    ReceiveLinkSpeed;
  ULONG64                    InOctets;
  ULONG64                    InUcastPkts;
  ULONG64                    InNUcastPkts;
  ULONG64                    InDiscards;
  ULONG64                    InErrors;
  ULONG64                    InUnknownProtos;
  ULONG64                    InUcastOctets;
  ULONG64                    InMulticastOctets;
  ULONG64                    InBroadcastOctets;
  ULONG64                    OutOctets;
  ULONG64                    OutUcastPkts;
  ULONG64                    OutNUcastPkts;
  ULONG64                    OutDiscards;
  ULONG64                    OutErrors;
  ULONG64                    OutUcastOctets;
  ULONG64                    OutMulticastOctets;
  ULONG64                    OutBroadcastOctets;
  ULONG64                    OutQLen;
} MIB_IF_ROW2, *PMIB_IF_ROW2;
```

## Members

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface.

- **InterfaceIndex**  
   The index that identifies the network interface. This index value might change when a network adapter is disabled and then enabled, and should not be considered persistent.

- **InterfaceGuid**  
   The GUID for the network interface.

- **Alias**  
   A NULL-terminated Unicode string that contains the alias name of the network interface.

- **Description**  
   A NULL-terminated Unicode string that contains a description of the network interface.

- **PhysicalAddressLength**  
   The length, in bytes, of the physical hardware address that the PhysicalAddress member specifies.

- **PhysicalAddress**  
   The physical hardware address of the adapter for this network interface.

- **PermanentPhysicalAddress**  
   The permanent physical hardware address of the adapter for this network interface.

- **Mtu**  
   The maximum transmission unit (MTU) size, in bytes, for this network interface.

- **Type**  
   The interface type as defined by the Internet Assigned Names Authority (IANA). For more information, see [IANAifType-MIB DEFINITIONS](https://go.microsoft.com/fwlink/p/?linkid=60066). Possible values for the interface type are listed in the Ipifcons.h header file.

    The following table lists common values for the interface type, although many other values are possible.

    <table>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>IF_TYPE_OTHER</p>
    <p>1</p></td>
    <td><p>Some other type of network interface</p></td>
    </tr>
    <tr class="even">
    <td><p>IF_TYPE_ETHERNET_CSMACD</p>
    <p>6</p></td>
    <td><p>An Ethernet network interface</p></td>
    </tr>
    <tr class="odd">
    <td><p>IF_TYPE_ISO88025_TOKENRING</p>
    <p>9</p></td>
    <td><p>A token ring network interface</p></td>
    </tr>
    <tr class="even">
    <td><p>IF_TYPE_PPP</p>
    <p>23</p></td>
    <td><p>A PPP network interface</p></td>
    </tr>
    <tr class="odd">
    <td><p>IF_TYPE_SOFTWARE_LOOPBACK</p>
    <p>24</p></td>
    <td><p>A software loopback network interface</p></td>
    </tr>
    <tr class="even">
    <td><p>IF_TYPE_ATM</p>
    <p>37</p></td>
    <td><p>An ATM network interface</p></td>
    </tr>
    <tr class="odd">
    <td><p>IF_TYPE_IEEE80211</p>
    <p>71</p></td>
    <td><p>An IEEE 802.11 wireless network interface</p></td>
    </tr>
    <tr class="even">
    <td><p>IF_TYPE_TUNNEL</p>
    <p>131</p></td>
    <td><p>A tunnel type encapsulation network interface</p></td>
    </tr>
    <tr class="odd">
    <td><p>IF_TYPE_IEEE1394</p>
    <p>144</p></td>
    <td><p>An IEEE 1394 (Firewire) high performance serial bus network interface</p></td>
    </tr>
    </tbody>
    </table>

- **TunnelType**  
   If the Type member is IF\_TYPE\_TUNNEL, a [**TUNNEL\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-tunnel_type) type that defines the encapsulation method that a tunnel uses.

- **MediaType**  
   The NDIS media type for the interface. This member can be one of the following values from the NDIS\_MEDIUM enumeration type that is defined in the Ntddndis.h header file.

    <table>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>NdisMedium802_3</p>
    <p>0</p></td>
    <td><p>An Ethernet (802.3) network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMedium802_5</p>
    <p>1</p></td>
    <td><p>A Token Ring (802.5) network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumFddi</p>
    <p>2</p></td>
    <td><p>A Fiber Distributed Data Interface (FDDI) network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumWan</p>
    <p>3</p></td>
    <td><p>A wide area network (WAN). This type covers various forms of point-to-point and WAN NICs and variant address/header formats that must be negotiated between the protocol driver and the underlying driver after the binding is established.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumLocalTalk</p>
    <p>4</p></td>
    <td><p>A LocalTalk network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumDix</p>
    <p>5</p></td>
    <td><p>An Ethernet network for which the drivers use the DIX Ethernet header format.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumArcnetRaw</p>
    <p>6</p></td>
    <td><p>An ARCNET network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumArcnet878_2</p>
    <p>7</p></td>
    <td><p>An ARCNET (878.2) network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumAtm</p>
    <p>8</p></td>
    <td><p>An ATM network. Connection-oriented client protocol drivers can bind themselves to an underlying miniport driver that returns this value. Otherwise, legacy protocol drivers bind themselves to the system-supplied LanE intermediate driver, which reports its medium type as either <strong>NdisMedium802_3</strong> or NdisMedium802_5, depending on how the network administrator configures the LanE driver.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumWirelessWan</p>
    <p>9</p></td>
    <td><p>A wireless network. NDIS 5. x miniport drivers that support wireless LAN (WLAN) or wireless WAN (WWAN) packets declare their medium as <strong>NdisMedium802_3</strong> and emulate Ethernet to higher-level NDIS drivers.</p>
    <p>Note This media type is not available for use on Windows Vista or later versions of Windows.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumIrda</p>
    <p>10</p></td>
    <td><p>An infrared (IrDA) network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumBpc</p>
    <p>11</p></td>
    <td><p>A broadcast computer network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumCoWan</p>
    <p>12</p></td>
    <td><p>A wide area network in a connection-oriented environment.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMedium1394</p>
    <p>13</p></td>
    <td><p>An IEEE 1394 (fire wire) network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumInfiniBand</p>
    <p>14</p></td>
    <td><p>An InfiniBand network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumTunnel</p>
    <p>15</p></td>
    <td><p>A tunnel network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisMediumNative802_11</p>
    <p>16</p></td>
    <td><p>A native IEEE 802.11 network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisMediumLoopback</p>
    <p>17</p></td>
    <td><p>An NDIS loopback network.</p></td>
    </tr>
    </tbody>
    </table>

- **PhysicalMediumType**  
   The NDIS physical medium type. This member can be one of the following values from the NDIS\_PHYSICAL\_MEDIUM enumeration type that is defined in the Ntddndis.h header file.

    <table>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>NdisPhysicalMediumUnspecified</p>
    <p>0</p></td>
    <td><p>The physical medium is none of the following values. For example, a one-way satellite feed is an unspecified physical medium.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumWirelessLan</p>
    <p>1</p></td>
    <td><p>Packets are transferred over a wireless LAN network through a miniport driver that complies with the 802.11 interface.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumCableModem</p>
    <p>2</p></td>
    <td><p>Packets are transferred over a DOCSIS-based cable network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumPhoneLine</p>
    <p>3</p></td>
    <td><p>Packets are transferred over standard telephone lines. This type includes HomePNA media.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumPowerLine</p>
    <p>4</p></td>
    <td><p>Packets are transferred over wiring that is connected to a power distribution system.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumDSL</p>
    <p>5</p></td>
    <td><p>Packets are transferred over a Digital Subscriber Line (DSL) network. This type includes ADSL, UADSL (G.Lite), and SDSL.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumFibreChannel</p>
    <p>6</p></td>
    <td><p>Packets are transferred over a Fibre Channel interconnect.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMedium1394</p>
    <p>7</p></td>
    <td><p>Packets are transferred over an IEEE 1394 bus.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumWirelessWan</p>
    <p>8</p></td>
    <td><p>Packets are transferred over a Wireless WAN link. This type includes CDPD, CDMA and GPRS.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumNative802_11</p>
    <p>9</p></td>
    <td><p>Packets are transferred over a wireless LAN network through a miniport driver that complies with the Native 802.11 interface.</p>
    <p>Note The Native 802.11 interface is supported in NDIS 6.0 and later versions.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumBluetooth</p>
    <p>10</p></td>
    <td><p>Packets are transferred over a Bluetooth network. Bluetooth is a short-range wireless technology that uses the 2.4 GHz spectrum.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumInfiniband</p>
    <p>11</p></td>
    <td><p>Packets are transferred over an InfiniBand interconnect.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumUWB</p>
    <p>13</p></td>
    <td><p>Packets are transferred over an ultra wide band network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMedium802_3</p>
    <p>14</p></td>
    <td><p>Packets are transferred over an Ethernet (802.3) network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMedium802_5</p>
    <p>15</p></td>
    <td><p>Packets are transferred over a Token Ring (802.5) network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumIrda</p>
    <p>16</p></td>
    <td><p>Packets are transferred over an infrared (IrDA) network.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumWiredWAN</p>
    <p>17</p></td>
    <td><p>Packets are transferred over a wired WAN network.</p></td>
    </tr>
    <tr class="even">
    <td><p>NdisPhysicalMediumWiredCoWan</p>
    <p>18</p></td>
    <td><p>Packets are transferred over a wide area network in a connection-oriented environment.</p></td>
    </tr>
    <tr class="odd">
    <td><p>NdisPhysicalMediumOther</p>
    <p>19</p></td>
    <td><p>Packets are transferred over a network that is not described by other possible values.</p></td>
    </tr>
    </tbody>
    </table>

- **AccessType**  
   A [**NET\_IF\_ACCESS\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_access_type) NDIS network interface access type.

- **DirectionType**  
   A [**NET\_IF\_DIRECTION\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_direction_type) NDIS network interface direction type.

- **InterfaceAndOperStatusFlags**  
   A set of the following flags that provide information about the interface. These flags are combined with a bitwise OR operation. If none of the flags applies, this member is set to zero.

    - **HardwareInterface**  
       The network interface is for hardware.

    - **FilterInterface**  
       The network interface is for a filter module.

    - **ConnectorPresent**  
       A connector is present on the network interface. This value is set if there is a physical network adapter.

    - **NotAuthenticated**  
       The default port for the network interface is not authenticated. If a network interface is not authenticated by the target, the network interface is not in an operational mode. Although this situation applies to both wired and wireless network connections, authentication is more common for wireless network connections.

    - **NotMediaConnected**  
       The network interface is not in a media-connected state. If a network cable is unplugged for a wired network, this value is set. For a wireless network, this value is set for the network adapter that is not connected to a network.

    - **Paused**  
       The network stack for the network interface is in the paused or pausing state. This value does not mean that the computer is in a hibernated state.

    - **LowPower**  
       The network interface is in a low power state.

    - **EndPointInterface**  
       The network interface is an endpoint device and not a true network interface that connects to a network. This value can be set by devices, such as smartphones, that use networking infrastructure to communicate to the computer but do not provide connectivity to an external network. These types of devices must set this flag.

- **OperStatus**  
   A [**IF\_OPER\_STATUS**](/windows/win32/api/ifdef/ne-ifdef-if_oper_status) NDIS network interface operational status type.

- **AdminStatus**  
   The [**NET\_IF\_ADMIN\_STATUS**](/windows/win32/api/ifdef/ne-ifdef-net_if_admin_status) administrative status type.

- **MediaConnectState**  
   The [**NET\_IF\_MEDIA\_CONNECT\_STATE**](/windows/win32/api/ifdef/ne-ifdef-net_if_media_connect_state) connection state type.

- **NetworkGuid**  
   The GUID that is associated with the network that the interface belongs to.

- **ConnectionType**  
   A [**NET\_IF\_CONNECTION\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_connection_type) NDIS network interface connection type.

- **TransmitLinkSpeed**  
   The speed, in bits per second, of the transmit link.

- **ReceiveLinkSpeed**  
   The speed, in bits per second, of the receive link.

- **InOctets**  
   The number of octets of data that are received without errors through this interface. This value includes octets in unicast, broadcast, and multicast packets.

- **InUcastPkts**  
   The number of unicast packets that are received without errors through this interface.

- **InNUcastPkts**  
   The number of non-unicast packets that are received without errors through this interface. This value includes broadcast and multicast packets.

- **InDiscards**  
   The number of incoming packets that were discarded even though they did not have errors.

- **InErrors**  
   The number of incoming packets that were discarded because of errors.

- **InUnknownProtos**  
   The number of incoming packets that were discarded because the protocol was unknown.

- **InUcastOctets**  
   The number of octets of data that are received without errors in unicast packets through this interface.

- **InMulticastOctets**  
   The number of octets of data that are received without errors in multicast packets through this interface.

- **InBroadcastOctets**  
   The number of octets of data that are received without errors in broadcast packets through this interface.

- **OutOctets**  
   The number of octets of data that are transmitted without errors through this interface. This value includes octets in unicast, broadcast, and multicast packets.

- **OutUcastPkts**  
   The number of unicast packets that are transmitted without errors through this interface.

- **OutNUcastPkts**  
   The number of non-unicast packets that are transmitted without errors through this interface. This value includes broadcast and multicast packets.

- **OutDiscards**  
   The number of outgoing packets that were discarded even though they did not have errors.

- **OutErrors**  
   The number of outgoing packets that were discarded because of errors.

- **OutUcastOctets**  
   The number of octets of data that are transmitted without errors in unicast packets through this interface.

- **OutMulticastOctets**  
   The number of octets of data that are transmitted without errors in multicast packets through this interface.

- **OutBroadcastOctets**  
   The number of octets of data that are transmitted without errors in broadcast packets through this interface.

- **OutQLen**  
   The transmit queue length. This field is not currently used.

## Remarks

The values for the Type field are defined in the Ipifcons.h header file. Only the possible values that are listed in the description of the Type member are currently supported.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
</tbody>
</table>

## See also

[**GetIfEntry2**](getifentry2.md)

[**GetIfTable2**](getiftable2.md)

[**MIB\_IF\_TABLE2**](mib-if-table2.md)

[**NET\_IF\_ACCESS\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_access_type)

[**NET\_IF\_ADMIN\_STATUS**](/windows/win32/api/ifdef/ne-ifdef-net_if_admin_status)

[**NET\_IF\_CONNECTION\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_connection_type)

[**NET\_IF\_DIRECTION\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_direction_type)

[**NET\_IF\_MEDIA\_CONNECT\_STATE**](/windows/win32/api/ifdef/ne-ifdef-net_if_media_connect_state)

[**NET\_LUID**](net-luid-value.md)

[**TUNNEL\_TYPE**](/windows/win32/api/ifdef/ne-ifdef-tunnel_type)
