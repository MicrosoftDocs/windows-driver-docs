---
title: Device Stacks for an ACPI Device
description: Device Stacks for an ACPI Device
MS-HAID:
- 'opregdg\_e6789f01-535e-440c-97f6-1eb80ae49345.xml'
- 'acpi.device\_stacks\_for\_an\_acpi\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f177d29f-eaf9-4126-8cb3-9355d977bfb0
keywords: ["ACPI devices WDK , device stacks", "device stacks WDK ACPI", "functional device objects WDK ACPI", "FDOs WDK ACPI", "filter DOs WDK ACPI", "root bus drivers WDK ACPI", "function drivers WDK ACPI , device stacks", "WDM function drivers WDK ACPI , device stacks"]
---

# Device Stacks for an ACPI Device


## <a href="" id="ddk-device-stacks-for-an-acpi-device-kg"></a>


This section describes the device stacks for an ACPI device that include an optional functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)) created by a vendor-supplied WDM function driver.

The system creates one of the two device stacks shown in the following figure for each device in the system's ACPI namespace.

![two diagrams illustrating, on the left, an acpi device stack with a filter do and, on the right, an acpi device stack without a filter do](images/acpidev1.png)

If an ACPI device is a hardware device integrated into the system board, the system creates a device stack with a bus filter device object (filter DO). The device's physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) is created by the system-supplied root bus driver and the ACPI driver creates a bus filter DO. The presence of the filter DO is transparent to other device objects above it in the device stack.

If the device is not a hardware device integrated into the system board, the ACPI driver enumerates the device and creates a PDO. In either case, a vendor can supply an optional FDO.

### System-Supplied Root Bus Driver and ACPI Driver

Microsoft supplies the root bus driver and the [ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493). On systems that have an ACPI BIOS, the HAL causes the ACPI driver to be loaded during system startup at the base of the device tree, where it acts as the interface between the operating system and the BIOS. The ACPI driver is transparent to other drivers.

### Vendor-Supplied Function Driver

A vendor can supply an optional WDM function driver for an ACPI device. The function driver implements the device's operation region and the related device-specific operation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Device%20Stacks%20for%20an%20ACPI%20Device%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




