---
title: Adding New Digital Formats to Control Panel
description: Adding New Digital Formats to Control Panel
ms.date: 09/29/2022
---

# Adding New Digital Formats to Control Panel


In Windows Vista and later versions of Windows, you can develop a third-party digital audio format that streams over SPDIF and make this format available in Control Panel.

After you develop your digital audio format, define a new GUID for the format and use an INF file to install the associated audio driver. The following code from an INF file shows how to add the necessary information about your new digital audio format to the registry:

```inf
[Version]
Signature=$WindowsNT$
...
[DDInstall]
AddReg = AddReg.NewDigitalFormat
...
...
[AddReg.NewDigitalFormat]
HKR, %My_SubKey%, "DisplayName",,"ABC Audio"
HKR, %My_SubKey%, "CustomIcon",,"c:\Program Files\MyVendor\myicon.ico"
HKR, %My_SubKey%, "TestFile",,"c:\Program Files\MyVendor\testfile.wav"
...
[Strings]
My_SubKey = "MMDevices\SPDIF_Formats\{00000682-0000-0010-8000-00aa00389b71}"
...
...
```

In the preceding example, the GUID shown in the \[Strings\] section is used to illustrate the placement of the GUID that you define for your new digital format. 

**Important**  The two HKR line entries for Mycion.ico and Testfile.wav are required. The "c:\\Program Files\\MyVendor\\" folder has been used to show that you must create an appropriate folder for your driver-related icon and test wave files.

 

 

 




