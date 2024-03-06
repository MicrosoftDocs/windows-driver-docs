---
title: Interaction of Battery Class and Miniclass Drivers
description: Learn about the interaction between battery class and miniclass drivers in a computer system and how they work together to manage battery usage.
keywords:
- battery miniclass drivers WDK, battery class driver interaction
- battery class drivers WDK, battery miniclass driver interaction
ms.date: 04/20/2017
---

# Interaction of battery class and miniclass drivers

Battery class and miniclass drivers work together to manage a computer's use of a battery. The following diagram illustrates their interaction.

:::image type="content" source="images/battmini.png" alt-text="Diagram illustrating the interaction between battery class and miniclass drivers in a computer system.":::

The miniclass driver serves as the primary function driver for the devices it controls. It receives Input/Output Request Packets (IRPs) from the power manager through the composite battery driver and calls support routines in the battery class driver to register its devices, report status, and handle certain system-defined battery IOCTLs.

The class driver gathers information and status from all miniclass drivers and reports it to the power manager through the composite battery driver. In response to battery IOCTLs, the class driver calls [battery miniclass driver routines](/windows-hardware/drivers/ddi/_battery/) (BatteryMini*Xxx* routines) in the miniclass drivers to perform specific device control operations. Additionally, applications like the power meter can send [**IRP\_MJ\_DEVICE\_CONTROL**](../kernel/irp-mj-device-control.md) requests to a miniclass driver to obtain information about a specific battery.

Designed to handle a wide range of battery information and conditions, the class driver manages temperature, capacity changes, and more. However, individual batteries vary in their ability to detect and report these conditions. Each miniclass driver should be tailored to manage its specific battery type and must respond appropriately to the class driver when asked for any unsupported information.
