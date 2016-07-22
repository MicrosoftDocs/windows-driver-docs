---
title: Device Instance ID
description: A device instance ID is a system-supplied device identification string that uniquely identifies a device in the system. The Plug and Play (PnP) manager assigns a device instance ID to each device node (devnode) in a system's device tree.
ms.assetid: 578973f4-463f-4707-8dc3-dff27b3d3052
---

# Device Instance ID


A device instance ID is a system-supplied device identification string that uniquely identifies a device in the system. The Plug and Play (PnP) manager assigns a device instance ID to each device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in a system's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).

## <a href="" id="ddk-device-instance-ids-dg"></a>


The format of this string consists of an [instance ID](instance-ids.md) concatenated to a [device ID](device-ids.md), as follows:

`<device-ID>\<instance-specific-ID>`

The number of characters of a device instance ID, excluding a NULL-terminator, must be less than MAX\_DEVICE\_ID\_LEN. This constraint applies to the sum of the lengths of all the fields and "\\" field separator between the *device ID* and *instance-specific-ID* fields.

A device instance ID is persistent across system restarts.

The following is an example of an instance ID ("1&08") concatenated to a device ID for a PCI device:

`PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02\1&08`

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Instance%20ID%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




