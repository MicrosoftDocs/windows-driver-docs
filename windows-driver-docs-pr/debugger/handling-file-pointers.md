---
title: Handling File Pointers
description: Handling File Pointers
ms.assetid: 9bc03ae0-3e03-492a-b8d7-760eeb18106a
keywords: ["SymProxy, file pointers"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Handling File Pointers


A UNC symbol store supports placing the actual files to be served in a separate location, with the client code finding the location of the files through file pointers. These pointers are generated in the symbol store using SymStore with the **/p** option. This handling is supported with other HTTP-based symbol stores only if the file pointers point to a UNC location that is directly accessible by the client. When SymProxy is loaded into the Web server, file-pointer handling is automatically enhanced. The client no longer needs to be able to directly access the target files because SymProxy serves them through the HTTP interface.

Because this feature is automatically applied, an option exists to turn it off in case you must use the proxy for serving some files and regular file pointer implementation for others. To do this, create a REG\_DWORD called "NoFilePointerHandler" in **HKLM\\Software\\Microsoft\\Symbol Server**. Set this value to 1 (or anything other than 0) to turn off the internal file pointer handler in SymProxy.

 

 





