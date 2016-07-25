---
title: Setting the Directory Path of the Text Logs
description: Setting the Directory Path of the Text Logs
ms.assetid: d56a8f6c-365b-427d-b965-65616ede3d7e
keywords: ["text logs WDK SetupAPI , directory path", "directory paths WDK SetupAPI logging", "LogPath"]
---

# Setting the Directory Path of the Text Logs


By default, the SetupAPI text logs are located in the system Windows directory. The location of the SetupAPI text logs can be changed by setting the following REG\_SZ registry value:

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Setup\\LogPath**

The **LogPath** registry value must be a fully qualified directory path. The path must exist, and the path cannot include a file name.

If the **LogPath** registry value is not present, the path does not exist, or the path includes a file name, SetupAPI locates the text logs in the *%SystemRoot%/Inf* directory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Setting%20the%20Directory%20Path%20of%20the%20Text%20Logs%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




