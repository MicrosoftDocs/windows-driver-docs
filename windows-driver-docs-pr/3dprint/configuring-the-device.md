---
title: Configuring the device
description: To configure the device, you should have a 3D printer device in the Devices and Printers Control Panel and can print to G-Code using the Microsoft Slicer.
ms.assetid: 897081C3-47A4-46A0-9A45-A49E4569216D
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




