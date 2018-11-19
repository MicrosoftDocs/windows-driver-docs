---
title: The SRV_OPEN Structure
description: The SRV_OPEN Structure
ms.assetid: 6cf4c6f6-a21f-4919-92b5-2403b650d8d0
keywords:
- server open WDK RDBSS
- open servers WDK RDBSS
- SRV_OPEN structure
- data structures WDK file systems
- RDBSS WDK file systems , connection and file structures
- Redirected Drive Buffering Subsystem WDK file systems , connection and file structures
- connection structures WDK RDBSS
- file structures WDK RDBSS
- structures WDK RDBSS
- connection information WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The SRV\_OPEN Structure


## <span id="ddk_the_srv_open_structure_if"></span><span id="DDK_THE_SRV_OPEN_STRUCTURE_IF"></span>


The SRV\_OPEN structure describes a specific open on the server. Multiple file objects and file object extensions (FOBXs) can share the same SRV\_OPEN structure if the access rights match. For example, where the file ID is stored for SMBs. A list of the file IDs is associated with the FCB. Similarly, all file object extensions that share the same server-side open are listed together here. Also, information is stored about whether a new open of the FCB can share the server-side open context.

The flag values that affect SRV\_OPEN operations are split into two groups:

-   Flags visible to network mini-redirectors

-   Private flags used internally by RDBSS and invisible to network mini-redirectors

The flags visible to network mini-redirectors consist of the lower 16 bits of the possible SRV\_OPEN flags. The upper 16 bits are reserved for use internally by RDBSS.

A SRV\_OPEN structure contains the following:

-   Signature and reference count

-   A backpointer to the FCB structure

-   A backpointer to the V\_NET\_ROOT structure (usually)

-   A list of FOBX structures

-   Access rights and collapsibility status

-   Additional storage requested by the network mini-redirector or the creator of the SRV\_OPEN structure

 

 




