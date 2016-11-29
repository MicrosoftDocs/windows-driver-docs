---
title: ComputerHardwareIds Output
description: ComputerHardwareIds Output
ms.assetid: 38a08dda-92db-4389-9c2c-91fe17a88051
---

# ComputerHardwareIds Output


The following is an example of the output produced by the ComputerHardwareIds tool:

```
Using the BIOS to gather information

## Computer Information
--------------------

BIOS Vendor: Contoso Inc.
BIOS Version string: A16
System BIOS Major Version: 6
System BIOS Minor Version: 0

System Manufacturer: Contoso Inc.
System Family: (null)
System ProductName: Contoso SYS01

Enclosure Type: Portable


Hardware IDs
------------
{346511cf-ccee-5c6d-8ee9-3c70fc7aae83}    <- Manufacturer + Family + ProductName + BIOS Vendor + BIOS Version + Major Version + Minor Version
{d7be59e5-29b5-589a-b49d-de7265ef6a7b}    <- Manufacturer + Family + ProductName
```

In this example, the vendor (Contoso Inc.) would typically use the second hardware ID (d7be59e5-29b5-589a-b49d-de7265ef6a7b) for the value of the [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) element in the [PackageInfo XML document](https://msdn.microsoft.com/library/windows/hardware/ff549602) of the vendor's device metadata package.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20ComputerHardwareIds%20Output%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




