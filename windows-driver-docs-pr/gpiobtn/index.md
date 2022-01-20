---
title: Hardware notifications design guide
description: Describes support for key buttons (Power, Windows, volume and rotation lock) and other indicators in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG).
ms.assetid: E18DAA6C-C64D-40B3-A112-682A935655D0
ms.date: 06/16/2017
ms.topic: article
---

# Hardware notifications design guide

Describes support for key buttons (Power, Windows, volume and rotation lock) and other indicators in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG).

## In this section

|Topic|Description|
|----|----|
|[GPIO buttons and indicators implementation guide](gpio-buttons-and-indicators-implementation-guide-for-windows-8-1.md)|Windows 8 introduced support for general-purpose I/O (GPIO) buttons and indicators by using a HID miniport class driver. The goal was to provide support for key buttons (Power, Windows, volume and rotation lock) in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG). Windows 8.1 is focused on enhancing the quality of the end-to-end user experience and unifying the behavior across various innovative form factors.|
|[GPIO buttons and indicators supplemental testing](gpio-buttons-and-indicators-supplemental-certification-testing-for-windows-8-1.md)|This topic describes Windows 8.1 test scenarios for hardware buttons and indicators, to ensure an optimal user experience for various form factors.|
|[Hardware notifications support](hardware-notifications-support.md)|Windows 10, version 1709 provides an infrastructure for the hardware-agnostic support of notification components such as LEDs and vibration mechanisms. This support is delivered through the introduction of a Kernel-Mode Driver Framework (KMDF) class extension specifically for hardware notification components that allows for the rapid development of client drivers. A KMDF class extension is essentially a KMDF driver that provides a defined set of functionality for a given class of devices, similar to a port driver in the Windows Driver Model (WDM). This section provides an overview of the architecture of the hardware notification class extension. For additional information about the KMDF, see [Using WDF to Develop a Driver](../wdf/using-the-framework-to-develop-a-driver.md).|

