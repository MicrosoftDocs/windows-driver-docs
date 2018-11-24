---
title: Checked and Free Build Differences
description: There are two distinct builds of the NT-based operating systems that are available free (retail) and checked (debug). There is a third option, called a partial checked build, that combines the elements of the two.
ms.assetid: 43aebfdb-2605-485c-a3a4-93e03b33aeca
keywords:
- checked builds WDK , vs. free builds
- free builds WDK
- retail builds WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checked and Free Build Differences


There are two distinct builds of the NT-based operating systems that are available: free (retail) and checked (debug). There is a third option, *called a partial checked build*, that combines the elements of the two.

- [Differences between the checked and free builds](#differences-between-the-checked-and-free-builds)
- [Where to find a checked build of Windows](#where-to-find-a-checked-build-of-windows)
- [When to use the checked build or partial checked build](#when-to-use-the-checked-build-or-partial-checked-build)

## Differences between the checked and free builds


This section lists some of the differences between the build choices.

**The free build (or retail build)**  
The free build of Microsoft Windows is used in production environments. The free build of the operating system is built with full compiler optimizations. When the free build discovers correctable problems, it continues to run.

The distribution media that contain the free build of the operating system do not have any special labels--in other words, the CD or download that contains the free build is labeled with the Windows version name, without any reference to the type of build.

**The checked build (or debug build)**  
The checked build of Microsoft Windows makes identifying and diagnosing operating-system-level problems easier.

The checked build differs from the free build in the following ways:

- Many compiler optimizations (such as stack frame elimination) are disabled in the checked build. This makes it easier to understand disassembled machine instructions, and therefore it is easier to trace the cause of problems in system software.

- The checked build enables a large number of debugging checks in the operating system code and system-provided drivers. This helps the checked build to identify internal inconsistencies and problems as soon as they occur.

**A partial checked build (or partial debug build)**  
A partial checked build of Microsoft Windows is similar to the full checked build. The principal difference is that the partial checked build includes only the checked operating system image (the kernel) and the checked hardware abstraction layer (HAL). The rest of the Windows components come from the free (retail) build of Windows.

The partial checked build differs from the free and full checked builds in the following ways:

-   As in the full checked build, many compiler optimizations (such as stack frame elimination) are disabled. This makes it easier to understand disassembled machine instructions, and therefore it is easier to trace the cause of problems.

-   The partial checked build enables a number of debugging checks in the operating system code and HAL. However, the system-provided drivers come from the free (retail) build, so unless you explicitly install the checked versions of system-provided drivers, you do not get the additional benefits of the full checked build to identify and debug problems.

-   The partial checked build requires that you first install the complete free (retail) build of Windows. Using boot options, you can configure the computer to load either the checked or free components at boot time. You can then use a single computer for testing a driver with both checked and free builds of Windows.

## Where to find a checked build of Windows


The downloads and distribution media that contain the checked build are clearly labeled as "Debug/Checked Build." The checked build downloads contain the checked version of the operating system, plus the checked versions of HALs, drivers, file systems, and even many user-mode components. For information about obtaining the checked and partial checked builds, see [Installing the Checked Build](installing-the-checked-build.md). For convenience, the checked versions of the kernel and HAL are provided in the /debug directory of the Windows Driver Kit (starting with WDK for Windows Vista).

## When to use the checked build or partial checked build


You should always use the checked build at some point in during development when you need to test your driver. The checked build can expose problems in how the driver interacts with the operating system. No testing can be considered complete without testing that your driver is able to run in the checked build without issues.

Because the checked build contains fewer optimizations and more debugging checks than the free build, the checked build is both larger in size and slower to run than the free build. As a result, the free build is used in production environments unless it is necessary to use the checked build to identify serious problems.

As an alternative to a full checked build, you can configure a computer to use a partial checked build. This gives you the advantage of the checked build for debugging, and the better performance of the free build. For information about configuring your computer for a partial checked build, see [Installing Just the Checked Operating System and HAL (For Windows Vista and Later)](installing-just-the-checked-operating-system-and-hal--for-windows-vist.md).

For more complete testing of your driver when you are using a partial checked build, you also consider installing the checked versions of the related system-provided drivers. For example, if you are developing a lower disk filter driver, you should consider extracting and installing the checked build of Disk.sys and Storport.sys from the full checked build.

 

 





