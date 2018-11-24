---
title: Getting Started with UMDF
description: This section describes User-Mode Driver Framework (UMDF) and details the differences between UMDF versions 1 and 2.
ms.assetid: 2C4DAFA4-783C-4739-8D27-A417AC63B447
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting Started with UMDF


This section describes User-Mode Driver Framework (UMDF) and details the differences between UMDF versions 1 and 2. It also provides high-level architectural information about UMDF. Use this section to determine if a UMDF driver is the right choice for your needs, and to decide which UMDF version to use.

Windows Driver Frameworks (WDF) contains UMDF, a framework for the creation of user-mode drivers. Like Kernel-Mode Driver Framework (KMDF), UMDF provides an abstraction layer from WDM, handling much of the Plug and Play (PnP) and power management functionality, and allowing the driver to opt in for specific functionality and event handling.

In Windows 8.1 onward, there are two major versions of UMDF, versions 1 and 2. UMDF version 1.11 (one dot eleven) is the most recent version of UMDF version 1, and is the final version before the advent of UMDF 2. For a table showing full version info and operating system relevance, see [UMDF Version History](umdf-version-history.md).

Writing a driver using UMDF version 1 requires using the COM programming model to write C++ code. While UMDF version 1 is based on the same conceptual driver programming model as KMDF, UMDF 1 implements the model with different components, device driver interfaces (DDIs), and data structures.

In contrast, starting in UMDF version 2, you can write a UMDF driver in the C programming language that calls many of the methods that are available to KMDF drivers. All of the interfaces that are shared between UMDF version 2 and KMDF have the same names, parameters, and structure definitions. If your driver uses only shared functionality, or uses conditional macros around calls that are only supported in one framework, you can write a single driver that you can compile with either UMDF or KMDF. For more information, see [How to generate a UMDF driver from a KMDF driver](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).

While there is significant commonality between UMDF 2 and KMDF, there is still a small amount of functionality that is available only in one framework or the other. For specifics, see [Comparing UMDF 2 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md). For a list of all UMDF 2 and KMDF callbacks and methods and which framework(s) they apply to, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591). In a few cases, a structure member or parameter of a method applies only to one framework or the other. The documentation describes these differences on the corresponding reference pages.

You must choose one or the other; you cannot write a UMDF driver that calls methods from both UMDF versions 1 and 2.

UMDF version 2 drivers run only on Windows 8.1 or later. If you need to write a UMDF driver that runs on operating systems earlier than Windows 8.1, you need to write a UMDF 1.x driver. You can use version 1.11 to build drivers that run on Windows Vista and later. For more info on version 1, see [UMDF 1.x Design Guide](user-mode-driver-framework-design-guide.md). This section describes UMDF version 2.



 

 
