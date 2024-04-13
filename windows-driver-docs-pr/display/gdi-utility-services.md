---
title: GDI Utility Services
description: GDI Utility Services
keywords:
- GDI WDK Windows 2000 display , utility services
- graphics drivers WDK Windows 2000 display , utility services
- drawing WDK GDI , utility services
ms.date: 04/20/2017
---

# GDI Utility Services


## <span id="ddk_gdi_utility_services_gg"></span><span id="DDK_GDI_UTILITY_SERVICES_GG"></span>


The following table lists the miscellaneous GDI utility services. These services include debugging support, getting and setting the last error, several conversion services that convert from one character encoding type to another, a sort routine, and others.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engbugcheckex" data-raw-source="[&lt;strong&gt;EngBugCheckEx&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engbugcheckex)"><strong>EngBugCheckEx</strong></a></p></td>
<td align="left"><p>Brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdebugbreak" data-raw-source="[&lt;strong&gt;EngDebugBreak&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdebugbreak)"><strong>EngDebugBreak</strong></a></p></td>
<td align="left"><p>Causes a breakpoint in the current process to occur.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdebugprint" data-raw-source="[&lt;strong&gt;EngDebugPrint&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdebugprint)"><strong>EngDebugPrint</strong></a></p></td>
<td align="left"><p>Prints the specified debug message to the kernel debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetlasterror" data-raw-source="[&lt;strong&gt;EngGetLastError&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetlasterror)"><strong>EngGetLastError</strong></a></p></td>
<td align="left"><p>Returns the last error code logged by GDI for the calling thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enghangnotification" data-raw-source="[&lt;strong&gt;EngHangNotification&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enghangnotification)"><strong>EngHangNotification</strong></a></p></td>
<td align="left"><p>Notifies the system that a specified device is inoperable or unresponsive.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-englpkinstalled" data-raw-source="[&lt;strong&gt;EngLpkInstalled&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-englpkinstalled)"><strong>EngLpkInstalled</strong></a></p></td>
<td align="left"><p>Determines whether the language pack is installed on the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmuldiv" data-raw-source="[&lt;strong&gt;EngMulDiv&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmuldiv)"><strong>EngMulDiv</strong></a></p></td>
<td align="left"><p>Multiplies two 32-bit values and then divides the 64-bit result by a third 32-bit value. The return value is rounded up or down to the nearest integer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmultibytetounicoden" data-raw-source="[&lt;strong&gt;EngMultiByteToUnicodeN&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmultibytetounicoden)"><strong>EngMultiByteToUnicodeN</strong></a></p></td>
<td align="left"><p>Converts the specified ANSI source string into a Unicode string using the current ANSI code page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmultibytetowidechar" data-raw-source="[&lt;strong&gt;EngMultiByteToWideChar&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmultibytetowidechar)"><strong>EngMultiByteToWideChar</strong></a></p></td>
<td align="left"><p>Converts an ANSI source string into a wide character string using the specified code page.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engprobeforread" data-raw-source="[&lt;strong&gt;EngProbeForRead&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engprobeforread)"><strong>EngProbeForRead</strong></a></p></td>
<td align="left"><p>Probes a structure for read accessibility.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engprobeforreadandwrite" data-raw-source="[&lt;strong&gt;EngProbeForReadAndWrite&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engprobeforreadandwrite)"><strong>EngProbeForReadAndWrite</strong></a></p></td>
<td align="left"><p>Probes a structure for read and write accessibility.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsetlasterror" data-raw-source="[&lt;strong&gt;EngSetLastError&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsetlasterror)"><strong>EngSetLastError</strong></a></p></td>
<td align="left"><p>Causes GDI to report an error code, which can be retrieved by an application.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsort" data-raw-source="[&lt;strong&gt;EngSort&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsort)"><strong>EngSort</strong></a></p></td>
<td align="left"><p>Performs a quick-sort on the specified list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunicodetomultibyten" data-raw-source="[&lt;strong&gt;EngUnicodeToMultiByteN&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunicodetomultibyten)"><strong>EngUnicodeToMultiByteN</strong></a></p></td>
<td align="left"><p>Converts the specified Unicode string into an ANSI string using the current ANSI code page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engwidechartomultibyte" data-raw-source="[&lt;strong&gt;EngWideCharToMultiByte&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engwidechartomultibyte)"><strong>EngWideCharToMultiByte</strong></a></p></td>
<td align="left"><p>Converts a wide character string into an ANSI source string using the specified code page.</p></td>
</tr>
</tbody>
</table>

 

