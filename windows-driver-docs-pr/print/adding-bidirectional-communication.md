---
title: Adding Bidirectional Communication
description: Adding Bidirectional Communication
ms.assetid: 30767eda-e456-4928-afac-40edd2ab48fc
keywords:
- print spooler customizing WDK , bidirectional communication
- spooler customizing WDK print , bidirectional communication
- customizing print spooler components WDK , bidirectional communication
- bidirectional communication WDK print
- bidi communication WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Bidirectional Communication





The spooler provides support for bidirectional ("BiDi") communication between an application or driver and a printer. This support enables the application or driver to send one or more requests to the printer, and the printer to respond to these requests.

![diagram illustrating bidirectional support architecture](images/bidi.png)

### Bidirectional Communication Requirements

Before an application or driver can use bidi communication, it must implement [bidirectional communication interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163): either the IBidiSpl COM interface or the IbidiSpl2 COM interface, together with at least one of the IBidiRequest and IBidiRequestContainer COM interfaces. In addition, one or both of the following must be true:

-   The [**SendRecvBidiData**](https://msdn.microsoft.com/library/windows/hardware/ff562068) function is implemented in a print provider DLL.

-   The [**SendRecvBidiDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff562071) function is implemented in a language monitor server DLL or in a port monitor server DLL.

To send a single request to the printer, an application or printer driver must first compose the request, and then call the IBidiSpl::SendRecv method. To send multiple requests, the application or driver composes a list of requests, and then calls the IBidiSpl::MultiSendRecv method.

After receiving the request, the client-side portion of the spooler (Winspool.drv) passes it on to the server-side spooler (spoolsv.exe). The server-side spooler can be on the local computer, or on a remote network print server. When the server-side spooler receives the request, it parses the data in the request, and fills in the members of a [**BIDI\_REQUEST\_CONTAINER**](https://msdn.microsoft.com/library/windows/hardware/ff545193) structure. The server-side spooler then calls [**SendRecvBidiData**](https://msdn.microsoft.com/library/windows/hardware/ff562068) or [**SendRecvBidiDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff562071). When either function returns, its *ppResData* parameter points to a memory location that contains the address of a filled-in [**BIDI\_RESPONSE\_CONTAINER**](https://msdn.microsoft.com/library/windows/hardware/ff545202) structure that contains the printer's response. The server-side spooler converts the data in this structure to a form suitable for use by the application or driver, and passes it back to the client-side spooler, and finally back to the originator of the request.

 

 




