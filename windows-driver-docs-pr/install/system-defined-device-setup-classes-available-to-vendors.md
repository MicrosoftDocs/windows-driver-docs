---
title: System-Defined Device Setup Classes Available to Vendors
description: Use the following list to select the right predefined values to use for the `Class` and `ClassGuid` entries in the [Version Section](inf-version-section.md) of the driver's INF file.
ms.date: 09/10/2024
---

# System-defined device setup classes available to vendors

Use the following list to select the right predefined values to use for the **Class** and **ClassGuid** entries in the [Version Section](inf-version-section.md) of the driver's INF file.

> [!NOTE]
> If you're looking for info on reserved classes and GUIDs, see [System-Defined Device Setup Classes Reserved for System Use](system-defined-device-setup-classes-reserved-for-system-use.md).

To see how these entries appear in an INF file, check out [cdrom.inf](https://github.com/microsoft/Windows-driver-samples/blob/aaeca58c5e7b67740a603a3150db225670b42bb6/storage/class/cdrom/src/cdrom.inf#L7-L8) in the [Windows driver samples](https://github.com/microsoft/Windows-driver-samples) repo.

Unless otherwise noted, you can use entries in the following list to install device drivers on Windows 2000 and later.

> [!NOTE]
> If you're looking for info on troubleshooting a problem with a CD or DVD drive, see [The CD drive or the DVD drive does not work as expected](https://support.microsoft.com/topic/the-cd-drive-or-the-dvd-drive-does-not-work-as-expected-on-a-computer-that-is-running-windows-vista-445f227d-6dc3-1ffe-4eab-bbf1a717adcf).

## Device categories and class values

The following table shows the predefined values to use for the **Class** and **ClassGuid** entries in the [Version Section](inf-version-section.md) of the driver's INF file.

| Device category | Class | Class GUID | Notes |
|--|--|--|--|
| **Audio Processing Objects (APOs)** | AudioProcessingObject | 5989fce8-9cd0-467d-8a6a-5419e31529d4 | Includes Audio processing objects (APOs). For more info, see [Windows Audio Processing Objects](../audio/windows-audio-processing-objects.md). |
| **Battery Devices** | Battery | 72631e54-78a4-11d0-bcf7-00aa00b7b32a | Includes battery devices and UPS devices. |
| **Biometric Device** | Biometric | 53D29EF7-377C-4D14-864B-EB3A85769359 | (Windows Server 2003 and later versions of Windows) Includes all biometric-based personal identification devices. |
| **Bluetooth Devices** | Bluetooth | e0cbf06c-cd8b-4647-bb8a-263b43f0f974 | (Windows XP SP1 and later versions of Windows) Includes all Bluetooth devices. |
| **Camera Device** | Camera | ca3e7ab9-b4c3-4ae6-8251-579ef933890f | (Windows 10 version 1709 and later versions of Windows) Includes universal camera drivers. |
| **CD-ROM Drives** | CDROM | 4d36e965-e325-11ce-bfc1-08002be10318 | Includes CD-ROM drives, including SCSI CD-ROM drives. By default, the system's CD-ROM class installer also installs a system-supplied CD audio driver and CD-ROM changer driver as Plug and Play filters. |
| **Disk Drives** | DiskDrive | 4d36e967-e325-11ce-bfc1-08002be10318 | Includes hard disk drives. See also the HDC and SCSIAdapter classes. |
| **Display Adapters** | Display | 4d36e968-e325-11ce-bfc1-08002be10318 | Includes video adapters. Drivers for this class include display drivers and video miniport drivers. |
| **Extension INF** | Extension | e2f84ce7-8efa-411c-aa69-97454ca4cb57 | (Windows 10 and later versions of Windows) Includes all devices requiring customizations. For more information, see [Using an Extension INF File](./using-an-extension-inf-file.md). |
| **Floppy Disk Controllers** | FDC | 4d36e969-e325-11ce-bfc1-08002be10318 | Includes floppy disk drive controllers. |
| **Floppy Disk Drives** | FloppyDisk | 4d36e980-e325-11ce-bfc1-08002be10318 | Includes floppy disk drives. |
| **Hard Disk Controllers** | HDC | 4d36e96a-e325-11ce-bfc1-08002be10318 | Includes hard disk controllers, including ATA/ATAPI controllers but not SCSI and RAID disk controllers. |
| **Human Interface Devices (HID)** | HIDClass | 745a17a0-74d3-11d0-b6fe-00a0c90f57da | Includes interactive input devices that are operated by the system-supplied [HID class driver](../hid/hid-architecture.md). This includes USB devices that comply with the [USB HID Standard](../hid/hid-over-usb.md) and non-USB devices that use a HID minidriver. For more information, see [HIDClass Device Setup Class](../hid/minidriver-operations.md). See also the Keyboard or Mouse classes. |
| **IEEE 1284.4 Devices** | Dot4 | 48721b56-6795-11d2-b1a8-0080c72e74a2 | Includes devices that control the operation of multifunction IEEE 1284.4 peripheral devices. |
| **IEEE 1284.4 Print Functions** | Dot4Print | 49ce6ac8-6f86-11d2-b1e5-0080c72e74a2 | Includes Dot4 print functions. A Dot4 print function is a function on a Dot4 device and has a single child device, which is a member of the Printer device setup class. |
| **IEEE 1394 Devices That Support the 61883 Protocol** | 61883 | 7ebefbc0-3200-11d2-b4c2-00a0C9697d07 | Includes IEEE 1394 devices that support the IEC-61883 protocol device class. The 61883 component includes the *61883.sys* protocol driver that transmits various audio and video data streams over the 1394 bus. These currently include standard/high/low quality DV, MPEG2, DSS, and Audio. The IEC-61883 specifications define these data streams. |
| **IEEE 1394 Devices That Support the AVC Protocol** | AVC | c06ff265-ae09-48f0-812c-16753d7cba83 | Includes IEEE 1394 devices that support the AVC protocol device class. |
| **IEEE 1394 Devices That Support the SBP2 Protocol** | SBP2 | d48179be-ec20-11d1-b6b8-00c04fa372a7 | Includes IEEE 1394 devices that support the SBP2 protocol device class. |
| **IEEE 1394 Host Bus Controller** | 1394 | 6bdd1fc1-810f-11d0-bec7-08002be2092f | Includes 1394 host controllers connected on a PCI bus, but not 1394 peripherals. Drivers for this class are system-supplied. |
| **Imaging Device** | Image | 6bdd1fc6-810f-11d0-bec7-08002be2092f | Includes still-image capture devices, digital cameras, and scanners. |
| **IrDA Devices** | Infrared | 6bdd1fc5-810f-11d0-bec7-08002be2092f | Includes infrared devices. Drivers for this class include Serial-IR and Fast-IR NDIS miniports, but see also the Network Adapter class for other NDIS network adapter miniports. |
| **Keyboard** | Keyboard | 4d36e96b-e325-11ce-bfc1-08002be10318 | Includes all keyboards. That is, it must also be specified in the (secondary) INF for an enumerated child HID keyboard device. |
| **Media Changers** | MediumChanger | ce5939ae-ebde-11d0-b181-0000f8753ec4 | Includes SCSI media changer devices. |
| **Memory Technology Driver** | MTD | 4d36e970-e325-11ce-bfc1-08002be10318 | Includes memory devices, such as flash memory cards. |
| **Modem** | Modem | 4d36e96d-e325-11ce-bfc1-08002be10318 | Includes [modem devices](/previous-versions/windows/hardware/modem/ff542476(v=vs.85)). An INF file for a device of this class specifies the features and configuration of the device and stores this information in the registry. An INF file for a device of this class can also be used to install device drivers for a *controllerless modem* or a *software modem*. These devices split the functionality between the modem device and the device driver. For more information about modem INF files and Microsoft Windows Driver Model (WDM) modem devices, see [Overview of Modem INF Files](/previous-versions/windows/hardware/modem/ff542559(v=vs.85)) and [Adding WDM Modem Support](/previous-versions/windows/hardware/modem/ff541218(v=vs.85)). |
| **Monitor** | Monitor | 4d36e96e-e325-11ce-bfc1-08002be10318 | Includes display monitors. An INF for a device of this class installs no device drivers, but instead specifies the features of a particular monitor to be stored in the registry for use by drivers of video adapters. (Monitors are enumerated as the child devices of display adapters.)
| **Mouse** | Mouse | 4d36e96f-e325-11ce-bfc1-08002be10318 | Includes all mouse devices and other kinds of pointing devices, such as trackballs. That is, this class must also be specified in the (secondary) INF for an enumerated child HID mouse device. |
| **Multifunction Devices** | Multifunction | 4d36e971-e325-11ce-bfc1-08002be10318 | Includes combo cards, such as a PCMCIA modem and network card adapter. The driver for such a Plug and Play multifunction device is installed under this class and enumerates the modem and network card separately as its child devices. |
| **Multimedia** | Media | 4d36e96c-e325-11ce-bfc1-08002be10318 | Includes Audio and DVD multimedia devices, joystick ports, and full-motion video capture devices. |
| **Multiport Serial Adapters** | MultiportSerial | 50906cb8-ba12-11d1-bf5d-0000f805f530 | Includes intelligent multiport serial cards, but not peripheral devices that connect to its ports. It doesn't include unintelligent (16550-type) multiport serial controllers or single-port serial controllers (see the Ports class). |
| **Network Adapter** | Net | 4d36e972-e325-11ce-bfc1-08002be10318 | Consists of network adapter drivers. These drivers must either call [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) or [**NetAdapterCreate**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptercreate). Drivers that don't use NDIS or NetAdapter should use a different setup class. |
| **Network Client** | NetClient | 4d36e973-e325-11ce-bfc1-08002be10318 | Includes network and/or print providers. **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later. |
| **Network Service** | NetService | 4d36e974-e325-11ce-bfc1-08002be10318 | Includes network services, such as redirectors and servers. |
| **Network Transport** | NetTrans | 4d36e975-e325-11ce-bfc1-08002be10318 | Includes NDIS protocols CoNDIS stand-alone call managers, and CoNDIS clients, in addition to higher level drivers in transport stacks. |
| **PCI SSL Accelerator** | SecurityAccelerator | 268c95a1-edfe-11d3-95c3-0010dc4050a5 | Includes devices that accelerate secure socket layer (SSL) cryptographic processing. |
| **PCMCIA Adapters** | PCMCIA | 4d36e977-e325-11ce-bfc1-08002be10318 | Includes PCMCIA and CardBus host controllers, but not PCMCIA or CardBus peripherals. Drivers for this class are system-supplied. |
| **Ports (COM & LPT ports)** | Ports | 4d36e978-e325-11ce-bfc1-08002be10318 | Includes serial and parallel port devices. See also the MultiportSerial class. |
| **Printers** | Printer | 4d36e979-e325-11ce-bfc1-08002be10318 | Includes printers. |
| **Printers, Bus-specific class drivers** | PNPPrinters | 4658ee7e-f050-11d1-b6bd-00c04fa372a7 | Includes SCSI/1394-enumerated printers. Drivers for this class provide printer communication for a specific bus. |
| **Processors** | Processor | 50127dc3-0f36-415e-a6cc-4cb3be910b65 | Includes processor types. |
| **SCSI and RAID Controllers** | SCSIAdapter | 4d36e97b-e325-11ce-bfc1-08002be10318 | Includes SCSI HBAs (Host Bus Adapters) and disk-array controllers. |
| **Security Devices** | Securitydevices | d94ee5d8-d189-4994-83d2-f68d7d41b0e6 | (Windows 8.1, Windows 10) Includes [Trusted Platform Module](/windows/security/information-protection/tpm/trusted-platform-module-top-node) chips. A TPM is a secure cryptoprocessor that helps you with actions such as generating, storing, and limiting the use of cryptographic keys. Any new manufactured device must implement and enable TPM 2.0 by default. For more information, see [TPM Recommendations](/windows/security/information-protection/tpm/tpm-recommendations). |
| **Sensors** | Sensor | 5175d334-c371-4806-b3ba-71fd53c9258d | (Windows 7 and later versions of Windows) Includes sensor and location devices, such as GPS devices. |
| **Smart Card Readers** | SmartCardReader | 50dd5230-ba8a-11d1-bf5d-0000f805f530 | Includes smart card readers. |
| **Software Component** | SoftwareComponent | 5c4c3332-344d-483c-8739-259e934c9cc8 | (Windows 10 version 1703 and later versions of Windows) Includes virtual child device to encapsulate software components. For more information, see [Adding Software Components with an INF file](./using-a-component-inf-file.md). |
| **Storage Volumes** | Volume | 71a27cdd-812a-11d0-bec7-08002be2092f | Includes storage volumes as defined by the system-supplied logical volume manager and class drivers that create device objects to represent storage volumes, such as the system disk class driver. |
| **System Devices** | System | 4d36e97d-e325-11ce-bfc1-08002be10318 | Includes HALs, system buses, system bridges, the system ACPI driver, and the system volume manager driver. |
| **Tape Drives** | TapeDrive | 6d807884-7d21-11cf-801c-08002be10318 | Includes tape drives, including all tape miniclass drivers. |
| **USB Device** | USBDevice | 88BAE032-5A81-49f0-BC3D-A4FF138216D6 | USBDevice includes all USB devices that don't belong to another class. This class isn't used for USB host controllers and hubs; drivers for these devices are provided by the operating system and should use the **USB** class described in [System-Defined Device Setup Classes Reserved for System Use](./system-defined-device-setup-classes-reserved-for-system-use.md). |
| **Windows CE USB ActiveSync Devices** | WCEUSBS | 25dbce51-6c8f-4a72-8a6d-b54c2b4fc835 | Includes Windows CE ActiveSync devices. The WCEUSBS setup class supports communication between a personal computer and a device that is compatible with the Windows CE ActiveSync driver (generally, PocketPC devices) over USB. |
| **Windows Portable Devices (WPD)** | WPD | eec5ad98-8080-425f-922a-dabf3de3f69a | (Windows Vista and later versions of Windows) Includes WPD devices. |
