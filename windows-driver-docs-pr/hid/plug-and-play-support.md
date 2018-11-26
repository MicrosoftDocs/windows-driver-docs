---
title: Plug and play support
description: This section describes the enumeration process on the Universal Serial Bus.
ms.assetid: CB3D76DB-4A96-4A19-BC1C-C9181A12B04E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plug and play support


This section describes the enumeration process on the Universal Serial Bus.

When a device is plugged in to a Windows-based computer, the Windows USB stack enumerates the device, extracting details from the device including the interface descriptor (or descriptors) of the device, and then generates a set of hardware IDs and compatible IDs for the device.

For a complete list of USB hardware IDs, see the "Device Identification Strings" section under Device Installation.

The examples in the following sections illustrate two scenarios:

-   USB IDs for a single interface USB device
-   USB IDs for a multi-interface (composite) USB device

*Example 1: Single Interface HID USB Device*

This example shows how the hardware IDs and compatible IDs are generated for a single-interface USB device on a system running Windows 2000 or Windows XP.

When the device is originally enumerated by the USB stack, the USBHUB driver extracts **idVendor**, **idProduct**, and **bcdDevice** from the device descriptor. These three fields are incorporated to generate a USB hardware ID. Note that the vendor, device, and revision numbers are always stored in hexadecimal format.

The generation of the compatible ID for the device is more complicated. The class code, subclass code, and protocol code are determined by the interface descriptor's **bInterfaceClass**, **bInterfaceSubClass**, and **bInterfaceProtocol**. These values are in two-digit hexadecimal format.

**Note**  If you are providing an INF, your hardware identifiers should match the **bold** identifiers in the left column of the following table. (You should avoid using the compatible identifiers listed in the right column.)

 

|                                        |                                      |
|----------------------------------------|--------------------------------------|
| Hardware Identifiers                   | Compatible Identifiers               |
| **USB\\Vid\_xxxx&Pid\_yyyy&Rev\_zzzz** | USB\\Class\_aa&SubClass\_bb&Prot\_cc |
| **USB\\Vid\_xxxx&Pid\_yyyy**           | USB\\Class\_aa&SubClass\_bb          |
|                                        | USB\\Class\_aa                       |

 

*Example 2: Multiple Interface/Function HID USB Device (Composite Device)*

USB devices with multiple functions are called composite devices. This example shows how the hardware IDs and compatible IDs are generated for composite USB devices on Windows. When a new USB composite device is plugged into a computer system running Windows, the USBHUB driver creates a physical device object (PDO) and notifies the operating system that its set of child devices has changed. After querying the hub driver for the hardware IDs associated with the new PDO, the system searches the appropriate INF files to find a match for the identifiers. If a vendor chooses to load just one driver for the entire device (that is, not using the composite device driver) and multiplex all interfaces in software with that driver, the vendor should specify a hardware ID match to prevent the operating system from picking up the lower-ranking match (USB\\COMPOSITE).

**Note**  If you are providing an INF, your hardware identifiers should match the **bold** identifiers in the left column of the following table. (You should avoid using the compatible identifiers listed in the right column.)

 

|                                        |                                      |
|----------------------------------------|--------------------------------------|
| Hardware Identifiers                   | Compatible Identifiers               |
| **USB\\Vid\_xxxx&Pid\_yyyy&Rev\_zzzz** | USB\\Class\_aa&SubClass\_bb&Prot\_cc |
| **USB\\Vid\_xxxx&Pid\_yyyy**           | USB\\Class\_aa&SubClass\_bb          |
|                                        | USB\\Class\_aa                       |
|                                        | USB\\COMPOSITE                       |

 

If, however, no hardware match is found, Windows Plug and Play makes use of the USB\\COMPOSITE identifier to load the USB Generic Parent driver (USBCCGP). The Generic Parent driver then creates a separate set of PDOs (one for every interface) with a separate set of hardware IDs for each interface of the composite device. The following section displays the format of hardware IDs for child PDOs.

To build the set of hardware IDs for each interface’s PDO, the USBCCGP driver appends the interface number (which is a zero-based hexadecimal value) to the end of the hardware ID.

The class code, subclass code, and protocol code are determined by the **bInterfaceClass**, **bInterfaceSubClass**, and **bInterfaceProtocol** fields of the interface descriptor, respectively. These values are in two-digit hexadecimal format.

**Note**  If you are providing an INF, either to load your driver or to provide a friendly device name, your hardware identifiers should match the **bold** identifiers in the left column of the following table. (You should avoid using the compatible identifiers listed in the right column.)

 

|                                               |                                      |
|-----------------------------------------------|--------------------------------------|
| Hardware Identifiers                          | Compatible Identifiers               |
| **USB\\Vid\_xxxx&Pid\_yyyy&Rev\_zzzz&MI\_ww** | USB\\Class\_aa&SubClass\_bb&Prot\_cc |
| **USB\\Vid\_xxxx&Pid\_yyyy&MI\_ww**           | USB\\Class\_aa&SubClass\_bb          |
|                                               | USB\\Class\_aa                       |

 

 

 




