---
title: Device Bus Connectivity
description: A Windows Precision Touchpad can use either USB or I²C for host connectivity. This topic includes examples of device configurations.
ms.assetid: E60C134A-9096-4B74-9C7F-CE9FC6A67BEB
---

# Device Bus Connectivity


A Windows Precision Touchpad can use either USB or I²C for host connectivity. This topic includes examples of device configurations.

## <span id="I2C_Devices"></span><span id="i2c_devices"></span><span id="I2C_DEVICES"></span>I²C Devices


A Windows Precision Touchpad module is defined as the combination of a controller IC, sensor and any associated mechanics.

An I²C connected Windows Precision Touchpad module shall expose, at a minimum, the required 5 pins for host connectivity, I²C data and clock lines (SDA and SCL), an interrupt line, and attachment to power rail and ground.

When connecting to an I²C controller, it is important to understand the bandwidth demands of all components that share that controller. The minimum I²C clock speed of a Windows Precision Touchpad shall be 400KHz. It is highly recommended that touch screen controllers and Windows Precision Touchpad controllers do not share the same I²C controller, because this can result in bandwidth demands that exceed bus capability.

We recommend that the interrupt line (also referred to as ATTN line) is connected to an On-SoC GPIO controller or an IOAPIC. The GPIO or IOAPIC resource to which the interrupt line is connected must be capable of waking the SoC to enable the Windows Precision Touchpad to wake the system in various scenarios.

To allow for various wake scenarios, the power rail that is used to feed to the Windows Precision Touchpad should not be shared with devices that are not wake capable (for example, a touch controller). The power rail must be energized during connected standby/S3 conditions.

![i2c connected windows precision touchpad](images/implementationfig1i2cconnected.jpg)

**Figure 1 I2C Connected Windows Precision Touchpad**

### <span id="ACPI_Table_Entries"></span><span id="acpi_table_entries"></span><span id="ACPI_TABLE_ENTRIES"></span>ACPI Table Entries

An I²C-connected Windows Precision Touchpad must define an entry in the ACPI table for the device to be recognized.

This entry should specify the following:

| Entry                          | Purpose                                                                                                                                                                                 |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACPI Device Entry Name         | A 4 character identification unique to that ACPI table to reference the device (for example, “TPAD”)                                                                                    |
| ACPI Hardware ID               | A 4 character + 4 number ACPI hardware ID to reference the device (exposed in device manager) (for example, “MSFT0001”)                                                                 |
| Compatible ID                  | This should always be “PNP0C50” to indicate that the device is HID I²C compatible                                                                                                       |
| GPIO Controller                | The GPIO controller used to connect the interrupt line for the device must be specified to allow the host to consume it (for example, “GPIO0” – for controller 0)                       |
| GPIO Interrupt Assertion Level | This defines the line level when the interrupt is asserted by the device. This can be specified as “ActiveLow” or “ActiveHigh”                                                          |
| GPIO Interrupt Assertion Type  | This defines whether the device will provide edge triggered or level triggered interrupts. HID I²C compliant devices should provide and indicate “Level” triggered interrupts           |
| GPIO Resource Type             | This defines the constraints around the GPIO resource. This should be “ExclusiveAndWake”                                                                                                |
| GPIO Resource/Pin              | The GPIO controller pin used to connect the interrupt line for the device must be specified to allow the host to associate it with the device (for example, “{35}” – for pin 35)        |
| I²C Controller                 | The I²C controller used to connect the device must be specified in order to communicate with it (for example, “I2C3” – for controller 3)                                                |
| I²C Slave Address              | The I²C slave address for the device must be specified to allow the host to address it (for example, “0x6F”)                                                                            |
| I²C Speed                      | The maximum speed supported by both the device and the I²C controller should be specified here to ensure communications performance. This should not be any lower than 400KHz (0x61A80) |

 

## <span id="USB_devices"></span><span id="usb_devices"></span><span id="USB_DEVICES"></span>USB devices


A USB 2.0 connected high-speed/full-speed Windows Precision Touchpad module shall expose the necessary pins for host connectivity.

Connection to the host can take many forms and is at the discretion of the integrator.

When connecting to a USB hub, it is important to understand the bandwidth demands of all components sharing that hub. It is highly recommended that high bandwidth devices and Windows Precision Touchpad controllers do not share the same USB hub because this can result in bandwidth demands that exceed bus capability.

### <span id="USB_bridge_devices__I2C____USB_"></span><span id="usb_bridge_devices__i2c____usb_"></span><span id="USB_BRIDGE_DEVICES__I2C____USB_"></span>USB bridge devices (I²C –&gt; USB)

If a USB bridge is elected for connecting an I²C Windows Precision Touchpad to the host, the bridge shall expose the Windows Precision Touchpad as a distinct device node together with the device’s unique attributes (wVendorID, wProductID, wVersionID).

 

 




