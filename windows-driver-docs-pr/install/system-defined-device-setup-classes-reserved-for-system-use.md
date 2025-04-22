---
title: System-Defined Device Setup Classes Reserved for System Use
description: A list of system-defined device setup classes reserved for Windows system use.
ms.date: 05/31/2024
ms.topic: concept-article
---

# System-defined device setup classes reserved for system use

> [!NOTE]
> If you're looking for info on predefined values to use for the `Class` and `ClassGuid` entries in the [Version Section](inf-version-section.md) of the driver's setup information (INF) file, see [System-Defined Device Setup Classes Available to Vendors](system-defined-device-setup-classes-available-to-vendors.md).

Don't use the following classes and GUIDs to install devices or drivers on Windows 2000 or later versions of Windows:

| Driver or device | Class | ClassGuid | Remarks |
|--|--|--|--|
| **Adapter** | Adapter | {4d36e964-e325-11ce-bfc1-08002be10318} | This class is obsolete. |
| **APM** | APMSupport | {d45b1c18-c8fa-11d1-9f77-0000f805f530} | This class is reserved for system use. |
| **Computer** | Computer | {4d36e966-e325-11ce-bfc1-08002be10318} | This class is reserved for system use. |
| **Decoders** | Decoder | {6bdd1fc2-810f-11d0-bec7-08002be2092f} | This class is reserved for future use. |
| **Host-side IEEE 1394 Kernel Debugger Support** | 1394Debug | {66f250d6-7801-4a64-b139-eea80a450b24} | This class is reserved for system use. |
| **IEEE 1394 IP Network Enumerator** | Enum1394 | {c459df55-db08-11d1-b009-00a0c9081ff6} | This class is reserved for system use. |
| **No driver** | NoDriver | {4d36e976-e325-11ce-bfc1-08002be10318} | This class is obsolete. |
| **Non-Plug and Play Drivers** | LegacyDriver | {8ecc055d-047f-11d1-a537-0000f8753ed1} | This class is reserved for system use. |
| **Other Devices** | Unknown | {4d36e97e-e325-11ce-bfc1-08002be10318} | This class is reserved for system use. Enumerated devices for which the system can't determine the type are installed under this class. Don't use this class if you're unsure in which class your device belongs. Either determine the correct device setup class or create a new class. |
| **Printer Upgrade** | PrinterUpgrade | {4d36e97a-e325-11ce-bfc1-08002be10318} | This class is reserved for system use. |
| **Print Queue** | PrintQueue | {1ed2bbf9-11f0-4084-b21f-ad83a8e6dcdc} | &nbsp; |
| **Software Device** | SoftwareDevice | {62f9c741-b25a-46ce-b54c-9bccce08b6f2} | &nbsp; |
| **Audio Endpoint** | AudioEndpoint | {c166523c-fe0c-4a94-a586-f1a80cfbbf3e} | &nbsp; |
| **Sound** | Sound | {4d36e97c-e325-11ce-bfc1-08002be10318} | This class is obsolete. |
| **Storage Volume Snapshots** | VolumeSnapshot | {533c5b84-ec70-11d2-9505-00c04F79deaf} | This class is reserved for system use. |
| **USB Bus Devices (hubs and host controllers)** | USB | {36fc9e60-c465-11cf-8056-444553540000} | This class includes USB host controllers and USB hubs, but not USB peripherals. Drivers for this class are provided by the operating system. Drivers for USB peripherals should use the appropriate class from [System-Defined Device Setup Classes Available to Vendors](./system-defined-device-setup-classes-available-to-vendors.md) that matches the functionality of the peripheral, or use the **USBDevice** class if no other class is a better fit. |
