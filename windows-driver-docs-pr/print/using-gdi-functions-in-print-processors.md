---
title: Using GDI Functions in Print Processors
description: Using GDI Functions in Print Processors
ms.assetid: 2ad62308-ab42-4475-ac42-f753d5091251
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549449" data-raw-source="[&lt;strong&gt;GdiDeleteSpoolFileHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549449)"><strong>GdiDeleteSpoolFileHandle</strong></a></p></td>
<td><p>Releases a spool file handle.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549463" data-raw-source="[&lt;strong&gt;GdiEndDocEMF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549463)"><strong>GdiEndDocEMF</strong></a></p></td>
<td><p>Completes EMF playback operations for a print job document.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549468" data-raw-source="[&lt;strong&gt;GdiEndPageEMF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549468)"><strong>GdiEndPageEMF</strong></a></p></td>
<td><p>Completes EMF playback operations for a physical page, and ejects the page from the printer.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549470" data-raw-source="[&lt;strong&gt;GdiGetDC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549470)"><strong>GdiGetDC</strong></a></p></td>
<td><p>Returns a handle to the printer&#39;s device context.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549478" data-raw-source="[&lt;strong&gt;GdiGetDevmodeForPage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549478)"><strong>GdiGetDevmodeForPage</strong></a></p></td>
<td><p>Returns a document page&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549492" data-raw-source="[&lt;strong&gt;GdiGetPageCount&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549492)"><strong>GdiGetPageCount</strong></a></p></td>
<td><p>Returns the number of document pages.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549505" data-raw-source="[&lt;strong&gt;GdiGetPageHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549505)"><strong>GdiGetPageHandle</strong></a></p></td>
<td><p>Returns a handle to a document page.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549517" data-raw-source="[&lt;strong&gt;GdiGetSpoolFileHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549517)"><strong>GdiGetSpoolFileHandle</strong></a></p></td>
<td><p>Returns a spool file handle, required as input to the other GDI functions.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549524" data-raw-source="[&lt;strong&gt;GdiPlayPageEMF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549524)"><strong>GdiPlayPageEMF</strong></a></p></td>
<td><p>Plays the EMF records associated with a document page.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549529" data-raw-source="[&lt;strong&gt;GdiResetDCEMF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549529)"><strong>GdiResetDCEMF</strong></a></p></td>
<td><p>Resets a printer&#39;s device context.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549534" data-raw-source="[&lt;strong&gt;GdiStartDocEMF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549534)"><strong>GdiStartDocEMF</strong></a></p></td>
<td><p>Performs initialization operations for the print job document.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549543" data-raw-source="[&lt;strong&gt;GdiStartPageEMF&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549543)"><strong>GdiStartPageEMF</strong></a></p></td>
<td><p>Performs initialization operations for a physical page.</p></td>
</tr>
</tbody>
</table>

 

An EMF print processor's [**PrintDocumentOnPrintProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff560724) should call [**GdiGetSpoolFileHandle**](https://msdn.microsoft.com/library/windows/hardware/ff549517) to obtain a spool file handle and [**GdiGetDC**](https://msdn.microsoft.com/library/windows/hardware/ff549470) to obtain the printer's device context handle. Then it can perform the following steps:

-   For each print job document, [**GdiStartDocEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549534) must be called before any EMF records are played and [**GdiEndDocEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549463) must be called after the last EMF record has been played.

-   For each physical page to be printed, [**GdiStartPageEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549543) must be called before any document pages are drawn on the page, and [**GdiEndPageEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549468) must be called after the last document page has been drawn on the physical page.

-   For each document page to be drawn on a physical page, [**GdiGetDevmodeForPage**](https://msdn.microsoft.com/library/windows/hardware/ff549478) must be called to determine if the DEVMODE structure contents have changed since the last document page was drawn. If the DEVMODE has changed, a new physical page must be started (by calling [**GdiEndPageEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549468) and [**GdiStartPageEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549543)), and the printer's device context must be updated by calling [**GdiResetDCEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549529). A document page is drawn on a physical page by first calling [**GdiGetPageHandle**](https://msdn.microsoft.com/library/windows/hardware/ff549505) to obtain a document page handle, and then calling [**GdiPlayPageEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549524) to draw the page.

After the job has been completely drawn, the print processor must call [**GdiDeleteSpoolFileHandle**](https://msdn.microsoft.com/library/windows/hardware/ff549449).

If a print processor requires the total page count before it can begin printing pages (such as for printing pages in reverse order) it can call [**GdiGetPageCount**](https://msdn.microsoft.com/library/windows/hardware/ff549492), but this function doesn't return until spooling ends and thus disables the ability to print while spooling.

If a print processor uses these GDI functions, its [**EnumPrintProcessorDatatypes**](https://msdn.microsoft.com/library/windows/hardware/ff548757) function must return "NT EMF" as a supported data type, which represents generic Windows 2000 and later EMF format. The print processor must not modify EMF records.

 

 




