---
title: Internal and External Version Numbers
description: Internal and External Version Numbers
ms.assetid: 705a2e5f-11b8-499c-815d-a2a54e907980
keywords:
- version numbers WDK audio
- audio miniport drivers WDK , version numbers
- miniport drivers WDK audio , version numbers
- audio drivers WDK , version numbers
- internal version numbers WDK audio
- external version numbers WDK audio
- files WDK audio
- driver-file version numbers WDK audio
- driver version numbers WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Internal and External Version Numbers


## <span id="internal_and_external_version_numbers"></span><span id="INTERNAL_AND_EXTERNAL_VERSION_NUMBERS"></span>


The driver's resource file specifies the driver-file version in two ways:

-   As an internal or binary version number that is specified in the double-DWORD value **FILEVERSION**. The operating system currently does not use this value.

-   As an external or display version number that is specified in the **FileVersion** character string. The operating system displays this string when the user views the properties of individual driver files.

Under the Windows XP user interface, for example, there are several alternative ways to view a driver file's **FileVersion** string:

-   In Windows Explorer:

-   1.  Right-click the file icon.
    2.  Select the **Properties** of the driver file.
    3.  On the **Version** tab, view the **File version** number.
-   In Device Manager:

-   1.  Select the **Properties** of a particular audio device.
    2.  On the **Driver** tab click **Driver Details**.
    3.  Select the driver file from the list of files in the driver package.
    4.  view the **File version** number of the selected driver file.
-   In Control Panel:

-   1.  Click the **Sounds and Audio Devices** icon.
    2.  On the **Hardware** tab select the device, click the **Properties** button.
    3.  On the **Driver** tab select **Driver Details**, select the driver file from the list of files in the driver package, and view the **File version** number of the selected driver file.

To make your driver version numbers compatible with both Windows and DirectX, follow these rules when you specify the internal and external version numbers:

-   The internal version number has the format *x*.*xx*.00.*xxxx*. The two extra zeros before the last dot are required.

-   The external version string should use the format *x*.*xx*.*xxxx* (without the two extra zeros in the internal version number).

These internal and external version numbers should match (except for the two extra zeros, as noted above).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Internal%20and%20External%20Version%20Numbers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


