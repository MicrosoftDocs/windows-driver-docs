---
title: Using GDI Functions in Print Processors
author: windows-driver-content
description: Using GDI Functions in Print Processors
ms.assetid: 2ad62308-ab42-4475-ac42-f753d5091251
keywords:
- EMF record playback WDK print processor
- GDI functions WDK print processor
- NT EMF WDK print processor
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using GDI Functions in Print Processors


## <a href="" id="ddk-using-gdi-functions-in-print-processors-gg"></a>


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
<td><p>[<strong>GdiDeleteSpoolFileHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549449)</p></td>
<td><p>Releases a spool file handle.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GdiEndDocEMF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549463)</p></td>
<td><p>Completes EMF playback operations for a print job document.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GdiEndPageEMF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549468)</p></td>
<td><p>Completes EMF playback operations for a physical page, and ejects the page from the printer.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GdiGetDC</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549470)</p></td>
<td><p>Returns a handle to the printer's device context.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GdiGetDevmodeForPage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549478)</p></td>
<td><p>Returns a document page's [<strong>DEVMODEW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GdiGetPageCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549492)</p></td>
<td><p>Returns the number of document pages.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GdiGetPageHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549505)</p></td>
<td><p>Returns a handle to a document page.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GdiGetSpoolFileHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549517)</p></td>
<td><p>Returns a spool file handle, required as input to the other GDI functions.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GdiPlayPageEMF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549524)</p></td>
<td><p>Plays the EMF records associated with a document page.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GdiResetDCEMF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549529)</p></td>
<td><p>Resets a printer's device context.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GdiStartDocEMF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549534)</p></td>
<td><p>Performs initialization operations for the print job document.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GdiStartPageEMF</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549543)</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20GDI%20Functions%20in%20Print%20Processors%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


