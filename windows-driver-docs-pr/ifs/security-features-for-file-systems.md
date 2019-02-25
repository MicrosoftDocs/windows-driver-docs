---
title: Security Features for File Systems
description: Security Features for File Systems
ms.assetid: 344083d5-781a-46e3-ab90-b70e57d07dd0
keywords:
- security WDK file systems , features
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Security Features for File Systems


## <span id="ddk_security_features_for_file_systems_if"></span><span id="DDK_SECURITY_FEATURES_FOR_FILE_SYSTEMS_IF"></span>


Unlike most other types of drivers, file systems are intimately involved in normal security processing. This is because of the nature of security and its implementation within Microsoft Windows. The general Windows security model associates a security descriptor with an object--in this case, the FILE\_OBJECT. File systems that support Windows security are responsible for storing and retrieving security descriptors. In addition, file systems are responsible for handing several other special security considerations that fall outside the normal scope of standard kernel-mode drivers.

This section discusses key features that may be added to a file system to support Windows security. None of these are mandatory and file systems can be constructed without using any of these interfaces. Further, it is possible to implement some security features while ignoring others--this is specific to the implementation of the file system.

This section includes the following topics:

[Security Descriptors](security-descriptors.md)

[Privileges](privileges.md)

[Auditing](auditing.md)

[Kernel Extended Attributes](kernel-extended-attributes.md)

 


