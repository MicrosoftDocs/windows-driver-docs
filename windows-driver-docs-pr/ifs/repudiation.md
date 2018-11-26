---
title: Repudiation
description: Repudiation
ms.assetid: ccb50b6c-9e7d-4a90-a049-6c62b1b57376
keywords:
- threat models WDK file systems , repudiation
- security threat models WDK file systems , repudiation
- repudiation WDK file systems
- ownership WDK file systems
- denying performed operation WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Repudiation


## <span id="ddk_repudiation_if"></span><span id="DDK_REPUDIATION_IF"></span>


The concept of repudiation is that a user might perform a particular operation, and then subsequently deny having performed it. For most drivers this is an unusual type of issue. For a file system, however, logging is used to track operations (deletion of important files, for example) and ensure that there is a clear trail of operations. This provides a mechanism for ensuring against such repudiation.

Additionally, the operating system can assign ownership of objects to specific security identifiers. The ownership information cannot be changed without appropriate privileges (**SeTakeOwnershipPrivilege**) in order to ensure that ownership of specific objects can be tracked. Object ownership provides another form of protection against repudiation.

 

 




