---
title: Requirements and Restrictions That Apply to IPsec Offloads
description: Requirements and Restrictions That Apply to IPsec Offloads
ms.assetid: c016d6dd-f760-4340-8d56-9bd69e4fe84e
keywords:
- ESP-protected packets WDK IPsec offload , requirements
- AH-protected packets WDK IPsec offload , requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements and Restrictions That Apply to IPsec Offloads

\[The IPsec Task Offload feature is deprecated and should not be used.\]




The following requirements and restrictions apply to Internet protocol security (IPsec) offloads:

-   The NIC must maintain the security association (SA) tables. This improves performance by eliminating the need to include keys or other information that is required for AH and ESP processing in send packets.

-   A NIC might be able to process both AH and ESP payloads for a single packet. In this case, the NIC must support the following possible combinations of integrity (authentication) algorithms for AH and ESP:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">AH</th>
    <th align="left">ESP</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>MD5</p></td>
    <td align="left"><p>MD5</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>SHA 1</p></td>
    <td align="left"><p>SHA 1</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>MD5</p></td>
    <td align="left"><p>SHA 1</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>SHA 1</p></td>
    <td align="left"><p>MD5</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>MD5</p></td>
    <td align="left"><p>Null (only if the NIC supports null encryption)</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>SHA 1</p></td>
    <td align="left"><p>Null (only if the NIC supports null encryption)</p></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   A NIC that supports DES algorithms must generate the initialization vector (IV) that these algorithms require.

-   The only IPsec tasks that a NIC performs are processing encrypted AH checksums or ESP checksums (or both) and encrypting and decrypting ESP payloads. For send packets, the TCP/IP transport creates all headers, padding, and replay numbers and chooses SPI values that are unique to destination address/IPsec protocol pairs. For receive packets, the TCP/IP transport performs inbound policy checks, handles replay detection and prevention, and handles audit events.

-   For a send packet, the TCP/IP transport does not provide explicit offsets (such as indicating the start of encrypted data) because the offload driver can easily determine this information from the particular security association (SA) that it uses to process the packet.

-   A packet with IPsec protocols must have authentication information in an authentication header (AH) or the encapsulating security payload (ESP) header (or both). It is not permissible for a IPsec packet to have no authentication.

-   IPsec tasks are not offloaded for send packets that require IP fragmentation or for receive packets that require reassembly from IP fragmentation.

-   IPsec tasks are not offloaded for send and receive packets that pass through a load-balancing miniport driver. For more information about load balancing, see [Load Balancing and Failover](https://msdn.microsoft.com/library/windows/hardware/ff549197).

 

 





