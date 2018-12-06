---
title: Sending I/O Requests to Lower Drivers
description: Sending I/O Requests to Lower Drivers
ms.assetid: 89868b4d-e2c1-4f38-b81e-a96b8cff3e4f
keywords:
- I/O requests WDK UMDF , lower drivers
- request processing WDK UMDF , lower drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending I/O Requests to Lower Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When a driver receives an I/O request that it cannot fully process, the driver typically forwards the received request to the next lower driver in the stack. The driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method to forward the request. To forward synchronously, the driver passes the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag in the *Flags* parameter. Otherwise, the driver forwards the request asynchronously. Before the driver forwards the request, it should register a completion routine. For more information, see [Completing I/O Requests](completing-i-o-requests.md).

 

 





