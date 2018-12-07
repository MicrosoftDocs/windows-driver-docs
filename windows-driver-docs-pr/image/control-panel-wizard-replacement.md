---
title: Control Panel Wizard Replacement
description: Control Panel Wizard Replacement
ms.assetid: d4a418b6-a9f9-41c4-99a9-20992abe80e9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control Panel Wizard Replacement





When the driver's icon (from the Control Panel, Scanners and Cameras), is double-clicking the default UI Scanner and Camera Wizard is displayed instead of the Vendor UI. This wizard is not replaceable using the same mechanism as the common dialog. It is possible to display your Vender UI from the Control Panel.

To display your Vendor UI from the Control Panel you will have to:

-   Register your acquisition application as the default persistent event handler for his device.

-   Write a custom wizard.

There is no relationship at all between the custom wizard and the dialog you replaced using the [**IWiaUIExtension::DeviceDialog**](https://msdn.microsoft.com/library/windows/hardware/ff545069) interface. But, please be careful. The icon in control panel will always default to the wizard in Windows Me and Windows XP. The user would have to right click and choose Scan explicitly to show the default WIA\_EVENT\_SCAN\_IMAGE event handler. In My Computer the opposite is true; whatever default handler you select will be the one used when the user double clicks on the device icon.

 

 




