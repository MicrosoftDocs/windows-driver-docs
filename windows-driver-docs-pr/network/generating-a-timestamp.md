---
title: Generating a Timestamp
description: Generating a Timestamp
ms.assetid: 68da434c-5081-4390-ac90-c1b112a2ff79
keywords:
- timestamps WDK TCP chimney offload , generating
- TCP timestamps WDK TCP chimney offload , generating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Generating a Timestamp


\[The TCP chimney offload feature is deprecated and should not be used.\]

To generate a timestamp, an offload target adds its timestamp delta to its current time:

*Timestamp*=*NicTime*+*NicDelta*

This equation contains the following:

-   *NicTime* is the offload target's current time.

-   *NicDelta* is the offload target's [timestamp delta](calculating-the-timestamp-delta.md).

The offload target supplies this sum (*NicTime*+*NicDelta*) as the timestamp in a TCP segment to be transmitted.

The host stack generates a timestamp in a similar way: it adds its delta to its current time and supplies this sum as the timestamp in a TCP segment to be transmitted.

 

 





