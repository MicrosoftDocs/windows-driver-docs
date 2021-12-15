---
title: ACPI button device
description: The generic button device is a standard device for reporting button events through hardware interrupts.
ms.date: 04/20/2017
---

# ACPI button device

The generic button device is a standard device for reporting button events through hardware interrupts, and mapping those interrupts to specific usages defined in the Human Interface Device (HID) specification.

In order to express the functionality of a button to the operating system, two pieces of information are required:

- Usage of the HID Control
- Usage of the HID Collection in which the Control belongs

A Usage is a combination of a Usage Page and Usage ID. For example, the Volume Up button is identified as the Volume Up Usage (Usage Page 0x0C, Usage Id 0xE9) in the Consumer Control Collection (Usage Page 0x0C, Usage Id 0x01).

ACPI device Id of a generic button device is ACPI0011. Windows loads the Microsoft-provided in-box driver, Hidinterrupt.sys for that device.

For more information about the generic button device, visit the [Unified Extensible Firmware Interface](https://uefi.org/specifications) specifications web site, and download the *ACPI Specification Version 6.0* PDF document. Then use the left-hand pane to navigate to **Section 9.19**.

## Sample ACPI button device for Windows 10 Core OS editions

Example for describing buttons in [ACPI Source Language (ASL)](https://uefi.org/htmlspecs/ACPI_Spec_6_4_html/19_ASL_Reference/ACPI_Source_Language_Reference.html?highlight=acpi%20source%20language) for device running Windows 10 Core OS.

```ASL
// Sample Buttons in ACPI Source Language for Windows 10.

Device(BTNS)
{
    Name(_HID, "ACPI0011")
    Name(_CRS, ResourceTemplate() {
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 0: Power Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 1: Volume Up Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 2: Volume Down Button
        GpioInt(Edge, ActiveHigh,...) {pin} // Index 3: Camera Auto-focus Button
        GpioInt(Edge, ActiveLow,...)  {pin} // Index 4: Camera Shutter Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 5: Back Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 6: Windows/Home Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 7: Search Button
    })
    Name(_DSD, Package(2) {
        //UUID for HID Button Descriptors:
        ToUUID("FA6BD625-9CE8-470D-A2C7-B3CA36C4282E"),
        //Data structure for this UUID:
        Package(9) {
            Package(5) {
                0,    // This is a Collection
                1,    // Unique ID for this Collection
                0,    // This is a Top-Level Collection
                0x01, // Usage Page ("Generic Desktop Page")
                0x0D  // Usage ("Portable Device Control")
            },
            Package(5) {
                1,    // This is a Control
                0,    // Interrupt index in _CRS for Power Button
                1,    // Unique ID of Parent Collection
                0x01, // Usage Page ("Generic Desktop Page")
                0x81  // Usage ("System Power Down")
            },
            Package(5) {
                1,    // This is a Control
                1,    // Interrupt index in _CRS for Volume Up Button
                1,    // Unique ID of Parent Collection
                0x0C, // Usage Page ("Consumer Page")
                0xE9  // Usage ("Volume Increment")
            },
            Package(5) {
                1,    // This is a Control
                2,    // Interrupt index in _CRS for Volume Down Button
                1,    // Unique ID of Parent Collection
                0x0C, // Usage Page ("Consumer Page")
                0xEA  // Usage ("Volume Decrement")
            },
            Package(5) {
                1,    // This is a Control
                3,    // Interrupt index in _CRS for Camera Auto-focus Button
                1,    // Unique ID of Parent Collection
                0x90, // Usage Page ("Camera Control Page")
                0x20  // Usage ("Camera Auto-focus")
            },
            Package(5) {
                1,    // This is a Control
                4,    // Interrupt index in _CRS for Camera Shutter Button
                1,    // Unique ID of Parent Collection
                0x90, // Usage Page ("Camera Control Page")
                0x21  // Usage ("Camera Shutter")
            },
            Package(5) {
                1,    // This is a Control
                5,    // Interrupt index in _CRS for Back Button
                1,    // Unique ID of Parent Collection
                0x0C, // Usage Page ("Consumer Page")
                0x224 // Usage ("AC Back")
            },
            Package(5) {
                1,    // This is a Control
                6,    // Interrupt index in _CRS for Windows/Home Button
                1,    // Unique ID of Parent Collection
                0x07, // Usage Page ("Keyboard Page")
                0xE3  // Usage ("Keyboard Left GUI")
            },
            Package(5) {
                1,    // This is a Control
                7,    // Interrupt index in _CRS for Search Button
                1,    // Unique ID of Parent Collection
                0x0C, // Usage Page ("Consumer Page")
                0x221 // Usage ("AC Search")
            }
        }
    })
}
```

## Sample buttons in ACPI for device running Windows 10 desktop editions

Example for describing buttons in [ACPI Source Language (ASL)](https://uefi.org/htmlspecs/ACPI_Spec_6_4_html/19_ASL_Reference/ACPI_Source_Language_Reference.html?highlight=acpi%20source%20language) for device running Windows 10 desktop editions (Home, Pro, Enterprise, and Education).

```ASL
Device(BTNS)
{
    Name(_HID, "ACPI0011")
    Name(_CRS, ResourceTemplate() {
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 0: Power Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 1: Volume Up Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 2: Volume Down Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 3: Windows/Home Button
        GpioInt(Edge, ActiveBoth,...) {pin} // Index 4: Rotation Lock Button
    })
    Name(_DSD, Package(2) {
        //UUID for HID Button Descriptors:
        ToUUID("FA6BD625-9CE8-470D-A2C7-B3CA36C4282E"),
        //Data structure for this UUID:
        Package(6) {
            Package(5) {
                0,    // This is a Collection
                1,    // Unique ID for this Collection
                0,    // This is a Top-Level Collection
                0x01, // Usage Page ("Generic Desktop Page")
                0x0D  // Usage ("Portable Device Control")
            },
            Package(5) {
                1,    // This is a Control
                0,    // Interrupt index in _CRS for Power Button
                1,    // Unique ID of Parent Collection
                0x01, // Usage Page ("Generic Desktop Page")
                0x81  // Usage ("System Power Down")
            },
            Package(5) {
                1,    // This is a Control
                1,    // Interrupt index in _CRS for Volume Up Button
                1,    // Unique ID of Parent Collection
                0x0C, // Usage Page ("Consumer Page")
                0xE9  // Usage ("Volume Increment")
            },
            Package(5) {
                1,    // This is a Control
                2,    // Interrupt index in _CRS for Volume Down Button
                1,    // Unique ID of Parent Collection
                0x0C, // Usage Page ("Consumer Page")
                0xEA  // Usage ("Volume Decrement")
            },
            Package(5) {
                1,    // This is a Control
                3,    // Interrupt index in _CRS for Windows/Home Button
                1,    // Unique ID of Parent Collection
                0x07, // Usage Page ("Keyboard Page")
                0xE3  // Usage ("Keyboard Left GUI")
            },
            Package(5) {
                1,    // This is a Control
                4,    // Interrupt index in _CRS for Rotation Lock Button
                1,    // Unique ID of Parent Collection
                0x01, // Usage Page ("Generic Desktop Page")
                0xCA  // Usage ("System Display Rotation Lock Slider Switch")
            }
        }
    })
}

```
