---
title: Multiplex ID Management
author: windows-driver-content
description: Multiplex ID Management
ms.assetid: feffc421-bd51-4174-80a4-1f9a36355667
keywords: ["RDBSS WDK file systems , multiplex ID", "Redirected Drive Buffering Subsystem WDK file systems , multiplex ID", "multiplex ID WDK network redirectors", "MID WDK network redirectors", "mapping MID", "MID_ATLAS structure", "MID_MAP structure"]
---

# Multiplex ID Management


## <span id="ddk_multiplex_id_management_if"></span><span id="DDK_MULTIPLEX_ID_MANAGEMENT_IF"></span>


RDBSS defines a multiplex ID (MID), a 16-bit value, that can be used by both the network client (mini-redirector) and the server to distinguish between the concurrently active requests on any connection. A network redirector can associate a MID with any arbitrary context or internal data structure that it uses. It is completely at the option of the network redirector whether MIDs are allocated and used.

A MID, as defined by RDBSS, is part of a MID\_ATLAS data structure that has been designed to meet several criterion. Associated with a MID\_ATLAS data structure are a series of one or more MID\_MAP data structures used to map MIDs to associated contexts.

The MID\_ATLAS data structure, the MID\_MAP structure, and MIDs should scale well to handle the differing capabilities of various remote servers. For example, the typical LAN Manager server on Windows permits 50 outstanding requests on any connection. Some types of servers may support as few as one outstanding request, while gateway servers may desire this number to be very high (on the order of thousands of outstanding connections).

The two primary operations that need to be handled well are:

-   Mapping a MID to the context associated with it. This routine will be invoked to process every packet received along any connection at both the client and the server (assuming the servers use MIDs).

-   Generating a new MID for sending requests to the server. This routine will be used at the client for enforcement of maximum connection limits as well as for tagging each concurrent request with a unique ID.

The MID must be able to efficiently manage the unique tagging and identification of a number of MIDs (typically 50) from a possible combination of 65,536 values. In some cases, it might make sense to create a small MID\_ATLAS structure to save kernel memory used by the MID\_MAP structure and expand the size of the MID\_ATLAS structure if needed to efficiently handle greater usage. To ensure a proper time-space tradeoff, the lookup is organized as a three-level hierarchy. The 16 bits used to represent a MID are split up into three-bitfields. The length of the right-most field (least significant ) is decided by the maximum number of MIDs that are allowed in the initial atlas. This maximum value is a parameter passed to the [**RxCreateMidAtlas**](https://msdn.microsoft.com/library/windows/hardware/ff554352) routine when the MID\_ATLAS data structure is first created. This maximum value determines the initial size of the MID\_ATLAS data structure that is created and how many MID\_MAP data structures can be accommodated. The remaining length is split up equally between the next two fields, which determine the maximum size of possible subordinate MID\_ATLAS structures that can be defined to expand and extend an existing MID\_ATLAS into a three-level hierarchy of MID\_MAP data structures. So, each MID\_ATLAS data structure can contain the maximum number of MID\_MAP structures or a pointer to one subordinate MID\_ATLAS and the MID\_MAP structures.

For example, if a maximum of 50 MIDs are allocated on creation , the length of the first field is 6 (64 ( 2 \*\* 6 ) is greater than 50 ). The remaining length is split into two fields of 5 bits each for the second and third hierarchical levels so that an existing MID\_ATLAS data structure can be expanded to accommodate more MID\_MAP entries.

RDBSS provides the following routines for creating and manipulating a MID\_ATLAS data structure, associated MID\_MAP data structures, and Multiplex IDs.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>RxAssociateContextWithMid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553388)</p></td>
<td align="left"><p>This routine associates the supplied opaque context with an available MID from a MID_ATLAS structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateMidAtlas</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554352)</p></td>
<td align="left"><p>This routine allocates a new instance of the MID_ATLAS data structure and initializes it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxDestroyMidAtlas</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554395)</p></td>
<td align="left"><p>This routine destroys an existing instance of a MID_ATLAS data structure and frees the memory allocated to it. As a side effect it invokes the passed in context destructor on every valid context in the MID_ATLAS structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxMapMidToContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554545)</p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxMapAndDissociateMidFromContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554541)</p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS structure and then disassociates the MID from the context.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxReassociateMid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554686)</p></td>
<td align="left"><p>This routine reassociates a MID with an alternate context.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Multiplex%20ID%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


