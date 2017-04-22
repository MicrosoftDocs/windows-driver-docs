---
title: Getting the Updated Core Driver Package
author: windows-driver-content
description: Getting the Updated Core Driver Package
ms.assetid: 7fac00e4-1d3e-4bb7-95cd-298176de374d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Getting the Updated Core Driver Package


After you [obtain](constructing-a-package-aware-driver-with-updated-core-drivers.md) the Microsoft standalone update (MSU) file containing the updated core driver package, the next step is to expand the contents of the MSU file.

To make the contents of the core driver package accessible to the PnP installer, open a Command Prompt window and use the expand command to expand the MSU file. Also expand the appropriate cabinet (.cab) file, which has a name that starts with "Windows6.0-", that is contained in the MSU file.

The following example shows how to use the **expand** command, which should be executed in the directory that contains the MSU file:

```
expand Windows6.0-KB123456-x86.MSU [dest directory] -F:*
expand Windows6.0-KB123456-x86.CAB [dest directory] -F:*
```

Following these two commands, the directory will contain a number of manifest files and subdirectories. One of these subdirectories will contain Ntprint.inf and the uncompressed driver components. This directory has a name that begins with the processor architecture for the fix (for example, x86), to which is appended "ntprint.inf", a GUID, and additional tracking information. For more information, see the definition of the **expand** command on the Microsoft [TechNet](http://go.microsoft.com/fwlink/p/?linkid=122164) Web site.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Getting%20the%20Updated%20Core%20Driver%20Package%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


