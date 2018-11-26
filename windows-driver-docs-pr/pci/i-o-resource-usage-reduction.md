---
title: I/O Resource Usage Reduction
description: I/O Resource Usage Reduction
ms.assetid: ad83856c-ad1a-42fc-97f0-7881f745174d
keywords:
- I/O resource usage reduction WDK
- resource usage WDK
- I/O resources WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# I/O Resource Usage Reduction


Microsoft has implemented support to help reduce the dependence that PCI, PCI-X, and PCI Express devices have on the usage of input/output (I/O) space addresses that are accessed by the I/O base address registers (BARs). The number of I/O resources used on a personal computer has continued to increase over the years. This I/O resource usage on PCI, PCI-X, and PCI Express buses is increasingly becoming a cause of resource contention problems. These problems are expected to become worse for systems using PCI Express buses, compared to those using PCI and PCI-X buses, due to the number of virtual PCI-to-PCI bridges that are used in both client and server systems. It is therefore becoming more necessary to transition hardware designs away from reliance on I/O resources and onto using memory resources, which are much more plentiful. For more information on how device manufacturers, driver developers, firmware engineers, and system manufacturers can disable unused I/O BARs and reduce or eliminate the amount of I/O space used in a computer, refer to the [I/O Resource Usage Reduction](http://go.microsoft.com/fwlink/p/?linkid=74197) white paper.

To reduce I/O resource usage in Windows 10, place the following entry in the device driver's INF file:

```cpp
[DDInstall.HW]
Include=pci.inf
Needs=PciIoSpaceNotRequired.HW
```

In Windows 8.1 and earlier, use this entry instead:

```cpp
[DDInstall.HW]
Include=machine.inf
Needs=PciIoSpaceNotRequired
```
