---
title: Processing a Print Job
author: windows-driver-content
description: Processing a Print Job
MS-HAID:
- 'provider\_b941f8a9-ddb3-47ca-afa2-d06c6de2ce74.xml'
- 'print.processing\_a\_print\_job'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c5e291d9-069c-4877-a167-862ba5794368
keywords: ["print processors WDK , print job processing", "print jobs WDK , processing", "sending print jobs", "jobs WDK print , processing", "EMF record playback WDK print processor", "N-up printing WDK", "PrintDocumentOnPrintProcessor", "output formats WDK print processor", "input formats WDK print processor", "jobs WDK print", "print jobs WDK"]
---

# Processing a Print Job


## <a href="" id="ddk-processing-a-print-job-gg"></a>


When the spooler is ready to send a print job to a print processor, it calls the print processor's [**OpenPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff559604) function. This function performs initialization activities and returns a handle.

The spooler can then call [**PrintDocumentOnPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff560724), which is the print processor function that converts the data stream from the input format to the output format and returns the converted stream to the spooler.

If the input format is NT-based-operating system EMF, the **PrintDocumentOnPrintProcessor** function can control the playback of the EMF records by using the functions listed in [Using GDI Functions in Print Processors](using-gdi-functions-in-print-processors.md). These functions provide an interface between the print processor and the printer driver. This interface allows print processors to control the physical layout of printer pages and thus facilitates implementing such features as printing multiple document pages per physical page ("N-up" printing), printing pages in reverse order, and printing multiple copies of each page.

A print processor's output data stream must be returned to the spooler. Typically, if the data conversion requires interaction with the printer driver's [printer graphics DLL](printer-graphics-dll.md) (as is the case for EMF input data), the graphics DLL returns the stream to the spooler by calling [**EngWritePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff565467). On the other hand, if the conversion does not call the printer graphics DLL (as is the case for RAW input data), then the print processor calls **WritePrinter** (described in the Microsoft Windows SDK documentation).

The **PrintDocumentOnPrintProcessor** function can be interrupted by asynchronous calls from the spooler to the print processor's [**ControlPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff546352) function. This function implements an application's ability to pause, resume, or cancel a print job.

After **PrintDocumentOnPrintProcessor** finishes converting the data stream and returns, the spooler calls the print processor's [**ClosePrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff545976) function.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Processing%20a%20Print%20Job%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


