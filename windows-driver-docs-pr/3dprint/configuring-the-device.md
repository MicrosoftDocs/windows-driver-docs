---
title: Configuring the device
author: windows-driver-content
description: To configure the device, you should have a 3D printer device in the Devices and Printers Control Panel and can print to G-Code using the Microsoft Slicer.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 897081C3-47A4-46A0-9A45-A49E4569216D
---

# Configuring the device


To configure the device, you should have a 3D printer device in the **Devices and Printers** Control Panel and can print to G-Code using the Microsoft Slicer.

Next you will need to change the Slicer and advanced settings in the configuration file.

There are two configuration files that control the printer properties and the slicer settings.

When printing to a hardware device: 

- **C:\\Windows\\System32\\MS3DPrint\\StandardGCode\*.XML** – this is used by StandardGCode.DLL and can change from device to device, depending on the registry mapping defined in the **ConfigurationXML** key under:

    - Per printer queue: HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\3DPRINTER\\{PrinterName}\\{node}

    - Per hardware ID: HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USB\\{VID&PID}\\{DeviceSerial}\\Device Parameters\\

When printing to a file (no USB driver present):

- **C:\\Windows\\System32\\Spool\\Drivers\\x64\\3\\MS3DPrinterDeviceConfig.xml** – this is global and used by the slicer.

For simplicity, edit the **MS3DPrinterDeviceConfig.xml** file as an **Administrator** if you are using the **Print to File** function (G-Code file) with no physical device attached and edit **StandardGCode.XML** when printing to a physical device.

Now you are ready to 3D print from an application like the 3D Builder app in Windows, or any store or desktop application that implements Windows native 3D printing.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Configuring%20the%20device%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


