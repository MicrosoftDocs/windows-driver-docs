---
title: Windows Touch Overview (Windows 7)
description: Windows Touch Overview (Windows 7)
ms.assetid: 1373c522-bd9d-4b14-97c9-0c3db5bc9f2a
keywords: ["Windows Touch WDK , about"]
---

# Windows Touch Overview (Windows 7)


Windows Touch is the name for the touch and multi-touch functionality in the Windows 7 operating system. In the context of Windows Touch, *touch* refers to support of a single physical contact point, whereas *multi-touch* refers to support for two or more concurrent physical contacts.

### <span id="choosing_to_provide_a_driver"></span><span id="CHOOSING_TO_PROVIDE_A_DRIVER"></span>Choosing to Provide a Driver

In Windows 7, vendors who support Windows Touch might be required to provide a driver. If your digitizer device supports HID in firmware, you are not required to provide a driver. If your device does not support HID in firmware, you must include a driver that simulates HID support.

We recommend that touch devices be USB HID devices, and that vendors do not supply a driver. In this scenario, the report descriptor and related information is provided in firmware.

Whether you provide a driver or not, you must support selective suspend in your INF file. For more information about how to support selective suspend, see [Enabling USB Selective Suspend for HID Devices](https://msdn.microsoft.com/library/windows/hardware/jj131716).

A vendor-supplied driver should limit the processing that it does to avoid slower system performance and shorter battery life in mobile scenarios. Touch devices should process as much as they can in firmware to provide an optimal user experience.

### <span id="driver_model"></span><span id="DRIVER_MODEL"></span>Driver Model

If you provide a driver, we recommend that you write a KMDF-based lower filter driver. Your driver should provide the same functionality as a HID minidriver, but register as a filter driver under a minimal WDM driver (also known as a shim driver). A shim driver is necessary because KMDF 1.9 does not natively support HID minidrivers. In Windows 7 and later versions of Windows, you can use the system-supplied Mshidkmdf.sys driver as a shim.

Mshidkmdf.sys is not system-supplied in earlier versions of Windows. If you are supporting versions of Windows earlier than Windows 7, you can build the shim driver yourself. The MSDN Code Gallery contains the source code for this driver in the hidmapper subdirectory of the sample package. For more information about how to build the shim driver, see the [HIDUSBFX2](http://go.microsoft.com/fwlink/p/?linkid=256121) sample readme in the MSDN Code Gallery.

WDM is not recommended for any natural input driver, including drivers that support Windows Touch.

### <span id="samples"></span><span id="SAMPLES"></span>Samples

The [WacomKMDF](wacomkmdf-driver.md) and [EloMT](elotouch-driver.md) sample drivers show how to pair Mshidkmdf.sys with a vendor-supplied lower filter driver.

EloMT is a KMDF-based sample digitizer driver that provides multi-touch support. WacomKMDF is a KMDF-based sample pen driver.

Both samples use Mshidkmdf.sys as the nominal HID minidriver while the vendor-supplied KMDF driver is a lower filter driver under Mshidkmdf.sys. Mshidkmdf.sys forwards IRPs to the vendor-supplied lower filter driver.

The EloMT sample includes all the functionality that is required for a multi-touch driver to run on Windows 7. The Elotouch driver can work as both a multi-touch and a mouse driver.

 

 




