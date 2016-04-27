---
title: Providing a Vendor-Defined ACPI Device Interface
description: Providing a Vendor-Defined ACPI Device Interface
MS-HAID:
- 'opregdg\_41ee73b4-351a-4bd0-9566-14b9ad69bd68.xml'
- 'acpi.providing\_a\_vendor\_defined\_acpi\_device\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5a7fd03b-6d4f-481b-8e4e-0e1deaf88583
keywords: ["ACPI devices WDK , device interfaces", "vendor-defined device interfaces WDK ACPI", "device interfaces WDK ACPI", "function drivers WDK ACPI , vendor-defined device interfaces", "WDM function drivers WDK ACPI , vendor-defined device interfaces"]
---

# Providing a Vendor-Defined ACPI Device Interface


## <a href="" id="ddk-providing-a-vendor-defined-acpi-device-interface-kg"></a>


A vendor can provide an optional [*device interface*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interface) and support for custom IOCTLs to operate an ACPI device's functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)).

The function driver typically calls [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) in its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine to register a device interface. The driver calls [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700) to enable the interface after Plug and Play starts the FDO. The driver should disable the interface if a device is removed by Plug and Play.

The device interface class GUID is vendor-defined.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Providing%20a%20Vendor-Defined%20ACPI%20Device%20Interface%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




