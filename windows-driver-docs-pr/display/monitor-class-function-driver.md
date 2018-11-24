---
title: Monitor Class Function Driver
description: Monitor Class Function Driver
ms.assetid: d16c3dcc-2fbf-4579-8962-1b89e6e7b347
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitor Class Function Driver


## <span id="ddk_monitor_class_function_driver_gg"></span><span id="DDK_MONITOR_CLASS_FUNCTION_DRIVER_GG"></span>


Each video output on the display adapter that has a monitor connected to it is represented by a device node that is a child of the display adapter's device node.

Typically, there are only two device objects in the device stack that represent a (video output, monitor) pair: the physical device object (PDO) and the functional device object (FDO). In some cases, there is a filter DO, associated with a vendor-supplied filter driver, above the FDO. For integrated monitors, such as the built-in flat panel on a laptop computer, there might be a filter DO, associated with the Advanced Configuration and Power Interface (ACPI) driver, above the PDO.

The following table shows the device stack for a video output that has a connected monitor.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Device object</th>
<th align="left">Required/Optional</th>
<th align="left">Driver</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Filter DO</p></td>
<td align="left"><p>Optional, typically not needed</p></td>
<td align="left"><p>Filter driver supplied by monitor vendor</p></td>
</tr>
<tr class="even">
<td align="left"><p>FDO</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Monitor class function driver (Monitor.sys) supplied by Microsoft</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Filter DO</p></td>
<td align="left"><p>Required only for integrated ACPI display panels</p></td>
<td align="left"><p>ACPI driver (Acpi.sys) supplied by Microsoft</p></td>
</tr>
<tr class="even">
<td align="left"><p>PDO</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Bus driver (display miniport/port pair) supplied by display adapter vendor</p></td>
</tr>
</tbody>
</table>

 

User-mode applications use WMI to invoke the services of the monitor class function driver. Those services include exposing a monitor's identification data and (in the case of an ACPI display) setting the brightness of the display.

A monitor stores its identification and capability information in an Extended Display Identification Data (EDID) structure, a format that lets the display supply the host with information about its identity and capabilities independent of the communications protocol used between the monitor and host. A request, from a user-mode application, to read a monitor's EDID is processed by the function driver (Monitor.sys) in that monitor's device stack. When the monitor function driver receives a request to retrieve the monitor's EDID, it sends a request to the display port/miniport driver pair that is represented by the physical device object (PDO) at the bottom of the monitor's device stack. The display port/miniport driver pair uses the Display Data Channel (DDC) protocol to read the monitor's EDID over the I²C bus, which is a simple two-wire bus built into all standard monitor cables.

The EDID can be obtained using the [ACPI_METHOD_OUTPUT_DDC](https://docs.microsoft.com/windows-hardware/drivers/bringup/other-acpi-namespace-objects) method whose alias is defined in [Dispmprt.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dispmprt/). This method is required for integrated LCDs that do not have another standard mechanism for returning EDID data.

For more information about communication between display adapters and monitors, see the following topic:

[I2C Bus and Child Devices of the Display Adapter](i2c-bus-and-child-devices-of-the-display-adapter.md)

For details about EDID structures and the DDC protocol, see the following standards published by the Video Electronics Standards Association (VESA):

-   Enhanced Display Data Channel Standard (E-DDC)

-   Enhanced EDID Standard (E-EDID)

You can download these standards from [vesa.org](https://vesa.org/vesa-standards/) in the *Free Standards* section.

For details about the I²C bus, see the [I²C Bus Specification](https://www.i2c-bus.org/specification/) published by Philips Semiconductors.

 

 





