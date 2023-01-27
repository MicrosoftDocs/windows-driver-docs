---
title: Implementing XPS Filters
description: Implementing XPS Filters
keywords:
- XPSDrv printer drivers WDK , render modules
- render modules WDK XPSDrv , XPS filters
- XPS filters WDK XPSDrv
- filters WDK XPS
- IPrintPipelineFilter
ms.date: 01/27/2023
---

# Implementing XPS Filters

[!include[Print Support Apps](../includes/print-support-apps.md)]

All XPS filters must implement the [IPrintPipelineFilter](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintpipelinefilter) interface.

During the call to the [**IPrintPipelineFilter::InitializeFilter**](/windows-hardware/drivers/ddi/filterpipeline/nf-filterpipeline-iprintpipelinefilter-initializefilter) method, a filter should:

1. Cache the pointer to the [IPrintPipelineManagerControl](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintpipelinemanagercontrol) interface.

1. Process relevant data in the [IPrintPipelinePropertyBag](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintpipelinepropertybag) interface.

1. Call the [**IInterFilterCommunicator::RequestReader**](/windows-hardware/drivers/ddi/filterpipeline/nf-filterpipeline-iinterfiltercommunicator-requestreader) and [**IInterFilterCommunicator::RequestWriter**](/windows-hardware/drivers/ddi/filterpipeline/nf-filterpipeline-iinterfiltercommunicator-requestwriter) methods of the **IInterfilterCommunicator** interface (pIInterFilterCom) to initialize the provider and consumer interfaces for the filter.

If the data contains a PrintTicket section, you can access the data through the Microsoft Win32 PrintTicket or PrintCapabilities API. For UniDrv and PScript5 drivers that are based on XPSDrv, filters can have access to the [IPrintCoreHelper](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelper) interface core Unidrv or PScript5 driver as their configuration service.

Filters may also be able to access proprietary configuration data through the property bag, depending on driver design.

The Inter-Filter Communicator is the part of the Filter Pipeline Manager that handles the communication between filters in the filter pipeline. When the Filter Pipeline Manager initializes a filter, an Inter-Filter Communicator interface ([IInterFilterCommunicator](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iinterfiltercommunicator)) is passed to the filter so that the filter can obtain the read and write interfaces that are defined for that filter.

Microsoft supplies the XPS document and stream interfaces, but you can create your own inter-filter interfaces that are defined for that filter. Microsoft provides the following interfaces:

- The XPS document interface reads and writes from different parts of an XPS spool file.

- The XPS stream interface reads and writes a serial stream of data. You can use this interface to write the page description language (PDL) from a filter to a printer that does not use XPS as a PDL.

Filters must conform to the rendering rules and PrintTicket processing rules that are defined in the XML Paper Specification (XPS).

Filters must not depend on the Microsoft .NET Common Language Runtime (CLR) or the Microsoft WinFX Runtime components.

Filters in the pipeline must not display user interface content.

The following recommendations apply to filters:

- Filters should not create separate processes or threads. If a separate process or thread is required, the filter must properly manage the process or thread lifetime.

- Filters should have isolated functionality. All functionality and implementation should be modular. Eliminate any order and functionality dependencies between filters whenever possible.

- Filters should handle the case in which they are put in the pipeline out of order. When a filter is not in the expected order, it should not crash and should handle the situation gracefully. If a filter depends on another filter, it should handle the situation gracefully if the dependency is not supplied.

For more information about adding asynchronous notification to your filter, see [Asynchronous Notifications in Print Filters](asynchronous-notifications-in-print-filters.md).
