---
title: The SRV_CALL Structure
description: The SRV_CALL Structure
ms.assetid: 9a3bb194-0289-47f4-a5c8-848d8d82cdd7
keywords:
- SRV_CALL structure
- server call context structure WDK RDBSS
- network server connection data WDK RDBSS
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

# The SRV\_CALL Structure


## <span id="ddk_the_srv_call_structure_if"></span><span id="DDK_THE_SRV_CALL_STRUCTURE_IF"></span>


The server call context structure, SRV\_CALL, maintains information about each specific network server connection maintained by a network mini-redirector.

A global list of the SRV\_CALL structures is maintained in global data by RDBSS. Each SRV\_CALL structure has a few elements common with other RDBSS structures, along with elements that are unique to a SRV\_CALL structure. The RDBSS routines that manage SRV\_CALL structures only modify the following elements:

-   Signature and reference count

-   A name and associated table information

-   A list of associated NET\_ROOT entries

-   A set of timing parameters that control how often the network mini-redirector wants to be called by RDBSS in different circumstances (idle timeouts, for example)

-   The associated network mini-redirector driver ID

-   Whatever additional storage is request by the network mini-redirector (or the creator of the SRV\_CALL data structure)

The Unicode name of the SRV\_CALL structure is carried in the structure itself at the end. Extra space reserved for use by the network mini-redirector begins at the end of the known SRV\_CALL data structure so that a network mini-redirector can simply refer to this extra space using context fields from an include file.

The finalization of a SRV\_CALL structure consists of two parts:

1.  Destroying the association with all NET\_ROOTS

2.  Freeing the memory

There can be a delay between these two actions, and a field in the SRV\_CALL structure prevents the first step from being duplicated.

 

 




