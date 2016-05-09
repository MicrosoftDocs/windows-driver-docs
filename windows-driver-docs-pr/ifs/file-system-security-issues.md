---
title: File System Security Issues
author: windows-driver-content
description: File System Security Issues
ms.assetid: 8c6d6a73-6f88-4b79-8381-5724004a529c
---

# File System Security Issues


## <span id="ddk_file_system_security_issues_if"></span><span id="DDK_FILE_SYSTEM_SECURITY_ISSUES_IF"></span>


The previous section described security considerations in general terms. In addition to general security issues of interest to all drivers, there are specific security issues related to file systems. This section attempts to provide a guide for those file systems looking to implement Windows-style security within their driver. This section discusses those specific issues and how they can be addressed within a file system. This section is not a reference guide nor does it provide a complete list of all possible security threats and how they may be mitigated. But rather, the goal of this section is to identify well known threats and key issues related to security that should be addressed by all file systems. Because the area of security itself is sufficiently broad, this document does not cover all possible security issues or implementations.

This section includes the following topics:

[Semantic Model Checks](semantic-model-checks.md)

[Security Checks](security-checks.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20File%20System%20Security%20Issues%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


