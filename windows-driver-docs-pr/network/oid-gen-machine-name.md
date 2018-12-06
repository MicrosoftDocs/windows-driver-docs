---
title: OID_GEN_MACHINE_NAME
description: As a set, the OID_GEN_MACHINE_NAME OID indicates the local computer name to a miniport driver.
ms.assetid: 771d21ff-e989-4717-8f3e-28f4b8afe274
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MACHINE_NAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MACHINE\_NAME


As a set, the OID\_GEN\_MACHINE\_NAME OID indicates the local computer name to a miniport driver.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Optional.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

Remarks
-------

The information buffer passed in this request contains an array of Unicode characters that represents the local computer name. The **InformationBufferLength** value that is supplied to the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function specifies the length of this array in bytes, not including a NULL terminator.

NDIS sets OID\_GEN\_MACHINE\_NAME only once after a miniport driver completes initialization. Under Windows XP, NDIS does not dynamically notify miniport drivers of a change in the computer name. After changing the computer name, a user must restart the computer so that NDIS notifies miniport drivers of the new computer name.

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

## See also


[*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416)

 

 




