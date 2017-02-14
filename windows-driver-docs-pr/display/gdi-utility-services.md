---
title: GDI Utility Services
description: GDI Utility Services
ms.assetid: 4ceec90d-5be2-4b79-87b3-1fdb6b0aea6b
keywords: ["GDI WDK Windows 2000 display , utility services", "graphics drivers WDK Windows 2000 display , utility services", "drawing WDK GDI , utility services"]
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
<td align="left"><p>[<strong>EngBugCheckEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564187)</p></td>
<td align="left"><p>Brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDebugBreak</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564773)</p></td>
<td align="left"><p>Causes a breakpoint in the current process to occur.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngDebugPrint</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564779)</p></td>
<td align="left"><p>Prints the specified debug message to the kernel debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetLastError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564940)</p></td>
<td align="left"><p>Returns the last error code logged by GDI for the calling thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngHangNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564958)</p></td>
<td align="left"><p>Notifies the system that a specified device is inoperable or unresponsive.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngLpkInstalled</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564969)</p></td>
<td align="left"><p>Determines whether the language pack is installed on the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngMulDiv</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564978)</p></td>
<td align="left"><p>Multiplies two 32-bit values and then divides the 64-bit result by a third 32-bit value. The return value is rounded up or down to the nearest integer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMultiByteToUnicodeN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564979)</p></td>
<td align="left"><p>Converts the specified ANSI source string into a Unicode string using the current ANSI code page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngMultiByteToWideChar</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564980)</p></td>
<td align="left"><p>Converts an ANSI source string into a wide character string using the specified code page.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngProbeForRead</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564983)</p></td>
<td align="left"><p>Probes a structure for read accessibility.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngProbeForReadAndWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564984)</p></td>
<td align="left"><p>Probes a structure for read and write accessibility.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngSetLastError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565015)</p></td>
<td align="left"><p>Causes GDI to report an error code, which can be retrieved by an application.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngSort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565022)</p></td>
<td align="left"><p>Performs a quick-sort on the specified list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngUnicodeToMultiByteN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565038)</p></td>
<td align="left"><p>Converts the specified Unicode string into an ANSI string using the current ANSI code page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngWideCharToMultiByte</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565466)</p></td>
<td align="left"><p>Converts a wide character string into an ANSI source string using the specified code page.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Utility%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




