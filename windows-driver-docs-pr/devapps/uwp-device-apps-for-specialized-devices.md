---
title: UWP Device Apps for Internal Devices
description: This topic introduces the ways that UWP device apps can access internal devices.
ms.date: 03/17/2023
---

# UWP device apps for internal devices

This topic introduces the ways that UWP device apps can access internal devices. *Internal devices* are devices that reside inside or are integrated with the PC enclosure.

Some APIs that are mentioned in this topic can be used to access external devices too. This topic focuses specifically on accessing internal devices. For more info about each API, see the [Windows API reference](/uwp/api/).

## Accessing internal devices

There are three ways that UWP apps can access internal devices:

| Recommended? | API | Developer | Is device metadata required? |
|--|--|--|--|
| Yes | Device scenario APIs (image capture, scanning, etc.) | all developers | no |
| Yes | Device protocol APIs (USB, HID, etc.) | OEM | yes (for internal devices only) |
| No | Custom driver access | OEM | yes |

## Device scenario APIs

The Windows Runtime provides several APIs for accessing common devices that are built-in or attached to the PC, such as APIs for image capture, scanning, printing, and using motion sensors. Because these APIs are designed with a specific scenario in mind, they are referred to as *device scenario APIs*. Device scenario APIs can be used by all developers and no device metadata is required to use them. For more info about scenario APIs, see [Integrating devices](/previous-versions/windows/apps/br229563(v=win.10)).

Any access beyond what the device scenario APIs offer is limited to OEMs (or component suppliers, working in coordination with OEMs), and requires device metadata for the system container.

## Device protocol APIs

When an OEM/component supplier needs to access an internal device in a way that is not satisfied by the scenario APIs, they can use the *device protocol APIs*. The device protocol APIs are Windows Runtime APIs that UWP apps can use to access USB and human interface devices (HID). The type of access varies per API.

| Device protocol API | Namespace | Access type |
|--|--|--|
| USB | [Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb) | exclusive read & exclusive write |
| HID | [Windows.Devices.HumanInterfaceDevice](/uwp/api/Windows.Devices.HumanInterfaceDevice) | shared read & exclusive write |

To access peripheral devices that use only Microsoft class drivers - the most common use for the device protocol APIs - device metadata is not required. However, to access internal devices with those APIs, metadata is required. When accessing an internal device, the app must be specified in the device metadata as a privileged app for the system container. This requirements restricts internal device access to OEMs.

For more info, see:

- [Writing apps for USB devices](/previous-versions/windows/apps/dn263144(v=win.10))

- [Supporting human interface devices (HID)](/previous-versions/windows/apps/dn263140(v=win.10))

- [Supporting Bluetooth devices](/previous-versions/windows/apps/dn264587(v=win.10))

- [Device driver requirements](step-1--create-a-uwp-device-app.md) (from step 1 of the step-by-step guide)

- [Creating device metadata](step-2--create-device-metadata.md) (step 2 of the step-by-step guide)

## Custom driver access

When OEMs or IHVs are unable to use the device protocol APIs to access their (internal or peripheral) device, they should first contact Microsoft to discuss their scenario with the Windows Ecosystem team. In some instances - upon Microsoft approval - a UWP device app can directly access a custom driver.

Custom driver access requires device metadata. To access a custom driver, the app must be specified in the device metadata as a privileged app for the peripheral device or system container. For more info about custom driver access, see [UWP device apps design guide for specialized devices internal to the PC](https://download.microsoft.com/download/F/0/D/F0DBC6F9-5CC7-4F13-A9A4-3DD7F1FA5F64/Windows%20Store%20Device%20App%20Design%20Guide%20for%20Specialized%20Devices%20Internal%20to%20the%20PC.docx).

## Component suppliers

Component suppliers can work with OEMs to develop UWP device apps for their internal device. This can happen in a couple of ways:

- **Component supplier develops and distributes the app**: In this case, the component supplier owns, develops, and distributes the app and driver that accesses the internal device. The OEM owns the device metadata.

- **OEM develops and distributes the app**: In this case, the OEM develops and distributes the app that accesses one or more internal devices from different component suppliers. The OEM ultimately owns app development, app distribution, and device metadata maintenance. The component supplier owns the driver.

For more info about these workflows, see [UWP device apps design guide for specialized devices internal to the PC](https://download.microsoft.com/download/F/0/D/F0DBC6F9-5CC7-4F13-A9A4-3DD7F1FA5F64/Windows%20Store%20Device%20App%20Design%20Guide%20for%20Specialized%20Devices%20Internal%20to%20the%20PC.docx).

## Related topics

[Identifying the location of internal cameras (UWP device apps)](identifying-the-location-of-internal-cameras.md)
