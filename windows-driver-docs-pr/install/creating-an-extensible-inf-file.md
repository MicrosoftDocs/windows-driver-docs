---
title: Using an Extension INF File
description: Starting in Windows 10 Mobile, you can extend a driver package INF file's functionality by providing an additional INF file called an extension INF.
ms.assetid: 124C4E58-7F06-46F5-B530-29A03FA75C0A
---

# Using an Extension INF File


Starting in Windows 10 Mobile, you can extend a driver package INF file's functionality by providing an additional INF file called an extension INF. An extension INF can supplement and, in some cases, override the configuration and settings of the primary INF. Multiple extension INFs can be associated with the same device. Extension INFs and the primary INF for a device can be developed and updated separately, by independent organizations.

An extension INF must be a universal driver package INF file. You can use extension INFs only with Windows 10 Mobile.

To associate an extension INF with a device, provide a [**\[Models\]**](inf-models-section.md) section that specifies the device IDs to which the extension INF applies.

Typically, an extension INF lists a more specific hardware ID than the primary INF, with the goal of further specializing a specific driver configuration. However, the extension INF might list the same hardware ID as the primary INF, for instance if the device is already very narrowly targeted, or if the primary INF already lists the most specific hardware ID. In some cases, the extension INF might provide a less specific device ID, like a compatible ID, in order to customize a setting across a broader set of devices.

## How extension INF and primary INF work together


Settings in an extension INF are applied after settings in a primary INF. As a result, if an extension INF and a primary INF specify the same setting, the version in the extension INF is applied. Similarly, if the primary INF changes, the extension INF remains and is applied over the new primary INF.

For example, Company A manufactures a component that is included in a device that Company B produces. Company A provides a primary INF for the component, and Company B provides an extension INF for the device. The extension INF might modify some of the settings, such as customizing the device friendly name, modifying a hardware configuration setting, or adding a filter driver.

## Specifying ExtensionId


When you write an extension INF, you generate a special GUID called the **ExtensionId**, which is an entry in the INF's **\[Version\]** section. The following guidelines apply:

-   For a given device, only one extension INF is installed for each unique **ExtensionId** value. Driver date and driver version are the tiebreakers, in that order, between multiple extension INFs with the same **ExtensionId**.
-   For multiple extension INFs to be applied to the same device, each extension INF must have a unique **ExtensionId**.

In addition to the primary INF selected for installation of a given device, Plug and Play (PnP) identifies any extension INFs that apply to a given device by matching the hardware ID and compatible IDs of the device to those specified in the [**\[Manufacturer\]**](inf-manufacturer-section.md) section of the extension INF. For each extension INF that specifies a unique **ExtensionId** value, PnP selects the best match and applies its settings over those of the primary INF.

To illustrate, let's consider a hypothetical device for which there are four extension INFs. Two extension INFs have the same **ExtensionId** value, and two have unique **ExtensionId** values. From the first two, the one with the most recent driver date is selected. If driver date is the same, driver version is the next tiebreaker. From the latter two, both are selected, because they have unique **ExtensionId** values. In this example, the system applies the primary INF for the device, and then applies three extension INFs for that device.

## Creating an extension INF


Here are the entries you need to define an INF as an extension INF.

1.  Specify these values for **Class** and **ClassGuid** in the [**\[Version\]**](inf-version-section.md) section.

    ```
    [Version]
    ...
    Class       = Extension
    ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
    ```

2.  Provide an **ExtensionId** entry in the [**\[Version\]**](inf-version-section.md) section. Generate a new GUID for the initial version of an extension INF, or reuse the last GUID for subsequent updates of the initial extension INF.

    ```
    ExtensionId = {028b4317-f2e4-4fb2-80af-aaac8c07e98e} ; Example GUID
    ```

3.  If you are updating an extension INF, keep the **ExtensionId** the same and increment the version or date (or both) specified by the [**DriverVer**](inf-driverver-directive.md) directive. For a given **ExtensionId** value, PnP selects the INF with the highest **DriverVer**.

4.  In the [**INF \[Models\] section**](inf-models-section.md), specify one or more hardware and compatible IDs that match the target device. Note that these hardware and compatible IDs do not need to match those of the primary INF.

    ```
    [DeviceExtensions.NTamd64]
    %Device.ExtensionDesc% = DeviceExtension_Install, USB\VID_XXXX&PID_XXXX&REV_XXXX
    ```

5.  Optionally, provide a **\[TargetComputers\]** section if you want to constrain which computers this INF can be installed on. You might do this if you are using extension INFs with less specific hardware IDs or compatible IDs that are applicable to a large number of devices.
6.  Do not define a service with SPSVCINST\_ASSOCSERVICE. However, an extension INF can define other services, such as a filter driver for the device. For more info about specifying services, see [**INF AddService Directive**](inf-addservice-directive.md).

## Example 1: Using an extension INF to set the device friendly name


The following snippet is a complete extension INF that shows how to set the device friendly name.

```
[Version]
Signature   = "$WINDOWS NT$"
Class       = Extension
ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
Provider    = %CONTOSO%
ExtensionId = {028b4317-f2e4-4fb2-80af-82ac8c07e98e}
DriverVer   = 05/28/2013,1.0.0.0
CatalogFile = delta.cat

[Manufacturer]
%CONTOSO% = DeviceExtensions,NTamd64

[DeviceExtensions.NTamd64]
%Device.ExtensionDesc% = DeviceExtension_Install, USB\VID_XXXX&PID_XXXX&REV_XXXX

[DeviceExtension_Install]
; No changes

[DeviceExtension_Install.HW]
AddReg = FriendlyName_AddReg

[FriendlyName_AddReg]
HKR,,FriendlyName,, "New Device Friendly Name"

[Strings]
CONTOSO              = "Contoso"
Device.ExtensionDesc = "Sample Device Extension"
```

## Example 2: Filter Drivers


You can also use an extension INF to install a filter driver for a device that uses system-supplied device drivers. The extension INF specifies the hardware ID of the device, and provides the service and filter driver settings.

The following code snippet shows how to use an extension INF to install a filter driver.

```
[Version]
Signature   = "$WINDOWS NT$"
Class       = Extension
ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
Provider    = %CONTOSO%
ExtensionId = {2485f42e-81f0-43d8-bb48-01f3007c43f1}
DriverVer   = 05/28/2013,1.0.0.0
CatalogFile = delta.cat

[Manufacturer]
%CONTOSO% = DeviceExtensions,NTx86

[DeviceExtensions.NTx86]
%Device.ExtensionDesc% = DeviceExtension_Install,USB\VID_XXXX&PID_XXXX&REV_XXXX

[DeviceExtension_Install]
CopyFiles = Filter_CopyFiles

[DeviceExtension_Install.HW]
AddReg = DeviceExtensionFilter_AddReg

[DeviceExtensionFilter_AddReg]
HKR,,"UpperFilters",0x00010008,"fltsample" 

[DeviceExtension_Install.Services]
AddService = fltsample,,FilterService_Install

[FilterService_Install]
DisplayName   = %FilterSample.ServiceDesc%
ServiceType   = 1   ; SERVICE_KERNEL_DRIVER
StartType     = 3   ; SERVICE_DEMAND_START
ErrorControl  = 1   ; SERVICE_ERROR_NORMAL
ServiceBinary = %12%\fltsample.sys

[Filter_CopyFiles]
fltsample.sys

[SourceDisksFiles]
fltsample.sys = 1

[SourceDisksNames]
1 = Disk

[DestinationDirs]
Filter_CopyFiles = 12

[Strings]
CONTOSO                  = "Contoso"
Device.ExtensionDesc     = "Sample Extension Device"
FilterSample.ServiceDesc = "Sample Upper Filter"
```

## Related topics


[Using a Universal INF File](using-a-configurable-inf-file.md)

[Getting Started with Universal Drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers)

 

 






