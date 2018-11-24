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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




