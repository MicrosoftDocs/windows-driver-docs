---
title: Implementing XPS Filters
description: Implementing XPS Filters
ms.assetid: 681f533f-d6f6-43a3-be0b-10d8c1a6f12e
keywords: ["XPSDrv printer drivers WDK , render modules", "render modules WDK XPSDrv , XPS filters", "XPS filters WDK XPSDrv", "filters WDK XPS", "IPrintPipelineFilter"]
---

# Implementing XPS Filters


All XPS filters must implement the [IPrintPipelineFilter](https://msdn.microsoft.com/library/windows/hardware/ff554286) interface.

During the call to the [**IPrintPipelineFilter::InitializeFilter**](https://msdn.microsoft.com/library/windows/hardware/ff554291) method, a filter should:

1.  Cache the pointer to the [IPrintPipelineManagerControl](https://msdn.microsoft.com/library/windows/hardware/ff554303) interface.

2.  Process relevant data in the [IPrintPipelinePropertyBag](https://msdn.microsoft.com/library/windows/hardware/ff554320) interface.

3.  Call the [**IInterFilterCommunicator::RequestReader**](https://msdn.microsoft.com/library/windows/hardware/ff551054) and [**IInterFilterCommunicator::RequestWriter**](https://msdn.microsoft.com/library/windows/hardware/ff551057) methods of the **IInterfilterCommunicator** interface (pIInterFilterCom) to initialize the provider and consumer interfaces for the filter.

If the data contains a PrintTicket section, you can access the data through the Microsoft Win32 PrintTicket or PrintCapabilities API. For UniDrv and PScript5 drivers that are based on XPSDrv, filters can have access to the [IPrintCoreHelper](https://msdn.microsoft.com/library/windows/hardware/ff552960) interface core Unidrv or PScript5 driver as their configuration service.

Filters may also be able to access proprietary configuration data through the property bag, depending on driver design.

The Inter-Filter Communicator is the part of the Filter Pipeline Manager that handles the communication between filters in the filter pipeline. When the Filter Pipeline Manager initializes a filter, an Inter-Filter Communicator interface ([IInterFilterCommunicator](https://msdn.microsoft.com/library/windows/hardware/ff551050)) is passed to the filter so that the filter can obtain the read and write interfaces that are defined for that filter.

Microsoft supplies the XPS document and stream interfaces, but you can create your own inter-filter interfaces that are defined for that filter. Microsoft provides the following interfaces:

-   The XPS document interface reads and writes from different parts of an XPS spool file.

-   The XPS stream interface reads and writes a serial stream of data. You can use this interface to write the page description language (PDL) from a filter to a printer that does not use XPS as a PDL.

Filters must conform to the rendering rules and PrintTicket processing rules that are defined in the XML Paper Specification (XPS).

Filters must not depend on the Microsoft .NET Common Language Runtime (CLR) or the Microsoft WinFX Runtime components.

Filters in the pipeline must not display user interface content.

The following recommendations apply to filters:

-   Filters should not create separate processes or threads. If a separate process or thread is required, the filter must properly manage the process or thread lifetime.

-   Filters should have isolated functionality. All functionality and implementation should be modular. Eliminate any order and functionality dependencies between filters whenever possible.

-   Filters should handle the case in which they are put in the pipeline out of order. When a filter is not in the expected order, it should not crash and should handle the situation gracefully. If a filter depends on another filter, it should handle the situation gracefully if the dependency is not supplied.

For more information about adding asynchronous notification to your filter, see [Asynchronous Notifications in Print Filters](asynchronous-notifications-in-print-filters.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Implementing%20XPS%20Filters%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




