---
title: Using GDI Functions in Print Processors
description: Using GDI Functions in Print Processors
keywords:
- EMF record playback WDK print processor
- GDI functions WDK print processor
- NT EMF WDK print processor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using GDI Functions in Print Processors





A set of user-mode GDI functions is exported by Gdi32.dll, for use by print processors that handle NT-based-operating system EMF as an input format. The following table lists the functions that are provided.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdideletespoolfilehandle" data-raw-source="[&lt;strong&gt;GdiDeleteSpoolFileHandle&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdideletespoolfilehandle)"><strong>GdiDeleteSpoolFileHandle</strong></a></p></td>
<td><p>Releases a spool file handle.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdienddocemf" data-raw-source="[&lt;strong&gt;GdiEndDocEMF&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdienddocemf)"><strong>GdiEndDocEMF</strong></a></p></td>
<td><p>Completes EMF playback operations for a print job document.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf" data-raw-source="[&lt;strong&gt;GdiEndPageEMF&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf)"><strong>GdiEndPageEMF</strong></a></p></td>
<td><p>Completes EMF playback operations for a physical page, and ejects the page from the printer.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdc" data-raw-source="[&lt;strong&gt;GdiGetDC&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdc)"><strong>GdiGetDC</strong></a></p></td>
<td><p>Returns a handle to the printer's device context.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdevmodeforpage" data-raw-source="[&lt;strong&gt;GdiGetDevmodeForPage&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdevmodeforpage)"><strong>GdiGetDevmodeForPage</strong></a></p></td>
<td><p>Returns a document page's <a href="/windows/win32/api/wingdi/ns-wingdi-devmodew" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](/windows/win32/api/wingdi/ns-wingdi-devmodew)"><strong>DEVMODEW</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagecount" data-raw-source="[&lt;strong&gt;GdiGetPageCount&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagecount)"><strong>GdiGetPageCount</strong></a></p></td>
<td><p>Returns the number of document pages.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagehandle" data-raw-source="[&lt;strong&gt;GdiGetPageHandle&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagehandle)"><strong>GdiGetPageHandle</strong></a></p></td>
<td><p>Returns a handle to a document page.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetspoolfilehandle" data-raw-source="[&lt;strong&gt;GdiGetSpoolFileHandle&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetspoolfilehandle)"><strong>GdiGetSpoolFileHandle</strong></a></p></td>
<td><p>Returns a spool file handle, required as input to the other GDI functions.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiplaypageemf" data-raw-source="[&lt;strong&gt;GdiPlayPageEMF&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiplaypageemf)"><strong>GdiPlayPageEMF</strong></a></p></td>
<td><p>Plays the EMF records associated with a document page.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiresetdcemf" data-raw-source="[&lt;strong&gt;GdiResetDCEMF&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiresetdcemf)"><strong>GdiResetDCEMF</strong></a></p></td>
<td><p>Resets a printer's device context.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartdocemf" data-raw-source="[&lt;strong&gt;GdiStartDocEMF&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartdocemf)"><strong>GdiStartDocEMF</strong></a></p></td>
<td><p>Performs initialization operations for the print job document.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf" data-raw-source="[&lt;strong&gt;GdiStartPageEMF&lt;/strong&gt;](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf)"><strong>GdiStartPageEMF</strong></a></p></td>
<td><p>Performs initialization operations for a physical page.</p></td>
</tr>
</tbody>
</table>

 

An EMF print processor's [**PrintDocumentOnPrintProcessor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-printdocumentonprintprocessor) should call [**GdiGetSpoolFileHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetspoolfilehandle) to obtain a spool file handle and [**GdiGetDC**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdc) to obtain the printer's device context handle. Then it can perform the following steps:

-   For each print job document, [**GdiStartDocEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartdocemf) must be called before any EMF records are played and [**GdiEndDocEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdienddocemf) must be called after the last EMF record has been played.

-   For each physical page to be printed, [**GdiStartPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf) must be called before any document pages are drawn on the page, and [**GdiEndPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf) must be called after the last document page has been drawn on the physical page.

-   For each document page to be drawn on a physical page, [**GdiGetDevmodeForPage**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetdevmodeforpage) must be called to determine if the DEVMODE structure contents have changed since the last document page was drawn. If the DEVMODE has changed, a new physical page must be started (by calling [**GdiEndPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf) and [**GdiStartPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdistartpageemf)), and the printer's device context must be updated by calling [**GdiResetDCEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiresetdcemf). A document page is drawn on a physical page by first calling [**GdiGetPageHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagehandle) to obtain a document page handle, and then calling [**GdiPlayPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiplaypageemf) to draw the page.

After the job has been completely drawn, the print processor must call [**GdiDeleteSpoolFileHandle**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdideletespoolfilehandle).

If a print processor requires the total page count before it can begin printing pages (such as for printing pages in reverse order) it can call [**GdiGetPageCount**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdigetpagecount), but this function doesn't return until spooling ends and thus disables the ability to print while spooling.

If a print processor uses these GDI functions, its [**EnumPrintProcessorDatatypes**](/windows-hardware/drivers/ddi/winspool/nf-winspool-enumprintprocessordatatypesa) function must return "NT EMF" as a supported data type, which represents generic Windows 2000 and later EMF format. The print processor must not modify EMF records.

