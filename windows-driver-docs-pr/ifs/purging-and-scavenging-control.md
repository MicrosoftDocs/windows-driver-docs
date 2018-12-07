---
title: Purging and Scavenging Control
description: Purging and Scavenging Control
ms.assetid: 103b05e6-333a-441a-a4f8-784ae43df59e
keywords:
- RDBSS WDK file systems , purge and scavenge structures
- Redirected Drive Buffering Subsystem WDK file systems , purge and scavenge structures
- purging WDK network redirectors
- scavenging WDK network redirectors
- FOBX structure
- cleanup FOBX structures WDK network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Purging and Scavenging Control


## <span id="ddk_purging_and_scavenging_control_if"></span><span id="DDK_PURGING_AND_SCAVENGING_CONTROL_IF"></span>


RDBSS provides a number of routines to purge and scavenge FOBX structures when they are no longer needed.

At cleanup, there are no more user handles associated with the file object. In such cases, the time window between close and cleanup is dictated by the additional references maintained by Memory Manager and Cache Manager. RDBSS uses a scavenger process that runs on a separate thread to scavenge and purge unneeded FOBX and other structures.

Currently, scavenging has been implemented for SRV\_CALL, NET\_ROOT and V\_NET\_ROOT structures. The FCB scavenging is handled separately. The FOBX can and should always be synchronously finalized. The only data structure that will have to be potentially enabled for scavenged finalization are SRV\_OPEN structures.

The scavenger process as it is implemented in RDBSS currently will not consume any system resources until there is a need for scavenged finalization. The first entry to be marked for scavenged finalization will result in a timer request being posted for the scavenger. In the current implementation, the timer requests are posted as one-shot timer requests. This implies that there are no guarantees regarding the time interval within which the entries will be finalized. The scavenger activation mechanism is a potential candidate for fine tuning at a later stage.

The RDBSS purging and scavenging routines include the following:

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554673" data-raw-source="[&lt;strong&gt;RxPurgeAllFobxs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554673)"><strong>RxPurgeAllFobxs</strong></a></p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554679" data-raw-source="[&lt;strong&gt;RxPurgeRelatedFobxs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554679)"><strong>RxPurgeRelatedFobxs</strong></a></p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554707" data-raw-source="[&lt;strong&gt;RxScavengeAllFobxs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554707)"><strong>RxScavengeAllFobxs</strong></a></p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given network mini-redirector device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554713" data-raw-source="[&lt;strong&gt;RxScavengeFobxsForNetRoot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554713)"><strong>RxScavengeFobxsForNetRoot</strong></a></p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given NET_ROOT structure.</p></td>
</tr>
</tbody>
</table>

 

 

 




