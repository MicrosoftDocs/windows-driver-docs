---
title: Client-Side Rendering Overview
author: windows-driver-content
description: Client-Side Rendering Overview
ms.assetid: 0c73ca03-0fde-423d-80c9-6800468176b5
keywords:
- client-side rendering WDK print , about client-side rendering
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Client-Side Rendering Overview


On Windows Vista, [Point and Print](introduction-to-point-and-print.md) loads the printer driver onto the client computer as in previous versions of the Windows operating system. Client-side rendering, which is enabled by default on Windows Vista, causes the printer driver to render the print job to the Page Description Language (PDL) that the printer uses instead of to the Enhanced Metafile (EMF) format or XML Paper Specification (XPS) format that the printer driver uses. The RAW-format PDL is then sent to the print server for queuing and printing by the new functionality in the print spooler.

In addition to moving the processing load of print-job rendering from the print server to the client computer, client-side rendering also offers these advantages to the user:

-   Driver mismatch problems are eliminated.

    Because the same computer that spooled the print job also renders the EMF-format data, there is no longer a problem if the client has a version of the printer driver that is incompatible with the version on the print server.

-   Offline printing is supported.

    An end-user can now spool a print job to a remote printer even if they are not connected to the print server that hosts the printer. The client-side rendering feature makes it possible for a user to spool and render a print job locally. When the client computer can establish a connection to the print spooler, the rendered print job is automatically sent to the print server for printing.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Client-Side%20Rendering%20Overview%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


