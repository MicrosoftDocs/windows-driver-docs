---
title: Bluetooth version and profile support in Windows 11
description: Provides information about Bluetooth version and profile support in Windows 11
ms.date: 07/12/2023
content_well_notification: 
  - AI-contribution
---

# Bluetooth version and profile support in Windows 11

> [!NOTE]
> Looking for drivers for your Bluetooth audio device? See [Fix connections to Bluetooth audio devices and wireless displays](https://go.microsoft.com/fwlink/p/?LinkID=623629).

## Which Bluetooth versions does Windows 11 support?

Windows 11 version 22H2, all editions support Bluetooth Core Specification version 5.3.

Windows Server **does not** have in-box Bluetooth wireless technology support. Third-party Bluetooth drivers might be available from independent hardware vendors (IHVs).

## Which Bluetooth profiles have in-box support in Windows 11?

### Core specification

Windows 11 supports Bluetooth core specification 5.3, including the following:

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
| Basic Audio Profile                         | BAP          | 1.1     |
| Bluetooth Network Encapsulation Protocol    | BNEP         | 1.0     |
| Call Control Profile                        | CIP          | 1.1     |
| Common Audio Profile                        | CAP          | 1.1     |
| Coordinated Set Identification Profile      | CSIP         | 1.0     |
| Device ID                                   | DID          | 1.3     |
| Dial Up Networking Profile                  | DUN          | 1.1     |
| Generic A/V Distribution Profile            | GAVDP        | 1.3     |
| Hands-Free Profile                          | HFP          | 1.7.2   |
| Hard Copy Replacement Profile 1.2           | HRCP         | 1.1     |
| Hearing Access Profile                      | HAP          | 1.1     |
| Human Interface Device                      | HID          | 1.1.1   |
| Media Control Profile                       | MCP          | 1.1     |
| Microphone Control Profile                  | MCAP         | 1.1     |
| Object Push Profile                         | OPP          | 1.1     |
| Personal Area Network Profile               | PAN          | 1.0     |
| Radio Frequency Communication               | RFCOMM       | 1.1     |
| Serial Port Profile                         | SPP          | 1.2     |
| Telephony and Media Audio Profile           | TMAP         | 1.1     |
| Volume Control Profile                      | VCP          | 1.1     |

## New features and recommendations for Windows 11 version 22H2 and later

To learn more about the new features and hardware developer recommendations for the different versions of Windows 11, see [Bluetooth](/windows-hardware/design/component-guidelines/bluetooth) in the [Hardware component guidelines](/windows-hardware/design/component-guidelines/components) section.

## Related topics

- [Bluetooth Support in Previous Windows Versions](bluetooth-support-in-previous-windows-versions.md)
