---
title: Gcdef.dll, the Default Analog Device Property Sheet
author: windows-driver-content
description: Gcdef.dll, the Default Analog Device Property Sheet
MS-HAID:
- 'di\_6d7b0dc9-e41d-4258-b9b8-cfa2a06e6319.xml'
- 'hid.gcdef\_dll\_\_the\_default\_analog\_device\_property\_sheet'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a8226abb-11c1-4425-93d8-b74e1960ba10
keywords: ["Gcdef.dll", "default analog device property sheet", "property sheets WDK DirectInput , Gcdef.dll", "game controllers WDK DirectInput , Gcdef.dll", "control panels WDK DirectInput , Gcdef.dll"]
---

# Gcdef.dll, the Default Analog Device Property Sheet


## <a href="" id="ddk-gcdef-dll-the-default-analog-device-property-sheet-di"></a>


Hardware vendors who do not create their own control panel use the services of the default analog device property sheet supplied by Gcdef.dll. Any controller that does not have a **ConfigCLSID** key in the registry under its **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM\\***CONTROLLER\_NAME* entry uses this default property sheet. This property sheet contains the following two pages:

-   **Test:** This page demonstrates that the device is responding properly. It returns a graphical representation of the registry settings that are associated with the device attributes and allows the user to view them.

-   **Settings:** This page allows the user to write specific information about the device to the system. Services are provided for calibration and for a rudder or pedals.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Gcdef.dll,%20the%20Default%20Analog%20Device%20Property%20Sheet%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


