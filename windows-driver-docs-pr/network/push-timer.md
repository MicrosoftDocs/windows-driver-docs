---
title: Push Timer
description: Push Timer
ms.assetid: f06fdc3c-70d3-4445-80a5-747237c07295
keywords:
- timers WDK TCP chimney offload , push timers
- TCP timers WDK TCP chimney offload , push timers
- push timers WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Push Timer


\[The TCP chimney offload feature is deprecated and should not be used.\]

The push timer count is not preserved across initiate offload and terminate offload operations.

The Windows default value for the push timer is 500 msec.

Before offloading a TCP connection, the host stack stops its push timer for the connection. In addition to offloading the connection, the host stack also offloads any receive data on the connection that it has not indicated to the application. (For more information about handling such receive data, see [Handling Buffered Receive Data During and After an Offload Operation](handling-buffered-receive-data-during-and-after-an-offload-operation.md).) After the connection has been offloaded, the offload target starts its push timer for the connection.

If the offload target receives any data on an offloaded TCP connection while the push timer for that connection is running, the offload target should restart the push timer for that connection.

Before terminating the offload of a TCP connection, an offload target stops its push timer for the connection. In addition to uploading the connection, the offload target also uploads any receive data on the connection that it has not indicated to the application. (For more information about uploading such data, see [Handling Buffered Receive Data During a Terminate Offload Operation](handling-buffered-receive-data-during-a-terminate-offload-operation.md).) After the connection has been uploaded, the host stack restarts its push timer for the connection.

 

 





