---
title: 3D print partner onboarding guide
author: windows-driver-content
description: TBD
---

# 3D print partner onboarding guide

Joining the Microsoft 3D Print ecosystem allows for any 3D Printer to offer a great Plug-and-Play experience on Windows 10. This strategy removes the hassle encountered by user to find and manually install their drivers. Additionally, Windows Update will ensure that the users are always using the latest driver for their device and are getting the best experience available.

## 3D print driver overview

A Plug-and-Play 3D Printer on Windows 10 is implemented through a pair of drivers published on Windows Update:

**Upper driver (Render filter)**

-   Implements the *slicer*: it takes 3MF (www.3mf.io) as input and produces G-Code or other similar machine level data

-   Creates the Print Queue: this makes the device show up under **Devices and Printers** and in the **3D Print Dialog** for compatible [3D Printing applications](https://developer.microsoft.com/en-us/windows/hardware/3d-software-partners).

**Lower driver (USB driver)**

-   Implements wire Protocol (typically USB Serial or native USB)

-   Kernel mode driver creates the ENUM\\3DPRINTER device node for the upper driver

-   User mode component (Partner DLL) sends the G-Code to the device

-   Reports device capabilities, job status and implements job cancel

-   Installs 3D Print Service and the 3D Port Monitor (3dmon)

## Choosing the right driver model


![onboarding driver models](images/onboarding-driver-models.png)

## 3D print driver with custom slicer

1. Obtain and verify the device USB hardware ID

    - Ensure the device firmware has a unique Vendor ID and Product ID (VID/PID) allocated by the [USB Implementers Forum (USB-IF)](http://www.usb.org). For USBSER devices, we strongly recommended that you use a unique serial number to prevent conflicts on a USB port changes.

2. Install Microsoft tools and SDKs 

    - Download and install [Visual Studio Community Edition](TBD)

    - Download and install the [Windows 10 SDK](TBD)

    - Download and install the [3D printing SDK](http://go.microsoft.com/fwlink/p/?LinkId=394375)

        - **Note** The 3D printing SDK will be installed in C:\\Program Files (x86)\\Microsoft SDKs\\3D Printing.

3. Implement the USB driver

    - A manufacturer can use the Microsoft USB Driver for its 3D printer by creating a partner DLL

    - According to the documentation here \[Link to Partner Driver Design Documentation\]

    - If the printer is using the Microsoft Slicer, the Hardware ID that it creates has to be Enum\\3DPrint\\MS3DPrint

**Note** If the the printer is using a custom slicer, continue with steps 4-7

4. Build the Fabrikam driver (slicer template only)

    - Build and obtain the driver package. This creates a x64 folder with the slicer part.

5. Adding the custom slicer

    - Modify the cpp file to include:

        -   3MF Parser (use the RS1 3MF API)

        -   Write GCode

6. Adding the printer node

    - Open the inf in Fabrikam Print driver.

    - Replace the entries hardware IDs with the CONTOSO ones.

        ```
        %DeviceName%=FabrikamPrintDriverV4\_Install,3DPRINTER\\Fabrikam1

        %DeviceNamePlus%=FabrikamPrintDriverV4\_Install,3DPRINTER\\Fabrikam2

        DeviceName="CONTOSO FABRIKAM 1"

        DeviceNamePlus=”CONTOSO FABRIKAM 2”
        ```

7. Publish to Sysdev 

    - [Purchase an EV certificate](https://msdn.microsoft.com/en-us/library/windows/hardware/hh801887(v=vs.85).aspx)

    - [Publish the driver through sysdev](https://msdn.microsoft.com/en-us/library/windows/hardware/br230778(v=vs.85).aspx)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")

