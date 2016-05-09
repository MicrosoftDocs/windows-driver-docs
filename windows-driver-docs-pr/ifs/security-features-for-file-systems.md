---
title: Security Features for File Systems
description: Security Features for File Systems
ms.assetid: 344083d5-781a-46e3-ab90-b70e57d07dd0
keywords: ["security WDK file systems , features"]
---

# Security Features for File Systems


## <span id="ddk_security_features_for_file_systems_if"></span><span id="DDK_SECURITY_FEATURES_FOR_FILE_SYSTEMS_IF"></span>


Unlike most other types of drivers, file systems are intimately involved in normal security processing. This is because of the nature of security and its implementation within Microsoft Windows. The general Windows security model associates a security descriptor with an object--in this case, the FILE\_OBJECT. File systems that support Windows security are responsible for storing and retrieving security descriptors. In addition, file systems are responsible for handing several other special security considerations that fall outside the normal scope of standard kernel-mode drivers.

This section discusses key features that may be added to a file system to support Windows security. None of these are mandatory and file systems can be constructed without using any of these interfaces. Further, it is possible to implement some security features while ignoring others--this is specific to the implementation of the file system.

This section includes the following topics:

[Security Descriptors](security-descriptors.md)

[Privileges](privileges.md)

[Auditing](auditing.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Security%20Features%20for%20File%20Systems%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




