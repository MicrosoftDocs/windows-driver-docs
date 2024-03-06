---
title: Overview of Microsoft USB Test Tool (MUTT) Devices
description: The Microsoft USB Test Tool (MUTT) is collection of devices for testing interoperability of your USB hardware with the Microsoft USB driver stack.
ms.date: 01/17/2024
---

# Overview of Microsoft USB Test Tool (MUTT) devices

The Microsoft USB Test Tool (MUTT) is collection of devices for testing interoperability of your USB hardware with the Microsoft USB driver stack. This article provides a brief overview of the different types of MUTT devices, the tests you can run by using the device, and suggests topologies for controller, hub, device, and BIOS/UEFI testing.

To communicate with MUTT devices, you need the MUTT software package. This package contains several test tools and drivers that let hardware test engineers test interoperability of their USB controller or hub with the Microsoft USB driver stack. The test tools validate USB host controller software, hardware (including firmware) and any USB hub that is installed between the host controller and the device.

**[Download the MUTT software package](https://go.microsoft.com/fwlink/p/?LinkId=786621)** to get the latest version of the test tools.

## How to get MUTT devices

The manufactures listed in this article sell MUTT hardware boards required to run interoperability tests.

| Device | Manufacturers |
|---|---|
| MUTT | [JJG Technologies](http://www.jjgtechnologies.com/Mutt20.htm) |
| MUTT Pack | [JJG Technologies](http://www.jjgtechnologies.com/MuttPack.htm) |
| SuperMUTT | [JJG Technologies](http://www.jjgtechnologies.com/supermutt.htm) |
| SuperMUTT Pack | [VIA Labs](https://www.via-labs.com/shop.php?id=2) |
| Dual-role (DR) MUTT | [JJG Technologies](http://www.jjgtechnologies.com/drmutt.htm) |
| Type-C dual-role (DR) connection exerciser | [MCCI](https://mcci.com/usb/dev-tools/3101-type-c-connection-exerciser/)<br>[JJG Technologies](http://www.jjgtechnologies.com/typecconne.htm) |

## MUTT

- Based on the design of the CY3681 EZ-USB FX2 Development Kit (Cypress FX2).
- Compatible with **FX2** capabilities, such as high speed and full speed transfers to bulk, isochronous, control, interrupt endpoints.
- Simulates traffic from USB 2.0 devices.

    :::image type="content" source="images/fig1-mutt-device.png" alt-text="Picture of a MUTT device.":::

## MUTT Pack

The MUTT Pack is a combination of a USB 2.0 hub and an FX2 device that controls the hub and acts as a downstream device.

- Based on the design on the Cypress Hub and Cypress FX2.
- Hub capabilities. This can operate as a multi-TT or single-TT high speed hub; simulates overcurrent.
- Exposes a downstream port that can be turned on or off.
- Simulates USB 2.0 hub behavior.
- Can operate in self-powered or bus-powered modes.

    :::image type="content" source="images/fig2-muttpackdevice.png" alt-text="Picture of a MUTT pack device.":::

The MUTT Pack has two USB connectors. The standard B connector is used to plug the MUTT Pack in to the host system. The standard A connector is downstream of the embedded hub on the MUTT Pack, and can be used for additional device testing (discussed later in this document).

:::image type="content" source="images/fig3-muttpackconnectors.png" alt-text="Picture of MUTT pack connectors.":::

### How to power the MUTT Pack

The MUTT Pack uses a small jumper (see Figure 3) to switch between self-powered and bus-powered modes. In bus-powered mode, the USB bus of the host system powers the MUTT Pack. In self-powered mode, the MUTT Pack is powered with an external 5V power adapter.

:::image type="content" source="images/fig4-muttpackpoweringflowchart.png" alt-text="MUTT pack powering flowchart.":::

Use the following flow chart to determine how to power the MUTT Pack:

> [!NOTE]
> Do not use the MUTT Pack without the power jumper.

:::image type="content" source="images/fig5-muttpackincorrectusage.png" alt-text="Picture showing incorrect usage of a MUTT pack, without the jumper.":::

This image shows how to use the jumper for powering the MUTT Pack by the USB bus of the host system:

:::image type="content" source="images/fig6-muttpackbuspowered.png" alt-text="Picture of a MUTT pack bus powered.":::

This image shows how to use the jumper for powering the MUTT pack with an external power adapter:

:::image type="content" source="images/fig7-muttpackselfpowered.png" alt-text="Picture of a MUTT pack self powered.":::

Disconnect any existing power adapters and the cable to the host system when you are changing the jumper on the MUTT Pack.

## SuperMUTT

- Based on the design of FX3 EZ-USB FX3.
- Implements SuperSpeed features such as the bulk streams feature.
- Simulates USB 3.0 device traffic.
- this device does not support operation at Low Speed.

:::image type="content" source="images/fig8-supermutt.png" alt-text="Picture of a SuperMUTT.":::

## SuperMUTT Pack

The SuperMUTT Pack is two devices in one. It is a USB 3.0 hub with a Cypress FX2 device downstream. The device controls the hub and also acts as a downstream device. The SuperMUTT Pack simulates USB 3.0 hub behaviors.

The downstream device is a 2.0 device, not a USB 3.0 device.

:::image type="content" source="images/supermuttpack.png" alt-text="Picture of a SuperMUTT pack.":::

## DR MUTT

The DR MUTT acts like a SuperMutt when testing host mode of the device under test, but it can also switch to host mode to test the function mode of the device under test.

## USB Type-C ConnEx

The USB Type-C Connection Exerciser (USB Type-C ConnEx) is a custom shield that has a four-to-one switch to automate USB Type-C interoperability scenarios. The shield has been designed to work with Arduino as the microcontroller. For more information, see [Test USB Type-C systems with USB Type-C ConnEx](test-usb-type-c-systems-with-mutt-connex-c.md).

:::image type="content" source="images/connexc-side.jpg" alt-text="Picture of a USB Type-C ConnEx.":::

## Related topics

- [USB](../index.yml)
