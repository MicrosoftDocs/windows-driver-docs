---
title: GDI Utility Services
description: GDI Utility Services
ms.assetid: 4ceec90d-5be2-4b79-87b3-1fdb6b0aea6b
keywords:
- GDI WDK Windows 2000 display , utility services
- graphics drivers WDK Windows 2000 display , utility services
- drawing WDK GDI , utility services
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564187" data-raw-source="[&lt;strong&gt;EngBugCheckEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564187)"><strong>EngBugCheckEx</strong></a></p></td>
<td align="left"><p>Brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564773" data-raw-source="[&lt;strong&gt;EngDebugBreak&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564773)"><strong>EngDebugBreak</strong></a></p></td>
<td align="left"><p>Causes a breakpoint in the current process to occur.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564779" data-raw-source="[&lt;strong&gt;EngDebugPrint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564779)"><strong>EngDebugPrint</strong></a></p></td>
<td align="left"><p>Prints the specified debug message to the kernel debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564940" data-raw-source="[&lt;strong&gt;EngGetLastError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564940)"><strong>EngGetLastError</strong></a></p></td>
<td align="left"><p>Returns the last error code logged by GDI for the calling thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564958" data-raw-source="[&lt;strong&gt;EngHangNotification&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564958)"><strong>EngHangNotification</strong></a></p></td>
<td align="left"><p>Notifies the system that a specified device is inoperable or unresponsive.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564969" data-raw-source="[&lt;strong&gt;EngLpkInstalled&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564969)"><strong>EngLpkInstalled</strong></a></p></td>
<td align="left"><p>Determines whether the language pack is installed on the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564978" data-raw-source="[&lt;strong&gt;EngMulDiv&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564978)"><strong>EngMulDiv</strong></a></p></td>
<td align="left"><p>Multiplies two 32-bit values and then divides the 64-bit result by a third 32-bit value. The return value is rounded up or down to the nearest integer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564979" data-raw-source="[&lt;strong&gt;EngMultiByteToUnicodeN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564979)"><strong>EngMultiByteToUnicodeN</strong></a></p></td>
<td align="left"><p>Converts the specified ANSI source string into a Unicode string using the current ANSI code page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564980" data-raw-source="[&lt;strong&gt;EngMultiByteToWideChar&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564980)"><strong>EngMultiByteToWideChar</strong></a></p></td>
<td align="left"><p>Converts an ANSI source string into a wide character string using the specified code page.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564983" data-raw-source="[&lt;strong&gt;EngProbeForRead&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564983)"><strong>EngProbeForRead</strong></a></p></td>
<td align="left"><p>Probes a structure for read accessibility.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564984" data-raw-source="[&lt;strong&gt;EngProbeForReadAndWrite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564984)"><strong>EngProbeForReadAndWrite</strong></a></p></td>
<td align="left"><p>Probes a structure for read and write accessibility.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565015" data-raw-source="[&lt;strong&gt;EngSetLastError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565015)"><strong>EngSetLastError</strong></a></p></td>
<td align="left"><p>Causes GDI to report an error code, which can be retrieved by an application.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565022" data-raw-source="[&lt;strong&gt;EngSort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565022)"><strong>EngSort</strong></a></p></td>
<td align="left"><p>Performs a quick-sort on the specified list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565038" data-raw-source="[&lt;strong&gt;EngUnicodeToMultiByteN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565038)"><strong>EngUnicodeToMultiByteN</strong></a></p></td>
<td align="left"><p>Converts the specified Unicode string into an ANSI string using the current ANSI code page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565466" data-raw-source="[&lt;strong&gt;EngWideCharToMultiByte&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565466)"><strong>EngWideCharToMultiByte</strong></a></p></td>
<td align="left"><p>Converts a wide character string into an ANSI source string using the specified code page.</p></td>
</tr>
</tbody>
</table>

 

 

 





