---
title: LoginToTarget
description: LoginToTarget
ms.assetid: 9ad66387-ca77-46e7-aa91-5c909251c2ce
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20LoginToTarget%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




