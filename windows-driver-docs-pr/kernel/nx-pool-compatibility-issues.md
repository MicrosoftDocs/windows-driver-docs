---
title: NX Pool Compatibility Issues
description: When you use the NX nonpaged pool in driver binaries for Windows 8, you will find compatibility issues if you run these binaries on earlier versions of Windows.
ms.assetid: 652AE9A2-D733-4EC2-9D49-B95DDABE42B1
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# NX Pool Compatibility Issues


When you use the NX nonpaged pool in driver binaries for Windows 8, you will find compatibility issues if you run these binaries on earlier versions of Windows.

Windows 8 is the first version of Windows to support the NX nonpaged pool. However, a large number of existing kernel-mode driver binaries are available for Windows 7 and earlier versions of Windows that run on the x86, x64, and IA64 processor architectures. To allocate nonpaged memory, these drivers use the executable nonpaged pool instead the NX nonpaged pool. For backward compatibility, kernel-mode driver binaries that run on Windows 7, and on some earlier versions of Windows, and that allocate memory from the nonpaged pool, will run on Windows 8 without modification. However, these drivers do not take advantage of the availability of NX nonpaged pool in Windows 8.

## Running Existing Driver Binaries on Windows 8


A driver binary that is built for Windows 7 (or possibly for an earlier version of Windows), and that uses the **NonPagedPool** pool type, is not prevented from running on Windows 8. To enable backward compatibility, the **NonPagedPoolExecute** constant is defined to have the same value as the **NonPagedPool** constant in the [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707) enumeration. Thus, in any version of Windows in which this driver runs, the memory that the driver allocates from nonpaged pool is always executable.

Windows 8 is the first version of Windows to support the ARM architecture. Thus, there are no driver binaries for ARM that are built for earlier versions of Windows and that require backward compatibility. Instead, all drivers written for Windows on ARM are expected to specify **NonPagedPoolNx** instead of **NonPagedPoolExecute** in their nonpaged pool allocations unless they explicitly require executable memory.

If a driver is ported to ARM from x86, x64, or IA64, the [POOL\_NX\_OPTIN\_AUTO](multiple-binary-opt-in-pool-nx-optin-auto.md) opt-in mechanism is automatically applied during the driver build process. This opt-in mechanism uses the preprocessor to replace, by default, all instances of the **NonPagedPool** constant name with **NonPagedPoolNx**. If necessary, you can use the [POOL\_NX\_OPTOUT](selective-opt-out-pool-nx-optout.md) opt-out mechanism to overrride this opt-in mechanism on a per-file basis.

## Other Compatibility Issues


The **NonPagedPoolNx** pool type is supported starting with Windows 8. Do not use this pool type in drivers for earlier versions of Windows. The pool allocators in these earlier versions of Windows do not operate correctly when the driver requests an allocation with a **NonPagedPoolNx** pool type.

In versions of Windows before Windows 8, the **NonPagedPoolExecute** pool type can be freely used as a substitute for the **NonPagedPool** pool type. The [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707) enumeration defines **NonPagedPool** and **NonPagedPoolExecute** to have the same value.

## NX Pool Type Porting Guidelines


When you port your driver code to Windows 8 or later from an earlier version of Windows, there are several ways to add support for the **NonPagedPoolNx** and **NonPagedPoolExecute** pool types. From the following list, choose the approach that best fits your requirements:

-   If your driver is not intended to run on a version of Windows earlier than Windows 8, replace most or all instances of **NonPagedPool** with **NonPagedPoolNx**. Only rarely should the developer replace an instance of **NonPagedPool** with **NonPagedPoolExecute.**

-   If your driver source code targets both Windows 8 and earlier versions of Windows, and you ship a different driver binary for each version, use the POOL\_NX\_OPTIN\_AUTO opt-in mechanism. This approach does not require replacing the instances of **NonPagedPool** in the driver source. For more information, see [NX Pool Opt-In Mechanisms](nx-pool-opt-in-mechanisms.md).

-   If your driver source code targets both Windows 8 and earlier versions of Windows, and you ship a single driver binary to run on all supported versions, use the POOL\_NX\_OPTIN opt-in mechanism. This approach does not require replacing the instances of **NonPagedPool** in the driver source. For more information, see [NX Pool Opt-In Mechanisms](nx-pool-opt-in-mechanisms.md).

By using one of these three approaches, most drivers can be ported quickly and with little effort.

Avoid simply replacing all instances of **NonPagedPool** in your driver code with **NonPagedPoolExecute**. Use the **NonPagedPoolExecute** pool type only for pool allocations that must be executable (for example, to run code produced by a just-in-time, or JIT, compiler).

 

 




