---
title: The V_NET_ROOT Structure
description: The V_NET_ROOT Structure
ms.assetid: 866eba91-13b6-4b15-93de-4f627a635c92
keywords:
- share mapping WDK RDBSS
- V_NET_ROOT structure WDK RDBSS
- mapping shares
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

# The V\_NET\_ROOT Structure


## <span id="ddk_the_v_net_root_structure_if"></span><span id="DDK_THE_V_NET_ROOT_STRUCTURE_IF"></span>


The V\_NET\_ROOT structure provides a mechanism for mapping into a share (for example, a user drive mapping that points below the root of the associated share point). The V\_NET\_ROOT name can be in one of the following formats:

```cpp
\server\share\d1\d2
\;m:\server\share\d1\d2
```

The format of the name depends on whether there is a local device ("X:", for example) associated with this V\_NET\_ROOT structure. In the case of a local drive mapping (d1\\d2, for example), the local drive mapping gets prefixed onto each [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) that is opened on this V\_NET\_ROOT structure.

V\_NET\_ROOT structures are also used to supply alternate credentials. The purpose for this kind of a V\_NET\_ROOT structure is to propagate the alternate credentials into the NET\_ROOT as the default. For this to work, there must be no other references.

A list of the V\_NET\_ROOT structures is maintained by RDBSS for each NET\_ROOT. Each V\_NET\_ROOT structure has a few elements common with other RDBSS structures, along with elements that are unique to a V\_NET\_ROOT structure. The RDBSS routines that manage V\_NET\_ROOT structures only modify the following elements:

-   Signature and reference count

-   A pointer to the associated NET\_ROOT structure and links

-   Name information for table lookup (prefix)

-   Name for a prefix to be added to whatever name the user sees (this is for simulating a NET\_ROOT structure that is not mapped at the root of the actual NET\_ROOT structure)

The finalization of a V\_NET\_ROOT structure consists of two parts:

1.  Destroying the association with all SRV\_OPEN structures

2.  Freeing the memory

There can be a delay between these two actions, and a field in the V\_NET\_ROOT structure prevents the first step from being duplicated.

 

 




