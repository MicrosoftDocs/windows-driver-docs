---
title: Removing Co-installers from Driver Packages
description: This page addresses common reasons for co-installers to be present in a driver package, and mechanisms to perform the same task without a co-installer.
ms.date: 03/27/2023
---

# Removing Co-installers from Driver Packages

> [!CAUTION]
> Starting in January 2023, [driver packages](../install/driver-packages.md) containing a co-installer are no longer signed by the [Hardware Developer Center portal](https://partner.microsoft.com/en-us/dashboard). For details of the requirement, please refer to [Windows Hardware Compatibility Program Specifications and Policies](/windows-hardware/design/compatibility/whcp-specifications-policies), specifically version 22H2 policies, section **Device.DevFund.INF.Declarative**.

This page addresses common reasons for co-installers to be present in a driver package, and offers mechanisms to perform the same task without a co-installer.

## WDF and WinUSB Co-installers

The WDF co-installer and WinUSB co-installer are not required on any system running Windows 10 and later. The WDF co-installer references can be removed without any additional work. The WinUSB co-installer references can be removed, and WinUSB should be referenced from the driver package INF using the Include and Needs directives.  
  
[WinUSB driver package guidance](../usbcon/winusb-installation.md)

## Installing software that presents user interface

Rather than launching an application during an installation, the application should be installed using an [AddSoftware](../install/inf-addsoftware-directive.md) directive in the [DDInstall.Software](../install/inf-ddinstall-software-section.md) section of the driver package INF. For additional details, see [Installing Associated Software](#installing-associated-software) below.

## Setting device friendly names

### INF File

A driver package INF can set the device friendly name as follows:
```
[DDInstall.HW]
AddReg = FriendlyName_AddReg

[FriendlyName_AddReg]
HKR,,FriendlyName,, "Device Friendly Name"
```

### Runtime

The friendly name can be set by the driver during the [Start IRP](../kernel/irp-mn-start-device.md) or the [PrepareHardware](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) phase by setting the [DEVPKEY_Device_FriendlyName](../install/devpkey-device-friendlyname.md) property with one of the following APIs:  

* [IoSetDevicePropertyData](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata)  
* [WdfAssignProperty](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)

## Other device settings/configurations:

When possible, the driver can change the device settings and configuration within the driver [Start IRP](../kernel/irp-mn-start-device.md) or the [PrepareHardware](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) phase. When modifying state at runtime, the driver should follow the [driver package isolation requirements](./driver-isolation.md). These requirements contain the guidance on driver configuration and state layout and help future-proof the driver by making it more resilient to external changes, easier to update, and more straightforward to install.
  
For settings and configuration that cannot be set within the driver itself, a driver package may also include user-mode runtime components that alter the settings and configuration. This can be a user-facing app or a Win32 service that updates the configuration. For info on how to include user-mode software for use with a device, see [Using a Component INF File](../install/using-a-component-inf-file.md).

If a persistent component such as a service is used, ensure that its functionality is necessary and cannot be performed in a less resource-intensive manner, such as within a driver package INF or within the driver itself. For info on how to ensure that a service only runs when relevant devices are connected, see [Service Triggers](/windows/win32/services/service-trigger-events), [Win32 services interacting with devices](../install/best-practices-win32services-interacting-with-devices.md), and [Registering for device interface notifications](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md). The service must also meet the latest requirements, for example passing [API Validator](./validating-windows-drivers.md#apivalidator).

## Installing Associated Software

The 'Componentized' portion of the [DCH driver requirements](../develop/dch-principles-best-practices.md) introduced a concept called the SoftwareComponent, which is a mechanism to decouple the install of a device driver from its associated software. When a software component is created by the INF, it will automatically create a child device that maps to the software component. This child device will exist for the purpose of installing the software associated to the parent device. This software can be installed and updated independently of the main device and driver.

Within a SoftwareComponent driver package INF, the recommended mechanism to install software is using an AddSoftware directive. This will trigger the download and installation of software from the Windows Store.  
  
* [SoftwareComponent](../install/using-a-component-inf-file.md)  
* [AddSoftware](../install/inf-addsoftware-directive.md)  
* [DCH Driver Package Sample](./dch-example.md)  
* [Pairing a driver with a UWP app](../install/pairing-app-and-driver-versions.md)

## Dependencies across drivers and devices

### Device start/enumeration ordering dependencies

To the extent possible, inter-device dependencies or start ordering requirements should be avoided.

For ACPI-enumerated devices, the dependency object (_DEP) may be used in the ACPI firmware to enforce device start ordering. For more info, see [Device Management Namespace](../bringup/device-management-namespace-objects.md).

Alternatively, the device stack can be created in such a way that there is a custom bus driver that enumerates the children in dependency order.

### Driver package install dependencies

The [CopyInf Directive](../install/inf-copyinf-directive.md) can be used to also install an additional driver package during the same install API call as another driver. The driver package passed to the install API will be installed before any CopyInf-referenced driver packages, but driver packages referenced by CopyInf are not guaranteed to be installed in any particular order.

## Configuring components from multiple vendors bundled in single driver package

Driver packages support a type of driver package INF called an extension INF. This is an INF file that is specifically designed to augment and extend the functionality of a "base" driver package INF. An extension may not supply the function driver for the device, but may otherwise use any other directives or write other settings for a device. During a driver installation, a single base driver package INF is selected using [driver ranking](../install/how-setup-ranks-drivers--windows-vista-and-later-.md) to provide the functionality for the device, then any extension INFs are selected for the device. For more info, see [Using an extension INF file](../install/using-an-extension-inf-file.md).
  
A common paradigm for utilizing extension driver package INFs is for the the hardware manufacturer to supply the base driver package INF, and for an OEM shipping that part inside a system to create an extension driver package INF that customizes it for that system.

## Installing/orchestrating firmware updates

Different firmware update mechanisms are recommended depending on the nature of the device being updated. Each of the following can be used to ship and install a firmware update via Windows Update.

### Non-removable

The UEFI firmware update platform is designed to update components of a system that cannot be removed, such as the system firmware. For more info, see [UEFI Firmware Update Platform](../bringup/windows-uefi-firmware-update-platform.md).

### Removable

For removable devices such as HID or USB devices, the CFU model allows for safe firmware updates. For more info, see [Component Firmware Update](../cfu/index.md).

### Custom Implementation

Alternatively, a custom driver can be written that updates the firmware of the device at the driver's discretion. For more info, see [Custom Firmware Updating Driver](../install/updating-device-firmware-using-windows-update.md).
