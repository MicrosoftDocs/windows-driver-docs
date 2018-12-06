---
title: Processing a Print Job
description: Processing a Print Job
ms.assetid: c5e291d9-069c-4877-a167-862ba5794368
keywords:
- print processors WDK , print job processing
- print jobs WDK , processing
- sending print jobs
- jobs WDK print , processing
- EMF record playback WDK print processor
- N-up printing WDK
- PrintDocumentOnPrintProcessor
- output formats WDK print processor
- input formats WDK print processor
- jobs WDK print
- print jobs WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing a Print Job





When the spooler is ready to send a print job to a print processor, it calls the print processor's [**OpenPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff559604) function. This function performs initialization activities and returns a handle.

The spooler can then call [**PrintDocumentOnPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff560724), which is the print processor function that converts the data stream from the input format to the output format and returns the converted stream to the spooler.

If the input format is NT-based-operating system EMF, the **PrintDocumentOnPrintProcessor** function can control the playback of the EMF records by using the functions listed in [Using GDI Functions in Print Processors](using-gdi-functions-in-print-processors.md). These functions provide an interface between the print processor and the printer driver. This interface allows print processors to control the physical layout of printer pages and thus facilitates implementing such features as printing multiple document pages per physical page ("N-up" printing), printing pages in reverse order, and printing multiple copies of each page.

A print processor's output data stream must be returned to the spooler. Typically, if the data conversion requires interaction with the printer driver's [printer graphics DLL](printer-graphics-dll.md) (as is the case for EMF input data), the graphics DLL returns the stream to the spooler by calling [**EngWritePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff565467). On the other hand, if the conversion does not call the printer graphics DLL (as is the case for RAW input data), then the print processor calls **WritePrinter** (described in the Microsoft Windows SDK documentation).

The **PrintDocumentOnPrintProcessor** function can be interrupted by asynchronous calls from the spooler to the print processor's [**ControlPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff546352) function. This function implements an application's ability to pause, resume, or cancel a print job.

After **PrintDocumentOnPrintProcessor** finishes converting the data stream and returns, the spooler calls the print processor's [**ClosePrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff545976) function.

 

 




