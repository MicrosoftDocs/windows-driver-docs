---
title: Multiplex ID Management
description: Multiplex ID Management
ms.assetid: feffc421-bd51-4174-80a4-1f9a36355667
keywords:
- RDBSS WDK file systems , multiplex ID
- Redirected Drive Buffering Subsystem WDK file systems , multiplex ID
- multiplex ID WDK network redirectors
- MID WDK network redirectors
- mapping MID
- MID_ATLAS structure
- MID_MAP structure
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553388" data-raw-source="[&lt;strong&gt;RxAssociateContextWithMid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553388)"><strong>RxAssociateContextWithMid</strong></a></p></td>
<td align="left"><p>This routine associates the supplied opaque context with an available MID from a MID_ATLAS structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554352" data-raw-source="[&lt;strong&gt;RxCreateMidAtlas&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554352)"><strong>RxCreateMidAtlas</strong></a></p></td>
<td align="left"><p>This routine allocates a new instance of the MID_ATLAS data structure and initializes it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554395" data-raw-source="[&lt;strong&gt;RxDestroyMidAtlas&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554395)"><strong>RxDestroyMidAtlas</strong></a></p></td>
<td align="left"><p>This routine destroys an existing instance of a MID_ATLAS data structure and frees the memory allocated to it. As a side effect it invokes the passed in context destructor on every valid context in the MID_ATLAS structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554545" data-raw-source="[&lt;strong&gt;RxMapMidToContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554545)"><strong>RxMapMidToContext</strong></a></p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554541" data-raw-source="[&lt;strong&gt;RxMapAndDissociateMidFromContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554541)"><strong>RxMapAndDissociateMidFromContext</strong></a></p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS structure and then disassociates the MID from the context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554686" data-raw-source="[&lt;strong&gt;RxReassociateMid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554686)"><strong>RxReassociateMid</strong></a></p></td>
<td align="left"><p>This routine reassociates a MID with an alternate context.</p></td>
</tr>
</tbody>
</table>

 

 

 




