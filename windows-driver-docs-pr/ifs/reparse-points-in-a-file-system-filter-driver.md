---
title: Reparse Points in a File System Filter Driver
description: Reparse Points in a File System Filter Driver
ms.assetid: 6aae70d9-c934-4759-bb26-728b0ac025d1
keywords:
- security WDK file systems , reparse points
- reparse points WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reparse Points in a File System Filter Driver


## <span id="ddk_reparse_points_in_a_file_system_filter_driver_if"></span><span id="DDK_REPARSE_POINTS_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


A filter driver that processes reparse points must be aware of the risk that an application program might create invalid reparse points. To ensure the strictest security, a driver that handles reparse points must ensure that the data contents of the reparse point itself are verifiable, whether through a secure checksum, encrypted contents, or some other mechanism that ensures invalid reparse points cannot be created by unprivileged applications. For example, a filter driver might require that its reparse points be encrypted using a password shared between an application (or the local security authority, for example), and the driver, in order to ensure that the data contents of the reparse point are valid.

Otherwise, it is possible that a malicious application could create reparse points that have invalid reparse point information. In this case, the file system filter driver must be prepared to handle invalid reparse point data, including self-referential data (data that creates reference loops that might cause some sort of overflow, for example), data overflow issues, and invalid data contents.

 

 




