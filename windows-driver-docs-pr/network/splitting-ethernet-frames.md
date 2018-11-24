---
title: Splitting Ethernet Frames
description: Splitting Ethernet Frames
ms.assetid: 7b857dee-2805-4004-8f31-452f0cff0e0c
keywords:
- header-data split WDK , Ethernet frame splitting
- splitting Ethernet frames
- Ethernet frame splitting WDK networking
- Ethernet frame splitting WDK networking , about Ethernet frame splitting
- header-data split providers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting Ethernet Frames





This section describes the specific header-data split requirements that apply to header-data split providers, depending on the type of Ethernet frame that the provider is splitting.

**Note**  After you read the general requirements in this topic, you can use the subsequent topics to understand the specific requirements for each type of Ethernet frame. The later topics build on the requirements in the earlier topics. For example, if a frame contains IPv4 and UDP information, you should read the [Splitting IPv4 Frames](splitting-ipv4-frames.md) and [Splitting Frames at the UDP Payload](splitting-frames-at-the-udp-payload.md) topics.

 

If the header-data split provider splits a frame in compliance with the header-data split requirements, the indicated [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures must have the NDIS\_NBL\_FLAGS\_HD\_SPLIT flag set in the **NblFlags** member. If the header-data split provider does not split a frame, the frame must be indicated with the following flags cleared in **NblFlags** :

-   NDIS\_NBL\_FLAGS\_HD\_SPLIT

-   NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_HEADER

-   NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_PAYLOAD

For more information about setting header-data split NET\_BUFFER\_LIST flags and other receive indication requirements, see [Receive Indications with Header-Data Split](receive-indications-with-header-data-split.md).

There are cases where a header-data split provider can split a received frame outside of the header-data split provider requirements. In these cases, the provider should never split Ethernet frames in the middle of the IP header, IPv4 options, IPsec headers, IPv6 extension headers, or upper-layer-protocol headers, unless the first MDL contains at least as many bytes as NDIS specified for the lookahead size. For more information about the lookahead size, see [OID\_GEN\_CURRENT\_LOOKAHEAD](https://msdn.microsoft.com/library/windows/hardware/ff569574).

This section includes:

[Splitting IPv4 Frames](splitting-ipv4-frames.md)

[Splitting IPv6 Frames](splitting-ipv6-frames.md)

[Splitting Fragmented IP Frames](splitting-fragmented-ip-frames.md)

[Splitting Frames at the Beginning of the Upper-Layer-Protocol Headers](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md)

[Splitting Frames at the TCP Payload](splitting-frames-at-the-tcp-payload.md)

[Splitting Frames at the UDP Payload](splitting-frames-at-the-udp-payload.md)

[Splitting Frames Other Than TCP and UDP](splitting-frames-other-than-tcp-and-udp.md)

 

 





