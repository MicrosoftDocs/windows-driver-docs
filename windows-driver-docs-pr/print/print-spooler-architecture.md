---
title: Print Spooler Architecture
author: windows-driver-content
description: Print Spooler Architecture
ms.assetid: 712da599-29cb-4df9-9627-49907f0aa500
keywords:
- spooler architecture WDK print
- print spooler architecture WDK
- jobs WDK print , print spoolers
- print jobs WDK , print spoolers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print Spooler Architecture


## <a href="" id="ddk-print-spooler-architecture-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Spooler%20Architecture%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


