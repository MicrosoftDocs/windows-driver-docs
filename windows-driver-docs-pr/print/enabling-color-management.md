---
title: Enabling Color Management
author: windows-driver-content
description: Enabling Color Management
ms.assetid: 750d1e44-6d1c-4f18-94cb-20f1f846c0d1
keywords: ["color management WDK print , enabling"]
---

# Enabling Color Management


## <a href="" id="ddk-enabling-color-management-gg"></a>


Color management can be enabled by either an application or a printer driver. Applications can enable color management by either of the following two methods:

-   Calling **SetICMMode** (described in the Microsoft Windows SDK documentation), specifying ICM\_ON.

    This method enables system-controlled color management.

-   Specifying a [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure when calling **CreateDC** to create a print job, and setting either DMICMMETHOD\_SYSTEM, DMICMMETHOD\_DRIVER, or DMICMMETHOD\_DEVICE in the DEVMODE structure's **dmICMMethod** member.

    This method allows the application to select system-controlled, driver-controlled, or device-controlled color management (assuming the specified control type is supported).

Printer drivers can enable color management by setting either DMICMMETHOD\_SYSTEM, DMICMMETHOD\_DRIVER, or DMICMMETHOD\_DEVICE in the **dmICMMethod** member of the driver's default DEVMODE structure. (An application can override the default setting if supplying a DEVMODE structure for **CreateDC**. Additionally, the driver is responsible for storing the user's choice for color management during execution of the driver's [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) function.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Enabling%20Color%20Management%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


