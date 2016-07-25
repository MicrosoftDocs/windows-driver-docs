---
title: Hardware ID
description: A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.assetid: 9eb894d6-4e83-4c08-8165-f30d6636da75
---

# Hardware ID


A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file. In most cases, a device has associated with it a list of hardware IDs. (However, there are exceptions − see [Identifiers for 1394 Devices](identifiers-for-1394-devices.md)). When an [*enumerator*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator) reports a list of hardware IDs for a device, the hardware IDs should be listed in order of decreasing suitability.

## <a href="" id="ddk-hardware-ids-dg"></a>


A hardware ID has one of the following generic formats:

<a href="" id="-enumerator---enumerator-specific-device-id-"></a>*&lt;enumerator&gt;\\&lt;enumerator-specific-device-ID&gt;*  
This is the most common format for individual PnP devices reported to the Plug and Play (PnP) manager by a single enumerator. New enumerators should use this format or the following format. For more information about enumerator-specific device IDs, see [Device Identifier Formats](device-identifier-formats.md).

<a href="" id="--generic-device-id-"></a>*\*&lt;generic-device-ID&gt;*  
The asterisk indicates that the device is supported by more than one enumerator, such as ISAPNP and the BIOS. For more information about this type of ID, see [Generic Identifiers](generic-identifiers.md).

<a href="" id="-device-class-specific-id-"></a>*&lt;device-class-specific-ID&gt;*  
An existing device class that has established its own naming convention might use a custom format. For information about their hardware ID formats, see the hardware specification for such buses. New enumerators should not use this format.

The number of characters of a hardware ID, excluding a NULL terminator, must be less than MAX\_DEVICE\_ID\_LEN. This constraint applies to the sum of the lengths of all the fields and any "\\" field separators in a hardware ID. For more information about constraints on device IDs, see the Operations section of [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679).

To obtain the list of hardware IDs for a device, call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) with the *DeviceProperty* parameter set to **DevicePropertyHardwareID**. The list of hardware IDs that this routine retrieves is a REG\_MULTI\_SZ value. The maximum number of characters in a hardware list, including a NULL terminator after each hardware ID and a final NULL terminator, is REGSTR\_VAL\_MAX\_HCID\_LEN. The maximum possible number of IDs in a list of hardware IDs is 64.

### Examples of Hardware IDs

In the following, the first example is a [generic identifier](generic-identifiers.md) for a PnP device, and the second example is an [identifier for a PCI device](identifiers-for-pci-devices.md):

root\\\*PNP0F08

PCI\\VEN\_1000&DEV\_0001&SUBSYS\_00000000&REV\_02

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Hardware%20ID%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




