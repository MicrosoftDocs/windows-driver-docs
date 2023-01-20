---
title: Hardware design of USB Type-C systems
description: Here are some example designs for USB Type-C system.
ms.date: 01/20/2023
---

# Hardware design: USB Type-C systems

Here are some example designs for USB Type-C systems.

A typical USB Type-C system has these components:

- **USB Dual-Role controller** is capable of operating either in host role or in function/device/peripheral role. This component is integrated into SoC.
- **Battery Charging 1.2 detection** might be integrated in certain SoCs. Some SoC vendors provide a PMIC module that implements detection logic, others implement in software. Windows 10 Mobile supports all those options. Contact your SoC vendor to get details about this component.
- **Type-C -PD Port controller** manages CC pins on the USB Type-C connector. Supports BMC encoding/decoding of power delivery messages. This component isn't integrated in most SoCs.
- **Mux** SuperSpeed USB pairs to a port on the controller depending on the orientation detected by Type-C port controller. Mux SuperSpeed pairs and possibly SBU lines elsewhere (usually the Display module) when entering an alternate mode.
- **VBus/VConn** source is required. Most PMICs implement VBus/VConn control. Contact your SoC/PMIC vendor for details.

## USB Type-C system design with an embedded controller

In addition to the components in the preceding list, a USB Type-C system can have an embedded controller. This intelligent microcontroller that acts as the Type-C and Power Delivery policy manager for the system.

Here's an example of a USB Type-C system with an embedded controller:

:::image type="content" source="images/type-c-hw1.png" alt-text="Diagram that shows a U S B Type-C hardware design example for embedded controller devices.":::

Here's another view:

:::image type="content" source="images/type-c-hw1-1.png" alt-text="Diagram of a USB Type-C hardware design example for embedded controller devices.":::

For a system that has an embedded controller, load the Microsoft provided in-box driver. UcmUcsi.sys implements USB Type-C Connector System Software Interface (UCSI) Specification.

[UCSI driver](ucsi.md). For information about the device stacks loaded for the driver, see [Drivers for supporting USB Type-C components for systems with embedded controllers](architecture--usb-type-c-in-a-windows-system.md#drivers-for-supporting-usb-type-c-components).

For a system that has an embedded controller that uses non-ACPI transport.

[Write a UCSI client driver](write-a-ucsi-driver.md)

[USB Type-C driver reference](/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference)

## USB Type-C system design

Here's an example of a USB Type-C system for a mobile device that doesn't have an embedded controller:

:::image type="content" source="images/type-c-hw2.png" alt-text="Diagram of a USB Type-C hardware design example for mobile devices.":::

Here's another view:

:::image type="content" source="images/type-c-hw2-1.png" alt-text="Diagram of a USB Type-C hardware design example device without an embedded controller.":::

For the preceding design, implement a driver that communicates with the connector and keeps the operating system informed about USB Type-C events on the connector.

[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)

[USB Type-C driver reference](/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference)

## Related topics

- [Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)
