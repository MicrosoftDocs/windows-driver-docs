---
title: 3D print partner onboarding guide
author: windows-driver-content
description: This topic describes how to implement 3D printer drivers that are then published on Windows Update.
---

# 3D print partner onboarding guide

Joining the Microsoft 3D print ecosystem enables 3D printer manufacturers to offer a great plug-and-play experience on Windows 10. This strategy removes the potential for problems encountered by users when locating and manually installing drivers. Additionally, Windows Update ensures that the users are always using the latest driver for their device and are getting the best experience available.

## 3D print driver overview

A plug-and-play 3D printer on Windows 10 is implemented through a pair of drivers published on Windows Update:

**Upper driver (Render filter)**

-   Implements the slicer. The driver takes [3MF](http://www.3mf.io) as input and produces G-Code or other similar machine level data.

-   Creates the print queue. The device appears under **Devices and Printers** and in the **3D Print Dialog** for compatible [3D Printing applications](https://developer.microsoft.com/en-us/windows/hardware/3d-software-partners).

**Lower driver (USB driver)**

-   Implements wire protocol (typically USB Serial or native USB)

-   Kernel mode driver creates the ENUM\\3DPRINTER device node for the upper driver

-   User mode component (Partner DLL) sends the G-Code to the device

-   Reports device capabilities, job status and implements job cancel

-   Installs 3D print service and the 3D port monitor (3dmon)

## Choosing the right driver model


![onboarding driver models](images/onboarding-driver-models.png)

## 3D print driver with custom slicer

1. Obtain and verify the device USB hardware ID

    - Ensure the device firmware has a unique Vendor ID and Product ID (VID/PID) allocated by the [USB Implementers Forum (USB-IF)](http://www.usb.org). For USBSER devices, we strongly recommended that you use a unique serial number to prevent conflicts on a USB port changes.

2. Install Microsoft tools and SDKs 

    - Download and install [Visual Studio Community Edition](https://go.microsoft.com/fwlink/p/?LinkId=534599)

    - Download and install the [Windows 10 SDK](https://go.microsoft.com/fwlink/p/?LinkID=822845)

    - Download and install the [3D printing SDK](http://go.microsoft.com/fwlink/p/?LinkId=394375)

        - **Note** The 3D printing SDK will be installed in C:\\Program Files (x86)\\Microsoft SDKs\\3D Printing.

3. Implement the USB driver

    - A manufacturer can use the Microsoft USB driver for their 3D printer by creating a partner DLL. For more information, see [3D printer custom USB interface support](3d-printer-custom-usb-interface.md).

    - If the printer is using the Microsoft Slicer, the Hardware ID that it creates must be **Enum\\3DPrint\\MS3DPrint**

**Note** If the the printer is using a custom slicer, continue with steps 4-7

4. Build the Fabrikam driver (slicer template only)

    - Build and obtain the driver package. This creates a x64 folder with the slicer part.

5. Adding the custom slicer

    - Modify the cpp file to include:

        -   3MF parser (use the Windows 10 version 1607 3MF API)

        -   Write G-Code

6. Adding the printer node

    - Open the inf in Fabrikam Print driver

    - Replace the entries hardware IDs:

        ```
        %DeviceName%=FabrikamPrintDriverV4\_Install,3DPRINTER\\Fabrikam1

        %DeviceNamePlus%=FabrikamPrintDriverV4\_Install,3DPRINTER\\Fabrikam2

        DeviceName="CONTOSO FABRIKAM 1"

        DeviceNamePlus="CONTOSO FABRIKAM 2"
        ```

7. Publish and distribute the driver

    - Follow the steps in these topics to publish your driver:
        
        - [Purchase an extended validation (EV) code signing certificate](https://msdn.microsoft.com/en-us/library/windows/hardware/hh801887(v=vs.85).aspx)

        - [Publish the driver using the designated workflow](https://msdn.microsoft.com/en-us/library/windows/hardware/br230778(v=vs.85).aspx)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")

