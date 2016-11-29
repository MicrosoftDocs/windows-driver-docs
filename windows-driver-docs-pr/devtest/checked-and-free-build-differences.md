---
title: Checked and Free Build Differences
description: There are two distinct builds of the NT-based operating systems that are available free (retail) and checked (debug). There is a third option, called a partial checked build, that combines the elements of the two.
ms.assetid: 43aebfdb-2605-485c-a3a4-93e03b33aeca
keywords: ["checked builds WDK , vs. free builds", "free builds WDK", "retail builds WDK"]
---

# Checked and Free Build Differences


There are two distinct builds of the NT-based operating systems that are available: free (retail) and checked (debug). There is a third option, *called a partial checked build*, that combines the elements of the two.

-   [Differences between the checked and free builds](#ddk-checked-and-free-build-differences-tools)
-   [Where to find a checked build of Windows?](#where-to-find-a-checked-build-of-windows-)
-   [When to use the checked build or partial checked build?](#when-to-use-the-checked-build-or-partial-checked-build-)

## <span id="ddk_checked_and_free_build_differences_tools"></span><span id="DDK_CHECKED_AND_FREE_BUILD_DIFFERENCES_TOOLS"></span>Differences between the checked and free builds


This section lists some of the differences between the build choices.

<span id="The__________________free_build__________________or__________________retail_build_"></span><span id="the__________________free_build__________________or__________________retail_build_"></span><span id="THE__________________FREE_BUILD__________________OR__________________RETAIL_BUILD_"></span>**The free build (or retail build)**  
The free build of Microsoft Windows is used in production environments. The free build of the operating system is built with full compiler optimizations. When the free build discovers correctable problems, it continues to run.

The distribution media that contain the free build of the operating system do not have any special labels--in other words, the CD or download that contains the free build is labeled with the Windows version name, without any reference to the type of build.

<span id="The__________________checked_build__________________or__________________debug_build_"></span><span id="the__________________checked_build__________________or__________________debug_build_"></span><span id="THE__________________CHECKED_BUILD__________________OR__________________DEBUG_BUILD_"></span>**The checked build (or debug build)**  
The checked build of Microsoft Windows makes identifying and diagnosing operating-system-level problems easier.

The checked build differs from the free build in the following ways:

-   Many compiler optimizations (such as stack frame elimination) are disabled in the checked build. This makes it easier to understand disassembled machine instructions, and therefore it is easier to trace the cause of problems in system software.

-   The checked build enables a large number of debugging checks in the operating system code and system-provided drivers. This helps the checked build to identify internal inconsistencies and problems as soon as they occur.

<span id="A__________________partial_checked_build__________________or__________________partial_debug_build_"></span><span id="a__________________partial_checked_build__________________or__________________partial_debug_build_"></span><span id="A__________________PARTIAL_CHECKED_BUILD__________________OR__________________PARTIAL_DEBUG_BUILD_"></span>**A partial checked build (or partial debug build)**  
A partial checked build of Microsoft Windows is similar to the full checked build. The principal difference is that the partial checked build includes only the checked operating system image (the kernel) and the checked hardware abstraction layer (HAL). The rest of the Windows components come from the free (retail) build of Windows.

The partial checked build differs from the free and full checked builds in the following ways:

-   As in the full checked build, many compiler optimizations (such as stack frame elimination) are disabled. This makes it easier to understand disassembled machine instructions, and therefore it is easier to trace the cause of problems.

-   The partial checked build enables a number of debugging checks in the operating system code and HAL. However, the system-provided drivers come from the free (retail) build, so unless you explicitly install the checked versions of system-provided drivers, you do not get the additional benefits of the full checked build to identify and debug problems.

-   The partial checked build requires that you first install the complete free (retail) build of Windows. Using boot options, you can configure the computer to load either the checked or free components at boot time. You can then use a single computer for testing a driver with both checked and free builds of Windows.

## <span id="Where_to_find_a_checked_build_of_Windows_"></span><span id="where_to_find_a_checked_build_of_windows_"></span><span id="WHERE_TO_FIND_A_CHECKED_BUILD_OF_WINDOWS_"></span>Where to find a checked build of Windows?


The downloads and distribution media that contain the checked build are clearly labeled as "Debug/Checked Build." The checked build downloads contain the checked version of the operating system, plus the checked versions of HALs, drivers, file systems, and even many user-mode components. For information about obtaining the checked and partial checked builds, see [Downloading a Checked Build of Windows](obtaining-the-checked-build.md). For convenience, the checked versions of the kernel and HAL are provided in the /debug directory of the Windows Driver Kit (starting with WDK for Windows Vista).

## <span id="When_to_use_the_checked_build_or_partial_checked_build_"></span><span id="when_to_use_the_checked_build_or_partial_checked_build_"></span><span id="WHEN_TO_USE_THE_CHECKED_BUILD_OR_PARTIAL_CHECKED_BUILD_"></span>When to use the checked build or partial checked build?


You should always use the checked build at some point in during development when you need to test your driver. The checked build can expose problems in how the driver interacts with the operating system. No testing can be considered complete without testing that your driver is able to run in the checked build without issues.

Because the checked build contains fewer optimizations and more debugging checks than the free build, the checked build is both larger in size and slower to run than the free build. As a result, the free build is used in production environments unless it is necessary to use the checked build to identify serious problems.

As an alternative to a full checked build, you can configure a computer to use a partial checked build. This gives you the advantage of the checked build for debugging, and the better performance of the free build. For information about configuring your computer for a partial checked build, see [Installing Just the Checked Operating System and HAL (For Windows Vista and Later)](installing-just-the-checked-operating-system-and-hal--for-windows-vist.md).

For more complete testing of your driver when you are using a partial checked build, you also consider installing the checked versions of the related system-provided drivers. For example, if you are developing a lower disk filter driver, you should consider extracting and installing the checked build of Disk.sys and Storport.sys from the full checked build.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Checked%20and%20Free%20Build%20Differences%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




