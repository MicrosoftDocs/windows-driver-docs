---
title: Process a Print Job
description: Provides information about how to process a print job.
keywords:
- print processors WDK , print job processing
- print jobs WDK, processing
- sending print jobs
- jobs WDK print, processing
- EMF record playback WDK print processor
- N-up printing WDK
- PrintDocumentOnPrintProcessor
- output formats WDK print processor
- input formats WDK print processor
- jobs WDK print
- print jobs WDK
ms.date: 09/16/2022
---

# Process a print job

When the spooler is ready to send a print job to a print processor, it calls the print processor's [**OpenPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-openprintprocessor) function. This function performs initialization activities and returns a handle.

The spooler can then call [**PrintDocumentOnPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-printdocumentonprintprocessor), which is the print processor function that converts the data stream from the input format to the output format and returns the converted stream to the spooler.

If the input format is NT-based-operating system EMF, the **PrintDocumentOnPrintProcessor** function can control the playback of the EMF records by using the functions listed in [Using GDI functions in print processors](using-gdi-functions-in-print-processors.md). These functions provide an interface between the print processor and the printer driver. This interface allows print processors to control the physical layout of printer pages and thus facilitates implementing such features as printing multiple document pages per physical page ("N-up" printing), printing pages in reverse order, and printing multiple copies of each page.

A print processor's output data stream must be returned to the spooler. Typically, if the data conversion requires interaction with the printer driver's [printer graphics DLL](printer-graphics-dll.md) (as is the case for EMF input data), the graphics DLL returns the stream to the spooler by calling [**EngWritePrinter**](/windows/win32/api/winddi/nf-winddi-engwriteprinter). On the other hand, if the conversion does not call the printer graphics DLL (as is the case for RAW input data), then the print processor calls [**WritePrinter**](/windows/win32/printdocs/writeprinter).

The **PrintDocumentOnPrintProcessor** function can be interrupted by asynchronous calls from the spooler to the print processor's [**ControlPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-controlprintprocessor) function. This function implements an application's ability to pause, resume, or cancel a print job.

After **PrintDocumentOnPrintProcessor** finishes converting the data stream and returns, the spooler calls the print processor's [**ClosePrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeprintprocessor) function.
