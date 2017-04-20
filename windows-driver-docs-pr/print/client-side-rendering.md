---
title: Client-Side Rendering
author: windows-driver-content
description: Client-Side Rendering
ms.assetid: 7b67de2a-b5aa-4d8c-9b2c-9caeffdb71c3
keywords:
- print jobs WDK , client-side rendering
- rendering print jobs WDK
- client-side rendering WDK print
- print spooler print-job rendering WDK
- spooler print-job rendering WDK print
- jobs WDK print , client-side rendering
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Client-Side%20Rendering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


