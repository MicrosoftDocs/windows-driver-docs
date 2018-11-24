---
title: INF Models Section
description: A Models section identifies a device, references its DDInstall section, and specifies a hardware identifier for the device.
ms.assetid: b870e8fb-21b4-439b-b858-c45bf9be2ec1
keywords:
- INF Models Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF Models Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Models Section


A per-manufacturer *Models* section identifies at least one device, references the *DDInstall* section of the INF file for that device, and specifies a unique-to-the-model-section [hardware identifier (ID)](hardware-ids.md) for that device.

Any entry in the per-manufacturer *Models* section can also specify one or more additional device IDs for models that are compatible with the device designated by the initial hardware ID and are controlled by the same drivers.

```cpp
[models-section-name] |
[models-section-name.TargetOSVersion]  (Windows XP and later versions of Windows)

device-description=install-section-name[,hw-id][,compatible-id...]
[device-description=install-section-name[,hw-id][,compatible-id]...] ...
```

## Entries


<a href="" id="device-description"></a>*device-description*  
Identifies a device to be installed, expressed as any unique combination of visible characters or as a **%**<em>strkey</em>**%** token defined in an [**INF Strings section**](inf-strings-section.md). The maximum length, in characters, of a device description is LINE_LEN.

<a href="" id="install-section-name"></a>*install-section-name*  
Specifies the undecorated name of the INF install sections to be used for the device (and compatible models of device, if any). For more information, see [**INF *DDInstall* Section**](inf-ddinstall-section.md).

<a href="" id="hw-id"></a>*hw-id*  
Specifies a vendor-defined [hardware ID](hardware-ids.md) string that identifies a device, which the PnP manager uses to find an INF-file match for this device. Such a hardware ID has one of the following formats:

<a href="" id="enumerator-enumerator-specific-device-id"></a>*enumerator\\enumerator-specific-device-id*  
Is the typical format for individual PnP devices reported to the PnP manager by a single enumerator. For example, `USB\VID_045E&PID_00B` identifies the Microsoft HID keyboard device on a USB bus. Depending on the enumerator, such a specification can even include the device's hardware revision number as, for example, `PCI\VEN_1011&DEV_002&SUBSYS_00000000&REV_02`.

<a href="" id="-enumerator-specific-device-id"></a>*\*enumerator-specific-device-id*  
Indicates with the asterisk (\*) that the device is supported by more than one enumerator. For example, `*PNP0F01` identifies the Microsoft serial mouse, which also has a compatible-id specification of `SERENUM\PNP0F01`.

<a href="" id="device-class-specific-id"></a>*device-class-specific-ID*  
Is an I/O bus-specific format, as described in the hardware specification for the bus, for the hardware IDs of all peripheral devices on that type of I/O bus.

Be aware that a single device can have more than one *hw-id* value. The PnP manager uses each such *hw-id* value, which is usually provided by the underlying bus when it enumerates its child devices, to create a subkey for each such device in the registry **Enum** branch. For manually installed devices, the system's setup code uses their *hw-id* values as specified in their respective INF files to create each such registry subkey.

<a href="" id="compatible-id"></a>*compatible-id*  
Specifies a vendor-defined [compatible ID](compatible-ids.md) string that identifies compatible devices. Any number of *compatible-id* values can be specified for an entry in the *Models* section, each separated from the next by a comma (**,**). All such compatible devices and/or device models are controlled by the same driver as the device designated by the initial *hw-id*.

Remarks
-------

Each *models-section-name* must be listed in the [**INF Manufacturer section**](inf-manufacturer-section.md) of the INF file. There can be one or more entries in any per-manufacturer *Models* section, depending on how many devices (and drivers) the INF file installs for a particular manufacturer.

Each *install-section-name* must be unique within the INF file and must follow the general rules for defining section names, described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md). The [***DDInstall***](inf-ddinstall-section.md) section name referenced in a per-manufacturer *Models* section can also have extensions appended to the given *install-section-name*, thus defining additional *DDInstall* sections for the OS-specific or platform-specific installation of the given devices. For more information about how to use extensions in cross-platform system files, see also [Creating an INF File](overview-of-inf-files.md).

Any specified *hw-id* or *compatible-id* value can also be specified in the [**INF ControlFlags section**](inf-controlflags-section.md) to prevent that device from being displayed to the end-user during manual installations. For more information about *hw-id* and *compatible-id* values, see [Device Identification Strings](device-identification-strings.md).

For each device and driver that is installed by using an INF file, the device installers use the information supplied in the [**INF Manufacturer section**](inf-manufacturer-section.md) and per-manufacturer *Models* sections to generate Device Description, Manufacturer Name, Device ID (if the installation is manual), and, possibly, Compatibility List value entries in the registry.

Starting with Windows XP, a *models section name* can include a *TargetOSVersion* decoration. For more information about this decoration, see [**INF Manufacturer Section**](inf-manufacturer-section.md).

**Important**  Starting with Windows Server 2003 SP1, INF files must decorate *models-section-name* entries in the INF **Manufacturer** section, along with the associated INF *Models* section names, with **.ntia64** or **.ntamd64** platform extensions to specify non-x86 target operating system versions. These platform extensions are not required in INF files for x86-based target operating system versions or non-PnP driver INF files (such as file system driver INF files for x64-based architectures). Each entry in a *Models* section is sometimes called a *driver node*.

 

Examples
--------

This example shows a per-manufacturer *Models* section with some representative entries from the system mouse class installer's INF file, defining the [***DDInstall***](inf-ddinstall-section.md) sections for some devices/models.

```cpp
[Manufacturer]
%StdMfg%    =StdMfg         ; (Standard types)
%MSMfg%     =MSMfg          ; Microsoft
; ... %otherMfg% omitted here

[StdMfg]  ; per-Manufacturer Models section 
  ; Std serial mouse
%*pnp0f0c.DeviceDesc%= Ser_Inst,*PNP0F0C,SERENUM\PNP0F0C,SERIAL_MOUSE
  ; Std InPort mouse
%*pnp0f0d.DeviceDesc%      = Inp_Inst,*PNP0F0D
; ... more StdMfg entries 
```

## See also


[**ControlFlags**](inf-controlflags-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[**Manufacturer**](inf-manufacturer-section.md)

[**Strings**](inf-strings-section.md)

 

 






