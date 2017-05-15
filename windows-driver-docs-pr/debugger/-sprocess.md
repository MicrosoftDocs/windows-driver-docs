---
title: sprocess
description: The sprocess extension displays information about the specified session process, or about all processes in the specified session.
ms.assetid: 03c69f3c-501a-44e4-98e0-bf851ca6d24e
keywords: ["sprocess Windows Debugging"]
topic_type:
- apiref
api_name:
- sprocess
api_type:
- NA
---

# !sprocess


The **!sprocess** extension displays information about the specified session process, or about all processes in the specified session.

``` syntax
!sprocess Session [Flags [ImageName]] 
!sprocess -?
```

## <span id="ddk__sprocess_dbg"></span><span id="DDK__SPROCESS_DBG"></span>Parameters


<span id="_______Session______"></span><span id="_______session______"></span><span id="_______SESSION______"></span> *Session*   
Specifies the session that owns the desired process. *Session* is always interpreted as a decimal number.

*Session* can have the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>-1</p></td>
<td align="left"><p>Use current session. This is the default.</p></td>
</tr>
<tr class="even">
<td align="left"><p>-2</p></td>
<td align="left"><p>Use [session context](changing-contexts.md#session-context).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>-4</p></td>
<td align="left"><p>Display all processes by session.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of detail in the display. *Flags* can be any combination of the following bits. The default is 0.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>Display minimal information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Bit 0 (0x1)</p></td>
<td align="left"><p>Display time and priority statistics.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Bit 1 (0x2)</p></td>
<td align="left"><p>Adds to the display a list of threads and events associated with the process and the wait states of the threads.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Bit 2 (0x4)</p></td>
<td align="left"><p>Adds to the display a list of threads associated with the process. If this bit is used without Bit 1 (0x2), each thread is displayed on a single line. If this is included with Bit 1, each thread is displayed with a stack trace.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Bit 3 (0x8)</p></td>
<td align="left"><p>Adds to the display of each function the return address, the stack pointer and, on Itanium-based systems, the <strong>bsp</strong> register value. It suppresses the display of function arguments.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Bit 4 (0x10)</p></td>
<td align="left"><p>Display only the return address of each function. Suppress the arguments and stack pointers.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______ImageName______"></span><span id="_______imagename______"></span><span id="_______IMAGENAME______"></span> *ImageName*   
Specifies the name of the process to be displayed. All processes whose executable image names match *ImageName* are displayed. The image name must match that in the EPROCESS block. In general, this is the executable name that was invoked to start the process, including the file extension (usually .exe), and truncated after the fifteenth character. There is no way to specify an image name that contains a space.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window. This help text has some omissions.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about sessions and processes in kernel mode, see [Changing Contexts](changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

The output of this extension is similar to that of [**!process**](-process.md), except that the addresses of \_MM\_SESSION\_SPACE and \_MMSESSION are displayed as well.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!sprocess%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




