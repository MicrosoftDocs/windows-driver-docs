---
title: Step 4 Test the device metadata for your Windows Store device app
description: This topic describes how you can test device metadata for your Windows Store device app locally before you submit it to the Windows Dev Center Dashboard.
ms.assetid: C1DA36DE-DB89-4A2A-8B9F-DF2A279D3EDD
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Step 4: Test the device metadata for your Windows Store device app


![device app workflow, step 4](images/4-device-app-workflow.png)

This topic describes how you can test device metadata for your Windows Store device app locally before you submit it to the Windows Dev Center Dashboard.

A Windows Store device app is a special kind of Windows Store app that device manufacturers create to serve as a companion to their internal or peripheral device. By using device metadata, device apps can run privileged operations and automatically install when a device is plugged in. For more info about Windows Store device apps, see [Meet Windows Store device apps](meet-windows-store-device-apps.md).

**Note**  This topic is part of a step-by-step series. See [Build a Windows Store device app step-by-step](build-a-windows-store-device-app-step-by-step.md) for the introduction.

 

## <span id="Before_you_begin"></span><span id="before_you_begin"></span><span id="BEFORE_YOU_BEGIN"></span>Before you begin


You can deploy device metadata to the local device metadata store on a local computer so you can test that your device works properly with it. Once device metadata is deployed, it should act the same way as it would if it were submitted to the Windows Dev Center Dashboard. For example, if AutoPlay is enabled for a device in the device metadata, the AutoPlay handler should work when the device is plugged in. If you change the model or publisher name, you can make sure those changes show up too.

Before you test your device metadata, the Windows Store app should be installed on the computer where you will be deploying the device metadata.

## <span id="Deploy_your_device_metadata_locally"></span><span id="deploy_your_device_metadata_locally"></span><span id="DEPLOY_YOUR_DEVICE_METADATA_LOCALLY"></span>Deploy your device metadata locally


Before you can test your device metadata, you must deploy it to the local device metadata store. You can do this by selecting the **Copy the device metadata package to the metadata store on the local computer** check box when you are creating the device metadata or by using the **Device Metadata Authoring Wizard** after the device metadata has been created.

**To deploy the device metadata by using the Device Metadata Authoring Wizard**

1.  Open the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86.
2.  On the **Tools** menu, click **Deploy Metadata Package**.
3.  Browse to the .devicemetadata-ms file, and then click **Open.**
4.  If the User Account Control dialog box appears, click **Yes**.
5.  After the device metadata has been deployed, you'll see a message that says **The device metadata package was successfully copied to the local metadata store on this computer**. Your device metadata is ready to be tested.

## <span id="Validate_your_device_metadata"></span><span id="validate_your_device_metadata"></span><span id="VALIDATE_YOUR_DEVICE_METADATA"></span>Validate your device metadata


You can validate your device metadata against a Windows Store device app or a device by using the **Device Metadata Authoring Wizard**.

**To validate your device metadata by using the Device Metadata Authoring Wizard**

1.  Open the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86.
2.  Click **Validate Metadata**.
3.  On the **Select metadata package to validate** page, do the following:
    -   Under the **Device metadata package** heading, click **Browse** to select your .devicemanifest-ms file, or click **Select from local metadata store** if you've already deployed your device metadata locally.
    -   If you want to validate against a Windows Store app, select the **Validate the device metadata package against a Windows Store device app** check box, and then click **Browse** to choose the Windows Store app package (.appx).
    -   If you want to validate against a device, select the **Validate the device metadata package against a device** check box, click **Select from devices**, choose your device, and then click **OK.**

4.  Click **Validate**.
5.  After validation is done, you can save the report. Click **Close**.
    **Caution**  You might get an error in the validation report saying "The experience ID does not match between storeManifest.xml in the app package and packageInfo.xml in the device metadata file." You can safely ignore this message.

     

## <span id="Next_step"></span><span id="next_step"></span><span id="NEXT_STEP"></span>Next step


[Step 5: Submit the app](step-5--submit-the-app.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devapps\devapps]:%20Step%204:%20Test%20the%20device%20metadata%20for%20your%20Windows%20Store%20device%20app%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




