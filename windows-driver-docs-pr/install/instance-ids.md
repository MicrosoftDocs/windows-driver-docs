---
title: Instance ID
description: An instance ID is a device identification string that distinguishes a device from other devices of the same type on a computer.
ms.assetid: 093063a6-1855-4e36-9465-1eedaa3cd0f9
---

# Instance ID


An instance ID is a device identification string that distinguishes a device from other devices of the same type on a computer. An instance ID contains serial number information, if supported by the underlying bus, or some kind of location information. The string cannot contain any "\\" characters; otherwise, the generic format of the string is bus-specific.

## <a href="" id="ddk-instance-ids-dg"></a>


The number of characters of an instance ID, excluding a NULL-terminator, must be less than MAX\_DEVICE\_ID\_LEN. In addition, when an instance ID is concatenated to a [device ID](device-ids.md) to create a device instance ID, the lengths of the device ID and the instance ID are further constrained by the maximum possible length of a device instance ID.

The **UniqueID** member of the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure for a device indicates if a bus-supplied instance ID is unique across the system, as follows:

-   If **UniqueID** is **FALSE**, the bus-supplied instance ID for a device is unique only to the device's bus. The Plug and Play (PnP) manager modifies the bus-supplied instance ID, and combines it with the corresponding device ID, to create a device instance ID that is unique in the system.

-   If **UniqueID** is **TRUE**, the device instance ID, formed from the bus-supplied device ID and instance ID, uniquely identifies a device in the system.

An instance ID is persistent across system restarts.

To obtain the bus-supplied instance ID for a device, use an [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) request and set the **Parameters.QueryId.IdType** member to **BusQueryInstanceID**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Instance%20ID%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




