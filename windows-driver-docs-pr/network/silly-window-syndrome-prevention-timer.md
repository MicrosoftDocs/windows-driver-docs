---
title: Silly Window Syndrome Prevention Timer
description: Silly Window Syndrome Prevention Timer
ms.assetid: 1d6053cd-e6ef-42f5-bfee-cef423667c32
keywords:
- timers WDK TCP chimney offload , SWS prevention timers
- TCP timers WDK TCP chimney offload , SWS prevention timers
- SWS prevention timers WDK TCP chimney offload
- Silly Window Syndrome prevention timers WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Silly Window Syndrome Prevention Timer


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target can optionally implement a Silly Window Syndrome (SWS) prevention timer for each offloaded TCP connection. The offload target uses the SWS prevention timer to suppress the transmission of TCP segments that contain less than the maximum segment size (MSS) of data.

To implement SWS prevention, an offload target must suppress sending a segment when all of the following are true:

-   The offload target has less than MSS data to send.

-   There is not enough send data to reach a send-request boundary (that is, fill the buffers that are associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure).

-   The amount of send data is less than half the maximum window size that the offload target has seen thus far on the connection.

When all these conditions are met, the offload target starts its SWS prevention timer. When the timer expires, the offload target sends as much data as the window will allow.

The SWS prevention timer count is not preserved across initiate offload and terminate offload operations.

Before offloading a TCP connection, the host stack stops its SWS prevention timer for the connection. After the connection has been offloaded, the offload target can do either of the following:

-   Restart its SWS prevention timer for the connection.

-   Immediately transmit any send data that the host stack has passed to the offload target during the initiate offload operation. (For more information about handling such data, see [Handling Outstanding Send Data During and After an Offload Operation](handling-outstanding-send-data-during-and-after-an-offload-operation.md).)

Before terminating the offload of a TCP connection, an offload target stops its SWS prevention timer for the connection. In addition to uploading the connection, the offload target can also upload send data for the connection. (For more information about such send data, see [Handling Outstanding Send Data During a Terminate Offload Operation](handling-outstanding-send-data-during-a-terminate-offload-operation.md).) After the connection has been uploaded, the host stack always restarts its SWS prevention timer for the connection.

 

 





