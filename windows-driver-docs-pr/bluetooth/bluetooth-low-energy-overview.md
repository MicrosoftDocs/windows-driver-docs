---
title: Bluetooth Low Energy (LE) overview
description: This article provides an overview of Bluetooth Low Energy (LE) in Windows.
ms.date: 03/02/2023
---

# Bluetooth Low Energy (LE) overview

Bluetooth LE introduces a new physical layer that shares the same frequency space as Bluetooth basic rate. Profiles that are developed on this technology are organized into the generic attribute profile (GATT).

Each profile defines the use of one or more services to create a use case or scenario. Compliant service implementations are constructed from characteristics organized in a way that conforms to the established schema defined on the Bluetooth Special Interest Group [developer website](https://www.bluetooth.com/specifications/gatt/services/).

The following diagram illustrates the way objects are structured inside a typical GATT service.

:::image type="content" source="images/bthleservicedeclaration.png" alt-text="Diagram of Bluetooth LE GATT service declarations.":::

When a Bluetooth LE device is paired with a Windows machine, the device becomes part of the system. Windows provides device objects to represent both the device and the primary services reported by the device.

:::image type="content" source="images/bthlewin8supt.png" alt-text="Diagram of the device object structure of the Windows Bluetooth LE implementation.":::

Each device and its primary services are represented as device objects in Windows and these device objects can be queried and managed using the [device installation functions](/windows-hardware/drivers/install/using-device-installation-functions) such as **[SetupDiEnumDeviceInfo](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo)**, and **[SetupDiGetDeviceProperty](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)**.

In addition to standard [Bluetooth profile driver functions](/windows-hardware/drivers/ddi/_bltooth/), [Bluetooth LE functions](/windows/win32/api/_bltooth/) provide functionality for the development of Bluetooth GATT client applications.

These functions allow for the enumeration of services and their objects (including services, characteristics and their descriptors) as well as read and write capabilities.
