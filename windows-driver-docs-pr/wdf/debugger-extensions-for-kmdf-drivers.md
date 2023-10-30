---
title: Summary of Debugger Extensions in Wdfkd.dll
description: The Windows Driver Kit (WDK) includes a debugger extension library, named Wdfkd.dll.
keywords:
- extensions WDK debuggers
- debugger extensions WDK KMDF
- debugging drivers WDK KMDF , debugger extensions
ms.date: 04/20/2017
---

#  Summary of Debugger Extensions in Wdfkd.dll


The Windows Driver Kit (WDK) includes a debugger extension library, named *Wdfkd.dll*. This library contains debugger extension commands that you can use to debug both Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers starting with version 2.

For a complete description of each command, see [**Windows Driver Framework Extensions (Wdfkd.dll)**](../debuggercmds/kernel-mode-driver-framework-extensions--wdfkd-dll-.md). For more information about all available debugger extension libraries, see the documentation that is supplied with the [Windows Debugging](../debuggercmds/index.md) package.

You can find a video series that demonstrates how to debug a KMDF driver at [Videos: Debugging KMDF Drivers](debugging-kernel-mode-driver-framework-drivers.md).

To debug a driver that uses UMDF version 1.11 or earlier, you must instead use the *Wudfext.dll* debugger extension library. For more info, see [User-Mode Driver Framework Extensions (Wudfext.dll)](../debuggercmds/user-mode-driver-framework-extensions--wudfext-dll-.md).

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
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfhelp" data-raw-source="[&lt;strong&gt;!wdfkd.wdfhelp&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfhelp.md)"><strong>!wdfkd.wdfhelp</strong></a></p></td>
<td align="left"><p>Displays this list of debugger extensions.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfchildlist" data-raw-source="[&lt;strong&gt;!wdfkd.wdfchildlist&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfchildlist.md)"><strong>!wdfkd.wdfchildlist</strong></a></p></td>
<td align="left"><p>Displays a child list's state and information about all of the device identification descriptions that are in the child list.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfcollection" data-raw-source="[&lt;strong&gt;!wdfkd.wdfcollection&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfcollection.md)"><strong>!wdfkd.wdfcollection</strong></a></p></td>
<td align="left"><p>Displays the objects that are contained in a collection.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfcommonbuffer" data-raw-source="[&lt;strong&gt;!wdfkd.wdfcommonbuffer&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfcommonbuffer.md)"><strong>!wdfkd.wdfcommonbuffer</strong></a></p></td>
<td align="left"><p>Displays information about a <a href="using-common-buffers.md" data-raw-source="[common buffer object](using-common-buffers.md)">common buffer object</a>.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfcrashdump" data-raw-source="[&lt;strong&gt;!wdfkd.wdfcrashdump&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfcrashdump.md)"><strong>!wdfkd.wdfcrashdump</strong></a></p></td>
<td align="left"><p>Displays the framework's event log records, if available, from a small memory dump. The framework's event log records are available if <a href="registry-values-for-debugging-kmdf-drivers.md" data-raw-source="[ForceLogsInMiniDump](registry-values-for-debugging-kmdf-drivers.md)">ForceLogsInMiniDump</a> is set in the registry, or if the framework can determine that your driver caused the bug check.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdevext" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdevext&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdevext.md)"><strong>!wdfkd.wdfdevext</strong></a></p></td>
<td align="left"><p>Displays the WDFDEVICE-typed object handle that is associated with the <strong>DeviceExtension</strong> member of a Microsoft Windows Driver Model (WDM) <a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object" data-raw-source="[&lt;strong&gt;DEVICE_OBJECT&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object)"><strong>DEVICE_OBJECT</strong></a> structure.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 1</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdevice" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdevice&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdevice.md)"><strong>!wdfkd.wdfdevice</strong></a></p></td>
<td align="left"><p>Displays information that is associated with a WDFDEVICE-typed handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdeviceinterrupts" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdeviceinterrupts&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdeviceinterrupts.md)"><strong>!wdfkd.wdfdeviceinterrupts</strong></a></p></td>
<td align="left"><p>Displays all the interrupt objects for a specified device handle</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdevicequeues" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdevicequeues&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdevicequeues.md)"><strong>!wdfkd.wdfdevicequeues</strong></a></p></td>
<td align="left"><p>Displays information about all of the queue objects that belong to a specified device.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdmaenabler" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdmaenabler&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdmaenabler.md)"><strong>!wdfkd.wdfdmaenabler</strong></a></p></td>
<td align="left"><p>Displays information about a <a href="framework-dma-objects.md" data-raw-source="[DMA enabler object](framework-dma-objects.md)">DMA enabler object</a>, along with its associated DMA transaction objects and common buffer objects.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdmaenablers" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdmaenablers&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdmaenablers.md)"><strong>!wdfkd.wdfdmaenablers</strong></a></p></td>
<td align="left"><p>Displays a summary of all DMA enabler objects, DMA transaction objects, and common buffer objects that are associated with a specified device object.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdmatransaction" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdmatransaction&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdmatransaction.md)"><strong>!wdfkd.wdfdmatransaction</strong></a></p></td>
<td align="left"><p>Displays information about a WDF direct memory access (DMA) transaction object.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfdriverinfo" data-raw-source="[&lt;strong&gt;!wdfkd.wdfdriverinfo&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfdriverinfo.md)"><strong>!wdfkd.wdfdriverinfo</strong></a></p></td>
<td align="left"><p>Displays information about a framework-based driver, such as its library version and hierarchy of object handles.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfextendwatchdog" data-raw-source="[&lt;strong&gt;!wdfkd.wdfextendwatchdog&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfextendwatchdog.md)"><strong>!wdfkd.wdfextendwatchdog</strong></a></p></td>
<td align="left"><p>Extends the time-out period (from 10 minutes to 24 hours) of the framework's watchdog timer during power transitions.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdffindobjects" data-raw-source="[&lt;strong&gt;!wdfkd.wdffindobjects&lt;/strong&gt;](../debuggercmds/-wdfkd-wdffindobjects.md)"><strong>!wdfkd.wdffindobjects</strong></a></p></td>
<td align="left"><p>Finds and displays framework objects.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfforwardprogress" data-raw-source="[&lt;strong&gt;!wdfkd.wdfforwardprogress&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfforwardprogress.md)"><strong>!wdfkd.wdfforwardprogress</strong></a></p></td>
<td align="left"><p>Displays information about the <a href="guaranteeing-forward-progress-of-i-o-operations.md" data-raw-source="[guaranteed forward progress](guaranteeing-forward-progress-of-i-o-operations.md)">guaranteed forward progress</a> capabilities of an I/O queue.</p></td>
<td align="left">KMDF</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfgetdriver" data-raw-source="[&lt;strong&gt;!wdfkd.wdfgetdriver&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfgetdriver.md)"><strong>!wdfkd.wdfgetdriver</strong></a></p></td>
<td align="left"><p>Displays the driver name.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfhandle" data-raw-source="[&lt;strong&gt;!wdfkd.wdfhandle&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfhandle.md)"><strong>!wdfkd.wdfhandle</strong></a></p></td>
<td align="left"><p>Displays information about a framework object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfinterrupt" data-raw-source="[&lt;strong&gt;!wdfkd.wdfinterrupt&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfinterrupt.md)"><strong>!wdfkd.wdfinterrupt</strong></a></p></td>
<td align="left"><p>Displays information about a framework interrupt object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfiotarget" data-raw-source="[&lt;strong&gt;!wdfkd.wdfiotarget&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfiotarget.md)"><strong>!wdfkd.wdfiotarget</strong></a></p></td>
<td align="left"><p>Displays information about a WDFIOTARGET-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfldr" data-raw-source="[&lt;strong&gt;!wdfkd.wdfldr&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfldr.md)"><strong>!wdfkd.wdfldr</strong></a></p></td>
<td align="left"><p>Displays information about all of the drivers that are using the framework library.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 1</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdflogdump" data-raw-source="[&lt;strong&gt;!wdfkd.wdflogdump&lt;/strong&gt;](../debuggercmds/-wdfkd-wdflogdump.md)"><strong>!wdfkd.wdflogdump</strong></a></p></td>
<td align="left"><p>Displays the framework's event log records, if available, from a complete memory dump, a kernel memory dump, or a live kernel-mode target.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdflogsave" data-raw-source="[&lt;strong&gt;!wdfkd.wdflogsave&lt;/strong&gt;](../debuggercmds/-wdfkd-wdflogsave.md)"><strong>!wdfkd.wdflogsave</strong></a></p></td>
<td align="left"><p>Saves the framework's event log records in an event trace log (.<em>etl</em>) file that you can view by using <a href="/windows-hardware/drivers/devtest/traceview" data-raw-source="[TraceView](../devtest/traceview.md)">TraceView</a>.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfmemory" data-raw-source="[&lt;strong&gt;!wdfkd.wdfmemory&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfmemory.md)"><strong>!wdfkd.wdfmemory</strong></a></p></td>
<td align="left"><p>Displays a memory object's buffer address and size.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfobject" data-raw-source="[&lt;strong&gt;!wdfkd.wdfobject&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfobject.md)"><strong>!wdfkd.wdfobject</strong></a></p></td>
<td align="left"><p>Displays information about a framework object.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfopenhandles" data-raw-source="[&lt;strong&gt;!wdfkd.wdfopenhandles&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfopenhandles.md)"><strong>!wdfkd.wdfopenhandles</strong></a></p></td>
<td align="left"><p>Displays information about all the handles that are open on the specified WDF device.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfpoolusage" data-raw-source="[&lt;strong&gt;!wdfkd.wdfpoolusage&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfpoolusage.md)"><strong>!wdfkd.wdfpoolusage</strong></a></p></td>
<td align="left"><p>Displays a driver's memory pool usage.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfqueue" data-raw-source="[&lt;strong&gt;!wdfkd.wdfqueue&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfqueue.md)"><strong>!wdfkd.wdfqueue</strong></a></p></td>
<td align="left"><p>Displays information about a WDFQUEUE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfrequest" data-raw-source="[&lt;strong&gt;!wdfkd.wdfrequest&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfrequest.md)"><strong>!wdfkd.wdfrequest</strong></a></p></td>
<td align="left"><p>Displays information about a WDFREQUEST-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfsearchpath" data-raw-source="[&lt;strong&gt;!wdfkd.wdfsearchpath&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfsearchpath.md)"><strong>!wdfkd.wdfsearchpath</strong></a></p></td>
<td align="left"><p>Sets the search path for locating the framework log's format files.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfsettraceprefix" data-raw-source="[&lt;strong&gt;!wdfkd.wdfsettraceprefix&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfsettraceprefix.md)"><strong>!wdfkd.wdfsettraceprefix</strong></a></p></td>
<td align="left"><p>Sets a prefix string for tracing messages in the framework's event log.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfsetdriver" data-raw-source="[&lt;strong&gt;!wdfkd.wdfsetdriver&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfsetdriver.md)"><strong>!wdfkd.wdfsetdriver</strong></a></p></td>
<td align="left"><p>Sets a driver name that is used as a default name for other commands that require a driver name.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfspinlock" data-raw-source="[&lt;strong&gt;!wdfkd.wdfspinlock&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfspinlock.md)"><strong>!wdfkd.wdfspinlock</strong></a></p></td>
<td align="left"><p>Displays information about a framework spin-lock object. This information includes the spin lock's acquisition history and the length of time that the lock was held.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdftagtracker" data-raw-source="[&lt;strong&gt;!wdfkd.wdftagtracker&lt;/strong&gt;](../debuggercmds/-wdfkd-wdftagtracker.md)"><strong>!wdfkd.wdftagtracker</strong></a></p></td>
<td align="left"><p>Displays tag information (including the tag value, line, file, and time) for a specified object tag.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdftmffile" data-raw-source="[&lt;strong&gt;!wdfkd.wdftmffile&lt;/strong&gt;](../debuggercmds/-wdfkd-wdftmffile.md)"><strong>!wdfkd.wdftmffile</strong></a></p></td>
<td align="left"><p>Specifies the trace message format (.<em>tmf</em>) files that the <strong>!wdflogdump</strong> extension will use to display event log records.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdftraceprtdebug" data-raw-source="[&lt;strong&gt;!wdfkd.wdftraceprtdebug&lt;/strong&gt;](../debuggercmds/-wdfkd-wdftraceprtdebug.md)"><strong>!wdfkd.wdftraceprtdebug</strong></a></p></td>
<td align="left"><p>Turns on the TracePrt diagnostic mode.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfumdevstack" data-raw-source="[&lt;strong&gt;!wdfkd.wdfumdevstack&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfumdevstack.md)"><strong>!wdfkd.wdfumdevstack</strong></a></p></td>
<td align="left"><p>Displays detailed information about a UMDF device stack in the implicit process.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfumdevstacks" data-raw-source="[&lt;strong&gt;!wdfkd.wdfumdevstacks&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfumdevstacks.md)"><strong>!wdfkd.wdfumdevstacks</strong></a></p></td>
<td align="left"><p>Displays information about all UMDF device stacks in the implicit process.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfumdownirp" data-raw-source="[&lt;strong&gt;!wdfkd.wdfumdownirp&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfumdownirp.md)"><strong>!wdfkd.wdfumdownirp</strong></a></p></td>
<td align="left"><p>Displays the kernel-mode I/O request packet (IRP) that is associated with a specified user-mode IRP.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfumfile" data-raw-source="[&lt;strong&gt;!wdfkd.wdfumfile&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfumfile.md)"><strong>!wdfkd.wdfumfile</strong></a></p></td>
<td align="left"><p>Displays information about a UMDF intra-stack file.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfumirp" data-raw-source="[&lt;strong&gt;!wdfkd.wdfumirp&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfumirp.md)"><strong>!wdfkd.wdfumirp</strong></a></p></td>
<td align="left"><p>Displays information about a user-mode I/O request packet (UM IRP).</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfumirps" data-raw-source="[&lt;strong&gt;!wdfkd.wdfumirps&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfumirps.md)"><strong>!wdfkd.wdfumirps</strong></a></p></td>
<td align="left"><p>Displays the list of pending user-mode I/O request packets (UM IRPs) in the implicit process.</p></td>
<td align="left"><p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfusbdevice" data-raw-source="[&lt;strong&gt;!wdfkd.wdfusbdevice&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfusbdevice.md)"><strong>!wdfkd.wdfusbdevice</strong></a></p></td>
<td align="left"><p>Displays information about a WDFUSBDEVICE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfusbinterface" data-raw-source="[&lt;strong&gt;!wdfkd.wdfusbinterface&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfusbinterface.md)"><strong>!wdfkd.wdfusbinterface</strong></a></p></td>
<td align="left"><p>Displays information about a WDFUSBINTERFACE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfusbpipe" data-raw-source="[&lt;strong&gt;!wdfkd.wdfusbpipe&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfusbpipe.md)"><strong>!wdfkd.wdfusbpipe</strong></a></p></td>
<td align="left"><p>Displays information about a WDFUSBPIPE-typed object handle.</p></td>
<td align="left"><p>KMDF</p>
<p>UMDF 2</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/debuggercmds/-wdfkd-wdfwmi" data-raw-source="[&lt;strong&gt;!wdfkd.wdfwmi&lt;/strong&gt;](../debuggercmds/-wdfkd-wdfwmi.md)"><strong>!wdfkd.wdfwmi</strong></a></p></td>
<td align="left"><p>Displays a device's Windows Management Instrumentation (WMI) information.</p></td>
<td align="left">KMDF</td>
</tr>
</tbody>
</table>

 

