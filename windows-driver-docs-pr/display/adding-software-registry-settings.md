---
title: Adding Software Registry Settings
description: Learn how to add software registry settings to the PnP software key in display driver INF files for proper device configuration.
keywords:
- INF files WDK display , software registry settings
- software registry settings WDK display
- registry WDK display
ms.date: 10/30/2025
ms.topic: concept-article
ai-usage: ai-assisted
---

# Adding Software Registry Settings

Display driver INF files must add all software-related registry settings to the Plug and Play (PnP) software key. The PnP software key (also called the driver key) stores driver-specific configuration data that persists across system restarts.

For display adapters, the software key is created under the Display adapter device class GUID `{4d36e968-e325-11ce-bfc1-08002be10318}`.

For more information, see [Plug and Play Registry Routines](../kernel/plug-and-play-registry-routines.md).

## Basic INF Structure

Display driver INF files are typically very large and complex, containing many sections for different architectures, device models, file copying, service installation, and more. The examples below show only the registry-related portions relevant to adding software settings to the PnP software key.

Your display driver INF file must include sections that define which registry settings to add. Here's a simplified fragment showing the basic structure:

```inf
[Xxx.Mfg]
"RADEON 8500/RADEON 8500LE (R200 LDDM)" = R200_R200, PCI\VEN_1002&DEV_514c&SUBSYS_003a1002

[R200_R200]
Include=msdv.inf
CopyFiles=R200.Miniport, R200.Display
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_R200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings
; ... many other directives omitted ...
```

This fragment shows:

- **[Xxx.Mfg]**: The manufacturer/models section that maps hardware IDs to install sections
- **[R200_R200]**: The DDInstall section that specifies what to install for this device
- **AddReg directives**: Reference sections that define which registry values to add
- **DelReg directive**: References sections that define which registry values to remove (for upgrade scenarios)

## Defining Registry Settings

The `AddReg` directives reference sections that contain the actual registry values. Here's an example showing what goes in the referenced sections. **Note**: A complete display driver INF would contain many additional registry values; these examples show only the most common software key settings:

```inf
[R200_SoftwareDeviceSettings]
HKR,, InstalledDisplayDrivers, %REG_MULTI_SZ%, R200umd
HKR,, UserModeDriverName, %REG_SZ%, %13%\R200umd.dll
HKR,, VgaCompatible, %REG_DWORD%, 0
HKR,, Acceleration.Level, %REG_DWORD%, 0
HKR,, CapabilityOverride, %REG_DWORD%, 0x8

[R200_R200_SoftwareDeviceSettings]
HKR,, VideoDebugLevel, %REG_DWORD%, 0
; ... device-specific settings ...
```

### Registry Value Format

Each registry entry follows this format:

```text
HKR, [subkey], value-name, flags, value
```

Where:

- **HKR**: Represents the hardware/software key root (the PnP software key)
- **subkey**: Optional subkey path (empty in most cases)
- **value-name**: The name of the registry value
- **flags**: Data type constant (like %REG_DWORD%, %REG_SZ%, %REG_MULTI_SZ%)
- **value**: The actual data to store

## Common Registry Settings

Display drivers typically set these registry values:

| Value Name | Type | Purpose |
|------------|------|---------|
| InstalledDisplayDrivers | REG_MULTI_SZ | List of user-mode driver DLL names (without .dll extension) |
| UserModeDriverName | REG_SZ | Path to the primary user-mode driver DLL |
| VgaCompatible | REG_DWORD | Indicates VGA compatibility (0 = not compatible, 1 = compatible) |
| Acceleration.Level | REG_DWORD | Graphics acceleration level (0 = full, 5 = none) |
| CapabilityOverride | REG_DWORD | Bitmask for overriding hardware capabilities |

## String Constants

Define the registry type constants in your INF file's [Strings] section:

```inf
[Strings]
REG_SZ = 0x00000000
REG_MULTI_SZ = 0x00010000
REG_DWORD = 0x00010001
```

## Multiple Devices Example

If your driver package supports multiple device models, use device-specific AddReg sections:

```inf
[Manufacturer]
%Contoso%=Contoso.Mfg, NTamd64

[Contoso.Mfg.NTamd64]
%Device1.DeviceDesc% = Device1_Install, PCI\VEN_1234&DEV_0001
%Device2.DeviceDesc% = Device2_Install, PCI\VEN_1234&DEV_0002

[Device1_Install]
CopyFiles = Miniport.Files, UMD.Files
AddReg = Common_Settings, Device1_Settings

[Device2_Install]
CopyFiles = Miniport.Files, UMD.Files
AddReg = Common_Settings, Device2_Settings

[Common_Settings]
HKR,, InstalledDisplayDrivers, %REG_MULTI_SZ%, ContosoUMD
HKR,, VgaCompatible, %REG_DWORD%, 0

[Device1_Settings]
HKR,, DeviceSpecificValue, %REG_DWORD%, 1

[Device2_Settings]
HKR,, DeviceSpecificValue, %REG_DWORD%, 2
```

## Best Practices

1. Use HKR for software settings: Always use HKR (not absolute paths) to ensure settings go to the correct PnP software key
2. Group common settings: Use shared AddReg sections for settings common across all device models
3. Use device-specific sections: Create separate AddReg sections for settings that differ between device models
4. Clean up on upgrade: Use DelReg sections to remove obsolete registry values when upgrading drivers
5. Document custom values: Add comments in your INF file explaining any vendor-specific or non-standard registry values

## See Also

- [INF AddReg Directive](../install/inf-addreg-directive.md)
- [INF DDInstall Section](../install/inf-ddinstall-section.md)
- [Opening a Device's Software Key](../install/opening-a-device-s-software-key.md)
