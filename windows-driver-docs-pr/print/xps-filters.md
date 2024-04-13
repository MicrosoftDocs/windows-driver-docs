---
title: XPS Filters
description: XPS Filters
keywords:
- XPSDrv printer drivers WDK , render modules
- render modules WDK XPSDrv , XPS filters
- XPS filters WDK XPSDrv
- DllGetClassObject
- filters WDK XPS
- IPrintPipelineFilter
ms.date: 01/26/2023
---

# XPS Filters

[!include[Print Support Apps](../includes/print-support-apps.md)]

For the XPS print path, filters are the primary way that a driver prepares print data for the printer. In versions of the Microsoft Windows operating system before Windows Vista, print processors and rendering modules did the work of filters.

An XPS filter is a DLL that exports [DllGetClassObject](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject) and [DllCanUnloadNow](/windows/win32/api/combaseapi/nf-combaseapi-dllcanunloadnow) functions. The filter pipeline manager calls these functions when it loads and unloads the XPS filter DLL. After loading the filter DLL, the filter pipeline manager does the following:

- Calls **DllGetClassObject** to obtain a reference to the filter object's [IClassFactory](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface.

- Calls the [IClassFactory::CreateInstance](/windows/win32/api/unknwn/nf-unknwn-iclassfactory-createinstance) method to obtain a reference to the filter object's [IPrintPipelineFilter](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintpipelinefilter) interface.

- Calls the [**IPrintPipelineFilter::InitializeFilter**](/windows-hardware/drivers/ddi/filterpipeline/nf-filterpipeline-iprintpipelinefilter-initializefilter) method to initialize the filter object.

Before unloading the filter DLL, the filter pipeline manager calls **DllCanUnloadNow**.

In some older XPS filters, the **DllGetClassObject** function retrieves a reference to the filter's **IPrintPipelineFilter** interface instead of to an **IClassFactory** interface. For backward compatibility, the filter pipeline manager in Windows Vista and later versions of Windows will continue to support these filters. However, for new filter designs, **DllGetClassObject** should retrieve a reference to an **IClassFactory** interface.

XPS filters make the printing subsystem more robust, because the filters run in a process different from the spooler. This "sandboxing" both protects against failures and allows a plug-in to run with different security permissions. XPSDrv also enables you to reuse filters across families of printers to lower costs and development time.

For maximum flexibility and reuse, each filter should perform a specific print processing function. For example, one filter would only apply a watermark, while another would only perform accounting.

The following [XPS driver and filter samples](/samples/microsoft/windows-driver-samples/xpsdrv-driver-and-filter-sample/) are available on GitHub:

- Booklet

- Color conversion

- Nup

- Page scaling

- Watermark

For more information about the filter pipeline manager, see [XPSDrv Render Module](xpsdrv-render-module.md).

For more information about implementing filters, see [Implementing XPS Filters](implementing-xps-filters.md).

For more information about asynchronous notifications in print filters, see [Asynchronous Notifications in Print Filters](asynchronous-notifications-in-print-filters.md).

You must configure filters by using the [filter pipeline configuration file](filter-pipeline-configuration-file.md).

For information about how to debug the print filter pipeline service, see [Attaching a Debugger to the Print Filter Pipeline Service](attaching-a-debugger-to-the-print-filter-pipeline-service.md).

In Windows 7, XPS filters can use the [XPS rasterization service](using-the-xps-rasterization-service.md) to convert fixed pages in XPS documents to bitmaps.

For information about the way Windows uses GPU acceleration for XPS rasterization, see [XPSRas GPU Usage Decision Tree](xpsras-usage-decision-tree.md).
