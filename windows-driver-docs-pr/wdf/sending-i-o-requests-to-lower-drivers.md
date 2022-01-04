---
title: Sending I/O Requests to Lower Drivers
description: Sending I/O Requests to Lower Drivers
keywords:
- I/O requests WDK UMDF , lower drivers
- request processing WDK UMDF , lower drivers
ms.date: 04/20/2017
---

# Sending I/O Requests to Lower Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

When a driver receives an I/O request that it cannot fully process, the driver typically forwards the received request to the next lower driver in the stack. The driver calls the [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method to forward the request. To forward synchronously, the driver passes the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag in the *Flags* parameter. Otherwise, the driver forwards the request asynchronously. Before the driver forwards the request, it should register a completion routine. For more information, see [Completing I/O Requests](completing-i-o-requests.md).

 

