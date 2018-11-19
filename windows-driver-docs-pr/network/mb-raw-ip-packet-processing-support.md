---
title: MB Raw IP Packet Processing Support
description: MB Raw IP Packet Processing Support
ms.assetid: 1c3327fa-1858-4247-9a18-b49d26e9a095
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Raw IP Packet Processing Support


MB miniport drivers that support Raw IP packet frames in their send/receive data path should observe the following guidelines:

### Net buffer list (NBL) flags for RAW IP packet processing

-   For IPv4 packets:

    The **NblFlags** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure must be set to NDIS\_NBL\_FLAGS\_IS\_IPV4.

    The **NetBufferListFrameType** member of the NET\_BUFFER\_LIST structure must be set to 0x0800 (Ethertype IPv4) in network byte order.

-   For IPv6 packets:

    The **NblFlags** member of NET\_BUFFER\_LIST structure must be set to NDIS\_NBL\_FLAGS\_IS\_IPV6.

    The **NetBufferListFrameType** member of the NET\_BUFFER\_LIST structure must be set to 0x86dd (Ethertype IPv6) in network byte order.

Miniport drivers can use the [**NdisSetNblFlag**](https://msdn.microsoft.com/library/windows/hardware/ff564542) macro to set flags in the net buffer list. The following line demonstrates how to set IPv4 packet flag in the net buffer list:

```C++
NdisSetNblFlag(pNbl, NDIS_NBL_FLAGS_IS_IPV4);
```

Miniport drivers can use the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) to get and set information in a net buffer list. The following line demonstrates how to modify the **NetBufferListFrameType** OOB in the network buffer list for IPV4 packets:

```C++
Value = ConvertToNetworkByteOrder(0x0800);
```

```C++
NET_BUFFER_LIST_INFO(pNbl, NetBufferListFrameType) = Value;
```

### Send Path Processing

The MB Service will set these flags in the NBL before passing the list to the miniport driver to send across the network. The miniport driver can verify the flags in the input NBL.

### Receive Path Processing

Miniport drivers should set flags in the NBL before passing the NBL to the MB Service for received packets.

If your miniport driver implements Raw IP Packet Processing during its driver development phase, but still has DHCP server spoofing enabled (EnableDhcp = 1), your miniport driver should ensure following:

-   The hardware address and its length set in DHCP response from the miniport driver should match the values of the **CurrentMacAddress** and **MacAddressLength** members specified by the miniport driver in the NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES structure.

-   Transaction ID (the **xid** member) of the DHCP response from the miniport driver should match exactly the transaction ID set in the DHCP request message from the client.

 

 





