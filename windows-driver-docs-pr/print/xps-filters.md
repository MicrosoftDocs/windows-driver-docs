---
title: XPS Filters
author: windows-driver-content
description: XPS Filters
ms.assetid: dd8044a6-6558-488e-9508-a83718fabb7d
keywords: ["XPSDrv printer drivers WDK , render modules", "render modules WDK XPSDrv , XPS filters", "XPS filters WDK XPSDrv", "DllGetClassObject", "filters WDK XPS", "IPrintPipelineFilter"]
---

# XPS Filters


For the XPS print path, filters are the primary way that a driver prepares print data for the printer. In versions of the Microsoft Windows operating system before Windows Vista, print processors and rendering modules did the work of filters.

An XPS filter is a DLL that exports [DllGetClassObject](http://go.microsoft.com/fwlink/p/?linkid=123418) and [DllCanUnloadNow](http://go.microsoft.com/fwlink/p/?linkid=123419) functions. The filter pipeline manager calls these functions when it loads and unloads the XPS filter DLL. After loading the filter DLL, the filter pipeline manager does the following:

-   Calls **DllGetClassObject** to obtain a reference to the filter object's [IClassFactory](http://go.microsoft.com/fwlink/p/?linkid=123420) interface.

-   Calls the [IClassFactory::CreateInstance](http://go.microsoft.com/fwlink/p/?linkid=123421) method to obtain a reference to the filter object's [IPrintPipelineFilter](https://msdn.microsoft.com/library/windows/hardware/ff554286) interface.

-   Calls the [**IPrintPipelineFilter::InitializeFilter**](https://msdn.microsoft.com/library/windows/hardware/ff554291) method to initialize the filter object.

Before unloading the filter DLL, the filter pipeline manager calls **DllCanUnloadNow**.

**Note**   In some older XPS filters, the **DllGetClassObject** function retrieves a reference to the filter's **IPrintPipelineFilter** interface instead of to an **IClassFactory** interface. For backward compatibility, the filter pipeline manager in Windows Vista and later versions of Windows will continue to support these filters. However, for new filter designs, **DllGetClassObject** should retrieve a reference to an **IClassFactory** interface.

 

XPS filters make the printing subsystem more robust, because the filters run in a process different from the spooler. This "sandboxing" both protects against failures and allows a plug-in to run with different security permissions. XPSDrv also enables you to reuse filters across families of printers to lower costs and development time.

For maximum flexibility and reuse, each filter should perform a specific print processing function. For example, one filter would only apply a watermark, while another would only perform accounting.

Windows Vista does not include any filters in-box, but the following sample filters are included in the Windows Driver Kit (WDK) in the \\Src\\Print\\Xpsdrvsmpl\\Src\\Filters folder:

-   Booklet

-   Color conversion

-   Nup

-   Page scaling

-   Watermark

For more information about the filter pipeline manager, see [XPSDrv Render Module](xpsdrv-render-module.md).

For more information about implementing filters, see [Implementing XPS Filters](implementing-xps-filters.md).

For more information about asynchronous notifications in print filters, see [Asynchronous Notifications in Print Filters](asynchronous-notifications-in-print-filters.md).

You must configure filters by using the [filter pipeline configuration file](filter-pipeline-configuration-file.md).

For information about how to debug the print filter pipeline service, see [Attaching a Debugger to the Print Filter Pipeline Service](attaching-a-debugger-to-the-print-filter-pipeline-service.md).

In Windows 7, XPS filters can use the [XPS rasterization service](using-the-xps-rasterization-service.md) to convert fixed pages in XPS documents to bitmaps.

For information about the way Windows uses GPU acceleration for XPS rasterization, see [XPSRas GPU Usage Decision Tree](xpsras-usage-decision-tree.md).

For more information about XPS filters, see the following white papers at the [WHDC](http://go.microsoft.com/fwlink/p/?linkid=69253) Web site:

[XPSDrv Configuration Module Implementation](http://go.microsoft.com/fwlink/p/?linkid=133878)

[XPSDrv Filter Pipeline](http://go.microsoft.com/fwlink/p/?linkid=133879)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPS%20Filters%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


