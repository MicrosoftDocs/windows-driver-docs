---
title: Security considerations for reparse points
description: File System Filter Driver security considerations for reparse points
keywords:
- security WDK file systems , reparse points
- reparse points WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Security considerations for reparse points


A filter driver that processes reparse points must be aware of the risk that an application program might create invalid reparse points. To ensure the strictest security, a driver that handles reparse points must ensure that the data contents of the reparse point itself are verifiable, whether through a secure checksum, encrypted contents, or some other mechanism that ensures invalid reparse points cannot be created by unprivileged applications. For example, a filter driver might require that its reparse points be encrypted using a password shared between an application (or the local security authority, for example), and the driver, in order to ensure that the data contents of the reparse point are valid.

Otherwise, it is possible that a malicious application could create reparse points that have invalid reparse point information. In this case, the file system filter driver must be prepared to handle invalid reparse point data, including self-referential data (data that creates reference loops that might cause some sort of overflow, for example), data overflow issues, and invalid data contents.

 

 




