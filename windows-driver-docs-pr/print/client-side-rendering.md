---
title: Client-Side Rendering
description: Client-Side Rendering
ms.assetid: 7b67de2a-b5aa-4d8c-9b2c-9caeffdb71c3
keywords:
- print jobs WDK , client-side rendering
- rendering print jobs WDK
- client-side rendering WDK print
- print spooler print-job rendering WDK
- spooler print-job rendering WDK print
- jobs WDK print , client-side rendering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Client-Side Rendering


Print-job rendering takes place, by default, on client computers that are running Windows Vista.

Before Windows 2000, Windows rendered print jobs on the client computer and the rendered data was sent to the print server for printing. Since Windows 2000 and before Windows Vista, print-job rendering took place on the print server. Print-job rendering was moved to print server beginning with Windows 2000 because print servers offered more processing power than the client computers. The more powerful print servers could then complete the processor-intensive task of print-job rendering.

Recently, however, client computers often have more available processor resources than print servers. In addition, many print servers handle more print queues and also serve as file, Web, and mail servers.

Starting with Windows Vista, the print spooler renders print jobs locally by default. The print spooler has changed to enable this type of rendering, but the printer driver and the end-user will not notice any change. Most printer drivers do not require any modifications to use client-side rendering successfully; however, there are some exceptions that are described in [Known Issues with Client-Side Rendering](known-issues-with-client-side-rendering.md).

This section includes:

[Client-Side Rendering Overview](client-side-rendering-overview.md)

[Known Issues with Client-Side Rendering](known-issues-with-client-side-rendering.md)

[Best Practices for Client-Side Rendering](best-practices-for-client-side-rendering.md)

 

 




