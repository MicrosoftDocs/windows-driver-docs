---
title: Sharing a Serial Device Interrupt
author: windows-driver-content
description: Sharing a Serial Device Interrupt
ms.assetid: 1d35fbc0-7031-42f3-bb22-52d2bcdcfa92
keywords: ["COM ports WDK serial devices", "serial devices WDK , COM ports", "legacy COM ports WDK serial devices", "sharing serial device interrupts", "serial devices WDK , interrupts", "interrupts WDK serial devices", "shared interrupts WDK serial devices", "Serial driver WDK , interrupts"]
---

# Sharing a Serial Device Interrupt


## <a href="" id="ddk-sharing-a-serial-device-interrupt-kg"></a>


Legacy COM ports on the same multiport board share a single interrupt. COM ports on a multiport board are identified by an index or a mask that associates a port with its corresponding device object.

Stand-alone serial devices can also share interrupts. However, a shared interrupt can only be used by one device at a time. When a device is opened, Serial allocates the interrupt to the device. When a device is closed, the driver releases the interrupt for use by another device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Sharing%20a%20Serial%20Device%20Interrupt%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


