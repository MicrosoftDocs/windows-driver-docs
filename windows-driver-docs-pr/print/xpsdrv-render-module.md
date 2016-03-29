---
title: XPSDrv Render Module
description: XPSDrv Render Module
ms.assetid: e844e320-bd3d-4855-bb47-fdfbdb157802
keywords: ["XPSDrv printer drivers WDK , render modules", "render modules WDK XPSDrv , about render modules", "filter pipelines WDK XPSDrv", "Filter Pipeline Manager WDK XPSDrv", "FPM WDK XPSDrv", "Inter-Filter Communicator WDK XPSDrv", "IFC WDK XPSDrv"]
---

# XPSDrv Render Module


The render module of an XPSDrv printer driver contains the filters that render the contents of the XPS spool file for output to the printer. The set of rendering filters for a driver are instantiated and run in a filter pipeline. The Filter Pipeline Manager (FPM) manages the filters, and the Inter-Filter Communicator (IFC) controls the interaction between filters.

The following diagram shows a filter pipeline.

![diagram illustrating a filter pipeline](images/xps-pipeline.png)

Microsoft provides the following XPS driver components:

-   Filter Pipeline Manager

-   Inter-Filter Communicator

-   Property bag

The Filter Pipeline Manager must:

1.  Load and initialize filters.

2.  Manage the data between filters.

3.  Unload the filters when a print job is finished.

Inter-Filter Communicators manage the transfer of data between filters, and the Filter Pipeline Manager manages Inter-Filter Communicators.

The following process describes what happens to a set of filters in a pipeline:

1.  The Filter Pipeline Manager reads the filter pipeline configuration (FPC) file.

2.  The filters that the FPC specifies are loaded.

3.  The filter pipeline is initialized, and the Filter Pipeline Manager starts the filter pipeline.

4.  The first filter in the pipeline reads the XPS data through XPS or stream interfaces that the Filter Pipeline Manager offers, and then the filter processes the contents.

5.  The first filter sends the processed XPS data to the second filter by using the interface that the Inter-Filter Communicator provides.

6.  The Inter-Filter Communicator maintains the intermediate processing results until the second filter is ready.

7.  Steps 1-6 are repeated from filter to filter until the results of the last filter are sent to the port that the driver has defined for output.

If a printer uses XPS as a page description language (PDL), and no other processing is desired, you can use an empty ("pass through") pipeline. If XPS is not the PDL for your printer, you will need to write a filter that converts XPS to the PDL of your printer, as well as any other processing that you want.

To develop an XPS driver, you must create the following components:

-   [XPS filters](xps-filters.md)

-   [XPS filter pipeline configuration file](filter-pipeline-configuration-file.md)

You can also add [Print Ticket Support to the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Render%20Module%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




