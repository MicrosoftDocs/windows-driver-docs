---
title: Specify AutoPlay Handler and Options in the Device Metadata Authoring Wizard
description: Specify AutoPlay Handler and options in the Device Metadata Authoring Wizard
keywords:
- Specify AutoPlay Handler and options in the Device Metadata Authoring Wizard
ms.date: 06/25/2025
ms.topic: how-to
---

# Specify AutoPlay Handler and options in the Device Metadata Authoring Wizard

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

To specify options for your device, including the disconnected state and AutoPlay Handler, click the **Options** tab.

## Disconnected State

To enable the device to be shown in a disconnected state, select **Show device in disconnected state**.

## AutoPlay Handler

An AutoPlay Handler allows a UWP app for a device to be listed in AutoPlay options when a device is connected. It doesn't automatically launch an app.

To define an AutoPlay Handler for a device, select from the following options under **AutoPlay Handler (Optional)**.

- If you don't want to define an AutoPlay Handler, select **None**.
- To define an AutoPlay Handler, fill out the following fields under **AutoPlay Handler**:
  - **Package Name**
  - **Publisher**
  - **App ID**
  - **Verb**
  - **AutoPlay Type**
    - From the list, select **Device** or **Content**.
- To define an AutoPlay Handler for a desktop app, fill out the fields under **Desktop AutoPlay Handler**.
    **Note**  You can't define both AutoPlay Handler and Desktop AutoPlay Handler.
