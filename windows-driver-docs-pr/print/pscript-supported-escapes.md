---
title: Pscript-Supported Escapes
description: Pscript-Supported Escapes
ms.assetid: c0133355-fa3b-4117-bd38-b6a8b3898f94
keywords:
- PostScript Printer Driver WDK print , escapes
- Pscript WDK print , escapes
- escapes WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript-Supported Escapes





The Pscript5 printer driver supports the following escapes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Escape</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BEGIN_PATH</p></td>
<td><p>Open a path.</p></td>
</tr>
<tr class="even">
<td><p>CHECKJPEGFORMAT</p></td>
<td><p>Determine whether a printer can handle a JPEG image. For more information about this escape, see CHECKJPEGFORMAT in the Microsoft Windows SDK documentation.</p>
<p>This escape produces a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556260" data-raw-source="[&lt;strong&gt;DrvQueryDeviceSupport&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556260)"><strong>DrvQueryDeviceSupport</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td><p>CHECKPNGFORMAT</p></td>
<td><p>Determine whether a printer can handle a PNG image. For more information about this escape, see CHECKPNGFORMAT in the Windows SDK documentation.</p>
<p>This escape produces a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556260" data-raw-source="[&lt;strong&gt;DrvQueryDeviceSupport&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556260)"><strong>DrvQueryDeviceSupport</strong></a> function.</p></td>
</tr>
<tr class="even">
<td><p>CLIP_TO_PATH</p></td>
<td><p>Define a clip region that is bounded by a path.</p></td>
</tr>
<tr class="odd">
<td><p>DOWNLOADHEADER</p></td>
<td><p>Download all of the procsets (that is, sets of PostScript procedures).</p></td>
</tr>
<tr class="even">
<td><p>DRAWPATTERNRECT</p></td>
<td><p>Create a white, grayscale, or solid black rectangle by using the pattern and rule capabilities of Page Control Language (PCL) on Hewlett Packard LaserJet or LaserJet-compatible printers. A grayscale is a gray pattern that contains a specific mixture of black and white pixels. For more information about this escape, see DRAWPATTERNRECT in the Windows SDK documentation.</p>
<p>This escape is associated with the driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff556217" data-raw-source="[&lt;strong&gt;DrvEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556217)"><strong>DrvEscape</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td><p>ENCAPSULATED_POSTSCRIPT</p></td>
<td><p>Send Encapsulated PostScript (EPS) data to the printer.</p>
<p>This escape is not supported in Microsoft Windows NT 4.0 printer drivers.</p>
<p>This escape is associated with the driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff556203" data-raw-source="[&lt;strong&gt;DrvDrawEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556203)"><strong>DrvDrawEscape</strong></a> function.</p></td>
</tr>
<tr class="even">
<td><p>END_PATH</p></td>
<td><p>End a path.</p></td>
</tr>
<tr class="odd">
<td><p>EPSPRINTING</p></td>
<td><p>Indicate the start or end of EPS printing.</p>
<p>The graphics device interface (GDI) intercepts this escape and translates it to a DDI call other than DrvEscape. The printer driver does not receive this escape.</p></td>
</tr>
<tr class="even">
<td><p>GET_PS_FEATURESETTING</p></td>
<td><p>Get information about a specified feature setting for a PostScript driver.</p>
<p>For more information about this escape, see GET_PS_FEATURESETTING in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>GETTECHNOLOGY</p></td>
<td><p>Get the general technology type for a printer. Printer drivers that are written for versions of the Windows operating system after Windows 3.0 might not support this escape.</p></td>
</tr>
<tr class="even">
<td><p>PASSTHROUGH</p></td>
<td><p>Send data directly to a PostScript printer driver in compatibility mode or GDI-centric mode. PostScript printer drivers in PostScript-centric mode do not support this escape.</p>
<p>For more information about this escape, see PASSTHROUGH in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>POSTSCRIPT_DATA</p></td>
<td><p>Send data directly to a printer driver. This escape is identical to the PASSTHROUGH escape except that PostScript printer drivers support this escape in Windows NT 4.0 compatibility mode only.</p>
<p>For more information about this escape, see POSTSCRIPT_DATA in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>POSTSCRIPT_IDENTIFY</p></td>
<td><p>Set a PostScript printer driver to GDI-centric or PostScript-centric mode.</p>
<p>For more information about this escape, see POSTSCRIPT_IDENTIFY in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>POSTSCRIPT_IGNORE</p></td>
<td><p>Suppress output.</p>
<p>Only PostScript printer drivers in Windows NT 4.0 compatibility mode or in GDI-centric mode support this escape. PostScript printer drivers in PostScript-centric mode do not support this escape.</p></td>
</tr>
<tr class="even">
<td><p>POSTSCRIPT_INJECTION</p></td>
<td><p>Insert a block of raw data in a PostScript job stream.</p>
<p>For more information about this escape, see POSTSCRIPT_INJECTION in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>POSTSCRIPT_PASSTHROUGH</p></td>
<td><p>Send data directly to a PostScript printer driver in Windows NT 4.0 compatibility mode or PostScript-centric mode. PostScript printer drivers in GDI-centric mode do not support this escape.</p>
<p>For more information about this escape, see POSTSCRIPT_PASSTHROUGH in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>QUERYESCSUPPORT</p></td>
<td><p>Determine whether the device driver implements a particular escape.</p>
<p>For more information about this escape, see QUERYESCSUPPORT in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>SETCOPYCOUNT</p></td>
<td><p>Set the number of copies to be printed.</p>
<p>This escape has been superseded by the <strong>DocumentProperties</strong> and <strong>PrinterProperties</strong> functions, which are described in the Windows SDK documentation.</p>
<p>For more information about this escape, see SETCOPYCOUNT in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>SPCLPASSTHROUGH2</p></td>
<td><p>Enable applications to include private procedures and other resources at the document level-save context.</p>
<p>For more information about this escape, see SPCLPASSTHROUGH2 in the Windows SDK documentation.</p></td>
</tr>
</tbody>
</table>

 

The following escapes were added in Windows NT 4.0 but are no longer supported:

-   ADDMSTT

-   IGNORESTARTPAGE

-   NOFIRSTSAVE

The following escapes are obsolete and provided only for compatibility with 16-bit versions of the Windows operating system.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Escape</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>ABORTDOC</p></td>
<td><p>This escape has been superseded by the <strong>AbortDoc</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>ENDDOC</p></td>
<td><p>This escape has been superseded by the <strong>EndDoc</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>GETPHYSPAGESIZE</p></td>
<td><p>This escape has been superseded by the PHYSICALWIDTH and PHYSICALHEIGHT values in the <strong>GetDeviceCaps</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>GETPRINTINGOFFSET</p></td>
<td><p>This escape has been superseded by the PHYSICALOFFSETX and PHYSICALOFFSETY values in the <strong>GetDeviceCaps</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>GETSCALINGFACTOR</p></td>
<td><p>This escape has been superseded by the SCALINGFACTORX and SCALINGFACTORY values in the <strong>GetDeviceCaps</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>NEWFRAME</p></td>
<td><p>This escape has been superseded by the <strong>EndPage</strong> function, which ends a page. Unlike NEWFRAME, <strong>EndPage</strong> is always called after printing a page. <strong>EndPage</strong> is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>NEXTBAND</p></td>
<td><p>Band information is no longer used.</p></td>
</tr>
<tr class="even">
<td><p>SETABORTPROC</p></td>
<td><p>This escape has been superseded by the <strong>SetAbortProc</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
<tr class="odd">
<td><p>SETCOPYCOUNT</p></td>
<td><p>This escape has been superseded by the <strong>DocumentProperties</strong> and <strong>PrinterProperties</strong> functions, which are described in the Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td><p>STARTDOC</p></td>
<td><p>This escape has been superseded by the <strong>StartDoc</strong> function, which is described in the Windows SDK documentation.</p></td>
</tr>
</tbody>
</table>

 

 

 




