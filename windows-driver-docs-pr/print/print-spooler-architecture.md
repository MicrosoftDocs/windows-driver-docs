---
title: Print Spooler Architecture
description: Print Spooler Architecture
ms.assetid: 712da599-29cb-4df9-9627-49907f0aa500
keywords:
- spooler architecture WDK print
- print spooler architecture WDK
- jobs WDK print , print spoolers
- print jobs WDK , print spoolers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Spooler Architecture





The Microsoft Windows 2000 and later print spooler is made up of a set of Microsoft-supplied and optional vendor-supplied components, with responsibilities that include:

-   Determining whether a print job should be handled locally or across a network.

-   Accepting a data stream created by GDI, in conjunction with a printer driver, for output on a particular type of printer.

-   Spooling the data to a file (if spooling is enabled).

-   Selecting the first available physical printer in a logical printer queue.

-   Converting a data stream from a spooled format (such as [*enhanced metafile (EMF)*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enhanced-metafile--emf-)) to a format that can be sent to printer hardware (such as [*printer control language (PCL)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-printer-control-language--pcl-)).

-   Sending a data stream to printer hardware.

-   Maintaining a registry-based database for [spooler components](spooler-components.md) and [printer forms](printer-forms-support.md).

-   (Windows Vista) Rendering print jobs on the client computer instead of on the print server. [Client-side rendering](client-side-rendering.md) eases the print server workload, is transparent to the print driver, and is enabled by default in Windows Vista.

-   For Windows 7, print drivers can run in a separate process from the spooler. This feature is called [Printer Driver Isolation](printer-configuration.md).

 

 




