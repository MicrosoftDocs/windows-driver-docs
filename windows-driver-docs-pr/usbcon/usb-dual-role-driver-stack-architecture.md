---
title: USB Dual Role Driver Stack Architecture
description: USB dual role controllers are now supported in Windows, starting with Windows 10.
ms.date: 09/17/2024
---

# USB dual role driver stack architecture

USB dual role controllers are now supported in Windows, starting with Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.

## Introduction

The USB dual role feature makes it possible for a system to be either a USB device or USB host. The detailed specification for USB dual role can be found at USB-IF's [USB on the Go](https://www.usb.org/usb-on-the-go) information page.

The dual role feature allows a mobile device, such as a phone, or a tablet, to designate itself as being a device or a host.

When a mobile device is in function mode, it's attached to a PC or some other device that acts as a host for the attached mobile device.

When a mobile device is in host mode, users can attach their device, such as a mouse or a keyboard. In this case, the mobile device hosts attached devices.

By providing support for USB dual role in Windows 10, we provide the following benefits:

- Connectivity to mobile peripheral devices via USB, which offers a larger data bandwidth compared to wireless protocols like Bluetooth.
- The option of battery charging over USB while connected to and communicating with other USB devices (as long as the required hardware support is present).
- Enable customers who will most likely own a mobile device, such as a smart phone for all their work. This feature allows improved productivity in a wired docking scenario, where a mobile device docks and thus hosts peripheral devices.

The following table shows the list of host class drivers that are available on desktop and mobile editions of Windows.

| USB host class drivers | Windows 10 Mobile | Windows 10 for desktop editions |
|--|--|--|
| USB Hubs (USBHUB) | Yes | Yes (Since Windows 2000) |
| HID - Keyboard/Mice (HidClass, KBDCLass, MouClass, KBDHid, MouHid) | Yes | Yes (Since Windows 2000) |
| USB Mass Storage (Bulk & UASP) | Yes | Yes (Since Windows 2000) |
| Generic USB Host Driver (WinUSB) | Yes | Yes (Since Windows Vista) |
| USB Audio in / out (USBAUDIO) | Yes | Yes (Since Windows XP) |
| Serial Devices (USBSER) | Yes | Yes (Since Windows 10) |
| Bluetooth (BTHUSB) | Yes | Yes (Since Windows XP) |
| Print (usbprint) | No | Yes (Since Windows XP) |
| Scanning (USBSCAN) | No | Yes (Since Windows 2000) |
| WebCam (USBVIDEO) | No | Yes (Since Windows Vista) |
| Media Transfer Protocol (MTP Initiator) | No | Yes (Since Windows Vista) |
| Remote NDIS (RNDIS) | No | Yes (Since Windows XP) |
| IP over USB (IPoverUSB) | No | Yes (New for Windows 10) |

The class drivers in the table were selected based on device class telemetry, and based on key scenarios that were selected for Windows 10. We plan on including a limited number of inbox, third party Host drivers, to support key devices on Windows 10 Mobile. And for Windows 10 for desktop editions, these drivers are available either on the OEM's website or via Windows Update (WU).

For Windows 10 Mobile, the third party drivers that aren't included inbox aren't available on Window Update. The disk footprint of the USB Host stack + HID is kept small. Which is why not all class drivers, and few third party drivers are included inbox for Windows 10 Mobile. An OEM who wishes to make third party drivers available can use a Board Support Package (BSP) to add them to OS images for their mobile devices.

The following table shows the function class drivers that are available on mobile editions of Windows.

> [!NOTE]
> Function drivers are not available on Windows 10 for desktop editions.

| USB Function class drivers | Windows 10 Mobile | Windows 10 for desktop editions | Notes |
|--|--|--|--|
| Media Transfer Protocol (MTP) Responder | Yes | No | There are no scenarios for MTP responder on Desktop. P2P scenarios between Desktop systems were enabled via Easy-MigCable over WinUSB. |
| Video Display out (vidstream) | Yes | No |  |
| Generic USB Function Driver (GenericUSBFn) | Yes | No | IPoverUSB and other desktop flashing scenarios need this driver. |

We monitor device attachment data to let us know if we need to provide more class driver support as the device class popularity list updates.

## Driver implementation

The Microsoft USB Role Switch (URS) driver allows a system implementer to take advantage of the dual-role USB capability of their platform.

The URS driver is intended to provide dual-role functionality for platforms that use a single USB controller that can operate in both host and peripheral roles over a single port. The *peripheral role* is also known as a *function role*. The URS driver manages the current role of the port. The URS driver loads and unloads appropriate software stacks, based on hardware events from the platform.

On a system that has a USB micro-AB connector, the driver makes use of hardware interrupts that indicates the state of the ID pin on the connector. This pin is used to detect whether the controller needs to assume the host role or the function role in a connection. For more information, see the [USB On-The-Go specification](https://www.usb.org/usb-on-the-go). On systems with a USB Type-C connector, the OEM implementer is expected to provide a connector client driver by using the [USB Type-C connector driver programming interfaces](/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference). The client driver communicates with the Microsoft-provided USB connector Manager class extension (UcmCx) to manage all aspects of the USB Type-C connector, such as CC detection, PD messaging, and others. For role switching, the client driver communicates the state of the USB Type-C connector to the URS driver.

The following diagram shows the USB software driver stack for a dual-role controller that uses the URS driver.

![usb role-switch driver stack architecture.](images/dual-role-arch.png)

The URS driver never loads the Function and Host stacks shown in the preceding diagram simultaneously. The URS driver loads either the Function stack, or the Host stack, depending on the role of the USB controller.

## Hardware requirements

If you're developing a platform that takes advantage of the URS driver, to provide dual-role USB functionality, the following hardware requirements have to be met:

- USB controller

    These drivers are provided by Microsoft as in-box drivers.

    Synopsys DesignWare Core USB 3.0 controller. Inbox INF: UrsSynopsys.inf.

    Chipidea High-Speed USB OTG Controller. Inbox INF: UrsChipidea.inf.

- ID pin interrupts

  - One or more ID pin interrupts for non-USB Type-C systems are implemented in one of two ways:

    1. Two edge-triggered interrupts: one that fires when the ID pin on the connector is grounded, and another one that fires when the ID pin is floating.
    1. A single active-both interrupt that is at active level when ID pin is grounded.

- USB controller enumeration

    The USB dual-role controller must be ACPI-enumerated.

- Software support

    The URS driver expects a software interface that allows control of VBus over the connector. This interface is SoC-specific. Contact your SoC vendor for more details.

These USB OTG features aren't supported in Windows:

- Accessory Charger Adapter detection (ACA).
- Session Request Protocol (SRP).
- Host Negotiation Protocol (HNP).
- Attach Detection Protocol (ADP).

## ACPI system configuration

In order to use the URS driver, you must create an ACPI definition file for your system. Additionally, there are some driver-related considerations that you must take into account.

Here's a sample ACPI definition for a USB dual-role controller.

```syntax
//
// You may name the device whatever you want; we don't depend on it being called 'URS0'.
//
Device(URS0)
{
    //
    // Replace with your own hardware ID. Microsoft will add it to the inbox INF,
    // or you may choose to author a custom INF that uses Needs & Includes directives
    // to include sections from the inbox INF.
    //
    Name(_HID, "ABCD1234")

    Name(_CRS, ResourceTemplate() {
        //
        // The register space for the controller must be defined here.
        //
        Memory32Fixed(ReadWrite, 0xf1000000, 0xfffff)


        //
        // The ID pin interrupts, if you are using two edge-triggered interrupts.
        //
        GpioInt(Edge, ActiveHigh, Exclusive, PullUp, 0, "\\_SB.GPI0", 0, ResourceConsumer, , ){0x1001}
        GpioInt(Edge, ActiveHigh, Exclusive, PullUp, 0, "\\_SB.GPI0", 0, ResourceConsumer, , ){0x1002}

        //
        // Following is an example of a single active-both interrupt.
        //
        // GpioInt(Edge, ActiveBoth, Exclusive, PullUp, 0, "\\_SB.GPI0", 0, ResourceConsumer, , ){0x12}
        //

        //
        // For a Type-C platform, you do not need to specify any interrupts here.
        //
    })

    //
    // This child device represents the USB host controller. This device node is in effect
    // when the controller is in host mode.
    // You may name the device whatever you want; we don't depend on it being called 'USB0'.
    //
    Device(USB0)
    {
        //
        // The host controller device node needs to have an address of '0'
        //
        Name(_ADR, 0)
        Name(_CRS, ResourceTemplate() {

            //
            // The controller interrupt.
            //
            Interrupt(ResourceConsumer, Level, ActiveHigh, Exclusive, , , ){0x10}
        })
    }

    //
    // This child device represents the USB function controller. This device node is in effect
    // when the controller is in device/function/peripheral mode.
    // You may name the device whatever you want; we don't depend on it being called 'UFN0'.
    //
    Device(UFN0)
    {
        //
        // The function controller device node needs to have an address of '1'
        //
        Name(_ADR, 1)
        Name(_CRS, ResourceTemplate() {

            //
            // The controller interrupt (this could be the same as the one defined in
            // the host controller).
            //
            Interrupt(ResourceConsumer, Level, ActiveHigh, Exclusive, , , ){0x11}
        })
    }
}
```

Here are some explanations for the main sections of the ACPI file:

- URS0 is the ACPI definition for the USB dual-role controller. The URS driver loads on this ACPI device.

- USB0 and UFN0 are child devices inside the scope of URS0. USB0 and UFN0 represent the two child stacks enumerated by the URS driver, and the host and function stacks respectively. \_ADR is the means by which ACPI matches these device definitions with the device objects that the URS driver creates.

- If the controller uses the same interrupt for both roles, the same controller interrupt can be described in both child devices. Even in that case, the interrupt can still be described as "Exclusive."

- You can make additions to this ACPI definition file as needed. For example, you can set any other necessary methods or properties on any of the devices in the ACPI definition file. Such additions don't interfere with the operation of the URS driver. Any other resources that are required in any of the stacks can also be described in the \_CRS of the appropriate device.

The URS driver assigns Hardware IDs to the host and function stacks. These Hardware IDs are derived from the Hardware ID of the URS device. For example, if you have a URS device whose Hardware ID is ACPI\\ABCD1234, then the URS driver creates Hardware IDs for the host and function stacks as follows:

- Host stack: URS\\ABCD1234&HOST

- Function stack: URS\\ABCD1234&FUNCTION

## INF driver installation packages

3rd-party driver packages can take a dependency on this scheme, if necessary.

If you're an IHV or an OEM and you're thinking of providing your own driver package, here are some things to consider:

- URS driver package

  The Hardware ID for the dual-role controller on each platform is added to the inbox INF for URS. However, if for some reason the ID can't be added, the IHV/OEM can provide a driver package with an INF that Needs/Includes the inbox INF and matches their Hardware ID.

  This driver package is necessary when the IHV/OEM requires a filter driver to be present in the driver stack.

- Host driver package

  An IHV/OEM-provided driver package that Needs/Includes the inbox *usbxhci.inf* and matches the host device Hardware ID is required. The Hardware ID match would be based on the scheme described in the preceding section.

  This driver package is necessary when the IHV/OEM requires a filter driver to be present in the driver stack.

  There's work in progress to make URS driver assign the XHCI Compatible ID for the host device.

- Function driver package

  An IHV/OEM-provided driver package that Needs/Includes the inbox *Ufxsynopsys.inf* and matches the peripheral device Hardware ID is required. The Hardware ID match would be based on the scheme described in the preceding section.

  The IHV/OEM can also include a filter driver in the driver package.

## See also

- [Dual-role controller driver reference](/windows-hardware/drivers/ddi/_usbref/#dual-role-controller-driver-reference)
