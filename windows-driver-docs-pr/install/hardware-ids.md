---
title: Hardware ID
description: A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.assetid: 9eb894d6-4e83-4c08-8165-f30d6636da75
ms.date: 04/20/2017
ms.localizationpriority: High
---

# Hardware ID


A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file. In most cases, a device has associated with it a list of hardware IDs. (However, there are exceptions − see Identifiers for 1394 Devices reports a list of hardware IDs for a device, the hardware IDs should be listed in order of decreasing suitability.




A hardware ID has one of the following generic formats:

`<enumerator>\\<enumerator-specific-device-ID>`

This is the most common format for individual PnP devices reported to the Plug and Play (PnP) manager by a single enumerator. New enumerators should use this format or the following format. For more information about enumerator-specific device IDs, see [Device Identifier Formats](device-identifier-formats.md).

`\*<generic-device-ID>`

The asterisk indicates that the device is supported by more than one enumerator, such as ISAPNP and the BIOS. For more information about this type of ID, see [Generic Identifiers](generic-identifiers.md).

`<device-class-specific-ID>`

## Selecting a hardware ID

Root enumerated devices sharing generic namespace such as `ROOT\SYSTEM` may cause conflicts and yellow-bang in device manager on OS upgrade.

To prevent this, use a unique namespace for each driver that includes a root enumerated device. For a USB or system device, instead of using `ROOT\USB` or `ROOT\SYSTEM”` use `ROOT\[COMPANYNAME]\[DEVICENAME]`.  In addition, the driver installer code should check to see if the devnode is already present and take any necessary corrective action before installing.

An existing device class that has established its own naming convention might use a custom format. For information about their hardware ID formats, see the hardware specification for such buses. New enumerators should not use this format.

The number of characters of a hardware ID, excluding a NULL terminator, must be less than MAX_DEVICE_ID_LEN. This constraint applies to the sum of the lengths of all the fields and any "\\" field separators in a hardware ID. For more information about constraints on device IDs, see the Operations section of [**IRP_MN_QUERY_ID**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-id).

## Obtaining the list of hardware IDs for a device

To obtain the list of hardware IDs for a device, call [**IoGetDeviceProperty**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdeviceproperty) with the *DeviceProperty* parameter set to **DevicePropertyHardwareID**. The list of hardware IDs that this routine retrieves is a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value. The maximum number of characters in a hardware list, including a NULL terminator after each hardware ID and a final NULL terminator, is REGSTR_VAL_MAX_HCID_LEN. The maximum possible number of IDs in a list of hardware IDs is 64.

## Examples of Hardware IDs

In the following, the first example is a [generic identifier](generic-identifiers.md) for a PnP device, and the second example is an [identifier for a PCI device](identifiers-for-pci-devices.md):

root\\\*PNP0F08

PCI\\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02





## See Also

[INF HardwareId Directive](https://docs.microsoft.com/windows-hardware/drivers/install/inf-hardwareid-directive)


