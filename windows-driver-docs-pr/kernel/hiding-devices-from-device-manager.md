---
title: Hiding Devices from Device Manager
author: windows-driver-content
description: Hiding Devices from Device Manager
ms.assetid: dd362ae1-ab14-44ee-982e-f972454c2623
keywords: ["Device Manager WDK , hidden devices", "devices WDK , hiding from Device Manager", "hidden devices WDK", "hiding devices WDK", "NoDisplayClass value WDK device installations"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Hiding Devices from Device Manager


By default, Device Manager shows the state of every device on a computer. In some situations, you might want to prevent certain devices from appearing in Device Manager. For example, a motherboard might have a CardBus controller with a slot that is not user-accessible. Because the user cannot use the slot, you do not want Device Manager to display any information about the device.

To hide a device in Device Manager, you can mark the device as a *hidden device*. Typically, Device Manager does not display hidden devices. (Note, however, that users can override this setting and display all devices within Device Manager, even hidden ones. For more information about how to override this setting, see [Viewing Hidden Devices](https://msdn.microsoft.com/library/windows/hardware/ff553955).)

There are two ways to mark your device as hidden: within the device's driver or by using the ACPI BIOS.

### Hiding Devices from Within a Driver

Drivers have two ways to mark a driver as hidden:

-   A function driver or function filter driver can ask the operating system to hide a successfully started device by responding to the [**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff551698) IRP. When the IRP arrives, the driver must set the PNP\_DEVICE\_DONT\_DISPLAY\_UI bit in **IoStatus.Information** to **TRUE** in the driver's dispatch routine.

-   On Windows XP and later versions of the Windows operating systems, a bus driver or bus filter driver can hide any device, started or otherwise, by responding to the [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) IRP. When the IRP arrives, the driver must set the **Parameters.DeviceCapabilities.NoDisplayInUI** member to **TRUE** in the driver's dispatch routine. In some cases, a bus filter driver might have to set this bit in a completion routine. This extra step is required when the underlying bus driver's dispatch routine incorrectly clears all capability fields that other drivers set.

### Hiding Devices By Using the ACPI BIOS

You can mark a device as hidden in the ACPI BIOS. The BIOS can expose a \_STA method for the device. The \_STA method returns a bitmask. Bit 2 (mask 0x4) specifies whether Device Manager should make the device visible by default. This bit should be 1 if the device should be made visible and 0 otherwise.

For example, the following code example shows how a USB controller on the root bus would be hidden.

```
Device(PCI0) // Root PCI bus
_HID *PNP0A03 
...
    Device(UCTL)  // USB controller
    _ADR 0xddddffff // dddd = device, ffff = function
    _STA 0xB // Device present, but not shown
```

In Microsoft Windows 2000, you can hide only started, working devices. In Windows XP and later versions of Windows, you can also hide broken devices. Bit 3 (mask 0x8) that is returned by the \_STA method indicates whether a device is working properly. This bit is 1 if the device is working properly and is 0 otherwise. For example, the following code example shows how a BIOS would indicate a USB controller is broken and should be hidden:

```
Device(PCI0) // Root PCI bus 
_HID *PNP0A03 
...
    Device(UCTL) // USB controller
    _ADR 0xddddffff //  dddd = device, ffff = function
    _STA 0x3 // Present, but broken and not shown 
```

**Note**   The "decoding" bit (0x2) does not have any relevance for devices that are described through \_ADR methods. The previous code examples also work without the decoding bit set. BIOS writers must track the decoding state only for devices that are described through \_HID methods.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Hiding%20Devices%20from%20Device%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


