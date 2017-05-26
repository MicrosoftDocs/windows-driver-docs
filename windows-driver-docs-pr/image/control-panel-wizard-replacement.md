---
title: Control Panel Wizard Replacement
author: windows-driver-content
description: Control Panel Wizard Replacement
ms.assetid: d4a418b6-a9f9-41c4-99a9-20992abe80e9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Control Panel Wizard Replacement


## <a href="" id="ddk-control-panel-wizard-replacement-si"></a>


When the driver's icon (from the Control Panel, Scanners and Cameras), is double-clicking the default UI Scanner and Camera Wizard is displayed instead of the Vendor UI. This wizard is not replaceable using the same mechanism as the common dialog. It is possible to display your Vender UI from the Control Panel.

To display your Vendor UI from the Control Panel you will have to:

-   Register your acquisition application as the default persistent event handler for his device.

-   Write a custom wizard.

There is no relationship at all between the custom wizard and the dialog you replaced using the [**IWiaUIExtension::DeviceDialog**](https://msdn.microsoft.com/library/windows/hardware/ff545069) interface. But, please be careful. The icon in control panel will always default to the wizard in Windows Me and Windows XP. The user would have to right click and choose Scan explicitly to show the default WIA\_EVENT\_SCAN\_IMAGE event handler. In My Computer the opposite is true; whatever default handler you select will be the one used when the user double clicks on the device icon.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Control%20Panel%20Wizard%20Replacement%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


