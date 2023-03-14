---
title: INF Models section
description: A Models section identifies a device, references its DDInstall section, and specifies a hardware identifier for the device.
keywords:
- INF Models Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF Models Section
api_type:
- NA
ms.date: 06/08/2022
---

# INF Models section

A per-manufacturer _Models_ section identifies at least one device, references the _DDInstall_ section of the INF file for that device, and specifies a unique-to-the-model-section Hardware identifier (ID) for that device.

Any entry in the per-manufacturer _Models_ section can also specify one or more additional device IDs for models that are compatible with the device designated by the initial hardware ID and are controlled by the same drivers.

```inf
[models-section-name] |
[models-section-name.TargetOSVersion]  (Windows XP and later versions of Windows)

device-description=install-section-name,[hw-id][,compatible-id...]
[device-description=install-section-name,[hw-id][,compatible-id]...] ...
```

> [!NOTE]
> INFs are required to specify at least one device ID for each entry in the models section.  This may be either a hardware ID or compatible ID.

## Entries

_device-description_  
Identifies a device to be installed, expressed as any unique combination of visible characters or as a **%**_strkey_**%** token defined in an [**INF Strings section**](inf-strings-section.md). The maximum length, in characters, of a device description is LINE_LEN.

_install-section-name_  
Specifies the undecorated name of the INF install sections to be used for the device (and compatible models of device, if any). For more information, see [**INF _DDInstall_ Section**](inf-ddinstall-section.md).

_hw-id_  
Specifies a vendor-defined [Hardware ID](hardware-ids.md) string that identifies a device, which the PnP manager uses to find an INF-file match for this device. Such a hardware ID has one of the following formats:

_enumerator\enumerator-specific-device-id_  
Is the typical format for individual PnP devices reported to the PnP manager by a single enumerator. For example, `USB\VID_045E&PID_00B` identifies the Microsoft HID keyboard device on a USB bus. Depending on the enumerator, such a specification can even include the device's hardware revision number as, for example, `PCI\VEN_1011&DEV_002&SUBSYS_00000000&REV_02`.

_*enumerator-specific-device-id_  
Indicates with the asterisk (*) that the device is supported by more than one enumerator. For example, `*PNP0F01` identifies the Microsoft serial mouse, which also has a compatible-id specification of `SERENUM\PNP0F01`.

_device-class-specific-ID_  
Is an I/O bus-specific format, as described in the hardware specification for the bus, for the hardware IDs of all peripheral devices on that type of I/O bus.

_compatible-id_  
Specifies a vendor-defined [compatible ID](compatible-ids.md) string that identifies compatible devices. Any number of _compatible-id_ values can be specified for an entry in the _Models_ section, each separated from the next by a comma (**,**). All such compatible devices and/or device models are controlled by the same driver as the device designated by the initial _hw-id_.

## Remarks

Each _models-section-name_ must be listed in the [**INF Manufacturer section**](inf-manufacturer-section.md) of the INF file. There can be one or more entries in any per-manufacturer _Models_ section, depending on how many devices (and drivers) the INF file installs for a particular manufacturer.

Each _install-section-name_ must be unique within the INF file and must follow the general rules for defining section names, described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md). The [**_DDInstall_**](inf-ddinstall-section.md) section name referenced in a per-manufacturer _Models_ section can also have extensions appended to the given _install-section-name_, thus defining additional _DDInstall_ sections for the OS-specific or platform-specific installation of the given devices. For more information about how to use extensions in cross-platform system files, see also [Creating an INF File](overview-of-inf-files.md).

Any specified _hw-id_ or _compatible-id_ value can also be specified in the [**INF ControlFlags section**](inf-controlflags-section.md) to prevent that device from being displayed to the end-user during manual installations. For more information about _hw-id_ and _compatible-id_ values, see [Device Identification Strings](device-identification-strings.md).

For each device and driver that is installed by using an INF file, the device installers use the information supplied in the [**INF Manufacturer section**](inf-manufacturer-section.md) and per-manufacturer _Models_ sections to generate Device Description, Manufacturer Name, Device ID (if the installation is manual), and, possibly, Compatibility List value entries in the registry.

A _models section name_ can include a _TargetOSVersion_ decoration. For more information about this decoration, see [**INF Manufacturer Section**](inf-manufacturer-section.md), specifically the Remarks section.

> [!IMPORTANT]
> Starting with Windows Server 2003 SP1, INF files must decorate _models-section-name_ entries in the INF **Manufacturer** section, along with the associated INF _Models_ section names, with platform extensions to specify non-x86 target operating system versions. These platform extensions are not required in INF files for x86-based target operating system versions but are recommended.

## Examples

This example shows a per-manufacturer _Models_ section with some representative entries from the system mouse class installer's INF file, defining the [**_DDInstall_**](inf-ddinstall-section.md) sections for some devices/models.

```inf
[Manufacturer]
%StdMfg% = StdMfg         ; (Standard types)
%MSMfg%  = MSMfg          ; Microsoft
; ... %otherMfg% omitted here

[StdMfg]  ; per-Manufacturer Models section 
  ; Std serial mouse
%*pnp0f0c.DeviceDesc%= Ser_Inst,*PNP0F0C,SERENUM\PNP0F0C,SERIAL_MOUSE
  ; Std InPort mouse
%*pnp0f0d.DeviceDesc%= Inp_Inst,*PNP0F0D
; ... more StdMfg entries 
```

## See also

[Hardware identifiers (HWIds)](hardware-ids.md)

[**ControlFlags**](inf-controlflags-section.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**Manufacturer**](inf-manufacturer-section.md)

[**Strings**](inf-strings-section.md)
