---
title: Partial Offloads and Offload Failures
description: Partial Offloads and Offload Failures
ms.assetid: 70b10b0f-f367-4ade-b85b-f86b30334d5c
keywords:
- state offloading process WDK TCP chimney offload , partial offloads
- offloading state process WDK TCP chimney offload , partial offloads
- partial offloads WDK TCP chimney offload
- failed offloads WDK TCP chimney offload
- state offloading process WDK TCP chimney offload , failed offloads
- offloading state process WDK TCP chimney offload , failed offloads
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Partial Offloads and Offload Failures


\[The TCP chimney offload feature is deprecated and should not be used.\]




When a [*MiniportInitiateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559393) request fails, the stack expects the offload target to set the **Status** member of the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure. The offload target must not modify the **Status** member of any of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures in the **NetBufferListChain** member of the **NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST** structure. The offload target must not call [**NdisTcpOffloadSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff564609) to complete the outstanding send data.

The following figure shows a partial offload and an offload failure.

![diagram illustrating a partial offload and an offload failure](images/failure-case.png)

When failing a *MiniportInitiateOffload* request the stack expects the offload target to set the Status member of the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure. The offload target must not modify the Status member of any of the NET\_BUFFER\_LIST structures in the **NetBufferListChain** member of the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure. The offload target must not complete the outstanding send data by calling **NdisTcpOffloadSendComplete**.

In the offload sequence that is shown in the preceding figure, the offload target:

1.  Offloads the Neighbor1 state object.

2.  Offloads the Path1 state object.

3.  Offloads the TCP1 state object.

4.  Fails to offload the TCP2 state object because of a resource constraint.

5.  Fails to offload the Path2 state object for a reason other than a resource constraint.

6.  Stops traversing the state tree and does not attempt to offload the TCP3 state object.

Note that, if the offload target cannot offload the state that is associated with the root block list, it stops traversing the tree.

For each state object in the preceding figure, the offload target writes the following value to the **Status** member of the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that is associated with the state object:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">State Object</th>
<th align="left">Value in Status Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Neighbor1</p></td>
<td align="left"><p>NDIS_STATUS_OFFLOAD_PARTIAL_SUCCESS</p></td>
<td align="left"><p>Neighbor1 and Path1 were successfully offloaded. However, Path2 was not offloaded.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Path1</p></td>
<td align="left"><p>NDIS_STATUS_OFFLOAD_PARTIAL_SUCCESS</p></td>
<td align="left"><p>Path1 and TCP1 were successfully offloaded. However, TCP2 was not offloaded.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TCP1</p></td>
<td align="left"><p>NDIS_STATUS_SUCCESS</p></td>
<td align="left"><p>TCP1 was successfully offloaded. There are no dependent state objects.</p></td>
</tr>
<tr class="even">
<td align="left"><p>TCP2</p></td>
<td align="left"><p>NDIS_STATUS_RESOURCES</p></td>
<td align="left"><p>TCP2 was not offloaded because of resource constraints.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Path2</p></td>
<td align="left"><p>NDIS_STATUS_FAILURE</p></td>
<td align="left"><p>Path2 was not offloaded. The problem was not a resource constraint.</p></td>
</tr>
<tr class="even">
<td align="left"><p>TCP3</p></td>
<td align="left"><p>NDIS_STATUS_FAILURE</p></td>
<td align="left"><p>TCP3 was not offloaded. The problem was not a resource constraint.</p></td>
</tr>
</tbody>
</table>

 

 

 





