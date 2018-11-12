---
title: Developing IPsec-Compatible Callout Drivers
description: Developing IPsec-Compatible Callout Drivers
ms.assetid: 5e4fad4e-a790-4294-b3ac-a796f76265ad
keywords:
- IPsec WDK Windows Filtering Platform , compatibility with WFP callout drivers
- Windows Filtering Platform callout drivers WDK , IPsec compatibility
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing IPsec-Compatible Callout Drivers


### Layers That Are Compatible With IPsec

To be fully compatible with the Windows implementation of IPsec that begins with Windows Vista and Windows Server 2008, a callout driver should be registered at one of the following run-time filtering layers:

<a href="" id="tcp-packet-filtering"></a>TCP Packet Filtering  
Stream Layers:

-   FWPS\_LAYER\_STREAM\_V4

-   FWPS\_LAYER\_STREAM\_V6

<a href="" id="non-tcp-and-non-error-icmp-packet-filtering"></a>Non-TCP and Non-Error ICMP Packet Filtering  
Datagram-Data Layers:

-   FWPS\_LAYER\_DATAGRAM\_DATA\_V4

-   FWPS\_LAYER\_DATAGRAM\_DATA\_V6

-   FWPS\_LAYER\_DATAGRAM\_DATA\_V4\_DISCARD

-   FWPS\_LAYER\_DATAGRAM\_DATA\_V6\_DISCARD

Except for the case when incoming packets must be rebuilt before they are receive-injected from a datagram-data layer, callout drivers that are registered at these data layers are compatible with IPsec.

### Layers That Are Incompatible With IPsec

Network and forwarding layers are incompatible with IPsec because at these layers IPsec traffic has not yet been decrypted or verified. IPsec policies are enforced at the transport layer, which occurs after a network layer classify operation.

The following run-time filtering layers are incompatible with IPsec because IPsec processing in Windows occurs below the following layers:

FWPS\_LAYER\_INBOUND\_IPPACKET\_V4

FWPS\_LAYER\_INBOUND\_IPPACKET\_V6

FWPS\_LAYER\_INBOUND\_IPPACKET\_V4\_DISCARD

FWPS\_LAYER\_INBOUND\_IPPACKET\_V6\_DISCARD

FWPS\_LAYER\_OUTBOUND\_IPPACKET\_V4

FWPS\_LAYER\_OUTBOUND\_IPPACKET\_V6

FWPS\_LAYER\_OUTBOUND\_IPPACKET\_V4\_DISCARD

FWPS\_LAYER\_OUTBOUND\_IPPACKET\_V6\_DISCARD

### Special Considerations for Transport Layers

To make a callout driver that is registered with a transport layer (FWPS\_LAYER\_*XXX*\_TRANSPORT\_V4 or \_V6) compatible with IPsec, follow these guidelines:

1.  Register the callout at ALE authorize receive/accept layers (**FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4** or **FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V6**) in addition to transport layers (FWPS\_LAYER\_*XXX*\_TRANSPORT\_V4 or \_V6).

2.  To prevent interference with internal Windows IPsec processing, register the callout at a sublayer that has a lower weight than **FWPM\_SUBLAYER\_UNIVERSAL**. Use the [**FwpmSubLayerEnum0**](https://msdn.microsoft.com/library/windows/desktop/aa364211) function to find the sublayer's weight. For information about this function, see the [Windows Filtering Platform](http://go.microsoft.com/fwlink/p/?linkid=90220) documentation in the Microsoft Windows SDK.

3.  An incoming transport packet that requires ALE classification must be inspected at the ALE authorize receive/accept layers (**FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4** or **FWPS\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V6**). Such a packet must be permitted from incoming transport layers. Beginning with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, use the **FWPS\_METADATA\_FIELD\_ALE\_CLASSIFY\_REQUIRED** metadata flag to determine whether the incoming packet will be indicated to the **FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V4** and **FWPM\_LAYER\_ALE\_AUTH\_RECV\_ACCEPT\_V6** filtering layers. This metadata flag replaces the **FWP\_CONDITION\_FLAG\_REQUIRES\_ALE\_CLASSIFY** condition flag that was used in Windows Vista.

4.  To prevent interference with internal Windows IPsec processing, do not intercept IPsec tunnel-mode traffic at transport layers if the IPsec traffic is not yet detunneled. The following code example shows how to bypass such packets.
    ```C++
    FWPS_PACKET_LIST_INFORMATION0 packetInfo = {0};
    FwpsGetPacketListSecurityInformation0(
     layerData,
        FWPS_PACKET_LIST_INFORMATION_QUERY_IPSEC |
        FWPS_PACKET_LIST_INFORMATION_QUERY_INBOUND,
        &packetInfo
        );

    if (packetInfo.ipsecInformation.inbound.isTunnelMode &&
        !packetInfo.ipsecInformation.inbound.isDeTunneled)
    {
     classifyOut->actionType = FWP_ACTION_PERMIT;
     goto Exit;
    }
    ```

5.  After an IPsec-protected packet is decrypted and verified at the transport layer, the AH/ESP header remains in the IP header. If such a packet has to be reinjected back into the TCP/IP stack, the IP header must be rebuilt to remove the AH/ESP header. Beginning with Windows Vista with SP1 and Windows Server 2008, you can do this by cloning the packet and calling the [**FwpsConstructIpHeaderForTransportPacket0**](https://msdn.microsoft.com/library/windows/hardware/ff551154) function that has the *headerIncludeHeaderSize* parameter set to the IP header size of the cloned packet.

6.  At the ALE receive/accept layer, a callout can detect IPsec-protected traffic by checking whether the **FWP\_CONDITION\_FLAG\_IS\_IPSEC\_SECURED** flag is set. At transport layers, a callout can detect IPsec-protected traffic by calling the [**FwpsGetPacketListSecurityInformation0**](https://msdn.microsoft.com/library/windows/hardware/ff551174) function and checking whether the **FWPS\_PACKET\_LIST\_INFORMATION0** flag is set in the *queryFlags* parameter.

### Working With IPsec ESP Packets

When the engine indicates decrypted encapsulating security payload (ESP) packets, it truncates them to exclude trailing ESP data. Because of the way the engine handles such packets, the MDL data in the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure does not reflect the correct packet length. The correct length can be obtained by using the [**NET\_BUFFER\_DATA\_LENGTH**](https://msdn.microsoft.com/library/windows/hardware/ff568382) macro to retrieve the data length of the **NET\_BUFFER** structure.

 

 





