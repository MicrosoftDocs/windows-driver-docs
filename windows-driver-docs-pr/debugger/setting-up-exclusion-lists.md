---
title: Setting Up Exclusion Lists
description: Setting Up Exclusion Lists
ms.assetid: 0b50e8a6-f68c-43e5-b8d5-4b2c40252d38
keywords: ["SymProxy, exclusion lists"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Setting Up Exclusion Lists


In some environments, you may find yourself debugging systems that have a large quantity of modules loaded for which you cannot obtain symbols. This is often the case if you have code that is called by a third-party vendor. This can result in a lot of failed attempts to find symbols, which is time-consuming and clogs up network resources. To alleviate this situation, you can use an *exclusion list* to specify symbols that should be excluded from the search. This feature exists in the client debugger, but you can also configure the SymProxy filter to use its own the exclusion list and prevent such network activity where it is most likely to take up resources.

The exclusion list is made up of the names of the files for which you want to prevent processing. The file names can contain wildcards. For example:

```console
dbghelp.pdb
symsrv.*
mso*
```

The list can be implemented in two ways. The first is in an .ini file, %WINDIR%\\system32\\inetsrv\\Symsrv.ini. A section called "exclusions" should contain the list:

```console
[exclusions]
dbghelp.pdb
symsrv.*
mso*
```

Alternatively, you can store the exclusions in the registry. Create a key named

```text
HKLM\ Software\Microsoft\Symbol Server\Exclusions
```

Store the file name list as string values (REG\_SZ) within this key. The name of the string value acts as the file name to exclude. The contents of the string value can be used as a comment describing why the file is being excluded.

SymProxy reads from the exclusion list every half-hour so that you do not need to restart the Web service to see changes take effect. Add files to the list in the registry or .ini file and wait a short period for the exclusions to be used.

**Note**   SymProxy does not support the use of both Symsrv.ini and the registry. If the .ini file exists, it is used. Otherwise, the registry is checked.

 

 

 





