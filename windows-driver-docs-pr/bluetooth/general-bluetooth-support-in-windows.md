---
title: Bluetooth Version and Profile Support - Windows 11
description: Get information about Bluetooth version and profile support in Windows 11, including profiles and protocols, core specifications, and GATT profiles and services.
ms.date: 07/14/2025
content_well_notification: 
  - AI-contribution
ai-usage: ai-assisted
ms.topic: overview
---

# Bluetooth version and profile support in Windows 11

This article describes Windows 11 support for Bluetooth versions, profiles, and protocols.

> [!NOTE]
> Looking for drivers for your Bluetooth audio device? You can find available options in [Fix Bluetooth problems in Windows](https://support.microsoft.com/windows/fix-bluetooth-problems-in-windows-723e092f-03fa-858b-5c80-131ec3fba75c).

## Supported Bluetooth versions

Windows 11 provides support for Bluetooth as follows:

- Windows 11 version 22H2, all editions support Bluetooth Core Specification version 5.3.

- Windows Server **doesn't** provide in-box support for Bluetooth wireless technology. Other Bluetooth drivers might be available from independent hardware vendors (IHVs).

## In-box support for Bluetooth profiles

The following Bluetooth profiles have in-box support in Windows 11.

### Core specification

Windows 11 supports Bluetooth core specification 5.3, including the following profiles and protocols:

| Profile or protocol                        | Abbreviation |
|--------------------------------------------|--------------|
| 4.0 Host Controller Interface              | HCI          |
| Attribute Protocol                         | ATT          |
| Generic Access Profile                     | GAP          |
| Generic Attribute Profile                  | GATT         |
| Host Controller Interface                  | HCI          |
| Logical Link Control and Adaption Protocol | L2CAP        |
| Service Discovery Protocol                 | SDP          |
| Security Manager Protocol                  | SMP          |

### GATT profiles and services

Windows 11 supports the following Generic ATTribute Profile (GATT) profiles and services:

| Profile or service               | Abbreviation | Version |
|----------------------------------|--------------|---------|
| Device Information Service       | DIS          | 1.1     |
| Generic Media Control Service    | GMCS         | 1.0     |
| Generic Telephone Bearer Service | GTBS         | 1.0     |
| HID over GATT Profile            | HOGP         | 1.0     |
| Scan Parameters Profile client   | ScPP         | 2.1     |

### Bluetooth profiles and protocols

Windows 11 version 22H2 supports Bluetooth version 5.3 and the following Bluetooth profiles and protocols:

| Profile or protocol                         | Abbreviation | Version |
|---------------------------------------------|--------------|---------|
| Advanced Audio Distribution Profile         | A2DP         | 1.3.2   |
| Audio/Video Control Transport Protocol      | AVCTP        | 1.4     |
| Audio Video Distribution Transport Protocol | AVDTP        | 1.3     |
| A/V Remote Control Profile                  | AVRCP        | 1.6.2   |
| Basic Audio Profile                         | BAP          | 1.0.1   |
| Bluetooth Network Encapsulation Protocol    | BNEP         | 1.0     |
| Call Control Profile                        | CCP          | 1.0     |
| Common Audio Profile                        | CAP          | 1.0     |
| Coordinated Set Identification Profile      | CSIP         | 1.0.1   |
| Device ID                                   | DID          | 1.3     |
| Dial Up Networking Profile                  | DUN          | 1.1     |
| Generic A/V Distribution Profile            | GAVDP        | 1.3     |
| Hands-Free Profile                          | HFP          | 1.7.2   |
| Hard Copy Replacement Profile 1.2           | HRCP         | 1.1     |
| Hearing Access Profile                      | HAP          | 1.0     |
| Human Interface Device                      | HID          | 1.1.1   |
| Media Control Profile                       | MCP          | 1.0     |
| Microphone Control Profile                  | MICP         | 1.0     |
| Object Push Profile                         | OPP          | 1.1     |
| Personal Area Network Profile               | PAN          | 1.0     |
| Radio Frequency Communication               | RFCOMM       | 1.1     |
| Serial Port Profile                         | SPP          | 1.2     |
| Telephony and Media Audio Profile           | TMAP         | 1.0     |
| Volume Control Profile                      | VCP          | 1.0     |

## New features and recommendations for recent versions

To learn about new features and hardware developer recommendations for recent Windows 11 versions, see [Bluetooth](/windows-hardware/design/component-guidelines/bluetooth) in the [Hardware component guidelines](/windows-hardware/design/component-guidelines/components) section.

## Related articles

- [Bluetooth version and profile support in previous Windows versions](bluetooth-support-in-previous-windows-versions.md)
