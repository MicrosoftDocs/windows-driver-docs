---
title: Introduction to File Systems Security
description: Introduction to File Systems Security
ms.assetid: 328568dc-a003-4e00-941a-9ccf15b1c735
keywords: ["security WDK file systems , about file system security"]
---

# Introduction to File Systems Security


## <span id="ddk_introduction_to_file_systems_security_if"></span><span id="DDK_INTRODUCTION_TO_FILE_SYSTEMS_SECURITY_IF"></span>


File system developers who use the WDK should be aware of security considerations during the implementation of their file systems. File system filter driver developers should also be aware of these issues, and should be familiar with the Microsoft Windows security interfaces in order to incorporate security considerations into their products.

This section focuses on Windows security and file systems. It is not intended to be a primer for those who want to develop security extensions for Windows, or for file system developers who want to implement a non-Windows security model within the Windows environment.

This section includes a number of code samples. The samples are extracted from real-world code, but are presented here in abbreviated form. Developers should adapt these samples for use in their particular environment.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Introduction%20to%20File%20Systems%20Security%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




