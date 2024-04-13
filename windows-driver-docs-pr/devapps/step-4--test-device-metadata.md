---
title: Step 4 Test the Device Metadata for your UWP Device App
description: This topic describes how you can test device metadata for your UWP device app locally before you submit it to the Windows Dev Center Dashboard.
ms.date: 03/17/2023
---

# Step 4: Test the device metadata for your UWP device app

![device app workflow, step 4.](images/4-device-app-workflow.png)

This topic describes how you can test device metadata for your UWP device app locally before you submit it to the Windows Dev Center Dashboard.

A UWP device app is a special kind of UWP app that device manufacturers create to serve as a companion to their internal or peripheral device. By using device metadata, device apps can run privileged operations and automatically install when a device is plugged in. For more info about UWP device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

This topic is part of a step-by-step series. See [Build a UWP device app step-by-step](build-a-uwp-device-app-step-by-step.md) for the introduction.

## Before you begin

You can deploy device metadata to the local device metadata store on a local computer so you can test that your device works properly with it. Once device metadata is deployed, it should act the same way as it would if it were submitted to the Windows Dev Center Dashboard. For example, if AutoPlay is enabled for a device in the device metadata, the AutoPlay handler should work when the device is plugged in. If you change the model or publisher name, you can make sure those changes show up too.

Before you test your device metadata, the Microsoft Store app should be installed on the computer where you will be deploying the device metadata.

## Deploy your device metadata locally

Before you can test your device metadata, you must deploy it to the local device metadata store. You can do this by selecting the **Copy the device metadata package to the metadata store on the local computer** check box when you are creating the device metadata or by using the **Device Metadata Authoring Wizard** after the device metadata has been created.

### To deploy the device metadata by using the Device Metadata Authoring Wizard

1. Open the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86.

1. On the **Tools** menu, click **Deploy Metadata Package**.

1. Browse to the .devicemetadata-ms file, and then click **Open.**

1. If the User Account Control dialog box appears, click **Yes**.

1. After the device metadata has been deployed, you'll see a message that says **The device metadata package was successfully copied to the local metadata store on this computer**. Your device metadata is ready to be tested.

## Validate your device metadata

You can validate your device metadata against a UWP device app or a device by using the **Device Metadata Authoring Wizard**.

### To validate your device metadata by using the Device Metadata Authoring Wizard

1. Open the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86.

1. Click **Validate Metadata**.

1. On the **Select metadata package to validate** page, do the following:

    - Under the **Device metadata package** heading, click **Browse** to select your .devicemanifest-ms file, or click **Select from local metadata store** if you've already deployed your device metadata locally.

    - If you want to validate against a UWP app, select the **Validate the device metadata package against a UWP device app** check box, and then click **Browse** to choose the Microsoft Store app package (.appx).

    - If you want to validate against a device, select the **Validate the device metadata package against a device** check box, click **Select from devices**, choose your device, and then click **OK.**

1. Click **Validate**.

1. After validation is done, you can save the report. Click **Close**.

    > [!CAUTION]
    > You might get an error in the validation report saying "The experience ID does not match between storeManifest.xml in the app package and packageInfo.xml in the device metadata file." You can safely ignore this message.

## Next step

[Step 5: Submit the app](step-5--submit-the-app.md)
