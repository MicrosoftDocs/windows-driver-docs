---
title: Printer INF File CopyFiles Sections
author: windows-driver-content
description: Printer INF File CopyFiles Sections
ms.assetid: 92c96019-d2dd-4b2c-818a-80ae091ec662
keywords:
- INF files WDK print , CopyFiles sections
- sections WDK printer
- CopyFiles directive
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer INF File CopyFiles Sections


## <a href="" id="ddk-printer-inf-file-copyfiles-sections-gg"></a>


When a printer INF file contains a file list section that is referenced by an [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346), each file in the file list must be specified using the following format:

**\[***file-list-section***\]**
*destination-file-name\[,,flag\]*
*destination-file-name\[,,flag\]*
*destination-file-name\[,,flag\]*
...
The *destination-file-name* field is required, and the *flag* field is optional. File specifications must not include the optional *source-file-name* or *temporary-file-name* fields that are defined for file list sections used with the INF CopyFiles directive. This restriction is required for installing print drivers from a Web page.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20INF%20File%20CopyFiles%20Sections%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


