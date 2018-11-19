---
title: Extensible Architecture
description: Extensible Architecture
ms.assetid: 48a9c3ea-282c-4d3c-83ca-dc7051fe5002
keywords:
- direct consumption WDK XPSDrv
- scalable consumption WDK XPSDrv
- print paths WDK XPSDrv
- XPSDrv printer drivers WDK , print paths
- XPSDrv printer drivers WDK , extensibility
- extensibility WDK XPSDrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extensible Architecture


Extensibility throughout the architecture makes it easier for you to add differentiating features and capabilities in a modular fashion. Each upgraded and new component within the XPS print path was designed to enable vendor extensibility, in the following ways:

-   The print schema enables extensibility and will be regularly updated to publicly expose desired device capabilities.

-   The new filter pipeline that XPSDrv drivers use is founded on the premise of a modular, extensible architecture to enable you to provide modularized functionality that can act alone or in an atomic fashion to produce your desired effects.

The filter pipeline is also built to support the concepts of *direct consumption* and *scalable consumption*:

-   Direct consumption means that the device can consume an XPS Document or the XPS spool file without host assistance. For output from a Windows-based computer, you must provide an XPSDrv driver that consists of a configuration module and a null filter pipeline. The configuration module represents the device and expresses the device capabilities to the application, but it does not process the spool file within the driver. The XPS spool file is delivered directly to the printer, so the printer then processes the document in its entirety.

-   Scalable consumption represents an XPSDrv driver that may perform some or all processing on the host. You can choose the division between host and device processing, so you can make trade-offs based on device capabilities, cost, and target market. With scalable consumption, you have significant flexibility in how you implement XPS.

To take advantage of the XPS print path, you should provide an XPSDrv driver. An XPSDrv driver is a filter pipeline that provides driver features such as host-based N-up, watermark, and rendering functions. Graphics processing is performed in a rendering filter and is performed on the visuals that are represented in the new spool file format. This type of processing is fundamentally different from the way that rendering operations occur with GDI-based drivers.

The modular construction of the filter pipeline provides a framework for developing function-specific filters. You can create a filter pipeline that is composed of self-contained filters. If these filters are appropriately contained, different drivers, and thus different pipelines can reuse the filters, so you can optimize your investment in XPSDrv development.

Versions of the Windows operation system before Windows Vista required printer drivers to have a printer interface DLL for printer configuration and control and a printer graphics DLL for processing and rendering the actual document content to be printed. Printer drivers for Windows Vista require the same functions as in previous printer driver versions. An XPSDrv driver communicates with devices and applications by using the Print Ticket and Print Capabilities technologies. You must add the additional interfaces that provide the enhanced PrintTicket and Print Capabilities functions of Windows Vista printing.

 

 




