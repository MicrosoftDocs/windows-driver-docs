---
title: Possible Future Requirements for TCP Chimney-Capable NICs
description: Possible Future Requirements for TCP Chimney-Capable NICs
ms.assetid: be36286c-1ce8-4898-8c49-a39789d3c52f
keywords:
- RFC compliance WDK TCP chimney offload
- IETF RFC compliance WDK TCP chimney offload
- task-offload engine NIC WDK TCP chimney offload
- TOE NIC WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Possible Future Requirements for TCP Chimney-Capable NICs


\[The TCP chimney offload feature is deprecated and should not be used.\]

We strongly recommend, although it is not yet required, that vendors implement the following in TCP/IP stack of a TOE NIC:

-   IP explicit congestion notification (ECN), as specified in RFC 3168

-   Support for the NewReno modification to TCP's fast recovery algorithm, as specified in RFC 2582

-   Enhancements to TCP's loss recovery, by using limited transmit, as specified in RFC 3042

-   Selective acknowledgement (SACK) handling, as specified in RFCs 2018, 2883, and 3517

-   [Silly Window Syndrome (SWS) prevention timer](silly-window-syndrome-prevention-timer.md)

 

 





