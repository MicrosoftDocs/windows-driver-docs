---
title: ComputerHardwareIds Output
description: ComputerHardwareIds Output
ms.assetid: 38a08dda-92db-4389-9c2c-91fe17a88051
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ComputerHardwareIds Output


The following is an example of the output produced by the ComputerHardwareIds tool:

```
Using the BIOS to gather information

## Computer Information

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

 

 





