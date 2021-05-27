---
description: This topic lists the Microsoft-provided drivers for the supported USB device classes.
title: USB device class drivers included in Windows
ms.date: 04/20/2017
ms.localizationpriority: High
---

# USB device class drivers included in Windows

> [!IMPORTANT]
> This topic is for programmers. If you are a customer experiencing USB problems, see [Troubleshoot common USB problems](https://support.microsoft.com/help/17614/windows-10-troubleshoot-common-usb-problems)

This topic lists the Microsoft-provided drivers for the supported USB device classes.

- Microsoft-provided drivers for USB-IF approved device classes.
- For composite devices, use [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) that creates physical device objects (PDOs) for each function.
- For non-composite devices or a function of a composite device, use [WinUSB (Winusb.sys)](winusb.md).

**If you are installing USB drivers:** You do not need to download USB device class drivers. They are installed automatically. These drivers and their installation files are included in Windows. They are available in the \\Windows\\System32\\DriverStore\\FileRepository folder. The drivers are updated through Windows Update.

**If you are writing a custom driver:** Before writing a driver for your USB device, determine whether a Microsoft-provided driver meets the device requirements. If a Microsoft-provided driver is not available for the USB device class to which your device belongs, then consider using generic drivers, Winusb.sys or Usbccgp.sys. Write a driver only when necessary. More guidelines are included in [Choosing a driver model for developing a USB client driver](winusb-considerations.md).

## USB Device classes

*USB Device classes* are categories of devices with similar characteristics and that perform common functions. Those classes and their specifications are defined by the USB-IF. Each device class is identified by USB-IF approved class, subclass, and protocol codes, all of which are provided by the IHV in device descriptors in the firmware. Microsoft provides in-box drivers for several of those device classes, called *USB device class drivers*. If a device that belongs to a supported device class is connected to a system, Windows automatically loads the class driver, and the device functions with no additional driver required.

Hardware vendors should not write drivers for the supported device classes. Windows class drivers might not support all of the features that are described in a class specification. If some of the device's capabilities are not implemented by the class driver, vendors should provide supplementary drivers that work in conjunction with the class driver to support the entire range of functionality provided by the device.

For general information about USB-IF approved device classes see the [USB Common Class Specification](https://usb.org/sites/default/files/usbccs10.pdf)

The current list of USB class specifications and class codes is documented in the [USB-IF Defined Class Code List](https://www.usb.org/defined-class-codes).

## Device setup classes

Windows categorizes devices by *device setup classes*, which indicate the functionality of the device.

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For more information, see [System-Defined Device Setup Classes](../install/system-defined-device-setup-classes-reserved-for-system-use.md).

Two important device setup classes for USB devices are as follows:

- **USBDevice** {88BAE032-5A81-49f0-BC3D-A4FF138216D6}: IHVs must use this class for custom devices that do not belong to another class. This class is not used for USB host controllers and hubs.

- **USB** {36fc9e60-c465-11cf-8056-444553540000}: IHVs must not use this class for their custom devices. This is reserved for USB host controllers and USB hubs.

The device setup classes are different from USB device classes discussed earlier. For example, an audio device has a USB device class code of 01h in its descriptor. When connected to a system, Windows loads the Microsoft-provided class driver, Usbaudio.sys. In Device Manager, the device is shown under is **Sound, video and game controllers**, which indicates that the device setup class is Media.

## Microsoft-provided USB device class drivers

<table>
  <thead>
    <tr>
      <th>USB-IF class code</th>
      <th>Device setup class</th>
      <th>Microsoft-provided driver and INF</th>
      <th>Windows support</th>
     <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Audio (01h)</td>
      <td><strong>Media</strong></br>
      {4d36e96c-e325-11ce-bfc1-08002be10318}</td>
      <td>Usbaudio.sys<p>Wdma\_usb.inf</p></td>
      <td>Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)</br>Windows 10 Mobile</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
      <td>Microsoft provides support for the USB audio device class by means of the Usbaudio.sys driver. For more information, see "USBAudio Class System Driver" in <a href="/windows-hardware/drivers/audio/kernel-mode-wdm-audio-components">Kernel-Mode WDM Audio Components</a>. For more information about Windows audio support, see the <a href="/windows-hardware/drivers/audio/">Audio Device Technologies for Windows</a> website.</td>
    </tr>
    <tr>
      <td rowspan="5">Communications and CDC Control (02h)</td>
        <tr>
        <td><strong>Ports</strong></br>{4D36E978-E325-11CE-BFC1-08002BE10318}</td>
        <td>Usbser.sys</br>Usbser.inf</td>
        <td>Windows 10 for desktop editions</br>Windows 10 Mobile</td>
        <td>In Windows 10, a new INF, Usbser.inf, has been added that loads Usbser.sys automatically as the function driver.<p>For more information, see <a href="usb-driver-installation-based-on-compatible-ids.md">USB serial driver (Usbser.sys)</a></p></td>
      </tr>
      <tr>
        <td><strong>Modem</strong></br>{4D36E96D-E325-11CE-BFC1-08002BE10318}<p>
        <strong>Note</strong>   Supports Subclass 02h (ACM)</td>
        <td>Usbser.sys</br>Custom INF that references mdmcpq.inf</td>
        <td>Windows 10 for desktop editions</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
        <td>In Windows 8.1 and earlier versions, Usbser.sys is not automatically loaded. To load the driver, you need to write an INF that references the modem INF (mdmcpq.inf) and includes \[Install\] and \[Needs\] sections.<p>Starting with Windows Vista, you can enable CDC and Wireless Mobile CDC (WMCDC) support by setting a registry value, as described in <a href="/windows-hardware/drivers/usbcon/support-for-interface-collections">Support for the Wireless Mobile Communication Device Class</a>.<p>When CDC support is enabled, the <a href="usb-common-class-generic-parent-driver.md">USB Common Class Generic Parent Driver</a> enumerates interface collections that correspond to CDC and WMCDC Control Models, and assigns physical device objects (PDO) to these collections.</td>
      </tr>
      <tr>
        <td><strong>Net</strong></br>{4d36e972-e325-11ce-bfc1-08002be10318}</br><strong>Note</strong>   Supports Subclass 0Dh (NCM)</td>
        <td>UsbNcm.sys</br>UsbNcm.inf</td>
        <td>Windows Server 2022</td>
        <td>Microsoft provides the UsbNcm.sys driver to operate devices that comply with <a href="https://www.usb.org/document-library/network-control-model-devices-specification-v10-and-errata-and-adopters-agreement">Usb NCM</a>. The source code for this driver is available at <a href="https://github.com/microsoft/NCM-Driver-for-Windows">NCM-Driver-for-Windows</a>.</td>
      </tr>
      <tr>
        <td><strong>Net</strong></br>{4d36e972-e325-11ce-bfc1-08002be10318}</br><strong>Note</strong>   Supports Subclass 0Eh (MBIM)</td>
        <td>wmbclass.sys</br>Netwmbclass.inf</td>
        <td>Windows 10 for desktop editions</br>Windows 8.1</br>Windows 8</td>
        <td>Starting in Windows 8, Microsoft provides the wmbclass.sys driver, for mobile broadband devices. See, <a href="/windows-hardware/drivers/network/mb-interface-model">MB Interface Model</a>.
</td>
      </tr>
      <tr>
        <td>HID (Human Interface Device) (03h)</td>
        <td><strong>HIDClass</strong></br>{745a17a0-74d3-11d0-b6fe-00a0c90f57da}</td>
        <td>Hidclass.sys</br>Hidusb.sys</br>Input.inf</td>
        <td>Windows 10 for desktop editions</br>Windows 10 Mobile</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
        <td>Microsoft provides the HID class driver (Hidclass.sys) and the miniclass driver (Hidusb.sys) to operate devices that comply with the <a href="https://go.microsoft.com/fwlink/p/?LinkId=761243">USB HID Standard</a>. For more information, see <a href="/windows-hardware/drivers/hid/hid-architecture">HID Architecture</a> and <a href="/windows-hardware/drivers/hid/minidriver-operations">Minidrivers and the HID class driver</a>. For further information about Windows support for input hardware, see the <a href="/windows-hardware/drivers/hid/">Input and HID - Architecture and Driver Support</a> website.</td>
      </tr>
      <tr>
        <td>Physical (05h)</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>Recommended driver: <a href="winusb.md">WinUSB (Winusb.sys)</a>
</td>
      </tr>
    <tr>
      <td>Image (06h)</td>
      <td><strong>Image</strong></br>{6bdd1fc6-810f-11d0-bec7-08002be2092f}</td>
      <td>Usbscan.sys</br>Sti.inf</td>
      <td>Windows 10 for desktop editions</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
      <td>Microsoft provides the Usbscan.sys driver that manages USB digital cameras and scanners for Windows XP and later operating systems. This driver implements the USB component of the Windows Imaging Architecture (WIA). For more information about WIA, see <a href="/windows-hardware/drivers/image/windows-image-acquisition-drivers">Windows Image Acquisition Drivers</a> and the <a href="/windows-hardware/drivers/image/">Windows Imaging Component</a> website. For a description of the role that Usbscan.sys plays in the WIA, see <a href="/windows-hardware/drivers/image/wia-core-components">WIA Core Components</a>.</td>
    </tr>
    <tr>
      <td>Printer (07h)</td>
      <td><strong>USB</strong><p><strong>Note</strong>   Usbprint.sys enumerates printer devices under the device set up class: <strong>Printer</strong><p> {4d36e979-e325-11ce-bfc1-08002be10318}.</td>
      <td>Usbprint.sys</br>Usbprint.inf</td>
      <td>Windows 10 for desktop editions</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
      <td>Microsoft provides the Usbprint.sys class driver that manages USB printers. For information about implementation of the printer class in Windows, see the <a href="/windows-hardware/drivers/print/">Printing - Architecture and Driver Support</a> website.</td>
    </tr>
    <tr>
      <td rowspan="3">Mass Storage (08h)</td>
        <tr>
          <td><strong>USB</strong></td>
          <td>Usbstor.sys</td>
          <td>Windows 10 for desktop editions</br>Windows 10 Mobile</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
          <td>Microsoft provides the Usbstor.sys port driver to manage USB mass storage devices with Microsoft's native storage class drivers. For an example device stack that is managed by this driver, see <a href="/windows-hardware/drivers/storage/device-object-example-for-a-usb-mass-storage-device">Device Object Example for a USB Mass Storage Device</a>. For information about Windows storage support, see the <a href="/windows-hardware/drivers/storage/">Storage Technologies</a> website.</td>
        </tr>
        <tr>
         <td><strong>SCSIAdapter</strong><p>{4d36e97b-e325-11ce-bfc1-08002be10318}</td>
         <td>SubClass (06) and Protocol (62)</br>Uaspstor.sys</br>Uaspstor.inf</td>
         <td>Windows 10 for desktop editions</br>Windows 10 Mobile</br>Windows 8.1</br>Windows 8</td>
         <td>Uaspstor.sys is the class driver for SuperSpeed USB devices that support bulk stream endpoints. For more information see:
          <ul>
           <li><a href="/previous-versions/windows/hardware/design/dn642103(v=vs.85)">Loading a UASP Storage Driver as a Class Driver on xHCI</a></li><li><a href="/previous-versions/windows/hardware/design/dn642113(v=vs.85)">USB Attached SCSI (UAS) Best Practices for Windows 8</a></li></ul></td>
        </tr>
    </tr>
    <tr>
      <td rowspan="3">Hub (09h)</td>
      <td rowspan="3"><strong>USB</strong><p>{36fc9e60-c465-11cf-8056-444553540000}</td>
      <tr>
      <td>Usbhub.sys</br>Usb.inf</td>
      <td>Windows 10 for desktop editions</br>Windows 10 Mobile</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
      <td>Microsoft provides the Usbhub.sys driver for managing USB hubs. For more information about the relationship between the hub class driver and the USB stack, see <a href="usb-3-0-driver-stack-architecture.md">USB host-side drivers in Windows</a>.
        </td>
      <tr>
      <td>Usbhub3.sys</br>Usbhub3.inf</td>
      <td>Windows 10 for desktop editions</br>Windows 8.1</br>Windows 8</td>
      <td>Microsoft provides the Usbhub3.sys driver for managing SuperSpeed (USB 3.0) USB hubs.<p>The driver is loaded when a SuperSpeed hub is attached to an xHCI controller. See <a href="usb-3-0-driver-stack-architecture.md">USB host-side drivers in Windows</a>.</td>
        </tr>
      </tr>
    </tr>
     <tr>
      <td>CDC-Data (0Ah)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Recommended driver: <a href="winusb.md">WinUSB (Winusb.sys)</a></td>
    </tr>
     <tr>
      <td rowspan="3">Smart Card (0Bh)</td>
      <td rowspan="3"><strong>SmartCardReader</strong><p>{50dd5230-ba8a-11d1-bf5d-0000f805f530}</td>
        <tr>
          <td>Usbccid.sys (Obsolete)</td>
          <td>Windows 10 for desktop editions</br>Windows 7</br>Windows Server 2008</br>Windows Vista</td>
          <td>Microsoft provides the Usbccid.sys mini-class driver to manage USB smart card readers. For more information about smart card drivers in Windows, see <a href="/windows-hardware/drivers/smartcard/index">Smart Card Design Guide</a>.
          <p>Note that for Windows Server 2003, Windows XP, and Windows 2000, special instructions are required for loading this driver because it might have been released later than the operating system.<p>
          <strong>Note</strong>   Usbccid.sys driver has been replaced by UMDF driver, WUDFUsbccidDriver.dll.</td>
          </tr>
         <tr>
           <td>WUDFUsbccidDriver.dll</br>WUDFUsbccidDriver.inf</td>
           <td>Windows 8.1</br>Windows 8</td>
           <td>WUDFUsbccidDriver.dll is a user-mode driver for USB CCID Smart Card Reader devices.</td>
         </tr>
       </tr>
       <tr>
      <td>Content Security (0Dh)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Recommended driver: <a href="usb-common-class-generic-parent-driver.md">USB Generic Parent Driver (Usbccgp.sys)</a>. Some content security functionality is implemented in Usbccgp.sys. See <a href="content-security-features-in-the-composite-client-generic-parent-drive.md">Content Security Features in Usbccgp.sys</a>.</td>
        </tr>
    </tr>
     <tr>
      <td>Video (0Eh)</td>
      <td><strong>Image</strong></br>{6bdd1fc6-810f-11d0-bec7-08002be2092f}</td>
      <td>Usbvideo.sys<p>
          Usbvideo.inf</td>
      <td>Windows 10 for desktop editions<p>Windows Vista</td>
      <td>Microsoft provides USB video class support by means of the Usbvideo.sys driver. For more information, see "USB Video Class Driver" under <a href="/windows-hardware/drivers/stream/avstream-minidrivers-design-guide">AVStream Minidrivers</a>.
      <p>Note that for Windows XP, special instructions are required for loading this driver because it might have been released later than the operating system.</td>
    </tr>
     <tr>
      <td>Personal Healthcare (0Fh)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Recommended driver: <a href="winusb.md">WinUSB (Winusb.sys)</a></td>
     </tr>
     <tr>
      <td>Audio/Video Devices (10h)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>     <tr>
      <td>Diagnostic Device (DCh)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Recommended driver: <a href="winusb.md">WinUSB (Winusb.sys)</a></td>
    </tr>     <tr>
      <td>Wireless Controller (E0h)
      <p><strong>Note</strong>   Supports Subclass 01h and Protocol 01h</td>
      <td>Bluetooth<p>{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}</td>
      <td>Bthusb.sys<p>Bth.inf</td>
      <td>Windows 10 for desktop editions</br>Windows 10 Mobile</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Vista</td>
      <td>Microsoft provides the Bthusb.sys miniport driver to manage USB Bluetooth radios. For more information, see <a href="/previous-versions/windows/hardware/drivers/ff536596(v=vs.85)">Bluetooth Design Guide</a>.</td>
    </tr>     <tr>
      <td>Miscellaneous (EFh)</td>
      <td><strong>Net</strong><p>
{4d36e972-e325-11ce-bfc1-08002be10318}<p><strong>Note</strong>  Supports SubClass 04h and Protocol 01h</td>
      <td>Rndismp.sys</br>Rndismp.inf</td>
      <td>Windows 10 for desktop editions</br>Windows 8.1</br>Windows 8</br>Windows 7</br>Windows Vista</td>
      <td><p><strong>Note</strong> Microsoft recommends that hardware vendors build USB NCM compatible devices instead. USB NCM is a public USB-IF protocol that offers better throughput performance.</p><p>Prior to Windows Vista, support for CDC was limited to the RNDIS-specific implementation of the Abstract Control Model (ACM) with a vendor-unique protocol (<strong>bInterfaceProtocol</strong>) value of 0xFF. The RNDIS facility centers the management of all 802-style network cards in a single class driver, Rndismp.sys. For a detailed discussion of remote NDIS, see <a href="/windows-hardware/drivers/network/overview-of-remote-ndis--rndis-">Overview of Remote NDIS</a>. The mapping of remote NDIS to USB is implemented in the Usb8023.sys driver. For further information about networking support in Windows, see <a href="/windows-hardware/drivers/network/">Networking and Wireless Technologies</a>.</td>
    </tr>
    <tr>
      <td>Application Specific (FEh)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Recommended driver: <a href="winusb.md">WinUSB (Winusb.sys)</a></td>
    </tr>
     <tr>
      <td>Vendor Specific (FFh)</td>
      <td>-</td>
      <td>-</td>
      <td>Windows 10 for desktop editions</br>Windows 10 Mobile</td>
      <td>Recommended driver: <a href="winusb.md">WinUSB (Winusb.sys)</a></td>
    </tr>
  </tbody>
</table>

## Related topics

[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)
