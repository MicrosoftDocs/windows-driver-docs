---
title: Order of Resources in Start-Device IRP
author: windows-driver-content
description: Order of Resources in Start-Device IRP
MS-HAID:
- 'pcidg\_fb942a42-adf3-4b15-82f4-dc78b893e2c3.xml'
- 'PCI.order\_of\_resources\_in\_start\_device\_irp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: df55105e-3da3-40cc-9f57-05632cb2d043
keywords: ["order of resources WDK PCI", "start-device IRP WDK PCI"]
---

# Order of Resources in Start-Device IRP


The order of the resources that are reported in the start-device I/O request packet (IRP) should match the order of the resources that are listed in the PCI base address registers (BARs). There are two types of resource lists, raw and translated. Each resource list has resource descriptors. The resource descriptors in the resource lists are in the order of base address registers (BARs) on PCI devices. The order of resources in the raw and translated lists is the same. There is device-private descriptor data between two consecutive resource descriptors. The resource descriptors for BARs are followed by one or more descriptors for extended message-signaled interrupt (MSI-X) messages, or one descriptor for MSI, or one or more descriptors for hardware-based interrupts. In some cases, such as with video devices, for example, the descriptors for BARs are followed by descriptors for legacy video resources. The ordering of descriptors for BARs in a resource list is guaranteed to match the BARs on a PCI device on all hardware platforms.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpci\buses%5D:%20Order%20of%20Resources%20in%20Start-Device%20IRP%20%20RELEASE:%20%285/19/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


