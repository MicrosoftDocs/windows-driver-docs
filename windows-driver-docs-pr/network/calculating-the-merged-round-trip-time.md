---
title: Calculating the Merged Round-Trip Time
description: Calculating the Merged Round-Trip Time
ms.assetid: 40aae723-144c-4cd5-84ed-5470284ecf26
keywords:
- timestamps WDK TCP chimney offload , Merged Round-Trip Time
- TCP timestamps WDK TCP chimney offload , Merged Round-Trip Time
- Merged Round-Trip Time WDK TCP chimney offload
- MRTT WDK TCP chimney offload
- round-trip time WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calculating the Merged Round-Trip Time


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target calculates the Merged Round-Trip Time (MRTT) as follows:

MRTT = ( *NicTime*+ *NicDelta*) - *TsEchoed*

This equation contains the following:

-   *NicTime* is the offload target's current time.

-   *NicDelta* is the offload target's [timestamp delta](calculating-the-timestamp-delta.md).

-   *TsEchoed* is the timestamp that is echoed in the acknowledgement from the remote TCP peer.

The host stack calculates the MRTT in a similar way: it adds its timestamp delta to its current time and, from this sum, subtracts the timestamp that is echoed by the remote TCP peer.

 

 





