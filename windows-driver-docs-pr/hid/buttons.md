---
title: HID button drivers
description: Use the Microsoft-provided button driver for GPIO buttons; otherwise, implement your driver that injects HID data to the operating system.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HID button drivers

Use the Microsoft-provided button driver for GPIO buttons; otherwise, implement your driver that injects HID data to the operating system.

Buttons (Power, Windows, volume and rotation lock) are typically used for tasks that occur while the physical keyboard is not available to the user, on form factors such as convertibles or slates. Buttons declare themselves to the operating system as HID devices by supplying [HID button report descriptors](./acpi-button-device.md). This allows the system to interpret the purpose and events of those buttons in a standardized way. When a button state changes, that event is mapped to a [HID Usages](hid-usages.md). A HID transport minidriver reports those events to upper-level drivers that then send details to HID clients in user mode or kernel mode.

For physical general-purpose I/O (GPIO) buttons, the HID transport minidriver is a Microsoft-provided in-box driver that reports the events based on the interrupts that are received on the defined GPIO hardware resources.

The in-box driver cannot service a button that is not wired to an interrupt line. For such buttons, you need to write a driver that exposes the button as a HID button and reports state changes to the HID class driver (Microsoft-provided). Your driver could be a HID source driver or a HID transport driver.

## Guidance for supporting HID buttons

Here are some general pointers to help you decide which implementation you should follow if you are creating HID buttons.

:::image type="content" source="images/button.png" alt-text="decision chart for implementing buttons." border="false":::

### Use the Microsoft-provided in-box button driver

:::image type="content" source="images/hid-acpi.png" alt-text="ACPI description of a HID button." border="false":::

If you are implementing a GPIO button, describe the button in the system ACPI so that Windows can load the in-box driver, Hidinterrupt.sys, as the button driver that reports events to the operating system.

- [ACPI button device](acpi-button-device.md)
- [Button Behavior](../gpiobtn/button-behavior.md)
- [Sample buttons ACPI for Windows 10 Core Editions](acpi-button-device.md#sample-acpi-button-device-for-windows-10-core-os-editions)

Microsoft encourages you to use the in-box transport-minidrivers whenever possible.

### Write a HID source driver in kernel mode

:::image type="content" source="images/hid-vhf.png" alt-text="Buttons using Virtual HID Framework." border="false":::

If you are implementing a non-GPIO button such as a stream of data in the HID format that needs to be injected by another software component, you can choose to write a kernel-mode driver. Starting in Windows 10, you can write a HID source driver by calling programming interfaces that communicate with Virtual HID Framework (VHF) and gets and sets HID Reports to and from the HID class driver.

- [How to write a HID source driver that interacts with Virtual HID Framework (VHF)](virtual-hid-framework--vhf-.md)
- [Virtual HID Framework Reference](/windows-hardware/drivers/ddi/_hid/)

Alternately, you can write a kernel-mode HID transport minidriver as supported by the earlier versions of Windows. However, we do not recommend this approach because poorly written KMDF HID transport minidrivers can crash the system.

- [Transport Minidrivers](transport-minidrivers.md)
- [HID Minidriver IOCTLs](/windows-hardware/drivers/ddi/_hid/#hid-class-driver-ioctls)

### Write a UMDF HID Minidriver

:::image type="content" source="images/hid-umdf.png" alt-text="HID Transport Minidriver." border="false":::

If you are implementing a non-GPIO button, instead of using preceding model of writing a HID source driver, you can write a HID transport minidriver in user mode. These drivers are easier to develop than kernel-mode drivers and errors in this driver do not bug check the whole system.

- [Creating UMDF HID Minidrivers](../wdf/creating-umdf-hid-minidrivers.md)
- [UMDF HID Minidriver IOCTLs](/previous-versions/hh463977(v=vs.85))"

## Universal Windows drivers for HID buttons

Starting with Windows 10, the HID driver programming interfaces are part of OneCoreUAP-based editions of Windows. By using that common set of interfaces, you can write a button driver by using [Virtual HID Framework](/windows-hardware/drivers/ddi/_hid) or [Transport Minidrivers](transport-minidrivers.md) interfaces. Those drivers will run on both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile, as well as other Windows 10 versions.

For step-by-step guidance, see [Getting Started with Universal Windows drivers](/windows-hardware/drivers).

## Related topics

[Human Interface Device](./index.md)