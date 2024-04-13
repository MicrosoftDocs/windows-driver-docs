---
title: System-Defined Device Setup Classes Reserved for System Use
description: System-Defined Device Setup Classes Reserved for System Use
ms.date: 12/14/2022
---

# System-Defined Device Setup Classes Reserved for System Use

> [!NOTE]
> If you're looking for info on pre-defined values to use for the `Class` and `ClassGuid` entries in the [Version Section](inf-version-section.md) of the driver's INF file, see [System-Defined Device Setup Classes Available to Vendors](system-defined-device-setup-classes-available-to-vendors.md).

The following classes and GUIDs should not be used to install devices (or drivers) on Windows 2000 or later versions of Windows:

**Adapter**<br/>
Class = Adapter<br/>
ClassGuid = {4d36e964-e325-11ce-bfc1-08002be10318}<br/>
This class is obsolete.

**APM**<br/>
Class = APMSupport<br/>
ClassGuid = {d45b1c18-c8fa-11d1-9f77-0000f805f530}<br/>
This class is reserved for system use.

<a href="" id="computer-"></a>**Computer**<br/>
Class = Computer<br/>
ClassGuid = {4d36e966-e325-11ce-bfc1-08002be10318}<br/>
This class is reserved for system use.

<a href="" id="decoders-"></a>**Decoders**<br/>
Class = Decoder<br/>
ClassGuid = {6bdd1fc2-810f-11d0-bec7-08002be2092f}<br/>
This class is reserved for future use.

**Host-side IEEE 1394 Kernel Debugger Support**<br/>
Class = 1394Debug<br/>
ClassGuid = {66f250d6-7801-4a64-b139-eea80a450b24}<br/>
This class is reserved for system use.

**IEEE 1394 IP Network Enumerator**<br/>
Class = Enum1394<br/>
ClassGuid = {c459df55-db08-11d1-b009-00a0c9081ff6}<br/>
This class is reserved for system use.

**No driver**<br/>
Class = NoDriver<br/>
ClassGuid = {4d36e976-e325-11ce-bfc1-08002be10318}<br/>
This class is obsolete.

<a href="" id="non-plug-and-play-drivers-"></a>**Non-Plug and Play Drivers**<br/>
Class = LegacyDriver<br/>
ClassGuid = {8ecc055d-047f-11d1-a537-0000f8753ed1}<br/>
This class is reserved for system use.

<a href="" id="other-devices-"></a>**Other Devices**<br/>
Class = Unknown<br/>
ClassGuid = {4d36e97e-e325-11ce-bfc1-08002be10318}<br/>
This class is reserved for system use. Enumerated devices for which the system cannot determine the type are installed under this class. Do not use this class if you are unsure in which class your device belongs. Either determine the correct device setup class or create a new class.

<a href="" id="printer-upgrade-"></a>**Printer Upgrade**<br/>
Class = PrinterUpgrade<br/>
ClassGuid = {4d36e97a-e325-11ce-bfc1-08002be10318}<br/>
This class is reserved for system use.

**Print Queue**<br/>
Class = PrintQueue<br/>
ClassGuid = {1ed2bbf9-11f0-4084-b21f-ad83a8e6dcdc}<br/>

**Software Device**<br/>
Class = SoftwareDevice<br/>
ClassGuid = {62f9c741-b25a-46ce-b54c-9bccce08b6f2}<br/>

**Audio Endpoint**<br/>
Class = AudioEndpoint<br/>
ClassGuid = {c166523c-fe0c-4a94-a586-f1a80cfbbf3e}<br/>

<a href="" id="sound-"></a>**Sound**<br/>
Class = Sound<br/>
ClassGuid = {4d36e97c-e325-11ce-bfc1-08002be10318}<br/>
This class is obsolete.

**Storage Volume Snapshots**<br/>
Class = VolumeSnapshot<br/>
ClassGuid = {533c5b84-ec70-11d2-9505-00c04F79deaf}<br/>
This class is reserved for system use.

**USB Bus Devices (hubs and host controllers)**<br/>
Class = USB<br/>
ClassGuid = {36fc9e60-c465-11cf-8056-444553540000}<br/>
This class includes USB host controllers and USB hubs, but not USB peripherals. Drivers for this class are system-supplied. Drivers for USB peripherals should use the appropriate class from [System-Defined Device Setup Classes Available to Vendors](./system-defined-device-setup-classes-available-to-vendors.md) that matches the functionality of the peripheral, or use the USBDevice class if no other class is a better fit.

 

 





