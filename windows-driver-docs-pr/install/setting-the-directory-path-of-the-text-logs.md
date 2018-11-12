---
title: Setting the Directory Path of the Text Logs
description: Setting the Directory Path of the Text Logs
ms.assetid: d56a8f6c-365b-427d-b965-65616ede3d7e
keywords:
- text logs WDK SetupAPI , directory path
- directory paths WDK SetupAPI logging
- LogPath
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Directory Path of the Text Logs


By default, the SetupAPI text logs are located in the system Windows directory. The location of the SetupAPI text logs can be changed by setting the following [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) registry value:

**HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Setup\\LogPath**

The **LogPath** registry value must be a fully qualified directory path. The path must exist, and the path cannot include a file name.

If the **LogPath** registry value is not present, the path does not exist, or the path includes a file name, SetupAPI locates the text logs in the *%SystemRoot%/Inf* directory.

 

 





