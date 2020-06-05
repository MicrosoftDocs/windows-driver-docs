---
title: HID Clients Overview
description: The HID Clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device (for example a sensor, a keyboard, or a mouse).
ms.assetid: C97E1F63-0CA5-42F3-A139-48E830F2E2B7
keywords:
- HID clients
- drivers
- services
- HID API
- HID Collection
ms.date: 02/26/2020
ms.localizationpriority: medium
---

# HID Clients Overview

Human Interface Devices (HID) clients are drivers, services or applications that communicate using the HID API and often represent a specific type of device such as a sensor, keyboard, or mouse. Devices are identified by a hardware ID or a specific HID Collection and communicate via the HID API.

| Topic | Description |
| --- | --- |
| [HID usages](https://docs.microsoft.com/windows-hardware/drivers/hid/hid-usages) | _HID usages_ identify the intended use of HID controls and what the controls actually measure. |
| [HID Collections](https://docs.microsoft.com/windows-hardware/drivers/hid/hid-collections) | _HID collection_ is a meaningful grouping of HID controls and their respective [HID usages](https://docs.microsoft.com/windows-hardware/drivers/hid/hid-usages) |
| [Opening HID collections](https://docs.microsoft.com/windows-hardware/drivers/hid/opening-hid-collections) | This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections. |
| [Handling HID Reports](https://docs.microsoft.com/windows-hardware/drivers/hid/handling-hid-reports) | This section describes the mechanisms that user-mode applications and kernel-mode drivers use for handling [HID reports](https://docs.microsoft.com/windows-hardware/drivers/hid/introduction-to-hid-concepts) |
| [Freeing Resources](https://docs.microsoft.com/windows-hardware/drivers/hid/freeing-resources) | User-mode applications and kernel-mode drivers that are HID clients should always free any resources that are no longer required. |
| [Installing HID clients](https://docs.microsoft.com/windows-hardware/drivers/hid/installing-hid-clients) | This section describes the following requirements for installing HIDClass devices in Microsoft Windows. |
| [HIDClass Hardware IDs for Top-Level Collections](https://docs.microsoft.com/windows-hardware/drivers/hid/hidclass-hardware-ids-for-top-level-collections) |This section specifies the hardware IDs that the HID class driver generates for top-level collections. |
| [Keyboard and mouse HID client drivers](https://docs.microsoft.com/windows-hardware/drivers/hid/keyboard-and-mouse-hid-client-drivers) | This topic discusses keyboard and mouse HID client drivers. Keyboards and mice represent the first set of HID clients that were standardized in the HID Usage tables and implemented in Windows operating systems. |
| [Sensor HID class driver](https://docs.microsoft.com/windows-hardware/drivers/hid/sensor-hid-class-driver) | Starting with Windows 8, the Windows operating system includes an in-box sensor HID Class driver (SensorsHIDClassDriver.dll), that supports eleven types of sensors that communicate using the HID transport. |
| [Airplane mode radio management](https://docs.microsoft.com/windows-hardware/drivers/hid/airplane-mode-radio-management) | Starting with Windows 8, the Windows operating system provides support via HID, for airplane mode radio management controls. |
| [Display brightness control](https://docs.microsoft.com/windows-hardware/drivers/hid/display-brightness-control) | Starting with Windows 8, a standardized solution has been added to allow keyboards (external or embedded on laptops), to control a laptop’s or tablet’s screen brightness through HID. |
