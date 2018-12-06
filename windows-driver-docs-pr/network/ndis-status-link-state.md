---
title: NDIS_STATUS_LINK_STATE
description: Miniport drivers use the NDIS_STATUS_LINK_STATE status indication to notify NDIS and overlying drivers that there has been a change in the physical characteristics of a medium.
ms.assetid: e9953fe5-68d2-47e5-aceb-b35289500262
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_LINK_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_LINK\_STATE


Miniport drivers use the NDIS\_STATUS\_LINK\_STATE status indication to notify NDIS and overlying drivers that there has been a change in the physical characteristics of a medium.

Remarks
-------

Overlying drivers should not use the [OID\_GEN\_LINK\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569595) OID to determine the link state. Instead, use the NDIS\_STATUS\_LINK\_STATE status indication for link state updates.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains the [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure. This structure specifies the physical state of the medium.

Miniport drivers should avoid sending the NDIS\_STATUS\_LINK\_STATE status indication if there have been no changes in the physical state of the medium. However, avoiding this status indication is not a requirement.

If a miniport adapter transitions to a low power state, NDIS 6.0 and later miniport drivers should indicate a connection status of **MediaConnectStateUnknown**. When the miniport adapter transitions back to the working power state, the miniport driver should indicate a status of **MediaConnectStateConnected** after the link has been re-established. NDIS 6.30 miniport drivers should indicate **MediaConnectStateUnknown** during a low power transition only when a wake on link change and selective suspend are disabled. In other words, a miniport driver must indicate a connection state of **MediaConnectStateUnknown** during a low power transition, if it is impossible to detect and wake on a connection state change from a low power state.

NDIS might not pass a status indication to overlying drivers if there are no changes in the link state as specified in the previously indicated link state. However, this behavior is not guaranteed. Overlying drivers that receive this status indication must determine which characteristics of the medium, if any, have changed.

If an overlying driver is an NDIS 5.*x* or earlier protocol driver, NDIS translates the NDIS\_STATUS\_LINK\_STATE status indication to appropriate NDIS 5.1 status indications. NDIS indicates link speed changes with the [**NDIS\_STATUS\_LINK\_SPEED\_CHANGE**](ndis-status-link-speed-change.md) status indication. NDIS indicates changes in the connection state with [**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md) and [**NDIS\_STATUS\_MEDIA\_DISCONNECT**](ndis-status-media-disconnect.md) status indications.

NDIS also translates the NDIS 5.*x* miniport driver status for overlying NDIS 6.0 and later drivers. NDIS uses status indications or media state changes that NDIS identified in an NDIS 5.*x* OID query to create NDIS\_STATUS\_LINK\_STATE status indications. NDIS performs the following translations:

-   The [**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md) status indication is translated to **MediaConnectStateConnected** in the [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure.

-   The [**NDIS\_STATUS\_MEDIA\_DISCONNECT**](ndis-status-media-disconnect.md) status indication is translated to **MediaConnectStateDisconnected** in the [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure.

-   The [**NDIS\_STATUS\_LINK\_SPEED\_CHANGE**](ndis-status-link-speed-change.md) status indication and the [OID\_GEN\_LINK\_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593) OID are used to generate the link speed status.

For more information about link status, see [OID\_GEN\_LINK\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569595).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_STATUS\_LINK\_SPEED\_CHANGE**](ndis-status-link-speed-change.md)

[**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md)

[**NDIS\_STATUS\_MEDIA\_DISCONNECT**](ndis-status-media-disconnect.md)

[OID\_GEN\_LINK\_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593)

[OID\_GEN\_LINK\_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569595)

 

 




