---
title: Using GDI Functions in Print Processors
description: Using GDI Functions in Print Processors
keywords:
- EMF record playback WDK print processor
- GDI functions WDK print processor
- NT EMF WDK print processor
ms.date: 02/06/2024
---

# Using GDI Functions in Print Processors

A set of user-mode GDI functions is exported by Gdi32.dll, for use by print processors that handle NT-based-operating system EMF as an input format. The following table lists the functions that are provided.

| Function name | Description |
|--|--|
| [**GdiDeleteSpoolFileHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdideletespoolfilehandle) | Releases a spool file handle. |
| [**GdiEndDocEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdienddocemf) | Completes EMF playback operations for a print job document. |
| [**GdiEndPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf) | Completes EMF playback operations for a physical page, and ejects the page from the printer. |
| [**GdiGetDC**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdc) | Returns a handle to the printer's device context. |
| [**GdiGetDevmodeForPage**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdevmodeforpage) | Returns a document page's DEVMODEW structure. |
| [**GdiGetPageCount**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagecount) | Returns the number of document pages. |
| [**GdiGetPageHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagehandle) | Returns a handle to a document page. |
| [**GdiGetSpoolFileHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetspoolfilehandle) | Returns a spool file handle, required as input to the other GDI functions. |
| [**GdiPlayPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiplaypageemf) | Plays the EMF records associated with a document page. |
| [**GdiResetDCEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiresetdcemf) | Resets a printer's device context. |
| [**GdiStartDocEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartdocemf) | Performs initialization operations for the print job document. |
| [**GdiStartPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf) | Performs initialization operations for a physical page. |

An EMF print processor's [**PrintDocumentOnPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-printdocumentonprintprocessor) should call [**GdiGetSpoolFileHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetspoolfilehandle) to obtain a spool file handle and [**GdiGetDC**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdc) to obtain the printer's device context handle. Then it can perform the following steps:

- For each print job document, [**GdiStartDocEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartdocemf) must be called before any EMF records are played and [**GdiEndDocEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdienddocemf) must be called after the last EMF record has been played.

- For each physical page to be printed, [**GdiStartPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf) must be called before any document pages are drawn on the page, and [**GdiEndPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf) must be called after the last document page has been drawn on the physical page.

- For each document page to be drawn on a physical page, [**GdiGetDevmodeForPage**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdevmodeforpage) must be called to determine if the DEVMODE structure contents have changed since the last document page was drawn. If the DEVMODE has changed, a new physical page must be started (by calling [**GdiEndPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf) and [**GdiStartPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf)), and the printer's device context must be updated by calling [**GdiResetDCEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiresetdcemf). A document page is drawn on a physical page by first calling [**GdiGetPageHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagehandle) to obtain a document page handle, and then calling [**GdiPlayPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiplaypageemf) to draw the page.

After the job has been completely drawn, the print processor must call [**GdiDeleteSpoolFileHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdideletespoolfilehandle).

If a print processor requires the total page count before it can begin printing pages (such as for printing pages in reverse order) it can call [**GdiGetPageCount**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagecount), but this function doesn't return until spooling ends and thus disables the ability to print while spooling.

If a print processor uses these GDI functions, its [**EnumPrintProcessorDatatypes**](/windows-hardware/drivers/ddi/winspool/nf-winspool-enumprintprocessordatatypesa) function must return "NT EMF" as a supported data type, which represents generic Windows 2000 and later EMF format. The print processor must not modify EMF records.
