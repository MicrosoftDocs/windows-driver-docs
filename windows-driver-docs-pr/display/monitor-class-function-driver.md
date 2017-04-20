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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

A monitor stores its identification and capability information in an Extended Display Identification Data ([*EDID*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-edid)) structure. A request, from a user-mode application, to read a monitor's EDID is processed by the function driver (Monitor.sys) in that monitor's device stack. When the monitor function driver receives a request to retrieve the monitor's EDID, it sends a request to the display port/miniport driver pair that is represented by the physical device object (PDO) at the bottom of the monitor's device stack. The display port/miniport driver pair uses the Display Data Channel (DDC) protocol to read the monitor's EDID over the I²C bus, which is a simple two-wire bus built into all standard monitor cables.

The [*EDID*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-edid) can be obtained using the ACPI\_METHOD\_OUTPUT\_DDC method whose alias is defined in Dispmprt.h. This method is required for integrated LCDs that do not have another standard mechanism for returning EDID data.

For more information about communication between display adapters and monitors, see the following topics:

[I2C Bus and Child Devices of the Display Adapter](i2c-bus-and-child-devices-of-the-display-adapter.md)

[I2C Functions](https://msdn.microsoft.com/library/windows/hardware/ff567383)

[I2C Functions Implemented by the Video Port Driver](https://msdn.microsoft.com/library/windows/hardware/ff567384)

For details about EDID structures and the DDC protocol, see the following standards published by the Video Electronics Standards Association (VESA):

-   Enhanced Display Data Channel Standard

-   Enhanced EDID Standard

For details about the I²C bus, see the I²C Bus Specification published by Philips Semiconductors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Monitor%20Class%20Function%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




