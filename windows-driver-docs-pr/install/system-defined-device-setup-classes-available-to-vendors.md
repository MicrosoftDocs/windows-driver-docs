---  
title: System-Defined Device Setup Classes Available to Vendors  
description: System-Defined Device Setup Classes Available to Vendors  
ms.assetid: d4b8a964-f843-4960-9077-46746af27a61
ms.date: 05/08/2018
ms.localizationpriority: medium
---  

# System-Defined Device Setup Classes Available to Vendors  
  
  
The following classes and GUIDs are defined by the operating system. Unless otherwise noted, these classes and GUIDs can be used to install devices (or drivers) on Windows 2000 and later versions of Windows:  
  
**Battery Devices**  
Class = Battery  
ClassGuid = {72631e54-78a4-11d0-bcf7-00aa00b7b32a}  
This class includes battery devices and UPS devices.  
  
**Biometric Device**  
Class = Biometric  
ClassGuid = {53D29EF7-377C-4D14-864B-EB3A85769359}  
(Windows Server 2003 and later versions of Windows) This class includes all biometric-based personal identification devices.  
  
**Bluetooth Devices**  
Class = Bluetooth  
ClassGuid = {e0cbf06c-cd8b-4647-bb8a-263b43f0f974}  
(Windows XP SP1 and later versions of Windows) This class includes all Bluetooth devices.  
  
**Camera Device**  
Class = Camera  
ClassGuid = {ca3e7ab9-b4c3-4ae6-8251-579ef933890f}  
(Windows 10 version 1709 and later versions of Windows) This class includes universal camera drivers.  
  
**CD-ROM Drives**  
Class = CDROM  
ClassGuid = {4d36e965-e325-11ce-bfc1-08002be10318}  
This class includes CD-ROM drives, including SCSI CD-ROM drives. By default, the system's CD-ROM class installer also installs a system-supplied CD audio driver and CD-ROM changer driver as Plug and Play filters.  
  
<a href="" id="disk-drives-"></a>**Disk Drives**  
Class = DiskDrive  
ClassGuid = {4d36e967-e325-11ce-bfc1-08002be10318}  
This class includes hard disk drives. See also the HDC and SCSIAdapter classes.  
  
**Display Adapters**  
Class = Display  
ClassGuid = {4d36e968-e325-11ce-bfc1-08002be10318}  
This class includes video adapters. Drivers for this class include display drivers and video miniport drivers.  
  
**Extension INF**  
Class = Extension  
ClassGuid = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}  
(Windows 10 and later versions of Windows) This class includes all devices requiring customizations. For more details, see [Using an Extension INF File](https://docs.microsoft.com/windows-hardware/drivers/install/using-an-extension-inf-file).  
  
<a href="" id="floppy-disk-controllers-"></a>**Floppy Disk Controllers**  
Class = FDC  
ClassGuid = {4d36e969-e325-11ce-bfc1-08002be10318}  
This class includes floppy disk drive controllers.  
  
**Floppy Disk Drives**  
Class = FloppyDisk  
ClassGuid= {4d36e980-e325-11ce-bfc1-08002be10318}  
This class includes floppy disk drives.  
  
<a href="" id="hard-disk-controllers-"></a>**Hard Disk Controllers**  
Class = HDC  
ClassGuid = {4d36e96a-e325-11ce-bfc1-08002be10318}  
This class includes hard disk controllers, including ATA/ATAPI controllers but not SCSI and RAID disk controllers.  
  
**Human Interface Devices (HID)**  
Class = HIDClass  
ClassGuid = {745a17a0-74d3-11d0-b6fe-00a0c90f57da}  
This class includes interactive input devices that are operated by the system-supplied [HID class driver](https://msdn.microsoft.com/library/windows/hardware/jj126193). This includes USB devices that comply with the [USB HID Standard](../hid/hid-over-usb.md) and non-USB devices that use a HID minidriver. For more information, see [HIDClass Device Setup Class](../hid/minidriver-operations.md). (See also the Keyboard or Mouse classes later in this list.)  
  
**IEEE 1284.4 Devices**  
Class = Dot4  
ClassGuid = {48721b56-6795-11d2-b1a8-0080c72e74a2}  
This class includes devices that control the operation of multifunction IEEE 1284.4 peripheral devices.  
  
**IEEE 1284.4 Print Functions**  
Class = Dot4Print  
ClassGuid = {49ce6ac8-6f86-11d2-b1e5-0080c72e74a2}  
This class includes Dot4 print functions. A Dot4 print function is a function on a Dot4 device and has a single child device, which is a member of the Printer device setup class.  
  
**IEEE 1394 Devices That Support the 61883 Protocol**  
Class = 61883  
ClassGuid = {7ebefbc0-3200-11d2-b4c2-00a0C9697d07}  
This class includes IEEE 1394 devices that support the IEC-61883 protocol device class.  
  
The 61883 component includes the *61883.sys* protocol driver that transmits various audio and video data streams over the 1394 bus. These currently include standard/high/low quality DV, MPEG2, DSS, and Audio. These data streams are defined by the IEC-61883 specifications.  
  
**IEEE 1394 Devices That Support the AVC Protocol**  
Class = AVC  
ClassGuid = {c06ff265-ae09-48f0-812c-16753d7cba83}  
This class includes IEEE 1394 devices that support the AVC protocol device class.  
  
**IEEE 1394 Devices That Support the SBP2 Protocol**  
Class = SBP2  
ClassGuid = {d48179be-ec20-11d1-b6b8-00c04fa372a7}  
This class includes IEEE 1394 devices that support the SBP2 protocol device class.  
  
<a href="" id="ieee-1394-host-bus-controller-"></a>**IEEE 1394 Host Bus Controller**  
Class = 1394  
ClassGuid = {6bdd1fc1-810f-11d0-bec7-08002be2092f}  
This class includes 1394 host controllers connected on a PCI bus, but not 1394 peripherals. Drivers for this class are system-supplied.  
  
<a href="" id="imaging-device-"></a>**Imaging Device**  
Class = Image  
ClassGuid = {6bdd1fc6-810f-11d0-bec7-08002be2092f}  
This class includes still-image capture devices, digital cameras, and scanners.  
  
**IrDA Devices**  
Class = Infrared  
ClassGuid = {6bdd1fc5-810f-11d0-bec7-08002be2092f}  
This class includes infrared devices. Drivers for this class include Serial-IR and Fast-IR NDIS miniports, but see also the Network Adapter class for other NDIS network adapter miniports.  
  
**Keyboard**  
Class = Keyboard  
ClassGuid = {4d36e96b-e325-11ce-bfc1-08002be10318}  
This class includes all keyboards. That is, it must also be specified in the (secondary) INF for an enumerated child HID keyboard device.  
  
**Media Changers**  
Class = MediumChanger  
ClassGuid = {ce5939ae-ebde-11d0-b181-0000f8753ec4}  
This class includes SCSI media changer devices.  
  
<a href="" id="memory-technology-driver-"></a>**Memory Technology Driver**  
Class = MTD  
ClassGuid = {4d36e970-e325-11ce-bfc1-08002be10318}  
This class includes memory devices, such as flash memory cards.  
  
<a href="" id="modem-"></a>**Modem**  
Class = Modem  
ClassGuid = {4d36e96d-e325-11ce-bfc1-08002be10318}  
This class includes [modem devices](https://msdn.microsoft.com/library/windows/hardware/ff542476). An INF file for a device of this class specifies the features and configuration of the device and stores this information in the registry. An INF file for a device of this class can also be used to install device drivers for a [*controllerless modem*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-controllerless-modem) or a [*software modem*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-modem). These devices split the functionality between the modem device and the device driver. For more information about modem INF files and Microsoft Windows Driver Model (WDM) modem devices, see [Overview of Modem INF Files](https://msdn.microsoft.com/library/windows/hardware/ff542559) and [Adding WDM Modem Support](https://msdn.microsoft.com/library/windows/hardware/ff541218).  
  
<a href="" id="monitor-"></a>**Monitor**  
Class = Monitor  
ClassGuid = {4d36e96e-e325-11ce-bfc1-08002be10318}  
This class includes display monitors. An INF for a device of this class installs no device driver(s), but instead specifies the features of a particular monitor to be stored in the registry for use by drivers of video adapters. (Monitors are enumerated as the child devices of display adapters.)  
  
<a href="" id="mouse-"></a>**Mouse**  
Class = Mouse  
ClassGuid = {4d36e96f-e325-11ce-bfc1-08002be10318}  
This class includes all mouse devices and other kinds of pointing devices, such as trackballs. That is, this class must also be specified in the (secondary) INF for an enumerated child HID mouse device.  
  
**Multifunction Devices**  
Class = Multifunction  
ClassGuid = {4d36e971-e325-11ce-bfc1-08002be10318}  
This class includes combo cards, such as a PCMCIA modem and netcard adapter. The driver for such a Plug and Play multifunction device is installed under this class and enumerates the modem and netcard separately as its child devices.  
  
<a href="" id="multimedia-"></a>**Multimedia**  
Class = Media  
ClassGuid = {4d36e96c-e325-11ce-bfc1-08002be10318}  
This class includes Audio and DVD multimedia devices, joystick ports, and full-motion video capture devices.  
  
**Multiport Serial Adapters**  
Class = MultiportSerial  
ClassGuid = {50906cb8-ba12-11d1-bf5d-0000f805f530}  
This class includes intelligent multiport serial cards, but not peripheral devices that connect to its ports. It does not include unintelligent (16550-type) multiport serial controllers or single-port serial controllers (see the Ports class).  
  
<a href="" id="network-adapter-"></a>**Network Adapter**  
Class = Net  
ClassGuid = {4d36e972-e325-11ce-bfc1-08002be10318}  
This class includes NDIS miniport drivers excluding Fast-IR miniport drivers, NDIS intermediate drivers (of virtual adapters), and CoNDIS MCM miniport drivers.  
  
<a href="" id="network-client-"></a>**Network Client**  
Class = NetClient  
ClassGuid = {4d36e973-e325-11ce-bfc1-08002be10318}  
This class includes network and/or print providers.  
  
**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.  
  
   
  
**Network Service**  
Class = NetService  
ClassGuid = {4d36e974-e325-11ce-bfc1-08002be10318}  
This class includes network services, such as redirectors and servers.  
  
<a href="" id="network-transport-"></a>**Network Transport**  
Class = NetTrans  
ClassGuid = {4d36e975-e325-11ce-bfc1-08002be10318}  
This class includes NDIS protocols CoNDIS stand-alone call managers, and CoNDIS clients, in addition to higher level drivers in transport stacks.  
  
**PCI SSL Accelerator**  
Class = SecurityAccelerator  
ClassGuid = {268c95a1-edfe-11d3-95c3-0010dc4050a5}  
This class includes devices that accelerate secure socket layer (SSL) cryptographic processing.  
  
<a href="" id="pcmcia-adapters-"></a>**PCMCIA Adapters**  
Class = PCMCIA  
ClassGuid = {4d36e977-e325-11ce-bfc1-08002be10318}  
This class includes PCMCIA and CardBus host controllers, but not PCMCIA or CardBus peripherals. Drivers for this class are system-supplied.  
  
<a href="" id="ports--com---lpt-ports--"></a>**Ports (COM & LPT ports)**  
Class = Ports  
ClassGuid = {4d36e978-e325-11ce-bfc1-08002be10318}  
This class includes serial and parallel port devices. See also the MultiportSerial class.  
  
<a href="" id="printers-"></a>**Printers**  
Class = Printer  
ClassGuid = {4d36e979-e325-11ce-bfc1-08002be10318}  
This class includes printers.  
  
**Printers, Bus-specific class drivers**  
Class = PNPPrinters  
ClassGuid = {4658ee7e-f050-11d1-b6bd-00c04fa372a7}  
This class includes SCSI/1394-enumerated printers. Drivers for this class provide printer communication for a specific bus.  
  
<a href="" id="processors-"></a>**Processors**  
Class = Processor  
ClassGuid = {50127dc3-0f36-415e-a6cc-4cb3be910b65}  
This class includes processor types.  
  
<a href="" id="scsi-and-raid-controllers-"></a>**SCSI and RAID Controllers**  
Class = SCSIAdapter  
ClassGuid = {4d36e97b-e325-11ce-bfc1-08002be10318}  
This class includes SCSI HBAs (Host Bus Adapters) and disk-array controllers.  
  
**Sensors**  
Class = Sensor  
ClassGuid = {5175d334-c371-4806-b3ba-71fd53c9258d}  
(Windows 7 and later versions of Windows) This class includes sensor and location devices, such as GPS devices.  
  
**Smart Card Readers**  
Class = SmartCardReader  
ClassGuid = {50dd5230-ba8a-11d1-bf5d-0000f805f530}  
This class includes smart card readers.  
  
**Software Component**  
Class = SoftwareComponent  
ClassGuid = {5c4c3332-344d-483c-8739-259e934c9cc8}  
(Windows 10 version 1703 and later versions of Windows) This class includes virtual child device to encapsulate software components. For more details, see [Adding Software Components with an INF file](https://docs.microsoft.com/windows-hardware/drivers/install/adding-software-components-with-an-inf-file).  
  
<a href="" id="storage-volumes-"></a>**Storage Volumes**  
Class = Volume  
ClassGuid = {71a27cdd-812a-11d0-bec7-08002be2092f}  
This class includes storage volumes as defined by the system-supplied logical volume manager and class drivers that create device objects to represent storage volumes, such as the system disk class driver.  
  
<a href="" id="system-devices-"></a>**System Devices**  
Class = System  
ClassGuid = {4d36e97d-e325-11ce-bfc1-08002be10318}  
This class includes HALs, system buses, system bridges, the system ACPI driver, and the system volume manager driver.  
  
<a href="" id="tape-drives-"></a>**Tape Drives**  
Class = TapeDrive  
ClassGuid = {6d807884-7d21-11cf-801c-08002be10318}  
This class includes tape drives, including all tape miniclass drivers.  
  
**USB Device**  
Class = USBDevice  
ClassGuid = {88BAE032-5A81-49f0-BC3D-A4FF138216D6}  
USBDevice includes all USB devices that do not belong to another class. This class is not used for USB host controllers and hubs.  
  
**Windows CE USB ActiveSync Devices**  
Class = WCEUSBS  
ClassGuid = {25dbce51-6c8f-4a72-8a6d-b54c2b4fc835}  
This class includes Windows CE ActiveSync devices.  
  
The WCEUSBS setup class supports communication between a personal computer and a device that is compatible with the Windows CE ActiveSync driver (generally, PocketPC devices) over USB.  
  
**Windows Portable Devices (WPD)**  
Class = WPD  
ClassGuid = {eec5ad98-8080-425f-922a-dabf3de3f69a}  
(Windows Vista and later versions of Windows) This class includes WPD devices.  
  
**Windows SideShow**  
Class = SideShow  
ClassGuid = {997b5d8d-c442-4f2e-baf3-9c8e671e9e21}  
(Windows Vista and later versions of Windows) This class includes all devices that are compatible with Windows SideShow.  
  
   
  
   
  

  
  
  
  
