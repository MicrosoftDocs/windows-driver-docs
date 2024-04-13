---
title: Stress Testing
description: Stress Testing
keywords:
- stress testing WDK printer
- bus stress testing WDK printer
ms.date: 01/30/2023
---

# Stress Testing

[!include[Print Support Apps](../includes/print-support-apps.md)]

You should run your printer through a stress test by sending large (over 100 MB), long (over 150 pages), and graphically intensive print jobs to it. For graphically intensive jobs, vary the combinations of different sizes and types of graphic images as much as possible.

## Specialized Bus Stress

When you create stress cases, take into consideration stress factors that can occur on a specialized bus. Many devices can share the same bus, so be sure to test that your device coexists gracefully with other devices on the same bus, devices of the same type or model, or common devices that a user could typically have attached to the system. For example, you could plug many devices at the same time into the same USB hub to which your printer is attached.

The following tests are recommended:

1. Verify that plugging several other devices into the hub or system does not interfere with your device.

1. Chain multiple hubs and devices together and verify that your device continues to function correctly.

1. Verify that all devices on the same bus can work simultaneously.

1. Verify that the your device uninstalls gracefully when the attached hub is unplugged from the system.

For Bluetooth-enabled printers, run stress tests on print jobs as follows:

1. Move the printer in and out of the maximum range of the Bluetooth radio, typically 30 to 90 feet (10 to 30 meters), depending on the radio.

1. Send the job to a printer just inside the range of the Bluetooth radio.

1. Send a job to a printer outside the maximum range of the Bluetooth radio. Wait for an error state to occur, and then move the printer back within range to verify that it recovers gracefully.
