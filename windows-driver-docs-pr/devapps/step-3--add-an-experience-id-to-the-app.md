---
title: Step 3 Add an Experience ID to the Microsoft Store Device App
description: This topic describes how to add the experience ID to your UWP device app.
ms.date: 03/17/2023
---

# Step 3: Add an experience ID to the Microsoft Store device app

![device app workflow, step 3.](images/3-device-app-workflow.png)

This topic describes how to add the experience ID to your UWP device app. The *experience ID* is a GUID that uniquely identifies a device metadata package; it's required if your app is configured for automatic installation, as is the case with [UWP device apps for printers](uwp-device-apps-for-printers.md) and [cameras](uwp-device-apps-for-webcams.md).

You can skip this step if your app is specified as a privileged app and it is not configured for automatic installation.

A UWP device app is a special kind of UWP app that device manufacturers create to serve as a companion to their internal or peripheral device. By using device metadata, device apps can run privileged operations and automatically install when a device is plugged in. For more info about UWP device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

This topic is part of a step-by-step series. See [Build a UWP device app step-by-step](build-a-uwp-device-app-step-by-step.md) for the introduction.

## Before you begin

This step requires the StoreManifest.xml file that was created in the [previous step](step-2--create-device-metadata.md). The StoreManifest.xml file specifies the experience ID.

## Add StoreManifest.xml to your project

The experience ID is specified in the StoreManifest.xml file. This ID links your app to the device metadata.

> [!IMPORTANT]
> The StoreManifest.xml file must be stored in the root folder of your app's project, and not in the solution's root folder.

### To add StoreManifest.xml to your project

1. In **Solution Explorer**, right-click the project and choose **Add > Existing Item**.

1. In the **Add Existing Item** dialog box, select the StoreManifest.xml file that you created in the [previous step](step-2--create-device-metadata.md).

1. Review the properties of the StoreManifest.xml file after it's been added to your project. Right-click the **StoreManifest.xml** file and select **Properties**. This highlights the **Properties** window.

1. In the **Properties** window, ensure that the **Build Action** property equals **Content** and the **Copy to Output Directory** property equals **Do not copy**.

For more info about the StoreManifest.xml file, see [StoreManifest schema reference](/uwp/schemas/storemanifest/storemanifestschema2010/schema-root).

## Next step

[Step 4: Test device metadata](step-4--test-device-metadata.md)
