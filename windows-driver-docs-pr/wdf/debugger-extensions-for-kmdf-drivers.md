---
title: Summary of Debugger Extensions in Wdfkd.dll
description: The Windows Driver Kit (WDK) includes a debugger extension library, named Wdfkd.dll.
ms.assetid: 5a83ea58-5dbf-40a6-b4cb-9c330851fc33
keywords: ["extensions WDK debuggers", "debugger extensions WDK KMDF", "debugging drivers WDK KMDF , debugger extensions"]
---

#  Summary of Debugger Extensions in Wdfkd.dll


The Windows Driver Kit (WDK) includes a debugger extension library, named *Wdfkd.dll*. This library contains debugger extension commands that you can use to debug both Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers starting with version 2.

For a complete description of each command, see [**Windows Driver Framework Extensions (Wdfkd.dll)**](https://msdn.microsoft.com/library/windows/hardware/ff551876). For more information about all available debugger extension libraries, see the documentation that is supplied with the [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) package.

You can find a video series that demonstrates how to debug a KMDF driver at [Videos: Debugging KMDF Drivers](debugging-kernel-mode-driver-framework-drivers.md).

To debug a driver that uses UMDF version 1.11 or earlier, you must instead use the *Wudfext.dll* debugger extension library. For more info, see [User-Mode Driver Framework Extensions (Wudfext.dll)](https://msdn.microsoft.com/library/windows/hardware/ff560030).

The extension commands that the *Wdfkd.dll* extension library provides include:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Extension</th>
<th align="left">Description</th>
<th align="left">Frameworks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfhelp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565761)</p></td>
<td align="left"><p>Displays this list of debugger extensions.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfchildlist</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565672)</p></td>
<td align="left"><p>Displays a child list's state and information about all of the device identification descriptions that are in the child list.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfcollection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565675)</p></td>
<td align="left"><p>Displays the objects that are contained in a collection.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfcommonbuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565679)</p></td>
<td align="left"><p>Displays information about a [common buffer object](using-common-buffers.md).</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfcrashdump</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565682)</p></td>
<td align="left"><p>Displays the framework's event log records, if available, from a small memory dump. The framework's event log records are available if [ForceLogsInMiniDump](registry-values-for-debugging-kmdf-drivers.md) is set in the registry, or if the framework can determine that your driver caused the bug check.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfdevext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565686)</p></td>
<td align="left"><p>Displays the WDFDEVICE-typed object handle that is associated with the <strong>DeviceExtension</strong> member of a Microsoft Windows Driver Model (WDM) [<strong>DEVICE_OBJECT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 1</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfdevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565703)</p></td>
<td align="left"><p>Displays information that is associated with a WDFDEVICE-typed handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfdeviceinterrupts</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265378)</p></td>
<td align="left"><p>Displays all the interrupt objects for a specified device handle</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfdevicequeues</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565715)</p></td>
<td align="left"><p>Displays information about all of the queue objects that belong to a specified device.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfdmaenabler</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565717)</p></td>
<td align="left"><p>Displays information about a [DMA enabler object](framework-dma-objects.md), along with its associated DMA transaction objects and common buffer objects.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfdmaenablers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565719)</p></td>
<td align="left"><p>Displays a summary of all DMA enabler objects, DMA transaction objects, and common buffer objects that are associated with a specified device object.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfdmatransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565721)</p></td>
<td align="left"><p>Displays information about a WDF direct memory access (DMA) transaction object.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfdriverinfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565724)</p></td>
<td align="left"><p>Displays information about a framework-based driver, such as its library version and hierarchy of object handles.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfextendwatchdog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565731)</p></td>
<td align="left"><p>Extends the time-out period (from 10 minutes to 24 hours) of the framework's watchdog timer during power transitions.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdffindobjects</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565738)</p></td>
<td align="left"><p>Finds and displays framework objects.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfforwardprogress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565743)</p></td>
<td align="left"><p>Displays information about the [guaranteed forward progress](guaranteeing-forward-progress-of-i-o-operations.md) capabilities of an I/O queue.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfgetdriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565751)</p></td>
<td align="left"><p>Displays the driver name.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfhandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565758)</p></td>
<td align="left"><p>Displays information about a framework object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfinterrupt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565787)</p></td>
<td align="left"><p>Displays information about a framework interrupt object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfiotarget</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565791)</p></td>
<td align="left"><p>Displays information about a WDFIOTARGET-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfldr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565803)</p></td>
<td align="left"><p>Displays information about all of the drivers that are using the framework library.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 1</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdflogdump</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565805)</p></td>
<td align="left"><p>Displays the framework's event log records, if available, from a complete memory dump, a kernel memory dump, or a live kernel-mode target.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdflogsave</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566102)</p></td>
<td align="left"><p>Saves the framework's event log records in an event trace log (.<em>etl</em>) file that you can view by using [TraceView](https://msdn.microsoft.com/library/windows/hardware/ff553872).</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfmemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566103)</p></td>
<td align="left"><p>Displays a memory object's buffer address and size.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfobject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566107)</p></td>
<td align="left"><p>Displays information about a framework object.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfopenhandles</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566110)</p></td>
<td align="left"><p>Displays information about all the handles that are open on the specified WDF device.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfpoolusage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566115)</p></td>
<td align="left"><p>Displays a driver's memory pool usage.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfqueue</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566118)</p></td>
<td align="left"><p>Displays information about a WDFQUEUE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfrequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566119)</p></td>
<td align="left"><p>Displays information about a WDFREQUEST-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfsearchpath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566120)</p></td>
<td align="left"><p>Sets the search path for locating the framework log's format files.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfsettraceprefix</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566123)</p></td>
<td align="left"><p>Sets a prefix string for tracing messages in the framework's event log.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfsetdriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566121)</p></td>
<td align="left"><p>Sets a driver name that is used as a default name for other commands that require a driver name.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfspinlock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566125)</p></td>
<td align="left"><p>Displays information about a framework spin-lock object. This information includes the spin lock's acquisition history and the length of time that the lock was held.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdftagtracker</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566126)</p></td>
<td align="left"><p>Displays tag information (including the tag value, line, file, and time) for a specified object tag.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdftmffile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566128)</p></td>
<td align="left"><p>Specifies the trace message format (.<em>tmf</em>) files that the <strong>!wdflogdump</strong> extension will use to display event log records.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdftraceprtdebug</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566129)</p></td>
<td align="left"><p>Turns on the TracePrt diagnostic mode.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfumdevstack</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265379)</p></td>
<td align="left"><p>Displays detailed information about a UMDF device stack in the implicit process.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfumdevstacks</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265380)</p></td>
<td align="left"><p>Displays information about all UMDF device stacks in the implicit process.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfumdownirp</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265381)</p></td>
<td align="left"><p>Displays the kernel-mode I/O request packet (IRP) that is associated with a specified user-mode IRP.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfumfile</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265382)</p></td>
<td align="left"><p>Displays information about a UMDF intra-stack file.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfumirp</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265383)</p></td>
<td align="left"><p>Displays information about a user-mode I/O request packet (UM IRP).</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfumirps</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265384)</p></td>
<td align="left"><p>Displays the list of pending user-mode I/O request packets (UM IRPs) in the implicit process.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfusbdevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566131)</p></td>
<td align="left"><p>Displays information about a WDFUSBDEVICE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfusbinterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566134)</p></td>
<td align="left"><p>Displays information about a WDFUSBINTERFACE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!wdfkd.wdfusbpipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566136)</p></td>
<td align="left"><p>Displays information about a WDFUSBPIPE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!wdfkd.wdfwmi</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566137)</p></td>
<td align="left"><p>Displays a device's Windows Management Instrumentation (WMI) information.</p></td>
<td align="left">KMDF</td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20%20Summary%20of%20Debugger%20Extensions%20in%20Wdfkd.dll%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




