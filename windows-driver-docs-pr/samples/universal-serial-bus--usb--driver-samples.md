---
title: Universal Serial Bus (USB) Driver Samples
description: The driver samples in this directory provide a starting point for writing a custom USB driver for your device.
ms.date: 01/09/2025
---

# Universal Serial Bus (USB) driver samples

The USB driver samples provide a starting point for writing a custom USB driver for your device.

> [!IMPORTANT]
> This topic is for USB device driver developers.
>
> If you are a Windows user experiencing problems with a USB device, please see [Fix USB-C problems in Windows](https://support.microsoft.com/windows/fix-usb-c-problems-in-windows-f4e0e529-74f5-cdae-3194-43743f30eed2).

There are several ways you can use the Windows 10 USB driver samples:

- Browse and download individual Windows 10 driver samples on the [Microsoft Samples portal](/samples/browse/?products=windows-wdk).

- Clone, fork, or download the [Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples) repo on GitHub.

- View the [Windows 10 USB driver samples](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb) on GitHub.

Previous versions of Windows driver samples can be found in the following locations:

- [Windows 8.1 driver samples](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.1%20Samples)

- [Windows 8 driver samples](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.0%20Samples)

| Sample | Description |
|--|--|
| [KMDF Bus Driver](/samples/microsoft/windows-driver-samples/sample-kmdf-bus-driver-for-osr-usb-fx2) | Demonstrates how to use KMDF for a bus driver with the OSR USB-FX2 device. |
| [Sample KMDF Function Driver for OSR USB-FX2](/samples/microsoft/windows-driver-samples/sample-kmdf-function-driver-for-osr-usb-fx2) | Demonstrates how to perform bulk and interrupt data transfers to a USB device. The sample is written for the OSR USB-FX2 Learning Kit. |
| [USB Function Client Driver](/samples/microsoft/windows-driver-samples/usb-function-client-driver) | A skeleton sample driver that shows how to create a Windows USB function controller driver using the USB function class extension driver (UFX). |
| [Sample UMDF Filter above KMDF Function Driver for OSR USB-FX2 (UMDF 1)](../wdf/user-mode-driver-framework-design-guide.md) | Demonstrates how to load a UMDF filter driver as an upper filter driver above the kmdf\_fx2 sample driver. The sample is written for the OSR USB-FX2 Learning Kit. |
| [Sample UMDF Filter above UMDF Function Driver for OSR USB-FX2 (UMDF 1)](../wdf/user-mode-driver-framework-design-guide.md) | demonstrates how to load a UMDF filter driver as an upper filter driver above the umdf\_fx2 sample driver. The sample is written for the OSR USB-FX2 Learning Kit. |
| [UMDF 1 Function Driver](../wdf/user-mode-driver-framework-design-guide.md) | A User-Mode Driver Framework (UMDF 1) driver for the OSR USB-FX2 device. It includes a test application and sample device metadata, and supports impersonation and idle power down. |
| [UMDF 2 Function Driver](/samples/microsoft/windows-driver-samples/sample-function-driver-for-osr-usb-fx2-umdf-version-2) | A User-Mode Driver Framework (UMDF 2) driver for the OSR USB-FX2 device. It includes a test application and sample device metadata, and supports impersonation and idle power down. |
| [Usbsamp Generic USB Driver](/samples/microsoft/windows-driver-samples/usbsamp-generic-usb-driver) | Demonstrates how to perform full speed, high speed, and SuperSpeed transfers to and from bulk and isochronous endpoints of a generic USB device. |
| [USBView](/samples/microsoft/windows-driver-samples/usbview-sample-application) | A Windows application that allows you to browse all USB controllers and connected USB devices on your system. |
| [WDF Sample Driver Learning Lab for OSR USB-FX2](/samples/microsoft/windows-driver-samples/wdf-sample-driver-learning-lab-for-osr-usb-fx2) | Contains a console test application and a series of iterative drivers for both KMDF and UMDF version 1. |
| [UcmCxUcsi Port Controller Client Driver](/samples/microsoft/windows-driver-samples/ucmtcpcicx-port-controller-client-driver-v2) | Demonstrates how to create a Windows USB Type-C port controller driver using the USB Connector Manager class extension driver (UcmCx). |
| [UcmTcpciCx Port Controller Client Driver](/samples/microsoft/windows-driver-samples/ucmtcpcicx-port-controller-client-driver) | Demonstrates how to create a Windows USB Type-C port controller driver using the USB Connector Manager Type-C Port Controller Interface class extension driver (UcmTcpciCx). |
| [UcmUcsiCx ACPI Client Driver](/samples/microsoft/windows-driver-samples/ucmucsicx-acpi-client-driver) | Demonstrates how to create a UCSI-compliant (ACPI transport) Windows USB Type-C port controller driver using the USB Connector Manager class extension driver (UcmCx). |
