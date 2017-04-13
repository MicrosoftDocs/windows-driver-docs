---
title: Local Print Provider
author: windows-driver-content
description: Local Print Provider
ms.assetid: c6f9ba42-5f0f-4919-bfac-e4cd1045de4d
keywords: ["print providers WDK , local print providers", "local print providers WDK"]
---

# Local Print Provider


## <a href="" id="ddk-local-print-provider-gg"></a>


**Warning**  
Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

The local print provider for Microsoft Windows 2000 and later provides job control and printer management capabilities for all printers that are accessed through the local print provider's port monitors. (A client administrator sets up access to such printers by selecting the **Local Printer** option when using the Add Printer Wizard.) Such printers include those connected to the local system's serial and parallel ports. They can also include devices connected to other I/O channels, such as SCSI ports, along with printers connected to remote non-NT-based-operating system servers.

The local print provider implements the entire set of [functions defined by print providers](functions-defined-by-print-providers.md). It also supplies the following capabilities:

-   Print job spooler, with despooling of jobs directed to locally accessible print queues.

-   Support for the Windows 2000 and later operating system versions [printer driver architecture](printer-driver-architecture.md) with calls to local printer interface DLLs.

-   Support for vendor-supplied print processors (see [Writing a Print Processor](writing-a-print-processor.md)).

-   Support for vendor-supplied print monitors (see [Writing a Print Monitor](writing-a-print-monitor.md)).

The following diagram provides a (somewhat simplified) view of control flow among the local printer provider's components, when an application creates a print job.

![diagram illustrating a view of control flow among the local printer provider's components when an application creates a print job](images/contflow.png)

As the diagram shows, an application creates a print job by calling the Graphics Driver Interface (GDI). Regardless of whether the print job's initial output format is EMF, the local print provider's job creation API creates a spool file. Later, when the job is scheduled, the spool file is read and, if the format is [*enhanced metafile (EMF)*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enhanced-metafile--emf-), the EMF print processor sends the job back to GDI for conversion to RAW format, with the help of a [printer graphics DLL](printer-graphics-dll.md). The converted data stream can then be sent back through the local print provider to the printer (without being respooled).

A vendor can create [*partial print providers*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-partial-print-provider) that work in conjunction with the local print provider to support custom network configurations.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Local%20Print%20Provider%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


