---
title: System-Defined Device Setup Classes Reserved for System Use
description: System-Defined Device Setup Classes Reserved for System Use
ms.assetid: 519a8833-8ed0-40c8-b7cb-a86f13191227
---

# System-Defined Device Setup Classes Reserved for System Use


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
This class includes USB host controllers and USB hubs, but not USB peripherals. Drivers for this class are system-supplied.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20System-Defined%20Device%20Setup%20Classes%20Reserved%20for%20System%20Use%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




