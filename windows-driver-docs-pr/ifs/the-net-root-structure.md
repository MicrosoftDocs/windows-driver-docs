---
title: The NET\_ROOT Structure
description: The NET\_ROOT Structure
ms.assetid: f7846343-9af6-4b7f-9c8d-190abb524946
keywords: ["net root structure WDK RDBSS", "network server\share connection data WDK RDBSS", "NET_ROOT structure", "server\share connection data WDK RDBSS", "root structure WDK RDBSS", "data structures WDK file systems", "RDBSS WDK file systems , connection and file structures", "Redirected Drive Buffering Subsystem WDK file systems , connection and file structures", "connection structures WDK RDBSS", "file structures WDK RDBSS", "structures WDK RDBSS", "connection information WDK RDBSS"]
---

# The NET\_ROOT Structure


## <span id="ddk_the_net_root_structure_if"></span><span id="DDK_THE_NET_ROOT_STRUCTURE_IF"></span>


A net root structure, NET\_ROOT, contains information for each specific network server\\share connection maintained by a network mini-redirector.

A NET\_ROOT is what the RDBSS and a network mini-redirector driver want to deal with, not a server. Accordingly, RDBSS normally creates and opens a NET\_ROOT structure and calls the network mini-redirector driver responsible for opening the server. The network mini-redirector driver is expected to populate the appropriate fields in the passed in NET\_ROOT structure.

A list of the NET\_ROOT structures is maintained by RDBSS for each SRV\_CALL. Each NET\_ROOT structure has a few elements common with other RDBSS structures, along with elements that are unique to a NET\_ROOT structure. The RDBSS routines that manage NET\_ROOT structures only modify the following elements:

-   Signature and reference count

-   A name and associated table information

-   A back pointer to the associated SRV\_CALL structure

-   Size information for the various substructures

-   A lookup table of associated FCB structures

-   Whatever additional storage is request by the network mini-redirector (or the creator of the NET\_ROOT data structure)

A NET\_ROOT structure also contains a list of RX\_CONTEXT structures that are waiting for the NET\_ROOT transitioning to be completed before resumption of IRP processing. This typically happens when concurrent requests are directed at a server. One of these requests is initiated while the other requests are queued. Extra space reserved for use by the network mini-redirector begins at the end of the known NET\_ROOT data structure so that a network mini-redirector can simply refer to this extra space using context fields from an include file.

The finalization of a NET\_ROOT structure consists of two parts:

1.  Destroying the association with all V\_NET\_ROOTS

2.  Freeing the memory

There can be a delay between these two actions, and a field in the NET\_ROOT structure prevents the first step from being duplicated.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20The%20NET_ROOT%20Structure%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




