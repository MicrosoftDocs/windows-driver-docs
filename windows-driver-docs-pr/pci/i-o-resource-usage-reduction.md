---
title: I/O Resource Usage Reduction
author: windows-driver-content
description: I/O Resource Usage Reduction
MS-HAID:
- 'pcidg\_8154a41f-05b5-4698-9f3b-7ae86b92bcb7.xml'
- 'PCI.i\_o\_resource\_usage\_reduction'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ad83856c-ad1a-42fc-97f0-7881f745174d
keywords: ["I/O resource usage reduction WDK", "resource usage WDK", "I/O resources WDK"]
---

# I/O Resource Usage Reduction


Microsoft has implemented support to help reduce the dependence that PCI, PCI-X, and PCI Express devices have on the usage of input/output (I/O) space addresses that are accessed by the I/O base address registers (BARs). The number of I/O resources used on a personal computer has continued to increase over the years. This I/O resource usage on PCI, PCI-X, and PCI Express buses is increasingly becoming a cause of resource contention problems. These problems are expected to become worse for systems using PCI Express buses, compared to those using PCI and PCI-X buses, due to the number of virtual PCI-to-PCI bridges that are used in both client and server systems. It is therefore becoming more necessary to transition hardware designs away from reliance on I/O resources and onto using memory resources, which are much more plentiful. For more information on how device manufacturers, driver developers, firmware engineers, and system manufacturers can disable unused I/O BARs and reduce or eliminate the amount of I/O space used in a computer, refer to the [I/O Resource Usage Reduction](http://go.microsoft.com/fwlink/p/?linkid=74197) white paper.

To reduce I/O resource usage, the driver developer must place the following entry in the device driver's INF file.

```
[DDInstall.HW]
Include=machine.inf
Needs=PciIoSpaceNotRequired
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpci\buses%5D:%20I/O%20Resource%20Usage%20Reduction%20%20RELEASE:%20%285/19/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


