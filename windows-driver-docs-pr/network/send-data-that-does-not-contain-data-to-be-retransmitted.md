---
title: Send Data That Does Not Contain Data to Be Retransmitted
description: Send Data That Does Not Contain Data to Be Retransmitted
ms.assetid: ac2dd6d4-c5c7-4e0d-afed-cd78d9c1484f
keywords:
- state offloading process WDK TCP chimney offload , outstanding send data
- offloading state process WDK TCP chimney offload , outstanding send data
- outstanding send data WDK TCP chimney offload
- send data outstanding WDK TCP chimney offload
- retransmitted data WDK TCP chimney offload
- SndUna WDK TCP chimney offload
- SndNxt WDK TCP chimney offload
- SndMax WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Send Data That Does Not Contain Data to Be Retransmitted


\[The TCP chimney offload feature is deprecated and should not be used.\]




The following figure shows how the **SndUna**, **SndNxt**, and **SndMax** members of the [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure segment send data that does not contain data to be retransmitted.

![diagram illustrating send data with no data to be retransmitted](images/send-data-no-retrans.png)

The data from the byte that is indicated by **SndUna** up to the byte before the byte that is indicated by **SndNxt** is data that the host stack transmitted but for which the host stack did not receive an acknowledgment from the remote host. The offload target must process any acknowledgments for this data and retransmit the data later, if necessary.

Because the send data does not contain any data to be retransmitted, the byte that is indicated by **SndNxt** equals the byte that is indicated by **SndMax**. The data to the right of the byte that is indicated by **SndNxt** and **SndMax** is unsent data that the offload target must send before sending any other data on the offloaded connection.

 

 





