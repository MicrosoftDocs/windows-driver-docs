---
title: Getting Started with UMDF
description: This section describes User-Mode Driver Framework (UMDF) and details the differences between UMDF versions 1 and 2.
ms.assetid: 2C4DAFA4-783C-4739-8D27-A417AC63B447
---

# Getting Started with UMDF


This section describes User-Mode Driver Framework (UMDF) and details the differences between UMDF versions 1 and 2. It also provides high-level architectural information about UMDF. Use this section to determine if a UMDF driver is the right choice for your needs, and to decide which UMDF version to use.

Windows Driver Frameworks (WDF) contains UMDF, a framework for the creation of user-mode drivers. Like Kernel-Mode Driver Framework (KMDF), UMDF provides an abstraction layer from WDM, handling much of the Plug and Play (PnP) and power management functionality, and allowing the driver to opt in for specific functionality and event handling.

As of Windows 8.1, there are two major versions of UMDF, versions 1 and 2. UMDF version 1.11 (one dot eleven) is the most recent version of UMDF version 1, and is the final version before the advent of UMDF 2.0. For a table showing full version info and operating system relevance, see [UMDF Version History](umdf-version-history.md).

Writing a driver using UMDF version 1.x requires using the COM programming model to write C++ code. While UMDF version 1 is based on the same conceptual driver programming model as KMDF, UMDF 1 implements the model with different components, device driver interfaces (DDIs), and data structures.

In contrast, starting in UMDF version 2, you can write a UMDF driver in the C programming language that calls many of the methods that are available to KMDF drivers. All of the interfaces that are shared between UMDF version 2 and KMDF have the same names, parameters, and structure definitions. If your driver uses only shared functionality, or uses conditional macros around calls that are only supported in one framework, you can write a single driver that you can compile with either UMDF or KMDF. For more information, see [How to generate a UMDF driver from a KMDF driver](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).

While there is significant commonality between UMDF version 2.0 and KMDF, there is still a small amount of functionality that is available only in one framework or the other. For specifics, see [Comparing UMDF 2.0 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md). For a list of all UMDF 2 and KMDF callbacks and methods and which framework(s) they apply to, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591). In a few cases, a structure member or parameter of a method applies only to one framework or the other. The documentation describes these differences on the corresponding reference pages.

You must choose one or the other; you cannot write a UMDF driver that calls methods from both UMDF versions 1 and 2.

UMDF version 2 drivers run only starting with Windows 8.1. If you need to write a UMDF driver that runs on operating systems earlier than Windows 8.1, you need to write a UMDF 1.x driver. You can use version 1.11 to build drivers that run on Windows Vista and later. For more info on version 1, see [UMDF 1.x Design Guide](user-mode-driver-framework-design-guide.md). This section describes UMDF version 2.

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
<td align="left"><p>[User-Mode Driver Framework Frequently Asked Questions](user-mode-driver-framework-frequently-asked-questions.md)</p></td>
<td align="left"><p>WDF is a set of libraries that you can use to write device drivers that run on the Windows operating system. WDF defines a single driver model that is supported by two frameworks: KMDF and UMDF. This topic provides answers to frequently asked questions about UMDF.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Advantages of Writing UMDF Drivers](advantages-of-writing-umdf-drivers.md)</p></td>
<td align="left"><p>This topic describes the advantages of writing a UMDF driver instead of a kernel-mode driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Overview of UMDF](overview-of-the-umdf.md)</p></td>
<td align="left"><p>This topic provides a high-level overview of UMDF components and describes how your driver interacts with system-supplied components. It applies to both UMDF versions 1 and 2.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[UMDF Driver Host Process](umdf-driver-host-process.md)</p></td>
<td align="left"><p>This topic describes the UMDF driver host process and how it works with other UMDF components. It applies to both UMDF versions 1 and 2.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Architecture of UMDF](detailed-view-of-the-umdf-architecture.md)</p></td>
<td align="left"><p>This topic describes how the driver manager builds a user-mode device stack, and how the host process, reflector, and driver manager process an I/O request that an application sends to a UMDF driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Comparing UMDF 2.0 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md)</p></td>
<td align="left"><p>This topic compares the functionality available to a KMDF driver with that available to a UMDF 2.0 driver. It is designed to help you decide whether you should write a UMDF 2.0 driver or a KMDF driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[How to convert a KMDF driver to a UMDF 2.0 driver (and vice-versa)](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md)</p></td>
<td align="left"><p>This topic describes how to convert a KMDF driver into a UMDF version 2.0 driver, and vice-versa.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Porting a Driver from UMDF 1 to UMDF 2](porting-a-driver-from-umdf-1-to-umdf-2.md)</p></td>
<td align="left"><p>This topic describes how to port a UMDF 1 driver to UMDF 2. You can start with a UMDF 1 driver that uses Sources/Dirs files (not a Visual Studio project), or you can convert a UMDF 1 driver that is contained in a Visual Studio project. The result will be a UMDF 2 driver project in Visual Studio. UMDF 2 drivers run on both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Getting%20Started%20with%20UMDF%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




