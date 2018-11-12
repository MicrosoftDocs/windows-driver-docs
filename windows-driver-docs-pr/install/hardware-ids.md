---
title: Hardware ID
description: A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.assetid: 9eb894d6-4e83-4c08-8165-f30d6636da75
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware ID


A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file. In most cases, a device has associated with it a list of hardware IDs. (However, there are exceptions − see [Identifiers for 1394 Devices](identifiers-for-1394-devices.md)). When an [*enumerator*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator) reports a list of hardware IDs for a device, the hardware IDs should be listed in order of decreasing suitability.




A hardware ID has one of the following generic formats:

<a href="" id="-enumerator---enumerator-specific-device-id-"></a>*&lt;enumerator&gt;\\&lt;enumerator-specific-device-ID&gt;*  
This is the most common format for individual PnP devices reported to the Plug and Play (PnP) manager by a single enumerator. New enumerators should use this format or the following format. For more information about enumerator-specific device IDs, see [Device Identifier Formats](device-identifier-formats.md).

<a href="" id="--generic-device-id-"></a>*\*&lt;generic-device-ID&gt;*  
The asterisk indicates that the device is supported by more than one enumerator, such as ISAPNP and the BIOS. For more information about this type of ID, see [Generic Identifiers](generic-identifiers.md).

<a href="" id="-device-class-specific-id-"></a>*&lt;device-class-specific-ID&gt;*  
An existing device class that has established its own naming convention might use a custom format. For information about their hardware ID formats, see the hardware specification for such buses. New enumerators should not use this format.

The number of characters of a hardware ID, excluding a NULL terminator, must be less than MAX_DEVICE_ID_LEN. This constraint applies to the sum of the lengths of all the fields and any "\\" field separators in a hardware ID. For more information about constraints on device IDs, see the Operations section of [**IRP_MN_QUERY_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679).

To obtain the list of hardware IDs for a device, call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) with the *DeviceProperty* parameter set to **DevicePropertyHardwareID**. The list of hardware IDs that this routine retrieves is a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value. The maximum number of characters in a hardware list, including a NULL terminator after each hardware ID and a final NULL terminator, is REGSTR_VAL_MAX_HCID_LEN. The maximum possible number of IDs in a list of hardware IDs is 64.

### Examples of Hardware IDs

In the following, the first example is a [generic identifier](generic-identifiers.md) for a PnP device, and the second example is an [identifier for a PCI device](identifiers-for-pci-devices.md):

root\\\*PNP0F08

PCI\\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02

 

 





