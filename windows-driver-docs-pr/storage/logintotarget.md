---
title: LoginToTarget
description: LoginToTarget
ms.assetid: 9ad66387-ca77-46e7-aa91-5c909251c2ce
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# LoginToTarget


The **LoginToTarget** method instructs a miniport driver that manages an HBA initiator to log on to a target portal.

Miniport drivers that implement the [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md) must support this method.

The miniport driver must expose information about the session that it creates through the [MSiSCSI\_InitiatorSessionInfo WMI class](msiscsi-initiatorsessioninfo-wmi-class.md).

The following table describes the types of logon sessions that initiators can establish.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Login session</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Discovery</p></td>
<td align="left"><p>A discovery session is used exclusively for <strong>SendTargets</strong> operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Informational</p></td>
<td align="left"><p>An informational session allows the initiator to query the target for information, but the initiator does not report logical unit numbers (LUNs) on the target to the Plug and Play (PnP) manager; the storage port driver does not enumerate the LUNs or expose them as local devices. Management applications can query these remote LUNs by establishing an informational session and calling iSCSI user-mode library routines, such as <strong>SendScsiInquiry</strong>, <strong>SendScsiReportLuns</strong>, and <strong>SendScsiReadCapacity</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Data</p></td>
<td align="left"><p>A data session is a full-featured session. The miniport driver that initiates the session should report the LUNs on the target to the port driver, so the port driver will enumerate them and load the appropriate drivers. Software can access these remote devices as though they were local devices.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Boot</p></td>
<td align="left"><p>A boot session is a full-featured session in which the iSCSI LUN is used as a boot device.</p></td>
</tr>
</tbody>
</table>

 

The identifier (ID) that the **LoginToTarget** method assigns to the session must remain constant for the lifetime of a session. Even if asynchronous logoffs or network events sever the connection to the target and force the miniport driver to reconnect, the miniport driver should continue to use the same session ID.

Miniport drivers should use the following guidelines when they reestablish data and informational sessions:

<span id="Periodic_reconnection_attempts"></span><span id="periodic_reconnection_attempts"></span><span id="PERIODIC_RECONNECTION_ATTEMPTS"></span>Periodic reconnection attempts  
The miniport driver should make periodically attempt to reconnect (5-second intervals are recommended) until a logon succeeds or the miniport driver receives a logoff request.

<span id="Device_removal_latency"></span><span id="device_removal_latency"></span><span id="DEVICE_REMOVAL_LATENCY"></span>Device removal latency  
The miniport driver should not immediately remove the target's logical units from the local operating system's device stack. Instead, the miniport driver should use locally cached data to process INQUIRY and REPORT LUNS requests and queue requests that the miniport driver must send to the remote target for processing.

If the miniport driver is unable to reestablish a session with the target after approximately 60 seconds, it should remove the target's logical units from the local device stack. By introducing the 60-second latency in the removal of devices from the device stack, the miniport driver can avoid unnecessarily interrupting the work of local applications that access data on the remote target. However, a latency of more than 60 seconds might require the miniport driver to queue a large number of requests, and these requests could potentially consume an unacceptable amount of system resources. The exact latency time should be configurable.

The **LoginToTarget** WMI method belongs to the [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md).

For an explanation of the algorithm that the iSCSI user-mode library uses to establish a log, see **LoginIScsiTarget**.

 

 





