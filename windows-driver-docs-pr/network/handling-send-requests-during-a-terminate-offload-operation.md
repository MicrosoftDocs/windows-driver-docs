---
title: Handling Send Requests During a Terminate Offload Operation
description: Handling Send Requests During a Terminate Offload Operation
ms.assetid: 7629c47d-c95c-4362-a4a4-7945a9beee6a
keywords:
- terminating offload state WDK TCP chimney offload , send requests during
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Send Requests During a Terminate Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




If the offload target is preparing to terminate a TCP connection and has not yet indicated an upload request to the host stack, it must complete any send requests on the TCP connection that is being terminated by calling the [**NdisTcpOffloadSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff564609) function. The offload target specifies NDIS\_STATUS\_UPLOAD\_IN\_PROGRESS in the **Status** member of each NET\_BUFFER\_LIST structure that it passes to the **NdisTcpOffloadSendComplete** function. After a host stack has called the [**NdisTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff564615) function to terminate the offload, it should not post any further send or receive requests on that TCP connection.

 

 





