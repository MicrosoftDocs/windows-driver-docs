---
title: DevCon SetHwID
description: Adds, deletes, and changes the order of hardware IDs of root-enumerated devices on a local computer.
keywords:
- DevCon SetHwID Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon SetHwID
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon SetHwID

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See [Replacing DevCon](devcon-migration.md) for more information.

Adds, deletes, and changes the order of hardware IDs of root-enumerated devices.

``` console
devcon sethwid {* | ID [ID ...] | =class [ID [ID ...]]} := [ = | + | - | ! ]HardwareIDs ...
```

## Parameters

**\***

The asterisk represents all devices on the computer.

*ID*

Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

|Character|Description|
|--- |--- |
|**\***|Matches any character or no character. Use the wildcard character (*) to create an ID pattern, for example, *disk.|
|**@**|Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**.|
|**'**</br>(single quote)|Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID.|

**=***\<class\>*

Specifies the device setup class of the root-enumerated devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

*HardwareIDs*

Specifies one or more hardware IDs.

If the hardware IDs are not preceded by a symbol parameter (**+**, **-**, **=**, **!**), DevCon adds or moves the specified hardware IDs to the end of the list of hardware IDs for the device in the specified order. This is equivalent to the - parameter.

**=**

Replaces the list of hardware IDs for the device with the specified hardware IDs in the specified order.

**+**

Adds or moves the specified hardware IDs to the beginning of the list of hardware IDs for the device.

**-**

Adds or moves the specified hardware IDs to the end of the list of hardware IDs for the device.

**!**

Deletes the specified hardware IDs from the list of hardware IDs for the device.

## Comments

A *root-enumerated* device is a device that appears in the ROOT registry subkey (HKEY\_LOCAL\_MACHINE\\System\\*ControlSet*\\Enum\\ROOT).

You can specify multiple hardware IDs in each command. The **!** (delete) parameter applies only to the hardware ID that it prefixes. The other symbol parameters apply to all hardware IDs that follow until the next symbol parameter in the command.

DevCon moves, rather than adds, a hardware ID if the specified hardware ID already exists in the list of hardware IDs for the device.

The success message for a **DevCon SetHwIDs** command reports the number of devices (or device lists) in which it has modified hardware IDs, not the number of modified hardware IDs .

## Sample usage

``` console
devcon sethwid @ROOT\LEGACY* := legacy
devcon sethwid @ROOT\LEGACY_AFD\0000 := =afd1 afd2 afd3
devcon sethwid legacy := devtype3 -devtype4
devcon sethwid legacy afd1 := +devtype3
devcon sethwid @ROOT\LEGACY_BEEP\0000 := !beep legacy
```

## Examples

- [Example 40: Assign a hardware ID to a legacy device](devcon-examples.md#example-40-assign-a-hardware-id-to-a-legacy-device)
- [Example 41: Add a hardware ID to all legacy devices](devcon-examples.md#example-41-add-a-hardware-id-to-all-legacy-devices)
- [Example 42: Delete a hardware ID from all legacy devices](devcon-examples.md#example-42-delete-a-hardware-id-from-all-legacy-devices)
- [Example 43: Add, delete, and replace hardware IDs](devcon-examples.md#example-43-add-delete-and-replace-hardware-ids)
- [Example 44: Forcibly update the HAL](devcon-examples.md#example-44-forcibly-update-the-hal)
