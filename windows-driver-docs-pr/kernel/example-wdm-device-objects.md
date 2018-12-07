---
title: Example WDM Device Objects
description: Example WDM Device Objects
ms.assetid: 8da56415-5018-468c-99c7-3969e5c00285
keywords: ["device objects WDK kernel , examples", "mouse WDK kernel", "keyboards WDK kernel", "functional device objects WDK kernel", "FDO WDK kernel", "physical device objects WDK kernel", "PDOs WDK kernel", "filter DOs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Example WDM Device Objects





The following figure illustrates the device objects that represent the keyboard and mouse devices shown previously in the figure illustrating [Keyboard and Mouse Hardware Configurations](sample-device-and-driver-configuration.md#keyboard-and-mouse-hardware-configurations). The keyboard and mouse drivers shown in the figure illustrating [Keyboard and Mouse Driver Layers](sample-device-and-driver-configuration.md#keyboard-and-mouse-driver-layers) create these device objects by calling an I/O support routine ([**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)).

![keyboard and mouse device objects](images/2sampdos.png)

For the keyboard and mouse devices, both their respective port and class drivers create device objects. The port driver creates a physical device object (PDO) to represent the physical port. Each class driver creates its own functional device object (FDO) to represent the keyboard or mouse device as a target for I/O requests.

Each class driver calls an I/O support routine to get a pointer to the next-lower-level driver's device object, so the class driver can chain itself above that driver, which is the port driver. Then the class driver can send I/O requests down to the port driver for the target PDO representing its physical device.

An optional filter driver added to the configuration would create a filter device object (filter DO). Like the class driver, an optional filter driver chains itself to the next-lower driver in the device stack and sends I/O requests for the target PDO down to the next-lower driver.

As shown previously in the [Keyboard and Mouse Driver Layers](sample-device-and-driver-configuration.md#keyboard-and-mouse-driver-layers) figure, each port driver is a bus (lowest-level) driver, so every port driver of a device that generates interrupts must set up interrupt object(s) and register an ISR.

A dual-device port driver, like the i8042 driver for the keyboard and auxiliary device controller shown in the [Keyboard and Mouse Hardware Configurations](sample-device-and-driver-configuration.md#keyboard-and-mouse-hardware-configurations) figure, must set up device-specific [*interrupt objects*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-interrupt-object) if each device uses a different interrupt vector. When writing such a driver, you can either implement separate ISRs for each device or implement a single ISR for both devices.

 

 




