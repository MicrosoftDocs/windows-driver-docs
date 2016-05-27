---
title: The V\_NET\_ROOT Structure
author: windows-driver-content
description: The V\_NET\_ROOT Structure
ms.assetid: 866eba91-13b6-4b15-93de-4f627a635c92
keywords: ["share mapping WDK RDBSS", "V_NET_ROOT structure WDK RDBSS", "mapping shares", "data structures WDK file systems", "RDBSS WDK file systems , connection and file structures", "Redirected Drive Buffering Subsystem WDK file systems , connection and file structures", "connection structures WDK RDBSS", "file structures WDK RDBSS", "structures WDK RDBSS", "connection information WDK RDBSS"]
---

# The V\_NET\_ROOT Structure


## <span id="ddk_the_v_net_root_structure_if"></span><span id="DDK_THE_V_NET_ROOT_STRUCTURE_IF"></span>


The V\_NET\_ROOT structure provides a mechanism for mapping into a share (for example, a user drive mapping that points below the root of the associated share point). The V\_NET\_ROOT name can be in one of the following formats:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20The%20V_NET_ROOT%20Structure%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


