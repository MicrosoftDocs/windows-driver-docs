---
title: Internal and External Version Numbers
description: Internal and External Version Numbers
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
ms.date: 10/22/2024
---

# Internal and External Version Numbers


## <span id="internal_and_external_version_numbers"></span><span id="INTERNAL_AND_EXTERNAL_VERSION_NUMBERS"></span>

The driver's resource file specifies the driver-file version in two ways:

- **Internal version number:** the internal or binary version number is specified in the double-DWORD value **FILEVERSION**. The operating system currently does not use this value.

- **External version number:** the external or display version number is specified in the **FileVersion** character string. The operating system displays this string when the user views the properties of individual driver files.

In Windows 10 there are several alternative ways to view a driver file's **FileVersion** string:

- In File Explorer:

    1. Go to the location of the driver file. Typically, this is in the **C:\Windows\System32\drivers** folder.
    1. **Select** the driver file. Driver files usually have a **.sys** extension.
    1. Right-click on the driver file and select **Properties** from the context menu.
    1. In the Properties window, go to the **Details** tab. Here you can see the **File version** and **Product version** numbers.

- In Device Manager:

    1. Expand the **Sound, video and game controllers** section.
    1. Right-click on your audio device and select **Properties**.
    1. Go to the **Driver** tab to see the **Driver Version**.
    1. On the Driver tab, click on **Driver Details** to view details about the installed driver files.
    1. Select the driver file from the list of files in the driver package, and view the **File version** number of the selected driver file.

- In Control Panel:

    1. Click the **Hardware and Sound** icon.
    1. Click the **Sound** icon.
    1. On the **Sound** window, select the device and click the **Properties** button.
    1. On the **General** tab select **Properties**.
    1. Go to the **Driver** tab to see the **Driver Version**.
    1. On the Driver tab, click on **Driver Details** to view details about the installed driver files.
    1. Select the driver file from the list of files in the driver package, and view the **File version** number of the selected driver file.

To make your driver version numbers compatible with both Windows and DirectX, follow these rules when you specify the internal and external version numbers:

- The internal version number has the format *x*.*xx*.00.*xxxx*. The two extra zeros before the last dot are required.

- The external version string should use the format *x*.*xx*.*xxxx* (without the two extra zeros in the internal version number).

These internal and external version numbers should match (except for the two extra zeros, as noted above).

 

 




