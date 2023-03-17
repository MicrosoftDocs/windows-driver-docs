---
title: Build a UWP device app step-by-step
description: This step-by-step guide describes in detail how to build a UWP device app with Microsoft Visual Studio and the Device Metadata Authoring Wizard.
ms.date: 03/17/2023
---

# Build a UWP device app step-by-step

This step-by-step guide describes in detail how to build a UWP device app with Microsoft Visual Studio and the Device Metadata Authoring Wizard. For a high-level introduction to this process, see [Building UWP device apps](the-workflow.md).

A UWP device app is a special type of UWP app that device manufacturers create to serve as a companion to their internal or peripheral device. By using device metadata, device apps can run privileged operations and automatically install when a device is plugged in. For more info about UWP device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

## In this section

| Topic | Description |
|--|--|
| [Step 1: Create a UWP device app](step-1--create-a-uwp-device-app.md) | This topic describes the basic process for creating a UWP device app by using Visual Studio. Learn about the tasks that are common to all UWP device apps. |
| [Step 2: Create device metadata](step-2--create-device-metadata.md) | This topic describes how to use the **Device Metadata Authoring Wizard** to create new device metadata that associates your UWP device app with a device. The wizard can also create a **StoreManifest.xml** file that you may need to add to your app in the next step. |
| [Step 3: Add an experience ID to the app](step-3--add-an-experience-id-to-the-app.md) | This topic describes how to add the experience ID to your UWP device app. The *experience ID* is a GUID that uniquely identifies a device metadata package; it's required if your app is configured for automatic installation, as is the case with [UWP device apps for printers](uwp-device-apps-for-printers.md) and [cameras](uwp-device-apps-for-webcams.md). |
| [Step 4: Test device metadata](step-4--test-device-metadata.md) | This topic describes how you can test device metadata for your UWP device app locally before you submit it to the Windows Dev Center Dashboard. |
| [Step 5: Submit the app](step-5--submit-the-app.md) | This topic describes how to submit your UWP device app to the Microsoft Store dashboard. |
| [Step 6: Submit device metadata](step-6--submit-device-metadata.md) | This topic describes how to submit device metadata for your UWP device app to the Windows Dev Center hardware dashboard. |
