---
title: Configuring Special Pool
description: Configuring Special Pool
ms.assetid: a6c90e88-8d67-47e8-8862-b7585a5d8bec
keywords: ["GFlags, configuring kernel special pool", "kernel special pool", "special pool", "pool tags and special pool"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuring Special Pool


## <span id="ddk_configuring_kernel_special_pool_dtools"></span><span id="DDK_CONFIGURING_KERNEL_SPECIAL_POOL_DTOOLS"></span>


The Gflags *Special Pool* feature directs Windows to request memory allocations from a reserved memory pool when the memory is allocated with a specified pool tag or is within a specified size range.

For detailed information about this feature, see [Special Pool](special-pool.md).

In Windows Vista and later versions of Windows, you can configure the Special Pool feature as a system-wide registry setting or as a kernel flags setting that does not require a reboot. In earlier versions of Windows, Special Pool is available only as a registry setting.

In Windows Vista and later versions of Windows, you can also use the command line to request special pool by pool tag. For information, see [**GFlags Commands**](gflags-commands.md).

This section includes the following topics.

[Requesting Special Pool by Pool Tag](requesting-special-pool-by-pool-tag.md)

[Requesting Special Pool by Allocation Size](requesting-special-pool-by-allocation-size.md)

[Canceling Requests for Special Pool](canceling-requests-for-special-pool.md)

[Detecting Overruns and Underruns](detecting-overruns-and-underruns.md)

**Note**   Use *Driver Verifier* to request special pool for allocations by a particular driver. For more information, see the "Special Pool" topic in the "Driver Verifier" section of the Windows Driver Kit (WDK).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Configuring%20Special%20Pool%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




