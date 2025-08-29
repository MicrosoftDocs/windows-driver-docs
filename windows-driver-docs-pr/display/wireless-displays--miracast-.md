---
title: Supporting Miracast Wireless Displays
description: Describes how to provide driver support for Miracast wireless displays.
keywords:
- Wireless displays , driver support , Miracast , Windows 10 , Windows 11
ms.date: 04/24/2025
ms.topic: concept-article
---

# Supporting Miracast wireless displays

Miracast is a wireless display standard that allows users to project their Windows device screen to a Miracast-enabled display. The Miracast standard is based on Wi-Fi Direct technology and uses the Wi-Fi Direct connection to establish a peer-to-peer connection between the source device and the display.

Starting in Windows 10 (WDDM 2.0), the operating system ships with a built-in [Miracast](https://www.wi-fi.org/discover-wi-fi/miracast) stack that can work on any GPU. Driver developers should no longer implement a custom Miracast stack. Microsoft might remove support for custom Miracast stacks in a future version of Windows.

For information about the Microsoft Miracast stack and the requirements of drivers and hardware to support Miracast displays starting in Windows 10, see the following documentation:

* [Building best-in-class Wireless projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection)

* The relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**

Before Windows 10, Windows 8.1 (WDDM 1.3) drivers could optionally support Miracast. For more information, see [Supporting Miracast in Windows 8.1](supporting-miracast-in-windows-8-1.md).
