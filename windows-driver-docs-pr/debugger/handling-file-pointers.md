---
title: Handling File Pointers
description: Handling File Pointers
ms.assetid: 9bc03ae0-3e03-492a-b8d7-760eeb18106a
keywords: ["SymProxy, file pointers"]
---

# Handling File Pointers


A UNC symbol store supports placing the actual files to be served in a separate location, with the client code finding the location of the files through file pointers. These pointers are generated in the symbol store using SymStore with the **/p** option. This handling is supported with other HTTP-based symbol stores only if the file pointers point to a UNC location that is directly accessible by the client. When SymProxy is loaded into the Web server, file-pointer handling is automatically enhanced. The client no longer needs to be able to directly access the target files because SymProxy serves them through the HTTP interface.

Because this feature is automatically applied, an option exists to turn it off in case you must use the proxy for serving some files and regular file pointer implementation for others. To do this, create a REG\_DWORD called "NoFilePointerHandler" in **HKLM\\Software\\Microsoft\\Symbol Server**. Set this value to 1 (or anything other than 0) to turn off the internal file pointer handler in SymProxy.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Handling%20File%20Pointers%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




