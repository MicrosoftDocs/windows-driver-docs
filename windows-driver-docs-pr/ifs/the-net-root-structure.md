---
title: The NET_ROOT Structure
description: The NET_ROOT Structure
ms.assetid: f7846343-9af6-4b7f-9c8d-190abb524946
keywords:
- net root structure WDK RDBSS
- network server share connection data WDK RDBSS
- NET_ROOT structure
- server share connection data WDK RDBSS
- root structure WDK RDBSS
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

# The NET_ROOT Structure


## <span id="ddk_the_net_root_structure_if"></span><span id="DDK_THE_NET_ROOT_STRUCTURE_IF"></span>


A net root structure, NET_ROOT, contains information for each specific network server\\share connection maintained by a network mini-redirector.

A NET_ROOT is what the RDBSS and a network mini-redirector driver want to deal with, not a server. Accordingly, RDBSS normally creates and opens a NET_ROOT structure and calls the network mini-redirector driver responsible for opening the server. The network mini-redirector driver is expected to populate the appropriate fields in the passed in NET_ROOT structure.

A list of the NET_ROOT structures is maintained by RDBSS for each SRV_CALL. Each NET_ROOT structure has a few elements common with other RDBSS structures, along with elements that are unique to a NET_ROOT structure. The RDBSS routines that manage NET_ROOT structures only modify the following elements:

-   Signature and reference count

-   A name and associated table information

-   A back pointer to the associated SRV_CALL structure

-   Size information for the various substructures

-   A lookup table of associated FCB structures

-   Whatever additional storage is request by the network mini-redirector (or the creator of the NET_ROOT data structure)

A NET_ROOT structure also contains a list of RX_CONTEXT structures that are waiting for the NET_ROOT transitioning to be completed before resumption of IRP processing. This typically happens when concurrent requests are directed at a server. One of these requests is initiated while the other requests are queued. Extra space reserved for use by the network mini-redirector begins at the end of the known NET_ROOT data structure so that a network mini-redirector can simply refer to this extra space using context fields from an include file.

The finalization of a NET_ROOT structure consists of two parts:

1.  Destroying the association with all V_NET_ROOTS

2.  Freeing the memory

There can be a delay between these two actions, and a field in the NET_ROOT structure prevents the first step from being duplicated.

 

 




