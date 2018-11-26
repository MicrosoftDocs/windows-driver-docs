---
title: Device management namespace objects
description: The ACPI 5.0 specification defines several types of namespace objects that can be used to manage devices.
ms.assetid: 26C3312D-B1B0-4843-BF4E-1B03630C0BDD
ms.date: 06/26/2018
ms.localizationpriority: medium
---

# Device management namespace objects


The [ACPI 5.0 specification](https://www.uefi.org/specifications) defines several types of namespace objects that can be used to manage devices. For example, device identification objects contain identification information for devices that connect to buses, such as I2C, that do not support hardware enumeration of child devices. Other types of namespace objects can specify system resources, describe device dependencies, and indicate which devices can be disabled.

## Device identification in Windows


Windows Plug and Play finds and loads device drivers based on a device identifier provided by the enumerator of the device. Enumerators are bus drivers that know how to extract identification information from the device. Some buses (such as PCI, SD, and USB) have hardware-defined mechanisms to do this extraction. For buses that do not (such as the processor bus or a simple peripheral bus), ACPI defines identification objects in the namespace.

The [Windows ACPI driver](https://docs.microsoft.com/windows-hardware/drivers/kernel/acpi-driver), Acpi.sys, assembles the values found in these objects into a variety of device identifier strings that can identify a device very specifically, or quite generically, depending on the needs of the driver. Some of the string patterns created to identify ACPI-enumerated devices are:

```syntax
ACPI\VEN_vvv[v]&DEV_dddd&SUBSYS_sss[s]nnnn&REV_rrrr
ACPI\VEN_vvv[v]&DEV_dddd&SUBSYS_sss[s]nnnn
ACPI\VEN_vvv[v]&DEV_dddd&REV_rrrr
ACPI\VEN_vvv[v]&DEV_dddd
ACPI\vvv[v]dddd
```

You can see the device identifiers that Windows creates for your device by opening Device Manager and inspecting the **Hardware IDs** and **Compatible IDs** properties of the enumerated device. Each of these strings is available to be specified in an INF file to identify the driver to load for the device. The order of INF matching is from the most specific hardware identifier (most preferred driver) to the least specific identifier (least preferred driver), so that drivers that know more about the specific features of the device can replace those that are less specific (and therefore support only a subset of the device features).

Device identifiers should be used for INF matching only, and should never be parsed or processed by the device driver. If the device driver has a need to identify the specific hardware it was loaded for, the recommended method is to have the INF file set appropriate registry keys at install time. The driver can then access these keys during initialization to obtain the required information.

## Device identification in ACPI


### Hardware ID (\_HID)

The minimum requirement for identifying a device in ACPI is the Hardware ID (\_HID) object. \_HID returns a string with the format of "ABC\[D\]*xxxx*", where "ABC\[D\]" is a 3- or 4-character string that identifies the manufacturer of the device (the "Vendor ID"), and *xxxx* is a hexadecimal number that identifies the specific device manufactured by that vendor (the "Device ID"). Vendor IDs must be unique across the industry. Microsoft allocates these strings to ensure that they are unique. Vendor IDs can be obtained from [Plug and Play ID - PNPID Request](http://go.microsoft.com/fwlink/p/?linkid=330999).

**Note**  ACPI 5.0 also supports the use of PCI-assigned vendor IDs in \_HID and other identification objects, so you might not need to get a vendor ID from Microsoft. For more information about hardware identification requirements, see section 6.1.5, "\_HID (Hardware ID)", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).



### Compatible ID (\_CID)

Microsoft has reserved the vendor ID "PNP" for devices that are compatible with inbox drivers shipped with Windows. Windows defines a number of device IDs for use with this vendor ID that can be used to load the Windows-provided driver for a device. A separate object, the Compatible ID (\_CID) object, is used to return these identifiers. Windows always prefers Hardware IDs (returned by \_HID) over Compatible IDs (returned by \_CID) in INF matching and driver selection. This preference allows the Windows-provided driver to be treated as a default driver if a vendor-provided device-specific driver is not available. The Compatible IDs in the following table are newly created for use with SoC platforms.

| Compatible ID | Description                                           |
|---------------|-------------------------------------------------------|
| PNP0C40       | Windows-compatible button array                       |
| PNP0C50       | HID-over-I²C compliant device                         |
| PNP0C60       | Convertible laptop display sensor device              |
| PNP0C70       | Dock sensor device                                    |
| PNP0D10       | XHCI-compliant USB controller with standard debug     |
| PNP0D15       | XHCI-compliant USB controller without standard debug  |
| PNP0D20       | EHCI-compliant USB controller without standard debug  |
| PNP0D25       | EHCI-compliant USB controller with standard debug     |
| PNP0D40       | SDA standard-compliant SD host controller             |
| PNP0D80       | Windows-compatible system power management controller |



### Subsystem ID (\_SUB), Hardware Revision (\_HRV), and Class (\_CLS)

ACPI 5.0 defines the \_SUB, \_HRV, and \_CLS objects that can be used along with the \_HID to create identifiers that more uniquely identify a specific version, integration, or hardware revision of a device, or to indicate membership in a PCI-defined device class. These objects are generally optional, but might be required by certain device classes in Windows. For more information about these objects, see section 6.1, "Device Identification Objects", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

For serviceability, there is a Windows Hardware Certification Kit (HCK) requirement that device IDs on OEM systems be "four-part" IDs. The four parts are the vendor ID, the device ID, the subsystem vendor (OEM) ID, and the subsystem (OEM) device ID. Therefore, the Subsystem ID (\_SUB) object is required for OEM platforms.

### Device-Specific Method (\_DSM)

The \_DSM method is defined in section 9.14.1, "\_DSM (Device Specific Method)", of the [ACPI 5.0 specification](https://www.uefi.org/specifications). This method provides for individual, device-specific data and control functions that can be called by a device driver without conflicting with other such device-specific methods. The \_DSM for a particular device or device class defines a UUID (GUID) that is guaranteed not to clash with other UUIDs. For each UUID, there is a set of defined functions that the \_DSM method can implement to provide data or to perform control functions for the driver. Class-specific data and data formats are provided in separate device-class-specific specifications, and are also discussed in [ACPI Device-Specific Methods](acpi-device-specific-methods.md).

### Address (\_ADR) and Unique ID (\_UID)

There are three additional requirements for device identification:

-   For devices that connect to a hardware-enumerable parent bus (for example, SDIO, USB HSIC), but that have platform-specific features or controls (for example, sideband power or wake interrupt), the \_HID is not used. Instead, the device identifier is created by the parent bus driver (as discussed previously). In this case, though, the Address Object (\_ADR) is required to be in the ACPI namespace for the device. This object enables the operating system to associate the bus-enumerated device with its ACPI-described features or controls.
-   On platforms where multiple instances of a particular IP block are used, so that each block has the same device identification objects, the Unique Identifier (\_UID) object is necessary to enable the operating system to distinguish between blocks.
-   No two devices in a particular namespace scope can have the same name.

## Device configuration objects


For each device identified in the namespace, the system resources (memory addresses, interrupts, and so on) consumed by the device must also be reported by the Current Resource Settings (\_CRS) object. Reporting of multiple possible resource configurations (\_PRS) and controls for changing a device's resource configuration (\_SRS) are supported but optional.

New for SoC platforms are GPIO and simple peripheral bus (SPB) resources that a device can consume. For more information, see [General Purpose I/O (GPIO)](general-purpose-i-o--gpio-.md) and [Simple Peripheral Bus (SPB)](simple-peripheral-bus--spb-.md).

Also new for SoC platforms is a general-purpose fixed DMA descriptor. The FixedDMA descriptor supports the sharing of DMA controller hardware by a number of system devices. The DMA resources (request line and channel registers) statically allocated to a particular system device are listed in the FixedDMA descriptor. For more information, see section 19.5.49, "FixedDMA (DMA Resource Descriptor Macro)", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

### Device status changes

ACPI-enumerated devices can be disabled or removed for a variety of reasons. The Status (\_STA) object is provided to enable such status changes to be communicated to the operating system. For a description of \_STA, see section 6.3.7 of the [ACPI 5.0 specification](https://www.uefi.org/specifications). Windows uses \_STA to determine if the device should be enumerated, shown as disabled, or not visible to the user. This control in the firmware is useful for many applications, including docking and USB OTG host-to-function switching.

Additionally, ACPI provides a notification mechanism that ASL can use to notify drivers of events in the platform, such as a device being removed as part of a dock. In general, when an ACPI device's status changes, the firmware must perform a "device check" or "bus check" notification to cause Windows to re-enumerate the device and re-evaluate its \_STA. For information about ACPI notifications, see section 5.6.6, "Device Object Notifications", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

## Enable/disable


As part of Windows Plug and Play, drivers must be capable of being dynamically enabled and disabled by the user or by the system (for example, for updating a driver).

On-SoC devices are integrated into the SoC chip and cannot be removed. Drivers for most on-SoC devices can be exempted from the requirements for enable and disable. For those drivers that are not exempt, there are driver interfaces for indicating that the driver supports orderly removal. For more information, see the document titled "Reducing PNP Requirements for SoC Drivers" on the [Microsoft Connect web site](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=47560).

If a driver supports orderly removal, and the device hardware can be disabled (that is, the device can be configured to stop accessing its assigned resources), then the ACPI namespace node for the device can include the Disable (\_DIS ) object. This method will be evaluated by the operating system whenever the driver is removed. Use of \_DIS has the following additional requirements:

-   \_STA must clear the "enabled and decoding its resources" bit whenever the device is disabled.
-   The device must provide the Set Resource Settings (\_SRS) object to re-enable the device hardware and set the above bit in \_STA.

For more information, see sections 6.2.3 (\_DIS), 6.2.15 (\_SRS), and 6.3.7 (\_STA) of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

## Device dependencies


Typically, there are hardware dependencies between devices on a particular platform. Windows requires that all such dependencies be described so that it can ensure that all devices function correctly as things change dynamically in the system (device power is removed, drivers are stopped and started, and so on). In ACPI, dependencies between devices are described in the following ways:

1.  **Namespace hierarchy**. Any device that is a child device (listed as a device within the namespace of another device) is dependent on the parent device. For example, a USB HSIC device is dependent on the port (parent) and controller (grandparent) it is connected to. Similarly, a GPU device listed within the namespace of a system memory-management unit (MMU) device is dependent on the MMU device.
2.  **Resource connections**. Devices connected to GPIO or SPB controllers are dependent on those controllers. This type of dependency is described by the inclusion of Connection Resources in the device's \_CRS.
3.  **OpRegion dependencies**. For ASL control methods that use OpRegions to perform I/O, dependencies are not implicitly known by the operating system because they are only determined during control method evaluation. This issue is particularly applicable to GeneralPurposeIO and GenericSerialBus OpRegions in which Plug and Play drivers provide access to the region. To mitigate this issue, ACPI defines the OpRegion Dependency (\_DEP) object. \_DEP should be used in any device namespace in which an OpRegion (HW resource) is referenced by a control method, and neither 1 nor 2 above already applies for the referenced OpRegion's connection resource. For more information, see section 6.5.8, "\_DEP (Operation Region Dependencies)", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

There can also be software dependencies between device drivers. These dependencies must also be described. For more information, see the following resources:

-   For driver-load-order dependencies, see [Specifying Driver Load Order](https://docs.microsoft.com/windows-hardware/drivers/install/specifying-driver-load-order).
-   For power-relations dependencies, see:

    -   [**IoInvalidateDeviceRelations**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioinvalidatedevicerelations) routine (To trigger establishing power relations, call the **IoInvalidateDeviceRelations** routine with the **DEVICE\_RELATION\_TYPE** enum value **PowerRelations**.)
    -   [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-device-relations)
    -   [Enumerating the Devices on a Bus](https://docs.microsoft.com/windows-hardware/drivers/wdf/enumerating-the-devices-on-a-bus)
    -   [Dynamic Enumeration](https://docs.microsoft.com/windows-hardware/drivers/wdf/dynamic-enumeration)
    -   [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks) method








