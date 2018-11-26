---
Description: This topic presents frequently asked questions for driver developers who are new to developing and integrating USB devices and drivers with Windows operating systems.
title: USB in Windows - FAQ
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB in Windows - FAQ


This topic presents frequently asked questions for driver developers who are new to developing and integrating USB devices and drivers with Windows operating systems.

-   [I hear numerous USB terms thrown around almost interchangeably. What do they all mean?](#usbterms)
-   [Does my PC have USB 3.0 ports?](#pc-3-ports)
-   [Do I need to install drivers for my eXtensible host controller?](#ext-drivers)
-   [Why do I see several host controllers on my system?](#hosts)
-   [Why do I see two hubs in Device Manager when I have connected only one USB 3.0 hub?](#twohubs)
-   [Which set of drivers is loaded for the devices that are connected to 2.0 ports?](#portdrivers)
-   [How do I determine whether my USB 3.0 device is operating as SuperSpeed?](#superspeed)
-   [Why isn't my SuperSpeed USB device faster than an equivalent high-speed USB device?](#whynotfaster)
-   [Is it possible to have a composite and a compound device in one piece of hardware?](#compositecompound)
-   [Why are some of my USB devices reinstalled when they are moved to a new port?](#why-reinstalled)
-   [Is there a list of design recommendations for USB product packaging?](#designrec)
-   [Do I have to rewrite my client driver to support USB 3.0 devices?](#rewritedriver)
-   [Which driver is loaded for my SuperSpeed storage device use, Uaspstor.sys or Usbstor.sys?](#loadeddriver)
-   [Which USB DWG Classes does Microsoft support?](#usbdwg)
-   [Which device setup class should I use for a custom USB device?](#customclass)
-   [Why won't my CPU enter C3 when I attach some USB devices?](#cpucthree)
-   [Which USB class drivers support Selective Suspend?](#selsuspend)
-   [Why can't a USB device awaken Windows from S3?](#usbawake)
-   [Do I need to install drivers for my enhanced (USB 2.0) host controller?](#enhdriver)
-   [Can I disable the "HI-SPEED USB Device plugged into non-HI-SPEED USB port" notice?](#disablehi)
-   [Is my USB 2.0 hub single-TT or multi-TT?](#singlett)
-   [What characters or bytes are valid in a USB serial number?](#usbsn)
-   [What LANGID is used in a string request on localized builds of Windows?](#langidloc)
-   [What LANGID is used to extract a device's serial number?](#langidsn)
-   [What is the maximum USB transfer size for different Windows versions?](#maxxfer)
-   [How should numbers be assigned to multiple interfaces on a composite device?](#nummultif)
-   [What are the major restrictions imposed by Usbccgp.sys?](#usbccgp)
-   [How do I enable debug tracing for USB core binaries?](#tracecorebin)
-   [Does Windows support Interface Association Descriptors?](#iadesc)
-   [Does the USB stack handle chained MDLs in a URB?](#mdlsinurb)
-   [Can a driver have more than one URB in an IRP?](#urbirp)
-   [Does Windows Support USB Composite Hubs?](#supportcomposite)
-   [Where can I find additional FAQs on USB?](#addlfaq)

## I hear numerous USB terms thrown around almost interchangeably. What do they all mean?


*"Thanks to USB 3.0, I can connect a SuperSpeed USB thumb drive to my PC's xHCI host controller and copy files faster."*

Let's understand the USB terms in the preceding sentence. USB 3.0, USB 2.0, and USB 1.0 refer to the USB specification revision number from the [USB Implementers Forum](http://www.usb.org/home). The USB specifications define how the host PC and USB device communicate with each another.

The version number also indicates the maximum transmission speed. The newest specification revision is USB 3.0, which specifies a maximum transmission speed up to 5 Gbps. USB 1.0 defines two different data rates, low speed USB (up to 1.5 Mbps) and full speed USB (up to 12 Mbps). USB 2.0 defines a new data rate, high-speed USB (480 Mbps), while maintaining support for low and full speed devices. USB 3.0 continues to work with all of the previously defined data rates. If you look at product packaging, SuperSpeed USB references the newest USB 3.0 devices. Hi-Speed USB is used to describe high-speed USB 2.0 devices. USB, with no descriptor, refers to low speed and full speed devices.

In addition to the USB protocol, there is a second specification for the USB host controller, the piece of hardware on the PC to which a device is connected. The Host Controller Interface specification defines how host controller hardware and software interact. The eXtensible Host Controller Interface (xHCI) defines a USB 3.0 host controller. The Enhanced Host Controller Interface (EHCI) defines a USB 2.0 host controller. The Universal Host Controller (UHCI) and the Open Host Controller (OHCI) are two, alternate implementations of a USB 1.0 host controller.

## Does my PC have USB 3.0 ports?


USB 3.0 ports are either marked with the SuperSpeed USB Logo or the port is typically blue.

![port with usb logo](images/usb-intro-faq-fig1-usblogo.png)

![blue usb 3.0 port](images/usb-intro-faq-fig2-blueusbport.png)

Newer PCs have both USB 3.0 and USB 2.0 ports. If you want your SuperSpeed USB device to perform at top speed, find a USB 3.0 port and connect the device to that port. A SuperSpeed device that is connected a USB 2.0 port, operates at high speed.

You can also verify that a particular port is a USB 3.0 port in Device Manager. In Windows Vista or later version of Windows, open Device Manager, and select the port from the list.

![usb host controllers in device manager](images/usb-host-controllers-dm.png)

If you have an eXtensible Host Controller, it supports USB 3.0.

## Do I need to install drivers for my eXtensible host controller?


Windows 8 and Windows Server 2012 include support for USB 3.0.

If the PC has USB 3.0 ports and is running a version of Windows earlier than Windows 8, the host controller drivers are provided by the PC manufacturer. If you need to reinstall those drivers, you must get them from the manufacturer.

If you added a USB 3.0 controller card to your PC that is running a version of Windows earlier than Windows 8, you must install the drivers provided by the controller card manufacturer.

In Windows 8, the Microsoft-provided set of USB 3.0 drivers (USB driver stack) work with most host controllers. Microsoft USB 3.0 driver stack does not work with the Fresco Logic FL1000 controller. To determine if you have an FL1000 controller, open Device Manager and expand **Universal Serial Bus controllers**. View the controller properties by right-clicking the controller node. On the **Details** tab, select **Hardware Ids** property in the list. If the hardware ID starts with PCI\\VEN\_1B73&DEV\_1000, it is the FL1000. For that controller, download and install drivers from your PC or controller card manufacturer.

## Why do I see several host controllers on my system?


In addition to the USB devices that you connect to your PC, there are a number of devices integrated within the PC that might be connected over USB, such as a webcam, fingerprint reader, SD Card reader. To connect all of those devices and still provide external USB ports, the PC supports several USB host controllers.

The USB 3.0 xHCI host controller is fully backwards compatible with all USB device speeds, SuperSpeed, high speed, full speed, and low speed. You can connect any device directly to an xHCI controller and expect that device to work. For EHCI controller, that is not the case. While the USB 2.0 specification supports all speeds of devices, the EHCI controller only supports high-speed USB devices. In order for full speed and low speed USB devices to work, they must be connected to the EHCI controller through a USB 2.0 hub, or they must be connected to a UHCI or OHCI Controller.

For newer PCs, most USB 2.0 ports exposed by PCs are downstream of a USB 2.0 hub. This hub is connected to an EHCI controller. This allows the PC’s USB 2.0 port to work with all speeds of devices. SuperSpeed devices behave as high-speed devices when connected to a 2.0 port.

After the USB 2.0 specification was released, PCs used a combination of host controllers in order to support all speeds of devices. A single USB 2.0 port would be wired to two host controllers, an EHCI host controller and either a UHCI or OHCI host controller. When you attach a device, the hardware dynamically routes the connection to one of the two hosts. The routine depends on the device’s speed.

## Why do I see two hubs in Device Manager when I have connected only one USB 3.0 hub?


While xHCI host controllers work with any speed of device, a SuperSpeed hub only works with SuperSpeed devices. To ensure that USB 3.0 hubs can work with all speeds, they have two parts: a SuperSpeed hub and a USB 2.0 hub. A USB 3.0 hub is able to support all speeds by dynamically routing devices, to the SuperSpeed hub or 2.0 hub, based on device speed.

Open Device Manager, view **Devices by connection**, and then locate your eXtensible Host Controller. When you connect a single USB 3.0 hub to your USB 3.0 port, there are two hubs downstream of the controllers’ Root Hub.

![usb 3.0 hub in device manager](images/usb-3-hub-dm.png)

In the example below, a SuperSpeed USB storage device and USB Audio device are both connected to a USB 3.0 hub. You can see the storage device is downstream of the SuperSpeed hub and the audio device is downstream of the USB 2.0 hub.

![usb 3.0 hub with connected devices in device manager](images/usb-3-hub-connected-devices-dm.png)

## Which set of drivers is loaded for the devices that are connected to 2.0 ports?


A different set of binaries is loaded for each type of host controller. It's important to understand that the USB driver stack that Windows loads correlates to the type of host controller, not to the connected device's speed.

In this image, you can see which drivers are loaded for each of the different types of USB host controllers.

![usb driver stack in windows 8](images/usb-win8-driver-stacks.png)

If the USB 3.0 port is correctly routed to an xHCI controller, Windows loads the xHCI driver stack (also referred to as the USB 3.0 driver stack).

If the USB 2.0 port is connected to an EHCI controller through a USB 2.0 hub, the traffic moves through the EHCI controller, and the USB 2.0 driver stack is loaded.

For more information about the drivers in the USB driver stack, see [USB host-side drivers in Windows](http://go.microsoft.com/fwlink/p/?linkid=320134).

If the PC's USB 2.0 ports use a companion controller, the host controller to which the port is routed depends on device speed. For example, a low speed device connects through a UHCI or an OHCI controller, and uses the USBUHCI or USBOHCI driver. The PC routes a high speed device to an EHCI controller, therefore, Windows uses the USBEHCI driver.

Different device speeds do not determine the driver that is loaded for the controller. However, different device speeds might determine which controller is used. The controller always uses the same driver.

## How do I determine whether my USB 3.0 device is operating as SuperSpeed?


In Windows 8, first, make sure that you have a USB 3.0 port and an xHCI host controller. If your SuperSpeed USB device is connected to the xHCI host controller, Windows 8 shows a "Connected to USB 3.0" message in specific portions of the Windows 8 UI. If the device is connected to an EHCI controller instead of your XHCI controller, the messages will instead read, "Device can perform faster when connected to USB 3.0".

You can view these UI messages in PC Settings.

1.  Open the Charms Bar (Drag the cursor to top or bottom right corner of the screen, type Windows Key + C, or swipe in from the right with your finger).
2.  Select **Settings** and then **Change PC settings**.
3.  Select the **Devices** under **PC settings**.

This image shows the UI message when the USB 3.0 device is operating at SuperSpeed.

![superspeed usb device operating at superspeed ](images/usb-superspeed.jpg)

This image shows the UI message when the USB device is operating at a bus speed that is lower than SuperSpeed.

![superspeed usb device operating at high-speed ](images/usb-high-speed.jpg)

You can view similar messages in Devices and Printers, as shown in these images.

![superspeed usb device operating at superspeed](images/usb-superspeed-devices.jpg)

![superspeed device operating at high-speed](images/usb-high-speed-devices.jpg)

If the USB 3.0 device is a storage device, Windows Explorer shows similar messages when the volume label is selected, as shown below. Note that the **View -&gt; Details** pane must be selected for the message to be visible.

![superspeed usb device operating at superspeed ](images/usb-superspeed-storage-device.jpg)

![superspeed usb device operating at high-speed](images/usb-high-speed-storage-device.jpg)

If you are writing a device driver, the [USBView](http://go.microsoft.com/fwlink/p/?linkid=320135) tool, included in the Windows Driver Kit (WDK), is very useful. For the Windows 8 WDK, Microsoft updated USBView to display SuperSpeed USB information. You can use this tool to determine whether or not your device is operating at SuperSpeed. This image shows a USB 3.0 device operating at SuperSpeed in USBView.

![superspeed usb device operating at superspeed](images/usb-superspeed-usbview.jpg)

If you are a device driver developer, the [USB driver stack](http://go.microsoft.com/fwlink/p/?linkid=320134) exposes a new IOCTL that is called [IOCTL\_USB\_GET\_NODE\_CONNECTION\_INFORMATION\_EX\_V2](http://go.microsoft.com/fwlink/p/?linkid=320136), which you can use to query speed information for USB 3.0 devices.

## Why isn't my SuperSpeed USB device faster than an equivalent high-speed USB device?


Generally, if a USB 3.0 USB device is not faster than a high-speed USB device, it's not performing at SuperSpeed. If the SuperSpeed USB device is connected to a USB 3.0 port, it may not operate at SuperSpeed for the following reasons:

-   You are using a USB 2.0 hub.

    If you are using a hub, verify that it's a USB 3.0 hub. If you're using a USB 2.0 hub, any attached SuperSpeed USB device will operate at high-speed. Either replace the hub with a USB 3.0 hub, or connect the device directly to the USB 3.0 port.

-   The firmware on the USB 3.0 hub is out of date.

    Certain earlier USB 3.0 hubs did not work well. As a result, Windows only uses the 2.0 portion of those hubs. If Device Manager indicates a "Non Functional" hub as shown in this image, Windows 8 is not using the 3.0 portion of your hub.

    ![non functional superspeed usb hub](images/usb-superspeed-nonfunctional.jpg)

    You can either connect your SuperSpeed device directly to the USB 3.0 port, or update the firmware on your hub. Windows 8 recognizes hubs that have newer firmware.

-   The device is connected with a USB 2.0 cable.

    Make sure that the cable that is used to connect the device is a USB 3.0 cable. It is also possible that the USB 3.0 cable has signal integrity issues. In that case, the device might switch to high speed. If that happens, you must use a different USB 3.0 cable.

-   The firmware on the device is out of date.

    Update the firmware for the SuperSpeed USB device by obtaining the latest version from the manufacturer's website. Some SuperSpeed USB device manufacturers release fixes, for bugs found in the device, as firmware updates.

-   The firmware on the host controller is out of date.

    Update the firmware for the USB 3.0 controller by obtaining the latest version from your PC manufacturer's site or from your add in card manufacturer's site. Some USB 3.0 controller manufacturers release fixes, for bugs found in the controller, as firmware updates.

-   The BIOS for your system is out of date.

    Update the BIOS for your system by obtaining the latest version from your PC maker. On some motherboards, the BIOS can incorrectly route a device that is connected to an xHCI host controller to an EHCI controller. That incorrect routing forces a SuperSpeed USB device to operate at high-speed. A BIOS update can fix this problem.

## Is it possible to have a composite and a compound device in one piece of hardware?


Yes. The Microsoft Natural Keyboard Pro, which has a three-port, bus-powered hub, is an example of a compound composite USB device. The device has a composite device attached to port 1. Two additional ports are exposed to the end user.

The device that is attached to port 1 is a low-speed composite device. The device has two interfaces, both of which comply with the USB standard device class definition for human interface devices (HID). The composite device provides two HID interfaces instead of multiplexing all collections over a single HID interface by using top-level collections. This design was chosen for compatibility with older BIOSs.

## Why are some of my USB devices reinstalled when they are moved to a new port?


In Windows 2000 and later operating systems, a new physical device object (PDO) is created when a USB device is moved from one port to another. If the hardware reports a unique USB serial number, a new PDO is not created.

To reuse the same PDO and to ensure that the device experience is unchanged whether the device is reinserted into the same port or a new port, hardware vendors must store a serial number on their device. According to Windows Hardware Certification Program requirements, the serial number must be unique for all devices that share the device installation identifier.

## Is there a list of design recommendations for USB product packaging?


The USB-IF has worked with Microsoft and other USB-IF member companies to develop a list of recommendations for independent hardware vendors to include on their packaging.

More information is available on the USB Web site.

For USB and Hi-Speed USB refer to: [http://www.usb.org/developers/packaging](http://www.usb.org/developers/packaging/)/.

For SuperSpeed USB refer to: <http://www.usb.org/channel/>.

## Do I have to rewrite my client driver to support USB 3.0 devices?


All existing client drivers should continue work, as is, when a low, full, or high-speed device is connected to a USB 3.0 port. In Windows 8, we have ensured compatibility with existing client drivers.

The USB 3.0 driver stack maintains IRQL levels, caller context, and error status; retry frequency and timing when interacting with devices, and more to make sure existing drivers continue to work. It is still very important to test.

Common failures occur because:

-   The driver's endpoint descriptor parsing breaks due to the presence of SuperSpeed endpoint companion descriptors.
-   Due to increased speed, you might run into timing issues at the application protocol level.
-   The maximum packet size supported by the endpoint might be different.
-   \\Due to function power management, timing for selective suspend operation might be different.

In Windows 7 and earlier version of the operating systems, the USB 3.0 driver stack is provided by third-party. Therefore, we highly recommend that you test your driver to work with third party USB driver stacks.

New client drivers in Windows 8 for high Speed and SuperSpeed USB devices should opt for new capabilities.

## Which driver is loaded for my SuperSpeed storage device use, Uaspstor.sys or Usbstor.sys?


The USB Attached SCSI (UAS) protocol is a new mass storage protocol designed to improve performance over the established USB mass storage protocol, Bulk-Only-Transport (BOT). It does so by reducing protocol overhead, supporting SATA native command queuing (NCQ) and by processing multiple commands in parallel. To do this, UAS makes use of a new USB 3.0 feature for bulk transfers called streams.

The existing mass storage driver, Usbstor.sys, uses the BOT protocol. It works with all speeds of devices, including SuperSpeed USB devices.

For Windows 8, Microsoft includes a new mass storage class driver, Uaspstor.sys which uses the UAS protocol. Because streams is new to USB 3.0, so Uaspstor.sys can only use streams when the hardware supports streams (a SuperSpeed USB device is connected to an xHCI host controller). The driver also includes support for software streams, so it can also load for devices operating at high-speed, regardless of the host type.

If you connect a mass storage device to Windows 8 and that device supports UAS, Windows loads Uaspstor.sys. In some cases, there might be known issues with hardware streams on a specific xHCI host controller or known issues with a device's UAS protocol implementation. In those cases, Windows falls back to the BOT protocol and loads the Usbstor.sys driver instead.

Uaspstor.sys is new to Windows 8. It is not present in earlier versions of Windows.

## Which USB DWG Classes does Microsoft support?


Windows supports several USB classes that the USB Device Working Group (DWG) has defined. For the current list of USB class specifications and class codes, visit the USB DWG Web site at [http://www.usb.org/developers/devclass\_docs]( http://go.microsoft.com/fwlink/p/?LinkId=623332).

This table highlights the USB DWG classes that are supported in Windows and also identifies the versions of Windows that support each class.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Class Specification</th>
<th>bDeviceClass Code</th>
<th>Driver Name</th>
<th>Windows Support</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Bluetooth class</td>
<td>0xE0</td>
<td>Bthusb.sys</td>
<td>Windows XP and later</td>
</tr>
<tr class="even">
<td>Chip/smart card interface devices (CCID)</td>
<td>0x0B</td>
<td>Usbccid.sys</td>
<td><p>Windows Server 2008 and later</p>
<p>Windows Vista and later</p>
<p>Windows Server 2003<em></p>
<p>Windows XP</em></p>
<p>Windows 2000<em></p></td>
</tr>
<tr class="odd">
<td>Hub class</td>
<td>0x09</td>
<td>Usbhub.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="even">
<td>Human interface device (HID)</td>
<td>0x03</td>
<td>Hidusb.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="odd">
<td>Mass storage class (MSC)</td>
<td>0x08</td>
<td>Usbstor.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="even">
<td>USB Attached SCSI (UAS)</td>
<td>0x08</td>
<td>Uaspstor.sys</td>
<td><p>Windows Server 2012</p>
<p>Windows 8</p></td>
</tr>
<tr class="odd">
<td>Printing class</td>
<td>0x07</td>
<td>Usbprint.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="even">
<td>Scanning/imaging (PTP)</td>
<td>0x06</td>
<td><p>WpdUsb.sys</p>
<p>Usbscan.sys</p></td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="odd">
<td>Media Transfer (MTP)</td>
<td>0x06</td>
<td>WpdUsb.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p></td>
</tr>
<tr class="even">
<td>USB Audio class</td>
<td>0x01</td>
<td>Usbaudio.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="odd">
<td>Modem class (CDC)</td>
<td>0x02</td>
<td>Usbser.sys</td>
<td><p>Windows Server 2003 and later</p>
<p>Windows XP and later</p>
<p>Windows 2000 and later</p></td>
</tr>
<tr class="even">
<td>Video class (UVC)</td>
<td>0x0E</td>
<td>Usbvideo.sys</td>
<td><p>Windows Vista and later</p>
<p>Windows XP</em></p></td>
</tr>
</tbody>
</table>

 

\*Special instructions are necessary to load this driver because this driver might have been released later than the operating system. Windows class drivers might not support all of the features that are described in a DWG class specification. In this case, the driver does not load based on class match. For additional details on implemented features within a class specification, see the WDK documentation.

## Which device setup class should I use for a custom USB device?


Microsoft provides system-defined setup classes for most device types. System-defined setup class GUIDs are defined in Devguid.h. For additional information, see the WDK. For a list of Windows class GUIDs, see these topics:

-   [System-Defined Device Setup Classes Available to Vendors](http://go.microsoft.com/fwlink/p/?linkid=320141)
-   [System-Defined Device Setup Classes Reserved for System Use](http://go.microsoft.com/fwlink/p/?linkid=320142)

Independent hardware vendors must use the setup class that is associated with the type of USB device, not with the bus type. If you are developing a device type for which Microsoft has not provided an existing class GUID, you can define a new device setup class.

In Windows 8, a new setup class has been defined, named **USBDevice** (ClassGuid = {88BAE032-5A81-49f0-BC3D-A4FF138216D6}). If you are developing a device type, associate your device with **USBDevice** instead of the setup class, **USB**. The **USBDevice** class works on Windows Vista and later versions of the operating system.

The setup class **USB** (ClassGuid = {36fc9e60-c465-11cf-8056-444553540000}) is reserved only for USB host controllers and USB hubs, and must not be used for other device categories. Using this setup class incorrectly may cause the device driver to fail Windows logo testing.

## Why won't my CPU enter C3 when I attach some USB devices?


When a USB device is connected, the USB host controller polls the frame scheduler, which is a direct memory access (DMA) bus master operation. "Break events" such as bus master traffic, interrupts, or several other system activities move a CPU out of C3 because, by definition, the CPU's cache cannot be snooped while it is in C3.

There are two ways to work around this issue:

-   Hardware removal.

    At times, the hardware can be electronically disconnected from the Universal Serial Bus. For example, when storage media is removed from the USB reader, the USB reader can emulate an electronic disconnect and reconnect when the media is reinserted. In this case, the C3 transitions can occur because no USB devices are on the host controller.

-   Selective Suspend.

    The only alternative available in Windows XP and later operating systems is to support USB Selective Suspend. This feature lets a driver suspend a USB device that it controls when the device becomes idle, even though the system itself remains in a fully operational power state (S0). Selective Suspend is especially powerful if all USB function drivers support it. If even one driver does not support it, the CPU cannot enter C3. For additional information on Selective Suspend, see the WDK.

## Which USB class drivers support Selective Suspend?


The following is a list of USB class drivers in Windows 8 that support Selective Suspend:

-   Bluetooth

    This driver can selectively suspend devices on computers that are running Windows XP Service Pack 2 and later versions of Windows. The driver requires the Bluetooth radio to set the self-powered and remote wake bits in the configuration descriptor. The driver selectively suspends (D2) the Bluetooth radio when no active Bluetooth connections exist.

-   USB HID

    This driver can selectively suspend an HID device. It is your responsibility to trigger the remote wake signal on all device state changes. To enable Selective Suspend in the HID stack, the SelectiveSuspendEnabled registry value must be enabled for the specific VID+PID of the device. For examples, see Input.inf.

    On systems that support Windows 8’s Connected Standby, this driver enters selective suspend (D2) when the system is in Connected Standby. This driver can wake the system and turn on the screen.

-   USB Hub

    This driver can selectively suspend a root or external hub when no devices are attached to it or when all devices that are attached to that hub can be selectively suspended.

-   USB Modem

    This driver can selectively suspend the device when no active modem connections exist.

-   USB Storage (BOT)

    This driver can selectively suspend (D3) storage devices on systems that support Windows 8 Connected Standby, when those systems go into Connected Standby. Like HID, there is a registry override to enable selective suspend on all Windows 8 systems.

-   USB Storage (UAS)

    This driver can selectively suspend (D3) a storage device when it’s idle for a disk timeout period.

-   USB Video

    This driver can selectively suspend (D3) a webcam on Windows Vista and later operating system.

-   USB Audio

    This driver can selectively suspend (D3) a USB audio device on Windows 7 and later operating systems when the computer is on battery power.

-   Composite USB

    This driver can selectively suspend (D3) composite devices when all children are in suspend. On systems that support D3-Cold, all children must opt into D3-Cold.

-   USB Smart Card

    This driver can selectively suspend (D2) Smart Card interface devices by default in Windows 7 and later operating systems.

-   Generic USB Peripherals (WinUSB)

    This driver can selectively suspend (D3) devices by default on Windows Vista and later operating systems.

-   WWAN: 3G or WiMax Dongles

    This driver can selectively suspend devices. When there is an active subscription, the device enters D2, without an active subscription, the device enters D3.

## Why can't a USB device awaken Windows from S3?


A USB device cannot awaken Windows from S3 for several reasons, including the following:

1.  Incorrect BIOS.

    Verify that the latest BIOS is installed on the computer. To obtain the latest BIOS revision for the computer, visit the Web site of the OEM or ODM.

2.  BIOS that is not enabled to wake.

    Some BIOSs make it possible to disable wake from S3 and S4. Verify that the BIOS is enabled to wake from S3.

3.  USBBIOSx registry key not being set.

    A clean installation of Windows XP does not have the USBBIOSx registry key. If the OEM or ODM validates that the BIOS can wake from S3, set this registry key to 0x00 and restart the computer.

4.  The Host Controller does not have power in S3 or S4.

    Many times the PC cuts power to an add-in card when the PC is in a lower power state. If the add-in card has no power, it will not be able to detect a wake event, and will not be able to wake the PC.

For additional information, see the USB troubleshooter in the Help and Support Center in Windows XP and later versions of Windows.

## Do I need to install drivers for my enhanced (USB 2.0) host controller?


The following versions of Windows support the USB 2.0 enhanced host controller:

-   Windows Vista and later
-   Windows Server 2003 and later
-   Windows XP Service Pack 1
-   Windows 2000 Service Pack 4

**Note**  
Because Windows 2000 and Windows XP were released before USB 2.0 hardware was available, the drivers were released for those operating systems in the service packs. To install drivers:

1.  Follow the procedure that was described in the answer to the first question to verify that your computer has USB 2.0 ports and that you need to install a driver for the enhanced host controller.
2.  In the Device Manager window, expand the **Other Devices** section as explained in the first question, and then double-click **Universal Serial Bus (USB) Controller**.
3.  On the **General** tab of the Properties dialog box, click **Reinstall Driver**.

    ![reinstall driver](images/usb-reinstall-driver.jpg)

4.  In the Add New Hardware Wizard, select **Install the software automatically (Recommended)**, and then click **Next**. Continue with the wizard, accepting all default options, until you reach the last page of the wizard, and then click **Finish**. You might be required to restart your computer to finish the installation.

 

For additional information about the availability of USB 2.0 in Windows XP Service Pack 1, see Microsoft Knowledge Base article 329632, "How to obtain and to install USB 2.0 drivers in Windows XP Service Pack 1" at [http://support.microsoft.com/default.aspx?scid=KB;EN-US;Q329632&](https://support.microsoft.com/kb/329632).

**Note**  
To ensure that you have the latest updates installed on your machine, visit Windows Update regularly.

 

## Can I disable the "HI-SPEED USB Device plugged into non-HI-SPEED USB port" notice?


Windows XP and later versions of Windows create a pop-up notice when a Hi-Speed USB device is plugged into a USB port that does not support high speed. To obtain the fastest performance from the device, users must click the notice and follow the instructions on the screen.

To disable the notice, follow these steps:

1.  Start Device Manager, as described in the first question in this FAQ.
2.  In the Device Manager window, expand the **Universal Serial Bus controllers** node. Look for a host controller with the word "Universal" or "Open" in the title. If you find one, double-click it.
3.  On the **Advanced** tab of the **Properties** dialog box, select **Don't tell me about USB errors**.

**Note**  
The preceding procedure disables all USB notices, not just "HI-SPEED USB Device plugged into non-HI-SPEED port".

 

For additional information about USB 2.0 support in Windows XP Service Pack 1, see Microsoft Knowledge Base article 329632, "How to obtain and to install USB 2.0 drivers in Windows XP Service Pack 1, at [http://support.microsoft.com/default.aspx?scid=KB;EN-US;Q329632](https://support.microsoft.com/kb/329632).

## Is my USB 2.0 hub single-TT or multi-TT?


A USB 2.0 hub can have one transaction translator (TT) for all downstream-facing ports on the hub (single TT), or it can have one TT for each downstream-facing port on the hub (multiple TT).

The value of the **bDeviceProtocol** field of the USB device descriptor and the **bInterfaceProtocol** field of the USB interface descriptor indicate whether a hub is single-TT or multi-TT:

-   Single-TT. **bDeviceProtocol** == 0x01
-   Multi-TT. **bDeviceProtocol** == 0x02

**Usbhub.sys** uses this setting to enable multi-TT mode or single-TT mode. On Windows XP and later, Usbhub.sys always enables multi-TT mode on a multi-TT hub. For additional details about TT layout, see sections 11.14.1.3 and 11.23.1 of the [USB 2.0 Specification](http://www.usb.org/developers/docs).

## What characters or bytes are valid in a USB serial number?


The USB device descriptor's **iSerialNumber** field indicates whether the device has a serial number and where the number is stored, as follows:

-   **iSerialNumber** == 0x00 : The USB device has no serial number.
-   **iSerialNumber** != 0x00 : The USB device has a serial number. The value assigned to **iSerialNumber** is the serial number's string index.

If the device has a serial number, the serial number must uniquely identify each instance of the same device.

For example, if two device descriptors have identical values for the i**dVendor**, **idProduct**, and **bcdDevice** fields, the **iSerialNumber** field must be different, to distinguish one device from the other.

Plug and Play requires that every byte in a USB serial number be valid. If a single byte is invalid, Windows discards the serial number and treats the device as if it had no serial number. The following byte values are not valid for USB serial numbers:

-   -   0x2C.
-   Values less than 0x20.
-   Values greater than 0x7F.

For additional details on the **iSerialNumber** value, see section 9.6.1 of the [USB 2.0 Specification](http://www.usb.org/developers/docs).

## What LANGID is used in a string request on localized builds of Windows?


A USB device indicates the presence of a serial number by setting the iSerialNumber field of the USB device descriptor to the serial number's string index. To retrieve the serial number, Windows issues a string request with the language identifier (LANGID) set to 0x0409 (U.S. English). Windows always uses this LANGID to retrieve USB serial numbers, even for versions of Windows that are localized for other languages.

## What LANGID is used to extract a device's serial number?


A USB device indicates the presence of a serial number by setting the iSerialNumber field of the USB device descriptor to the serial number's string index. To retrieve the serial number, Windows issues a string request with the language identifier (LANGID) set to 0x0409 (U.S. English). Windows always uses this LANGID to retrieve USB serial numbers, even for versions of Windows that are localized for other languages.

## What is the maximum USB transfer size for different Windows versions?


See [Maximum size of USB transfers on various operating systems](https://support.microsoft.com/kb/832430).

## How should numbers be assigned to multiple interfaces on a composite device?


Windows treats USB devices that have more than one interface on the first configuration as composite devices.

For Windows XP Service Pack 1 and earlier versions of Windows:

-   Interface numbers must be zero-based.
-   Interface numbers must be consecutive and increasing.

For Windows XP Service Pack 2 and later versions of Windows, interface numbers are only required to be increasing, not consecutive.

For additional information about interface numbers, see [Composite USB devices whose interfaces are not sequentially numbered do not work in Windows XP](https://support.microsoft.com/kb/814560).

Alternate settings for an interface should be assigned as follows for all versions of Windows:

-   The default value for an interface is always alternate setting zero.
-   Additional alternate setting numbers must be consecutive and increasing.

For additional information on alternate settings, see Section 9.6.5 of the [USB 2.0 Specification](http://www.usb.org/developers/docs).

## What are the major restrictions imposed by Usbccgp.sys?


**Usbccgp.sys** supports composite devices for:

-   Windows Me
-   Windows XP
-   Windows Server 2003
-   Windows Vista
-   Windows Server 2008

Although it might still be possible to load **Usbhub.sys** as the parent driver for the composite device on these and later versions of Windows, Microsoft does not recommend it because it might cause hardware compatibility errors. You should use **Usbccgp.sys** instead.

To ensure that you load the correct driver for your composite device, use the Include and Needs directives in your INF files, as follows:

``` syntax
Include = USB.INF
Needs = Composite.Dev
```

The major restrictions imposed on hardware devices and drivers by **Usbccgp.sys** are as follows:

-   Usbccgp supports only the default configuration, configuration 0.
-   Usbccgp does not support Selective Suspend in Windows XP and Windows Server 2003. This feature is supported only in Windows Vista and later versions of Windows.
    **Note**  
    Usbccgp supports Selective Suspend in Windows XP SP1 and later versions of Windows XP, but with limited features. For these versions of Windows, the composite device is put into Selective Suspend only if each child function of the device has a pending Idle IRP. Usbccgp does not support Selective Suspend in Windows XP RTM

     

-   Usbccgp supports the interface association descriptor (IAD) only in Windows XP SP2, Windows Server 2003 SP1, and later versions of Windows.
-   Usbccgp supports nonconsecutive interface numbers only in Windows XP SP2, Windows Server 2003 SP1, and later versions of Windows.

## How do I enable debug tracing for USB core binaries?


See the blog post about [How to include and view WPP trace messages in a driver’s public PDB files](http://blogs.msdn.com/b/usbcoreblog/archive/2013/06/29/wpp-blog-post.aspx).

For additional information about USB core stack debugging, see [How to enable verbose debug tracing in various drivers and subsystems](https://support.microsoft.com/kb/314743).

## Does Windows support Interface Association Descriptors?


Yes. The USB 2.0 Interface Association Descriptor (IAD) Engineering Change Notification (ECN) introduced a new standard method for describing a grouping of interfaces and their alternate settings within a function. IAD can be used to identify two or more consecutive interfaces and alternate settings within one function.

Microsoft is currently working with IHVs to develop devices that support IAD. The following operating systems have support for IAD:

-   Windows XP Service Pack 2 and later
-   Windows Server 2003 Service Pack 1 and later
-   Windows Vista

## Does the USB stack handle chained MDLs in a URB?


This functionality is supported by the USB 3.0 driver stack that is included with Windows.

## Can a driver have more than one URB in an IRP?


No. This functionality is not supported by the USB stack that is included with Windows.

## Does Windows Support USB Composite Hubs?


A composite USB device - also referred to as a multifunction USB device - exposes multiple functions, each of which can be treated as an independent device. The system loads the USB generic parent driver, **Usbccgp.sys**, to serve as the parent driver for eaech of the device's functions. The USB generic parent driver enumerates the composite device's functions as though they were separate USB devices and then creates a PDO and constructs a device stack for each function.

A composite USB device cannot expose a function that serves as a hub. Windows does not enumerate such hubs properly and attempting to install the device might cause a system crash.

## Where can I find additional FAQs on USB?


See the USB-IF FAQ page at <http://www.usb.org/developers/usbfaq/>.

## Related topics
[USB concepts for all developers](usb-concepts-for-all-developers.md)  
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



