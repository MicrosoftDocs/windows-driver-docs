---
title: Virtual Subunit Driver Stack
author: windows-driver-content
description: Virtual Subunit Driver Stack
ms.assetid: 5aa1804f-b871-4577-8e8a-ce4ad5150ee0
keywords:
- virtual subunit driver stack WDK AV/C
- driver stacks WDK AV/C
- stacks WDK AV/C
- subunit support WDK AV/C
- AV/C WDK , driver stacks
- Avc.sys function driver WDK , driver stacks
- compatible IDs WDK AV/C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Virtual Subunit Driver Stack


The IEEE 1394 driver stack can be configured to expose system hardware to other AV/C subunits on the IEEE 1394 bus through the IEEE 1394, IEC 61883, and Audio/Video Control (AV/C) protocol drivers. This configuration is known as virtual IEEE 1394 device support. *Avc.sys* uses this capability to enable the computer to become a virtual IEEE 1394 device to other physical AV/C units on the IEEE 1394 bus.

The *Avc.sys* virtual driver stack consists of the subunit drivers that are loaded to represent capabilities and resources of the computer as a virtual AV/C unit on the IEEE 1394 bus. The virtual subunit stack is where *Avc.sys* implements the AV/C specification through software in the computer. A virtual AV/C driver stack is instantiated if any of the computer's resources will be exposed as an AV/C subunit.

Windows loads *Avc.sys* to provide virtual AV/C subunit support based on registry settings that are specified in an INF file or through application control by using I/O controls (IOCTLs). Each instance of *Avc.sys* that is loaded to support a virtual subunit registers a new instance of the GUID\_VIRTUAL\_AVC\_CLASS device interface. For more information about the GUID\_VIRTUAL\_AVC\_CLASS device interface, see [Using Avc.sys](using-avc-sys.md) and [**IOCTL\_AVC\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560789).

The registry is the persistent way to save AV/C (and more generally IEEE 1394) virtual device configuration, but virtual device configuration must not be manually entered into the registry. Instead, the configuration must be set up by using an INF file or through a combination of IOCTLs. For more information about virtual device configuration see [AV/C Device IDs](av-c-device-identifiers.md) and [Virtual Subunit Device IDs](virtual-subunit-device-identifiers.md).

The virtual IEEE 1394 device provides the following support:

-   Ability to implement in software hardware that does not yet exist. This feature permits new hardware to be prototyped and new subunit drivers to be developed before physical hardware is available to test.

-   Ability to develop automated test suites for peer subunit drivers without requiring the presence of actual hardware. This feature permits testing of boundary error conditions that is not otherwise possible with the range of hardware devices available, and it reduces the need for expensive hardware to test against.

-   Ability to implement extensions to AV/C subunit target functionality, such as Authentication and Key Exchange (AKE) and the Connection and Compatibility Management (CCM) protocol by third parties on the computer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Virtual%20Subunit%20Driver%20Stack%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


