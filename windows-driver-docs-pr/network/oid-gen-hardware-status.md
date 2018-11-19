---
title: OID_GEN_HARDWARE_STATUS
description: As a query, the OID_GEN_HARDWARE_STATUS OID specifies the current hardware status of the underlying NIC.
ms.assetid: beab6f7a-b064-446f-8008-ef8db9d7c080
ms.date: 08/08/2017
keywords: 
 -OID_GEN_HARDWARE_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_HARDWARE\_STATUS


As a query, the OID\_GEN\_HARDWARE\_STATUS OID specifies the current hardware status of the underlying NIC.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Obsolete.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

The OID\_GEN\_HARDWARE\_STATUS OID specifies the current hardware status of the underlying NIC as one of the following NDIS\_HARDWARE\_STATUS-type values:

<a href="" id="ndishardwarestatusready"></a>**NdisHardwareStatusReady**  
Available and capable of sending and receiving data over the wire

<a href="" id="ndishardwarestatusinitializing"></a>**NdisHardwareStatusInitializing**  
Initializing

<a href="" id="ndishardwarestatusreset"></a>**NdisHardwareStatusReset**  
Resetting

<a href="" id="ndishardwarestatusclosing"></a>**NdisHardwareStatusClosing**  
Closing

<a href="" id="ndishardwarestatusnotready"></a>**NdisHardwareStatusNotReady**  
Not ready

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 




