---
title: Client-Side Rendering Overview
description: Client-Side Rendering Overview
ms.assetid: 0c73ca03-0fde-423d-80c9-6800468176b5
keywords:
- client-side rendering WDK print , about client-side rendering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Client-Side Rendering Overview

[Point and Print](introduction-to-point-and-print.md) loads the printer driver onto the client computer as in previous versions of the Windows operating system. Client-side rendering causes the printer driver to render the print job to the Page Description Language (PDL) that the printer uses instead of to the Enhanced Metafile (EMF) format or XML Paper Specification (XPS) format that the printer driver uses. The RAW-format PDL is then sent to the print server for queuing and printing by the new functionality in the print spooler.

In addition to moving the processing load of print-job rendering from the print server to the client computer, client-side rendering also offers these advantages to the user:

-   Driver mismatch problems are eliminated.

    Because the same computer that spooled the print job also renders the EMF-format data, there is no longer a problem if the client has a version of the printer driver that is incompatible with the version on the print server.

-   Offline printing is supported.

    An end-user can now spool a print job to a remote printer even if they are not connected to the print server that hosts the printer. The client-side rendering feature makes it possible for a user to spool and render a print job locally. When the client computer can establish a connection to the print spooler, the rendered print job is automatically sent to the print server for printing.
