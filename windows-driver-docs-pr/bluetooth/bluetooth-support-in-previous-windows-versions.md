---
title: Bluetooth version and profile support in previous Windows versions
description: Bluetooth version and profile support in previous Windows versions
ms.date: 03/07/2022
---

# Bluetooth version and profile support in previous Windows versions

> [!NOTE]
> Looking for drivers for your Bluetooth audio device? See [Fix connections to Bluetooth audio devices and wireless displays](https://go.microsoft.com/fwlink/p/?LinkID=623629).

> [!NOTE]
> For information about Bluetooth support in Windows 11, see [Bluetooth Support in Windows 11](general-bluetooth-support-in-windows.md).

## Which previous versions of Windows support Bluetooth wireless technology?

The following previous versions of Windows include in-box support for Bluetooth wireless technology:

- All SKUs of Windows 10
- All SKUs of Windows 8.1

The following previous versions of Windows **do not** have in-box support for Bluetooth wireless technology:

- All SKUs of Windows Server 2016
- All SKUs of Windows Server 2012 R2

Although these versions of Windows do not have in-box Bluetooth wireless technology support, third-party Bluetooth drivers might be available from independent hardware vendors (IHVs).

## Which Bluetooth versions do previous versions of Windows support?

Windows supports Bluetooth version 1.1 and later versions. Bluetooth version 2.1 radios and devices are backward compatible with earlier versions of Bluetooth.

Windows 8 is Bluetooth Smart Ready, it supports Bluetooth version 4.0, and is able to connect with Bluetooth Smart devices.

Windows support for different versions of the Bluetooth specification depends on the Windows version, as shown in the following table:

| Windows version                         | V 1.1 | V 2.0 | V 2.0 with EDR | V 2.1 | V 2.1 with EDR | V 4.0 | V 4.1 | V 5.1 |
|-----------------------------------------|-------|-------|----------------|-------|----------------|-------|-------|-------|
| Windows 10 (version 2004)               | X     | X     | X              | X     | X              | X     | X     | X     |
| Windows 8.1                             | X     | X     | X              | X     | X              | X     |       |       |

## What's new in Windows 10?

To learn more about the new features and hardware developer recommendations for the different versions of Windows 10, see [Bluetooth](/windows-hardware/design/component-guidelines/bluetooth) in the [Hardware component guidelines](/windows-hardware/design/component-guidelines/components) section.

## What's new in Windows 8.1?

Windows 8.1 includes the following enhancements to the Bluetooth stack and related software:

- Inbox radio management control for Bluetooth version 4.0 radios.
- Windows Runtime API support for [**RFCOMM**](/uwp/api/Windows.Devices.Bluetooth.Rfcomm) and [**GATT**](/uwp/api/Windows.Devices.Bluetooth.GenericAttributeProfile) protocol access.

## Which Bluetooth profiles have in-box support in previous versions of Windows?

### Windows 10 in-box Bluetooth profiles

Windows 10 (version 2004) supports Bluetooth version 5.1.

### Core specification

Windows 10 supports Bluetooth core specification 5.1, including the following:

| Profile or protocol                        | Abbreviation |
|--------------------------------------------|--------------|
| 4.0 Host Controller Interface              | HCI          |
| Attribute Protocol                         | ATT          |
| Generic Access Profile                     | GAP          |
| Generic Attribute Profile                  | GATT         |
| Logical Link Control and Adaption Protocol | L2CAP        |
| Service Discovery Protocol                 | SDP          |
| Security Manager Protocol                  | SMP          |

### GATT profiles and services

| Profile or service             | Abbreviation | Version |
|--------------------------------|--------------|---------|
| Device Information Service     | DIS          | 1.1     |
| HID over GATT Profile          | HOGP         | 1.0     |
| Scan Parameters Profile client | ScPP         | 2.1     |

### Traditional Bluetooth profiles and protocols

| Profile or protocol                         | Abbreviation | Version |
|---------------------------------------------|--------------|---------|
| Advanced Audio Distribution Profile         | A2DP         | 1.3.2   |
| Audio/Video Control Transport Protocol      | AVCTP        | 1.4     |
| Audio Video Distribution Transport Protocol | AVDTP        | 1.3     |
| A/V Remote Control Profile                  | AVRCP        | 1.6.2   |
| Bluetooth Network Encapsulation Protocol    | BNEP         | 1.0     |
| Device ID                                   | DID          | 1.3     |
| Dial Up Networking Profile                  | DUN          | 1.1     |
| Generic A/V Distribution Profile            | GAVDP        | 1.3     |
| Hands-Free Profile                          | HFP          | 1.7.2   |
| Hard Copy Replacement Profile 1.2           | HRCP         | 1.1     |
| Human Interface Device                      | HID          | 1.1     |
| Object Push Profile                         | OPP          | 1.1     |
| Personal Area Network Profile               | PAN          | 1.0     |
| Radio Frequency Communication               | RFCOMM       | 1.1     |
| Serial Port Profile                         | SPP          | 1.2     |

### Windows 8.1 in-box Bluetooth profiles

Because Windows 8.1 provides both kernel-mode and user-mode programming interfaces for their Bluetooth stacks, hardware and software vendors can implement additional profiles in both kernel mode and user mode. We encourage vendors that create such profiles to test their software by using the appropriate [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) test suites and have their software packages digitally signed

## Do users have to re-pair their Bluetooth devices after they upgrade a system to Windows 8.1?

If users upgrade from Windows 7 to Windows 8.1, they must perform a clean installation of Windows 8.1. In this situation, any Bluetooth software that the OEM provides must be re-installed and all devices must be re-paired. If users upgrade from Windows 8 to Windows 8.1, complex devices such as phones might require re pairing so that third-party drivers will reload. However, a simpler device such as a keyboard or a mouse does not require re-pairing.

Therefore, pairing information is preserved if users upgrade from Windows 8 to Windows 8.1 for some devices, primarily Bluetooth keyboards, mice, and audio devices. This ensures that customers are not required to use a wired keyboard and mouse to upgrade their Windows version. They can use their Bluetooth keyboard and mouse for the entire procedure.

## What programming interfaces were introduced in Windows 8.1?

Windows 8.1 introduces new Windows Runtime APIs for accessing the [**RFCOMM**](/uwp/api/Windows.Devices.Bluetooth.Rfcomm) (over standard Bluetooth) and [**GATT**](/uwp/api/Windows.Devices.Bluetooth.GenericAttributeProfile) (over Bluetooth Low Energy).

## See also

- [Bluetooth version and profile support in Windows 11](general-bluetooth-support-in-windows.md)
