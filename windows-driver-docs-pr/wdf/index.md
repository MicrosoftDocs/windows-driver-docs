---
title: WDF Driver Development Guide
description: This section describes Windows Driver Frameworks (WDF) driver development concepts, including power management, I/O requests, and interrupt handling.
ms.assetid: 46009B18-7EDD-4E58-B561-36775A335B87
---

# WDF Driver Development Guide


This section describes Windows Driver Frameworks (WDF) driver development concepts, including power management, I/O requests, and interrupt handling.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[What's New for WDF Drivers](what-s-new-for-wdf-drivers.md)</p></td>
<td align="left"><p>This topic summarizes the new features and improvements for WDF drivers in Windows 10.</p>
<p>Windows 10 includes Kernel-Mode Driver Framework (KMDF) version 1.15 and User-Mode Driver Framework (UMDF) version 2.15.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[WDF Architecture](kernel-mode-driver-framework-architecture.md)</p></td>
<td align="left"><p>This topic describes the object-based interfaces that WDF provides for drivers. </p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Getting Started with UMDF](getting-started-with-umdf-version-2.md)</p></td>
<td align="left"><p>This section describes UMDF and details the differences between UMDF versions 1 and 2. It also provides high-level architectural information about UMDF. Use this section to determine if a UMDF driver is the right choice for your needs, and to decide which UMDF version to use.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Writing a Simple WDF Driver](writing-a-simple-kmdf-driver.md)</p></td>
<td align="left"><p>This topic describes the minimal functionality you need to write a KMDF driver. You need the same minimal functionality to write a UMDF driver starting in UMDF version 2.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Using WDF to Develop a Driver](using-the-framework-to-develop-a-driver.md)</p></td>
<td align="left"><p>This topic provides a high-level overview of the framework objects you'll use to develop a KMDF driver. Except where indicated, you'll use the same objects to develop a UMDF driver starting in UMDF version 2.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Framework Library Versioning](framework-library-versioning.md)</p></td>
<td align="left"><p>In this topic, you'll learn about the naming conventions for the file names of the KMDF library and the UMDF library.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[KMDF Version History](kmdf-version-history.md)</p></td>
<td align="left"><p>This topic lists versions of KMDF, the corresponding versions of the Windows operating system, and the changes made in each release.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[UMDF Version History](umdf-version-history.md)</p></td>
<td align="left"><p>This topic lists versions of UMDF, the corresponding versions of the Windows operating system, and the changes made in each release.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Sample KMDF Drivers](sample-kmdf-drivers.md)</p></td>
<td align="left"><p>This topic lists the KMDF sample drivers that you can download from the [Windows Dev Center - Hardware](http://go.microsoft.com/fwlink/p/?linkid=256387).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Sample UMDF Drivers](sample-umdf-drivers.md)</p></td>
<td align="left"><p>This topic lists available UMDF sample drivers that you can download from the [Windows driver samples repository](http://go.microsoft.com/fwlink/p/?LinkId=616507) on GitHub.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Sample Toaster Driver Programming Tour](sample-toaster-driver-programming-tour.md)</p></td>
<td align="left"><p>This topic provides a code walkthrough of the [Toaster](http://go.microsoft.com/fwlink/p/?LinkId=618939) sample, which contains KMDF and UMDF drivers designed for learning purposes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Developing Drivers with the Windows Driver Foundation: Reference Book](developing-drivers-with-wdf.md)</p></td>
<td align="left"><p>The <em>Developing Drivers with Windows Driver Foundation</em> book is also available to help you learn the concepts and fundamentals of WDF. This book introduces Windows drivers and basic kernel-mode programming, and then describes the WDF architecture and programming model. It provides a practical, sample-oriented guide to using the frameworks to develop Windows drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[WDF Objects](wdf-objects.md)</p></td>
<td align="left"><p>This section describes common characteristics of framework objects and how a WDF driver uses object-based interfaces to call methods, register callback routines, set and retrieve property data, and manage object reference counts.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[PnP and Power Management](pnp-and-power-management.md)</p></td>
<td align="left"><p>The topics in this section describe the default PnP and power management support that the framework provides.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Handling I/O Requests](handling-i-o-requests-in-wdf-drivers.md)</p></td>
<td align="left"><p>This section describes how a WDF driver can use I/O queues to manage the I/O requests that the driver receives.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Using I/O Targets](using-i-o-targets.md)</p></td>
<td align="left"><p>The topics in this section describe how a WDF driver can forward an I/O request or create and send a new request to another driver, called an I/O target.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Synchronization Techniques](synchronization-techniques-for-wdf-drivers.md)</p></td>
<td align="left"><p>This section describes how a WDF driver can customize the framework's built-in callback synchronization, or use manual locks to control when the framework calls the driver's callback routines.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[WDF Support Objects](wdf-support-objects.md)</p></td>
<td align="left"><p>The topics in this section describe how a WDF driver uses memory buffers, timers, string objects, work items, and other support functionality that the framework provides.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Handling Hardware Interrupts](handling-hardware-interrupts.md)</p></td>
<td align="left"><p>The topics in this section describe how a WDF driver creates framework interrupt objects to service hardware interrupts, and how your driver synchronizes access to interrupt data buffers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Handling DMA Operations in KMDF Drivers](handling-dma-operations-in-kmdf-drivers.md)</p></td>
<td align="left"><p>This section describes how a KMDF driver converts I/O requests into direct memory access (DMA) operations. KMDF supports bus-master and system-mode DMA.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Supporting WMI in KMDF Drivers](supporting-wmi-in-kmdf-drivers.md)</p></td>
<td align="left"><p>The topics in this section describe how a KMDF driver registers as a WMI data provider, responds to requests for instance data, and sends events to registered WMI clients.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Accessing WDM Interfaces in KMDF Drivers](accessing-wdm-interfaces-in-kmdf-drivers.md)</p></td>
<td align="left"><p>Most KMDF drivers do not need to access Windows Driver Model (WDM) interfaces directly. This section describes the limited cases when a KMDF driver requires direct access to WDM data structures, for example to obtain WDM information or manipulate an IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Handling Hardware Resources](hardware-resources-for-kmdf-drivers.md)</p></td>
<td align="left"><p>A system's hardware resources are the I/O ports, interrupt vectors, DMA channels, and other communication paths that must be assigned to each device that is connected to the system. The topics in this section describe how KMDF drivers negotiate hardware resource requirements for a device, review the proposed resource list, and then receive the assigned resources. This section also discusses how both KMDF and UMDF drivers access and map assigned resources.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Building, Installing, and Testing](building--installing--and-testing-a-wdf-driver.md)</p></td>
<td align="left"><p>This section describes how you build a WDF driver in Microsoft Visual Studio, whether you need to provide a co-installer, and how you test your driver using the WDF Verifier and built-in event logging.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Debugging WDF Drivers](debugging-a-wdf-driver.md)</p></td>
<td align="left"><p>The topics in this section describe techniques and tools that you can use to debug a KMDF or UMDF driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Porting a Driver from WDM to WDF](wdf-porting-guide.md)</p></td>
<td align="left"><p>The topics in this section describe how to convert an existing WDM driver to a KMDF driver or a UMDF version 2 driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Additional Topics for KMDF Drivers](kmdf-only-functionality.md)</p></td>
<td align="left"><p>This section contains information that applies only to KMDF.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[UMDF 1.x Design Guide](user-mode-driver-framework-design-guide.md)</p></td>
<td align="left"><p>This section contains information that applies only to UMDF versions 1.11 and earlier.</p></td>
</tr>
</tbody>
</table>







[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF%20Driver%20Development%20Guide%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




