---
title: The SRV\_CALL Structure
author: windows-driver-content
description: The SRV\_CALL Structure
ms.assetid: 9a3bb194-0289-47f4-a5c8-848d8d82cdd7
keywords: ["SRV_CALL structure", "server call context structure WDK RDBSS", "network server connection data WDK RDBSS", "data structures WDK file systems", "RDBSS WDK file systems , connection and file structures", "Redirected Drive Buffering Subsystem WDK file systems , connection and file structures", "connection structures WDK RDBSS", "file structures WDK RDBSS", "structures WDK RDBSS", "connection information WDK RDBSS"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20The%20SRV_CALL%20Structure%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


