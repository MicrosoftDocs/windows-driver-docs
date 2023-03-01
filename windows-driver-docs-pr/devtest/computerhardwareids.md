---
title: ComputerHardwareIds
description: To run ComputerHardwareIds, type a command at the command prompt in the WDK bin directory.
keywords:
- ComputerHardwareIds Overview Driver Development Tools
topic_type:
- apiref
api_name:
- ComputerHardwareIds Overview
api_type:
- NA
ms.date: 02/28/2023
---

# ComputerHardwareIds

ComputerHardwareIds (ComputerHardwareIds.exe) is a Windows Driver Kit (WDK) command-line tool that can be used to generate hardware IDs for a specific model of a vendor's computer system. The vendor can use these hardware IDs to match device metadata packages to that specific computer model.

The ComputerHardwareIds tool is supported on systems that run Windows 7 or later versions of the Windows operating system. This tool is included in the Windows Driver Kit (WDK) under the `bin` directory. There are separate versions for 32-bit Windows platforms (x86) and 64-bit Windows platforms (x64).

For information on downloading and installing the WDK, see [Download the Windows Driver Kit (WDK)](/windows-hardware/drivers/download-the-wdk).

## Run ComputerHardwareIds

To run ComputerHardwareIds, type the command at the command prompt.

```console
C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64>ComputerHardwareIds> ComputerHardwareIds
```

### Parameters

None  

## Comments

The ComputerHardwareIds tool creates hardware IDs for the computer based on information from fields in the System Management BIOS (SMBIOS) for the computer. For a list of the fields, see [Specifying Hardware IDs for a Computer](../install/specifying-hardware-ids-for-a-computer.md).

For more information about selecting hardware ID values for the computer as well as more information about device metadata packages, see [Specifying Hardware IDs for a Computer](../install/specifying-hardware-ids-for-a-computer.md).

## ComputerHardwareIds example output

The following is an example of the output produced by the ComputerHardwareIds tool.

```console
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

In this example, the vendor (Contoso Inc.) would typically use the second hardware ID (d7be59e5-29b5-589a-b49d-de7265ef6a7b) for the value of the [**HardwareID**](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) element in the [PackageInfo XML document](../install/packageinfo-xml-document.md) of the vendor's device metadata package.

For more information about the Windows Development Kit, see [Windows Driver Kit (WDK)](../index.yml).

For more information about device metadata packages, see [Device Metadata Packages](../install/overview-of-device-metadata-packages.md).

## See also

[Specifying Hardware IDs for a Computer](../install/specifying-hardware-ids-for-a-computer.md)

[Download the Windows Driver Kit (WDK)](/windows-hardware/drivers/download-the-wdk)
