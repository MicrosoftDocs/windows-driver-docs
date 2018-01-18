---
title: Setting Up Exclusion Lists
description: Setting Up Exclusion Lists
ms.assetid: 0b50e8a6-f68c-43e5-b8d5-4b2c40252d38
keywords: ["SymProxy, exclusion lists"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Exclusion Lists


In some environments, you may find yourself debugging systems that have a large quantity of modules loaded for which you cannot obtain symbols. This is often the case if you have code that is called by a third-party vendor. This can result in a lot of failed attempts to find symbols, which is time-consuming and clogs up network resources. To alleviate this situation, you can use an *exclusion list* to specify symbols that should be excluded from the search. This feature exists in the client debugger, but you can also configure the SymProxy filter to use its own the exclusion list and prevent such network activity where it is most likely to take up resources.

The exclusion list is made up of the names of the files for which you want to prevent processing. The file names can contain wildcards. For example:

```
dbghelp.pdb
symsrv.*
mso*
```

The list can be implemented in two ways. The first is in an .ini file, %WINDIR%\\system32\\inetsrv\\Symsrv.ini. A section called "exclusions" should contain the list:

```
[exclusions]
dbghelp.pdb
symsrv.*
mso*
```

Alternatively, you can store the exclusions in the registry. Create a key named

```
HKLM\ Software\Microsoft\Symbol Server\Exclusions
```

Store the file name list as string values (REG\_SZ) within this key. The name of the string value acts as the file name to exclude. The contents of the string value can be used as a comment describing why the file is being excluded.

SymProxy reads from the exclusion list every half-hour so that you do not need to restart the Web service to see changes take effect. Add files to the list in the registry or .ini file and wait a short period for the exclusions to be used.

**Note**   SymProxy does not support the use of both Symsrv.ini and the registry. If the .ini file exists, it is used. Otherwise, the registry is checked.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Exclusion%20Lists%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




