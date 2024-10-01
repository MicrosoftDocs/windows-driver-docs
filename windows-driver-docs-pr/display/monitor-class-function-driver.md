---
title: Monitor Class Function Driver
description: Monitor Class Function Driver
keywords:
- multiple monitors WDK
- Monitor class function drivers WDK
- function drivers WDK monitors
- monitor device stacks WDK
- device stacks WDK monitors
- physical device objects WDK monitors
- functional device objects WDK monitors
- PDOs WDK monitors
- FDOs WDK monitors
- filter DOs WDK monitors
ms.date: 09/23/2024
---

# Monitor class function driver

A [device node](../gettingstarted/device-nodes-and-device-stacks.md) is used to represent each video output on a display adapter that has a connected monitor. The device node is a child of the display adapter's device node.

Typically, there are only two device objects in the device stack that represent a video output/monitor pair:

* The physical device object (PDO).
* The functional device object (FDO).

In some cases, there's a filter device object (DO) associated with a vendor-supplied filter driver. This filter device object sits above the FDO.

For integrated monitors, such as the built-in flat panel on a laptop computer, there might be a filter DO associated with the Advanced Configuration and Power Interface (ACPI) driver. This filter DO sits above the PDO.

The following table shows the device stack for a video output that has a connected monitor.

| Device object | Required/Optional | Driver |
| ------------- | ----------------- | ------ |
| Filter DO | Optional, typically not needed | Filter driver supplied by monitor vendor |
FDO | Required | Monitor class function driver (*Monitor.sys*) supplied by Microsoft |
| Filter DO | Required only for integrated ACPI display panels | ACPI driver (*Acpi.sys*) supplied by Microsoft |
PDO | Required | Bus driver (display miniport/port pair) supplied by display adapter vendor |

User-mode applications use WMI to invoke the services of the monitor class function driver. Those services include exposing a monitor's identification data. For an ACPI display, services include setting the brightness of the display.

A monitor stores its identification and capability information in an Extended Display Identification Data (EDID) structure. EDID is a metadata format that lets the display supply the host with information about its identity and capabilities independent of the communications protocol used between the monitor and host. The FDO processes a request from a user-mode application to read a monitor's EDID in that monitor's device stack. When the FDO receives a request to retrieve the monitor's EDID:

* The FDO sends a request to the PDO at the bottom of the monitor's device stack.
* The PDO uses the Display Data Channel (DDC) protocol to read the monitor's EDID over the I²C bus, which is a simple two-wire bus built into all standard monitor cables.

The EDID can be obtained using the [ACPI_METHOD_OUTPUT_DDC](../bringup/other-acpi-namespace-objects.md) method whose alias is defined in [*Dispmprt.h*](/windows-hardware/drivers/ddi/dispmprt/). This method is required for integrated LCDs that don't have another standard mechanism for returning EDID data.

For more information about communication between display adapters and monitors, see [I2C Bus and Child Devices of the Display Adapter](i2c-bus-and-child-devices-of-the-display-adapter.md).

For details about EDID structures and the DDC protocol, see the following standards published by the Video Electronics Standards Association (VESA):

* Enhanced Display Data Channel Standard (E-DDC)

* Enhanced EDID Standard (E-EDID)

You can download these standards from [vesa.org](https://vesa.org/vesa-standards/) in the *Free Standards* section.

For details about the I²C bus, see the [I²C Bus Specification](https://www.i2c-bus.org/specification/) published by Philips Semiconductors.
