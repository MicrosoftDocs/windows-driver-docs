---
Description: The Microsoft USB Test Tool (MUTT) is collection of devices for testing interoperability of your USB hardware with the Microsoft USB driver stack.
title: Microsoft USB Test Tool (MUTT) devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Microsoft USB Test Tool (MUTT) devices


**Summary**

-   Description of MUTT devices
-   The manufactures listed in this section sell MUTT hardware boards required to run interoperability tests.
-   [![download the mutt software package](images/download.png)](http://go.microsoft.com/fwlink/p/?LinkId=786621) the MUTT software package to get the latest version of the test tools.

The Microsoft USB Test Tool (MUTT) is collection of devices for testing interoperability of your USB hardware with the Microsoft USB driver stack. This section provides a brief overview of the different types of MUTT devices, the tests you can run by using the device, and suggests topologies for controller, hub, device, and BIOS/UEFI testing.

To communicate with MUTT devices, you need the MUTT software package. This package contains several test tools and drivers that let hardware test engineers test interoperability of their USB controller or hub with the Microsoft USB driver stack. The test tools validate USB host controller software, hardware (including firmware) and any USB hub that is installed between the host controller and the device.

## How to get MUTT devices


<a href="" id="mutt"></a>MUTT  
[JJG Technologies]( http://go.microsoft.com/fwlink/p/?linkid=618287)

<a href="" id="mutt-pack"></a>MUTT Pack  
[JJG Technologies]( http://go.microsoft.com/fwlink/p/?linkid=618287)

<a href="" id="supermutt"></a>SuperMUTT  
[JJG Technologies]( http://go.microsoft.com/fwlink/p/?linkid=618287)

[Pactron](http://pactronstore.com/products/supermutt.mdl)

<a href="" id="supermutt-pack"></a>SuperMUTT Pack  
[VIA Labs](http://go.microsoft.com/fwlink/p/?linkid=618285)

<a href="" id="dr-mutt"></a>DR MUTT  
[JJG Technologies]( http://go.microsoft.com/fwlink/p/?linkid=618287)

<a href="" id="mutt-connex-c"></a>USB Type-C ConnEx
[MCCI](http://go.microsoft.com/fwlink/p/?LinkId=733488)

[JJG Technologies]( http://go.microsoft.com/fwlink/p/?linkid=618287)

## MUTT


-   Based on the design of the CY3681 EZ-USB FX2 Development Kit (Cypress FX2).
-   Compatible with **FX2** capabilities, such as high speed and full speed transfers to bulk, isochronous, control, interrupt endpoints.
-   Simulates traffic from USB 2.0 devices.

    ![mutt device](images/fig1-mutt-device.png)

## MUTT Pack


The MUTT Pack is a combination of a USB 2.0 hub and an FX2 device that controls the hub and acts as a downstream device.

-   Based on the design on the Cypress Hub and Cypress FX2.
-   Hub capabilities. This can operate as a multi-TT or single-TT high speed hub; simulates overcurrent.
-   Exposes a downstream port that can be turned on or off.
-   Simulates USB 2.0 hub behavior.
-   Can operate in self-powered or bus-powered modes.

    ![mutt pack device](images/fig2-muttpackdevice.png)

The MUTT Pack has two USB connectors. The standard B connector is used to plug the MUTT Pack in to the host system. The standard A connector is downstream of the embedded hub on the MUTT Pack, and can be used for additional device testing (discussed later in this document).

![mutt pack connectors](images/fig3-muttpackconnectors.png)

### How to power the MUTT Pack

The MUTT Pack uses a small jumper (see Figure 3) to switch between self-powered and bus-powered modes. In bus-powered mode, the USB bus of the host system powers the MUTT Pack. In self-powered mode, the MUTT Pack is powered with an external 5V power adapter.

![mutt pack powering flowchart](images/fig4-muttpackpoweringflowchart.png)

Use the following flow chart to determine how to power the MUTT Pack:

**Note**  Do not use the MUTT Pack without the power jumper.

 

![incorrect usage](images/fig5-muttpackincorrectusage.png)

This image shows how to use the jumper for powering the MUTT Pack by the USB bus of the host system:

![mutt pack bus powered](images/fig6-muttpackbuspowered.png)

This image shows how to use the jumper for powering the MUTT pack with an external power adapter:

![mutt pack self powered](images/fig7-muttpackselfpowered.png)

**Note**  Disconnect any existing power adapters and the cable to the host system when you are changing the jumper on the MUTT Pack.

 

## SuperMUTT


-   Based on the design of FX3 EZ-USB FX3.
-   Implements SuperSpeed features such as the bulk streams feature.
-   Simulates USB 3.0 device traffic.
-   Note: this device does not support operation at Low Speed.

    ![supermutt](images/fig8-supermutt.png)

## SuperMUTT Pack


The SuperMUTT Pack is two devices in one. It is a USB 3.0 hub with a Cypress FX2 device downstream. The device controls the hub and also acts as a downstream device. The SuperMUTT Pack simulates USB 3.0 hub behaviors.

**Note**  The downstream device is a 2.0 device, not a USB 3.0 device.

 

![supermutt pack](images/supermuttpack.png)

## DR MUTT


The DR MUTT acts like a SuperMutt when testing host mode of the device under test, but it can also switch to host mode to test the function mode of the device under test.

## USB Type-C ConnEx


The USB Type-C Connection Exerciser (USB Type-C ConnEx) is a custom shield that has a four-to-one switch to automate USB Type-C interoperability scenarios. The shield has been designed to work with Arduino as the microcontroller. For more information, see [Test USB Type-C systems with USB Type-C ConnEx](test-usb-type-c-systems-with-mutt-connex-c.md).

![USB Type-C ConnEx](images/connexc-side.jpg)

## Related topics
[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[Testing USB hardware, drivers, and apps in Windows](usb-driver-testing-guide.md)  




