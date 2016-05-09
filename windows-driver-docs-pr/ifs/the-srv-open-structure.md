---
title: The SRV\_OPEN Structure
description: The SRV\_OPEN Structure
ms.assetid: 6cf4c6f6-a21f-4919-92b5-2403b650d8d0
keywords: ["server open WDK RDBSS", "open servers WDK RDBSS", "SRV_OPEN structure", "data structures WDK file systems", "RDBSS WDK file systems , connection and file structures", "Redirected Drive Buffering Subsystem WDK file systems , connection and file structures", "connection structures WDK RDBSS", "file structures WDK RDBSS", "structures WDK RDBSS", "connection information WDK RDBSS"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20The%20SRV_OPEN%20Structure%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




