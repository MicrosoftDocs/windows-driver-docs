---
Description: Here are some example designs for USB Type-C system.
title: Hardware design of USB Type-C systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware design: USB Type-C systems


**Last Updated**

-   December 2016

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Here are some example designs for USB Type-C system.

A typical USB Type-C system has these components:

-   **USB Dual-Role controller** is capable of operating either in host role or in function/device/peripheral role. This component is integrated into SoC.
-   **Battery Charging 1.2 detection** might be integrated in certain SoCs. Some SoC vendors provide a PMIC module that implements detection logic, others implement in software. Windows 10 Mobile supports all those options. Contact your SoC vendor to get details about this component.
-   **Type-C -PD Port controller** manages CC pins on the USB Type-C connector. Supports BMC encoding/decoding of power delivery messages. This component is usually not integrated in most SoCs.
-   **Mux** SuperSpeed USB pairs to a port on the controller depending on the orientation detected by Type-C port controller. Mux SuperSpeed pairs and possibly SBU lines elsewhere (usually the Display module) when entering an alternate mode.
-   **VBus/VConn** source is required. Most PMICs implement VBus/VConn control. Contact your SoC/PMIC vendor for details.

## <a href="" id="emb"></a>USB Type-C system design with an embedded controller


In addition to the components in the preceding list, a USB Type-C system can have an embedded controller. This intelligent microcontroller that acts as the Type-C and Power Delivery policy manager for the system.

Here is an example of a USB Type-C system with an embedded controller:

![usb type-c hardware design example for embedded controller devices](images/type-c-hw1.png)

Here is another view:

![usb type-c hardware design example for embedded controller devices](images/type-c-hw1-1.png)

For a system that has an embedded controller, load the Microsoft provided in-box driver, UcmUcsi.sys, that implements USB Type-C Connector System Software Interface (UCSI) Specification.

[UCSI driver](ucsi.md). For information about the device stacks loaded for the driver, see [Drivers for supporting USB Type-C components for systems with embedded controllers](architecture--usb-type-c-in-a-windows-system.md#drivers).


For a system that has an embedded controller that uses non-ACPI transport. 

[Write a UCSI client driver](write-a-ucsi-driver.md)

[USB Type-C driver reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#type-c-driver-reference)

## <a href="" id="hardware"></a>USB Type-C system design


Here is an example of a USB Type-C system for a mobile device that does not have an embedded controller:

![usb type-c hardware design example for mobile devices](images/type-c-hw2.png)

Here is another view:

![usb type-c hardware design example device without an embedded controller](images/type-c-hw2-1.png)

For the preceding design, implement a driver that communicates with the connector and keeps the operating system informed about USB Type-C events on the connector.

[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)

[USB Type-C driver reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#type-c-driver-reference)

## Related topics
[Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)  



