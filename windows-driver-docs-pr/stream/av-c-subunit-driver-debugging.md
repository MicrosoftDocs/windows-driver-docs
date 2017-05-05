---
title: AV/C Subunit Driver Debugging
author: windows-driver-content
description: AV/C Subunit Driver Debugging
ms.assetid: d669157c-60fa-4b7a-8f33-58923a3f2230
keywords:
- Avc.sys function driver WDK , debugging
- trace messages WDK AV/C
- messages WDK AV/C
- debugging drivers WDK AV/C
- generic messages WDK AV/C
- Plug and Play WDK AV/C
- PnP WDK AV/C
- power management WDK AV/C
- I/O WDK AV/C
- connection messages WDK AV/C
- AV/C WDK , debugging
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AV/C Subunit Driver Debugging


## <a href="" id="ddk-debugging-av-c-subunit-drivers-ksg"></a>


Prior to Windows Vista, the debug version of *Avc.sys* permits trace messages to be output to a debug window. The Windows Vista version of *Avc.sys* uses Event Tracing for Windows (ETW).

The *AvcDebugLevel* ULONG type is a bitmap of possible trace levels. Each nibble represents a category of trace output. The default value is 0x00CCCCCC, which sets all message categories to ERROR and WARNING output levels. The best setting to monitor AV/C command activity is 0x000ECCCC (adds the TRACE class of messages to the AV/C category of output). To turn off all debug output, set all bits to 0. The bitmaps for each category are described below.

**Generic Message Category**

The GENERIC category applies to all generic output. The most interesting class of output is FLOW that, when enabled, logs a message at each function's entry and exit points. On computers running Windows Millennium Edition (Windows Me), Windows 98, or Windows 95, all TL\_FLOW (and most TL\_TRACE messages) go to the .ntkern circular buffer pool. To see these log entries, use type **.ntkern** in the debugger, and select the D option. Press the SPACEBAR after pressing D to continue dumping the buffer, one page at a time. Press any other key to cancel the dump. To turn off the .ntkern logging and send the messages to the standard debug output, use the **e ulind** debugger command to set the **ulind** variable to 1 (the default setting is 0).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Meaning</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TL_MASK</p></td>
<td><p>0x0000000F</p></td>
</tr>
<tr class="even">
<td><p>TL_FLOW</p></td>
<td><p>0x00000001</p></td>
</tr>
<tr class="odd">
<td><p>TL_TRACE</p></td>
<td><p>0x00000002</p></td>
</tr>
<tr class="even">
<td><p>TL_WARNING</p></td>
<td><p>0x00000004</p></td>
</tr>
<tr class="odd">
<td><p>TL_ERROR</p></td>
<td><p>0x00000008</p></td>
</tr>
</tbody>
</table>

 

**Plug and Play Message Category**

The Plug and Play (PnP) category applies to all output related to PnP.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Meaning</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TL_PNP_MASK</p></td>
<td><p>0x000000F0</p></td>
</tr>
<tr class="even">
<td><p>TL_PNP_TRACE</p></td>
<td><p>0x00000020</p></td>
</tr>
<tr class="odd">
<td><p>TL_PNP_WARNING</p></td>
<td><p>0x00000040</p></td>
</tr>
<tr class="even">
<td><p>TL_PNP_ERROR</p></td>
<td><p>0x00000080</p></td>
</tr>
</tbody>
</table>

 

**Power Management Message Category**

The Power Management category applies to all output related to power management, including hibernation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Meaning</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TL_POWER_MASK</p></td>
<td><p>0x00000F00</p></td>
</tr>
<tr class="even">
<td><p>TL_POWER_TRACE</p></td>
<td><p>0x00000200</p></td>
</tr>
<tr class="odd">
<td><p>TL_POWER_WARNING</p></td>
<td><p>0x00000400</p></td>
</tr>
<tr class="even">
<td><p>TL_POWER_ERROR</p></td>
<td><p>0x00000800</p></td>
</tr>
</tbody>
</table>

 

**I/O Message Category**

The I/O category applies to all output related to interdriver communication, including IRP processing.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Meaning</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TL_IO_MASK</p></td>
<td><p>0x0000F000</p></td>
</tr>
<tr class="even">
<td><p>TL_IO_NOISE</p></td>
<td><p>0x00001000</p></td>
</tr>
<tr class="odd">
<td><p>TL_IO_TRACE</p></td>
<td><p>0x00002000</p></td>
</tr>
<tr class="even">
<td><p>TL_IO_WARNING</p></td>
<td><p>0x00004000</p></td>
</tr>
<tr class="odd">
<td><p>TL_IO_ERROR</p></td>
<td><p>0x00008000</p></td>
</tr>
</tbody>
</table>

 

**AV/C Message Category**

The AV/C category applies to all output that is related to AV/C commands, plus some internal driver messages of potential relevance to object lists and spin locks (TL\_IO\_NOISE I/O Message Category). Included in the TL\_IO\_TRACE category of messages are command execution times.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Meaning</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TL_AVC_MASK</p></td>
<td><p>0x000F0000</p></td>
</tr>
<tr class="even">
<td><p>TL_AVC_NOISE</p></td>
<td><p>0x00010000</p></td>
</tr>
<tr class="odd">
<td><p>TL_AVC_TRACE</p></td>
<td><p>0x00020000</p></td>
</tr>
<tr class="even">
<td><p>TL_AVC_WARNING</p></td>
<td><p>0x00040000</p></td>
</tr>
<tr class="odd">
<td><p>TL_AVC_ERROR</p></td>
<td><p>0x00080000</p></td>
</tr>
</tbody>
</table>

 

**Connection Message Category**

The Connection category deals with all plug connection-related output.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Meaning</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TL_CXN_MASK</p></td>
<td><p>0x00F00000</p></td>
</tr>
<tr class="even">
<td><p>TL_CXN_NOISE</p></td>
<td><p>0x00100000</p></td>
</tr>
<tr class="odd">
<td><p>TL_CXN_TRACE</p></td>
<td><p>0x00200000</p></td>
</tr>
<tr class="even">
<td><p>TL_CXN_WARNING</p></td>
<td><p>0x00400000</p></td>
</tr>
<tr class="odd">
<td><p>TL_CXN_ERROR</p></td>
<td><p>0x00800000</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Subunit%20Driver%20Debugging%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


