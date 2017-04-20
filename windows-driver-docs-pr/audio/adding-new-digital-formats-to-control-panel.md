---
title: Adding New Digital Formats to Control Panel
description: Adding New Digital Formats to Control Panel
ms.assetid: ce36738c-6471-4b68-82ad-80b8509c052b
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding New Digital Formats to Control Panel


In Windows Vista and later versions of Windows, you can develop a third-party digital audio format that streams over SPDIF and make this format available in Control Panel.

After you develop your digital audio format, define a new GUID for the format and use an INF file to install the associated audio driver. The following code from an INF file shows how to add the necessary information about your new digital audio format to the registry:

```
[Version]
Signature=$WindowsNT$
...
[DDInstall]
AddReg = AddReg.NewDigitalFormat
...
...
[AddReg.NewDigitalFormat]
HKLM, %My_SubKey%, "DisplayName",,"ABC Audio"
HKLM, %My_SubKey%, "CustomIcon",,"c:\Program Files\MyVendor\myicon.ico"
HKLM, %My_SubKey%, "TestFile",,"c:\Program Files\MyVendor\testfile.wav"
...
[Strings]
My_SubKey = "SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\SPDIF_Formats\{00000682-0000-0010-8000-00aa00389b71}"
...
...
```

In the preceding example, the GUID shown in the \[Strings\] section is used to illustrate the placement of the GUID that you define for your new digital format. HKLM is used as the standard abbreviation for HKEY\_LOCAL\_MACHINE.

**Important**  The two HKLM line entries for Mycion.ico and Testfile.wav are required. The "c:\\Program Files\\MyVendor\\" folder has been used to show that you must create an appropriate folder for your driver-related icon and test wave files.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Adding%20New%20Digital%20Formats%20to%20Control%20Panel%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


