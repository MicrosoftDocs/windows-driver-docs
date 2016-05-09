---
title: Purging and Scavenging Control
author: windows-driver-content
description: Purging and Scavenging Control
ms.assetid: 103b05e6-333a-441a-a4f8-784ae43df59e
keywords: ["RDBSS WDK file systems , purge and scavenge structures", "Redirected Drive Buffering Subsystem WDK file systems , purge and scavenge structures", "purging WDK network redirectors", "scavenging WDK network redirectors", "FOBX structure", "cleanup FOBX structures WDK network redirectors"]
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
<td align="left"><p>[<strong>RxPurgeAllFobxs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554673)</p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPurgeRelatedFobxs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554679)</p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxScavengeAllFobxs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554707)</p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given network mini-redirector device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxScavengeFobxsForNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554713)</p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given NET_ROOT structure.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Purging%20and%20Scavenging%20Control%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


