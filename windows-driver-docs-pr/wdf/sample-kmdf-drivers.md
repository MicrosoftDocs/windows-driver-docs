---
title: Sample KMDF Drivers
description: This topic lists the Kernel-Mode Driver Framework (KMDF) sample drivers that you can download from the Windows Dev Center - Hardware.
ms.assetid: 83d15b96-63b1-4584-8ef4-ccbdcc1522bb
keywords: ["kernel-mode drivers WDK KMDF , samples", "KMDF WDK , sample drivers", "Kernel-Mode Driver Framework WDK , sample drivers", "framework-based drivers WDK KMDF , samples", "sample drivers WDK KMDF"]
---

# Sample KMDF Drivers


This topic lists the Kernel-Mode Driver Framework (KMDF) sample drivers that you can download from the [Windows Dev Center - Hardware](http://go.microsoft.com/fwlink/p/?linkid=256387).

## <a href="" id="ddk-sample-framework-based-drivers-df"></a>


For information on building the samples, see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver).

<a href="" id="1394"></a>1394  
Demonstrates how to interact with the 1394 driver stack.

For more information about this sample, see [1394VDEV and 1394DIAG - WDF Version](http://go.microsoft.com/fwlink/p/?linkid=256208).

<a href="" id="amcc5933"></a>AMCC5933  
Demonstrates how to write driver for a PCI device that supports direct memory access (DMA) and uses the AMCC PCI Matchmaker Developer's kit (S5935DK1) board.

For more information about this sample, see [AMCC5933 - PCI Device Driver Using WDF](http://go.microsoft.com/fwlink/p/?linkid=256077).

<a href="" id="echo"></a>ECHO  
Demonstrates how to use the framework's queue and request objects and automatic synchronization.

For more information about this sample, see the [KMDF Echo Sample](http://go.microsoft.com/fwlink/p/?linkid=256129).

<a href="" id="fakemodem"></a>FakeModem  
Demonstrates a simple controllerless modem driver that sends and receives AT commands.

For more information about this sample, see the [Fakemodem Driver](http://go.microsoft.com/fwlink/p/?linkid=256110).

<a href="" id="firefly"></a>FIREFLY  
Demonstrates programming a human input device (HID) device by using I/O control codes (IOCTLs), and provides a Windows Management Instrumentation (WMI) interface.

For more information about this sample, see the [FIREFLY - WDF filter driver for HID device](http://go.microsoft.com/fwlink/p/?linkid=256113).

This sample is installed in the *\\src\\hid* subdirectory.

<a href="" id="hidusbfx2"></a>HIDUSBFX2  
Demonstrates how to write a minidriver for a HID device and how to map a non-HID USB device to a HID device. The device is contained in the OSR USB-FX2 Learning Kit.

For more information about this sample, see [HIDUSBFX2](http://go.microsoft.com/fwlink/p/?linkid=256121).

<a href="" id="kbfiltr"></a>KbFiltr  
Demonstrates an upper device filter driver for a PS/2 keyboard.

For more information about this sample, see the [Keyboard Input WDF Filter Driver (Kbfiltr)](http://go.microsoft.com/fwlink/p/?linkid=256125).

<a href="" id="ndisprot"></a>NDISProt  
Demonstrates a connection-less NDIS 5.0/5.1 and NDIS 6.0 protocol driver.

For more information about this sample, see [NDISProt Connection-less WDF Protocol](http://go.microsoft.com/fwlink/p/?linkid=256145).

<a href="" id="nonpnp"></a>NONPNP  
Demonstrates a non-Plug and Play (PnP) driver that uses the framework.

For more information about this sample, see [NONPNP](http://go.microsoft.com/fwlink/p/?linkid=256148).

<a href="" id="kmdf-fx2"></a>KMDF\_FX2  
Demonstrates how to perform bulk and interrupt data transfers to the USB device that is contained in the OSR USB-FX2 Learning Kit.

For more information about this sample, see [kmdf\_fx2](http://go.microsoft.com/fwlink/p/?linkid=256131).

<a href="" id="pcidrv"></a>PCIDRV  
A fully functional framework-based driver for Intel 82557/82558-based PCI Ethernet adapters (10/100) and Intel compatibles.

For more information about this sample, see the [PCIDRV - WDF Driver for PCI Device](http://go.microsoft.com/fwlink/p/?linkid=256154).

<a href="" id="pcmcia"></a>PCMCIA  
The PCMCIA Smart Card Driver is used for the SCM PCMCIA smart card reader.

For more information about this sample, see the [PCMCIA Smart Card Driver](http://go.microsoft.com/fwlink/p/?linkid=256155).

<a href="" id="plx9x5x"></a>PLX9x5x  
Demonstrates how to write a driver for a generic PCI device that supports DMA and uses the PLX9656/9653RDK-LITE board.

For more information about this sample, see the [PLX9x5x PCI Driver](http://go.microsoft.com/fwlink/p/?linkid=256157).

<a href="" id="ramdisk"></a>RAMDISK  
Demonstrates a software-only driver.

For more information about this sample, see the [RAMDisk Storage Driver](http://go.microsoft.com/fwlink/p/?linkid=256171).

<a href="" id="serial"></a>Serial  
A framework-based serial driver that is based on the WDM serial sample driver.

For more information about this sample, see the [Serial sample](http://go.microsoft.com/fwlink/p/?linkid=256183).

<a href="" id="storage-sdio"></a>Storage SDIO  
A framework-based driver for an SDIO development board (Mars board). The board implements the SDIO protocol without additional functionality.

For more information about this sample, see the [Storage SDIO Driver](http://go.microsoft.com/fwlink/p/?linkid=256105).

<a href="" id="toaster"></a>Toaster  
Framework-based versions of the WDM toaster sample drivers. The toaster sample includes a filter driver, a function driver, and a bus driver that create a single driver stack. The sample also includes an additional kernel-mode driver that uses a remote I/O target to communicate with the driver stack.

For more information about this sample, see [Toaster](http://go.microsoft.com/fwlink/p/?linkid=256195).

<a href="" id="usbsamp"></a>UsbSamp  
Demonstrates how to use the framework to perform bulk and isochronous data transfers to a USB device.

For more information about this sample, see the [Usbsamp Sample](http://go.microsoft.com/fwlink/p/?linkid=256204).

<a href="" id="wmisamp"></a>WmiSamp  
Demonstrates how to register WMI providers and create provider instances for framework device objects and how to handle WMI queries that applications send to the device.

For more information about this sample, see the [WmiSamp WMI Provider](http://go.microsoft.com/fwlink/p/?linkid=256220).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Sample%20KMDF%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




