---
title: Other ACPI namespace objects
description: For some specific classes of device, there are requirements for additional ACPI namespace objects to appear under those devices in the namespace.
ms.assetid: 41EA8C3D-F2C9-4BA9-A839-FCB66F271E3C
ms.date: 05/16/2018
ms.localizationpriority: medium
---

# Other ACPI namespace objects


For some specific classes of device, there are requirements for additional Advanced Configuration and Power Interface (ACPI) namespace objects to appear under those devices in the namespace. This section lists the additional objects required for SoC-based platforms.

## Processor identification objects


Processors must be enumerated in the ACPI namespace. Processors are declared under \\\_SB using the "Device" statement, as with other devices on the platform. Processor devices must contain the following objects:

-   \_HID: ACPI0007
-   \_UID: A unique number that matches the processor's entry in the MADT.

## Display-specific objects


For more information about display-specific objects, see Appendix B, "Video Extensions", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

**Display-Specific Object Requirements**

| Method | Description                                        | Requirement                                                                      |
|--------|----------------------------------------------------|----------------------------------------------------------------------------------|
| \_DOS  | Enable/Disable output switching.                   | Required if system supports display switching or LCD brightness levels.          |
| \_DOD  | Enumerate all devices attached to display adapter. | Required if integrated controller supports output switching.                     |
| \_ROM  | Get ROM Data.                                      | Required if ROM image is stored in proprietary format.                           |
| \_GPD  | Get POST Device.                                   | Required if \_VPO is implemented.                                                |
| \_SPD  | Set POST Device.                                   | Required if \_VPO is implemented.                                                |
| \_VPO  | Video POST Options.                                | Required if system supports changing post VGA device.                            |
| \_ADR  | Return the unique ID for this device.              | Required.                                                                        |
| \_BCL  | Query list of brightness control levels supported. | Required if embedded LCD supports brightness control.                            |
| \_BCM  | Set the brightness level.                          | Required if \_BCL is implemented.                                                |
| \_DDC  | Return the EDID for this device.                   | Required if embedded LCD does not support return of EDID via standard interface. |
| \_DCS  | Return status of output device.                    | Required if the system supports display switching (via hotkey).                  |
| \_DGS  | Query graphics state.                              | Required if the system supports display switching (via hotkey).                  |
| \_DSS  | Device state set.                                  | Required if the system supports display switching (via hotkey).                  |



## USB host controllers and devices


USB host controllers are used on SoC platforms for connecting internal and external devices. Windows includes inbox drivers for standard USB host controllers that are compliant with the EHCI or XHCI specifications.

On SoC-based platforms, the USB host controller can be enumerated by ACPI. Windows uses the following ACPI namespace objects when enumerating and configuring compatible USB hardware:

-   A vendor-assigned ACPI-compliant Hardware ID (\_HID).
-   A Unique ID (\_UID) object, if there is more than one instance of the USB controller in the namespace (that is, two or more nodes that have identical device identification objects).
-   A Compatible ID (\_CID) for the EHCI or XHCI Standard-compliant USB host controller (EHCI: PNP0D20), (XHCI: PNP0D10).
-   The Current Resource Settings (\_CRS) assigned to the USB controller. The controller's resources are described in the appropriate hardware interface specification (EHCI or XHCI).

### USB Device-Specific Method (\_DSM)

Windows defines a Device-Specific Method (\_DSM) to support device-class-specific configuration of the USB subsystem. For more information, see [USB Device-Specific Method](usb-device-specific-method---dsm-.md).

### USB integrated transaction translator (TT) support (\_HRV)

Standard EHCI host controllers support only high-speed USB devices. On SoC platforms, Windows supports two common designs of EHCI-compliant host controllers which implement an integrated transaction translator for low-speed and full-speed USB devices. The Hardware Revision (\_HRV) object indicates the type of integrated TT support to the USB host controller driver.

The \_HRV is set according to the following criteria:

-   **NoIntegratedTT - \_HRV = 0**

    Standard EHCI host controllers do not implement integrated transaction translators, and an \_HRV value of 0 is only valid for these controllers. It is not necessary to include the \_HRV object for these controllers.

-   **IntegratedTTSpeedInPortSc - \_HRV = 1**

    Enable integrated TT support. This flavor of interface includes the LowSpeed and HiSpeed bits in the PORTSC register itself. These bits are at bit offsets 26 and 27, respectively. When determining the speed, the EHCI driver will read the PORTSC, and extract the speed information from these bits.

-   **IntegratedTTSpeedInHostPc - \_HRV = 2**

    Enable integrated TT support. This flavor of interface includes the LowSpeed and HiSpeed bits in a separate HOSTPC register. When the EHCI driver needs to determine the port speed, it will read the HOSTPC register corresponding to the port of interest and extract the speed information.

### USB XHCI D3cold support

In addition to selective suspend, internal USB devices connected to XHCI controllers can be put into a D3cold state and powered off when they are not in use. For more information, see [Device Power Management](device-power-management.md). All USB device function drivers must opt-in to D3cold.

### USB port-specific objects

Windows needs to know the visibility and connect-ability of USB Ports on the system. This is required in order to provide accurate information to the user about ports and devices. Two objects, Physical Device Location (\_PLD) and USB Port Capabilities (\_UPC), are used for this purpose. For more information, see the following:

-   Sections 6.1.6, "Device Identification Objects", and 9.13.1, "USB 2.0 Host Controllers and \_UPC and \_PLD", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).
-   [Using ACPI to Configure USB Ports on a Computer](https://docs.microsoft.com/windows-hardware/drivers/install/using-acpi-to-configure-usb-ports-on-a-computer).

## SD host controllers and devices


SD host controllers are used on SoC platforms for access to storage as well as I/O devices. Windows includes an inbox driver for SDA-standard host controller hardware. For compatibility with this driver, an SD Host Controller device must comply with the SD Association's [SD Host Controller Specification](https://www.sdcard.org/developers/overview/host_controller/).

On SoC platforms, the SD host controller can be enumerated by ACPI. Windows uses the following ACPI namespace objects when enumerating and configuring compatible SD hardware:

-   A vendor-assigned ACPI-compliant Hardware ID (\_HID).
-   A Unique ID (\_UID) object, if there is more than one instance of the SD controller in the namespace (that is, two or more nodes that have identical device identification objects).
-   A Compatible ID (\_CID) for the SDA standard-compliant SD host controller (PNP0D40).
-   The Current Resource Settings (\_CRS) assigned to the controller. The controller's resources are described as follows:

    -   Hardware resources for all implemented slots are included. A slot is a connection point on the SDIO bus for a memory or I/O device. Each slot is associated with a standard set of registers and an interrupt in the SD host controller, which are used for communication with the connected device. SD host controllers may implement any number of slots, but on SoC platforms, there is typically only one.
    -   Slot resources are listed together, in order of slot number (slot 0's resources are first, slot 1's resources are second, and so on).
    -   For each slot, resources are listed in the following order:

        -   The base address of the SD standard register set for the slot.
        -   The SD standard interrupt for the slot.
        -   A GPIO interrupt resource for the slot, for signaling card insertions and removals (if the standard SD card-detect interface is not supported during all power states).
        -   A GPIO input resource for the slot for reading whether a card is currently in the slot (if the standard SD card-detect interface is not supported during all power states). Uses the same pin as the insertion/removal interrupt.
        -   A second GPIO input resource for reading whether the card in the slot is write-protected (if the standard SD write-protect interface is not supported during all power states).

The interrupts must be wake-capable (described as "SharedAndWake" or "ExclusiveAndWake").

### Embedded SD devices

SD-connected devices are enumerated by the SD bus driver. SD devices that are integrated into the platform must also be listed in the ACPI namespace as children of the SD host controller. This requirement enables the operating system to associate the bus-enumerated device with the platform-specific attributes provided for the device by ACPI objects (for example, non-removability, device power states, GPIO or SPB resources consumed, and so on). To make this association, the device namespace requires the Address (\_ADR) object, which communicates the address of the device on the SDIO bus. The \_ADR object returns an integer. For the SDIO bus, the value of this integer is defined as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SDIO bus</td>
<td><p>High word – Slot number (0–first slot)</p>
<p>Low word – Function number (See SD specification for definitions.)</p></td>
</tr>
</tbody>
</table>



An embedded SD device namespace must also include:

-   A Remove method (\_RMV) object that returns 0 (to indicate that the device cannot be removed).
-   A \_CRS object for the sideband resources the device requires (such as GPIO pins or SPB connections), if any are required.

## Imaging class devices (cameras)


Camera devices may be enumerated by the graphics driver or by USB. In either case, Windows needs to know the physical location of the camera so that the appropriate UI can be shown. To do this, camera devices that are built into the chassis of the system and have mechanically fixed direction are included in the ACPI namespace and provide the Physical Device Location (\_PLD) object. This requires:

-   The camera device to appear as a child (nested device) of the enumerator device (either the GPU device or the USB device).
-   The camera device to provide the Address (\_ADR) object that contains the camera's address on the parent device's bus.

    -   For USB, see [ACPI namespace hierarchy and \_ADR for embedded USB devices](#adr).
    -   For graphics, this is the identifier that is specified in the \_DOD method provided under the GPU device. For more information, see Appendix B, "Video Extensions", of the ACPI 5.0 specification.
-   The camera device to provide the \_PLD object.
-   If there are any sideband resources required by the camera driver (such as GPIO interrupt or I/O connections, or an SPB connection), the \_CRS object is provided for these resources.

In the \_PLD object, the **Panel** field (bits 67-69), **Lid** field (bit 66) and **Dock** field (bit 65) are set to correct values for the surface on which the camera is mounted. All other fields are optional. For handheld mobile devices, including tablets, the front panel is the one holding the display screen, and its origin is in the lower-left corner when the display is viewed in the portrait orientation. Using this reference, "Front" indicates that the camera views the user (webcam), while "Back" indicates that the camera views away from the user (still or video camera). For more information, see, section 6.1.8, "\_PLD (Physical Location of Device)", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

### ACPI namespace hierarchy and \_ADR for embedded USB devices

When adding embedded USB devices to the ACPI namespace, the hierarchy of the device nodes must exactly match that of the devices that are enumerated by the Windows USB driver. This can be determined by examining Windows Device Manager in its "View by Connection" mode. The entire hierarchy, starting from the USB host controller and extending down to the embedded device, must be included. The "Address" property provided in Device Manager for each device is the address that the firmware must report in the device's \_ADR.

The [ACPI 5.0 specification](https://www.uefi.org/specifications) defines the addresses for USB devices as follows:

|              |                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------|
| USB Root HUB | Only child of the host controller. It must have an \_ADR of 0. No other children or values of \_ADR are allowed. |
| USB Ports    | Port number (1-n)                                                                                                |



USB devices connected to a particular port share the address of that port.

If the device connected to a port is a composite USB device, functions within the composite device must use the following address:

|                                            |                                                                                                                                             |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| USB function within a Composite USB device | Port number of the port to which the composite device is connected, PLUS the first Interface number of the function. (Arithmetic addition). |



For more information, see [Identifying the Location of Internal Cameras](http://go.microsoft.com/fwlink/p/?linkid=331060).

### ASL code examples

The following ASL code example describes a USB webcam that is connected directly to USB port 3.

```asl
Device (EHCI) {
    ...  // Objects required for EHCI devices
    Device {RHUB) {         // the Root HUB
     Name (_ADR, ZERO)      // Address is always 0.
     Device (CAM0) {          // Camera connected directly to USB
                       //   port number 3 under the Root.
            Name (_ADR, 3)      // Address is the same as the port.
            Method (_PLD, 0, Serialized) {...}
            }  //  End of Camera device
    } // End of Root Hub Device
}  // End of EHCI device
```

The following ASL code example describes a USB composite device that implements a webcam as Function 2.

```asl
Device (EHCI) {
    ...  // Objects required for EHCI devices
    Device {RHUB) {
     Name (_ADR, ZERO)
     Device (CUSB) {        // Composite USB device
                    //   connected to USB port number 3
                    //   under the Root.
            Name (_ADR, 3)      // Address is the same as the port.
            Device (CAM0) { // Camera function within the
                    //   Composite USB device.
                Name (_ADR, 5)  // Camera function has a first
                    //   Interface number of 2, so
                    //   Address is 3 + 2  = 5.
                Method (_PLD, 0, Serialized) {...}
            }  //  End of Camera device
        } // End of Composite USB Device
    } // End of Root Hub Device
}  // End of EHCI device
```

The following ASL code example describes a webcam connected over I2C.

```asl
Device (GPU0) {
    ... // Other objects required for graphics devices
    Name (_DOD, Package ()  // Identifies the children of this graphics device.
                // Each integer must be unique within the GPU0 namespace.
                {
                    0x00024321,  // The ID for CAM0. It is a non-VGA
                    //   device, cannot be detected by
                    //   the VGA BIOS, and uses a vendor-
                    //   specific ID format in bits 15:0
                    //   (see the _DOD specification).
                    ...     // Other child device IDs (for
                    //   example, display output ports)
                })
    Device (CAM0) {
        Name (_ADR, 0x00024321) // The identifier for this device
                    //   (Same as in _DOD above)
        Name (_CRS, ResourceTemplate()
            {
            // I2C Resource
            // GPIO interrupt resource(s), if required by
            //   driver
            // GPIO I/O resource(s), if required by driver
                ...
            })
        Method (_PLD, 0, Serialized) {...}
    } // End of CAM0 device
} // End of GPU0 device
```

## HID-over-I2C devices


Windows includes a class driver for Human Interface Devices (HID). This driver enables generic support for a broad range of input devices (such as touch panels, keyboards, mice, and sensors). On SoC platforms, HID devices can be connected to the platform over I2C, and are enumerated by ACPI. For compatibility with the HID class support in Windows, the following namespace objects are used:

-   A vendor-specific \_HID
-   A \_CID of PNP0C50
-   A \_CRS with:
    -   An I2CSerialBusConnection resource for access to the device
    -   A GpioInt resource for interrupt(s)
-   The HIDI2C \_DSM method for returning the HID Descriptor Register address in the device. For more information, see [HIDI2C Device-Specific Method (\_DSM)](hidi2c-device-specific-method---dsm-.md).

## Button devices


For SoC platforms, Windows supports both the ACPI-defined Control Method Power Button, as well as a Windows-compatible five-button array. The power button, whether implemented as an ACPI Control Method Power Button or as part of the Windows-compatible Button Array, does the following:

-   Causes the platform to power-up if it is off.
-   Generates the Power Button Override event when held down. For more information, see section 4.8.2.2.1.3, "Power Button Override", of the ACPI 5.0 specification.

### Control method power button

Clamshell designs, and other systems with built-in or connected keyboards, implement the ACPI-defined Control Method Power Button (section 4.8.2.2.1.2 of the ACPI 5.0 specification) using GPIO-Signaled ACPI Events (section 5.6.5 of the ACPI 5.0 specification). To support the power button device, the namespace:

-   Describes the power button's GPIO interrupt pin as a non-shared (Exclusive) GPIO interrupt resource.
-   Lists the power button's GPIO interrupt resource in the \_AEI object of the GPIO controller to which it is connected.
-   Provides the associated event method (Lxx/Exx/EVT) under the GPIO controller device. This event method notifies the Control Method Button driver in the operating system that the button event has occurred.

For more information, see [Hardware buttons for Windows 8 tablet and convertible devices](http://go.microsoft.com/fwlink/p/?linkid=331284).

### Windows-compatible button array

For touch-first (keyboard-less) platforms, such as slates, Windows provides a generic driver for an array of five buttons. Each button in the array has its defined function (see the numbered items in the list below), and certain "hold-and-press" button combinations have additional meaning in the UI. No button combinations are defined that require the power button to be held down. For compatibility with the Windows inbox button driver, the Windows-compatible Button Array ACPI device is implemented. The device is defined as follows:

-   Each of the five buttons is connected to its own dedicated interrupt pin on the platform.
-   Each interrupt pin is configured as a non-shared (Exclusive), edge-triggered (Edge) interrupt resource that interrupts on both edges (ActiveBoth).
-   The device namespace contains a vendor-defined \_HID as well as a \_CID of PNP0C40.
-   The GPIO interrupt resources in the \_CRS object are listed in the following order:

    1.  Interrupt corresponding to the "Power" button

        The "Power" button must be wake-capable (ExclusiveAndWake).

    2.  Interrupt corresponding to the "Windows" button

        The Windows button must be wake-capable (ExclusiveAndWake).

    3.  Interrupt corresponding to the "Volume Up" button

        The "Volume Up" button must not be wake-capable (must use Exclusive).

    4.  Interrupt corresponding to the "Volume Down" button

        The "Volume Down" button must not be wake-capable (must use Exclusive).

    5.  Interrupt corresponding to the "Rotation Lock" button, if supported

        The "Rotation Lock" button must not be wake-capable (must use Exclusive).

For more information, see [Hardware buttons for Windows 8 tablet and convertible devices](http://go.microsoft.com/fwlink/p/?linkid=331284).

To support evolution of the Windows Button UI, Windows defines a Device-Specific Method (\_DSM) for the Windows Button Array device. For more information, see [Windows Button Array Device-Specific Method (\_DSM)](windows-button-array-device-specific-method---dsm-.md).

## Dock and convertible PC sensing devices


Windows supports docks and convertibles (clamshell/tablet combos) by the use of two sensing devices in the ACPI namespace. These devices are supported by the Windows inbox button driver. Note that the same requirements that apply to the Button Array device also apply to these devices:

-   GPIO ActiveBoth interrupts must be connected to an on-SoC GPIO controller (not to an SPB-connected GPIO controller).
-   The GPIO controller must support level-mode interrupts and dynamic polarity reprogramming.
-   The GPIO controller driver must use ActiveBoth emulation provided by the [GPIO framework extension](https://docs.microsoft.com/windows-hardware/drivers/gpio/gpioclx-i-o-and-interrupt-interfaces) (**GpioClx**).
-   If the asserted state ("Docked" or "Converted") is not asserted logic level low, the GPIO controller \_DSM method is required to override the GPIO driver stack's default behavior. For more information, see the **GPIO controller devices** section in the [General-purpose I/O (GPIO)](general-purpose-i-o--gpio-.md) topic.

For more information, see [Hardware buttons for Windows 8 tablet and convertible devices](http://go.microsoft.com/fwlink/p/?linkid=331284).

### Dock-sensing device

A dock-sensing device interrupts the system when a dock is attached or unattached from the system. This mode change information is used to update the user input and output experience, as required. The device's namespace requires:

-   A vendor-specific \_HID
-   A \_CID of PNP0C70
-   A \_CRS with one ActiveBoth interrupt

    Interrupt cannot be wake-capable.

### Convertible PC sensing device

A convertible-PC-sensing device interrupts the system when a convertible PC switches from tablet to clamshell form factor. This mode change information is used to update the user input and output experience, as required. The device's namespace requires:

-   A vendor-specific \_HID
-   A \_CID of PNP0C60
-   A \_CRS with one ActiveBoth interrupt

    Interrupt cannot be wake-capable.
