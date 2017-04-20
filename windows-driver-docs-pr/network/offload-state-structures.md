---
title: Offload State Structures
description: Offload State Structures
ms.assetid: e4fc3c65-a509-4aa6-88e1-9ca564cefa4b
keywords:
- offload state WDK TCP chimney offload , structures
- structures WDK TCP chimney offload
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Offload State Structures


\[The TCP chimney offload feature is deprecated and should not be used.\]

## <a href="" id="ddk-offload-state-structures-ng"></a>


The following table indicates which structures a host stack uses to package offload state.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">State layer</th>
<th align="left">Variables</th>
<th align="left">Structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Neighbor</p></td>
<td align="left"><p>Constant</p></td>
<td align="left"><p>[<strong>NEIGHBOR_OFFLOAD_STATE_CONST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568324)</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Cached</p></td>
<td align="left"><p>[<strong>NEIGHBOR_OFFLOAD_STATE_CACHED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568323)</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>Delegated</p></td>
<td align="left"><p>[<strong>NEIGHBOR_OFFLOAD_STATE_DELEGATED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568325)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Path</p></td>
<td align="left"><p>Constant</p></td>
<td align="left"><p>[<strong>PATH_OFFLOAD_STATE_CONST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569984)</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>Cached</p></td>
<td align="left"><p>[<strong>PATH_OFFLOAD_STATE_CACHED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569983)</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Delegated</p></td>
<td align="left"><p>[<strong>PATH_OFFLOAD_STATE_CACHED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569983)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TCP</p></td>
<td align="left"><p>Constant</p></td>
<td align="left"><p>[<strong>TCP_OFFLOAD_STATE_CONST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570938)</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>Cached</p></td>
<td align="left"><p>[<strong>TCP_OFFLOAD_STATE_CACHED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570937)</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>Delegated</p></td>
<td align="left"><p>[<strong>TCP_OFFLOAD_STATE_DELEGATED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570939)</p></td>
</tr>
</tbody>
</table>

 

When passed between the host stack and the offload target, an offload state structure is always associated with an [offload block list](offload-block-lists.md).

 

 





