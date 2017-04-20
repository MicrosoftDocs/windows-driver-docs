---
title: Connection and Name Resolution
author: windows-driver-content
description: Connection and Name Resolution
ms.assetid: e61d09f1-7951-4291-93ce-e5ccbe0be576
keywords:
- mini-redirectors WDK , connections
- mini-redirectors WDK , name resolution
- names WDK file systems
- connections WDK mini-redirectors
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connection and Name Resolution


Network mini-redirectors establish connections to remote servers and handle name resolution using several routines. RDBSS abstracts this process into several structures including the SRV\_CALL, NET\_ROOT, and V\_NET\_ROOT structures that are reference counted. In network mini-redirector terms, the establishment of a connection is often called a "tree connect." This connection establishment requires creating a SRV\_CALL, a NET\_ROOT, and a V\_NET\_ROOT structure. So the normal procedure would be a call to the network mini-redirector [**MRxCreateSrvCall**](https://msdn.microsoft.com/library/windows/hardware/ff549864) routine followed by a call to the [**MRxSrvCallWinnerNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550824) and [**MRxCreateVNetRoot**](https://msdn.microsoft.com/library/windows/hardware/ff549869) routines. These calls are usually issued in response to a request from a user-mode application or service to mount a drive (**net use x: \\\\server\\public**, for example). These calls can also result from a request for a UNC file object (**notepad \\\\server\\public\\readme.txt**, for example). RDBSS handles both of these cases internally for the network mini-redirector and initiates the **MRxCreateSrvCall** sequence.

When a connection is deleted, similar finalize calls are made to tear down the SRV\_CALL, and NET\_ROOT structures and release any memory used. These calls to the network mini-redirector include [**MRxFinalizeVNetRoot**](https://msdn.microsoft.com/library/windows/hardware/ff550663), [**MRxFinalizeNetRoot**](https://msdn.microsoft.com/library/windows/hardware/ff550653), and [**MRxFinalizeSrvCall**](https://msdn.microsoft.com/library/windows/hardware/ff550656).

The original design for RDBSS was that various network mini-redirectors would all share a single copy of RDBSS, but this was not implemented. A holdover from this original design is that various network mini-redirectors compete to fulfill the request for a network connection (\\\\server\\share, for example). The [**MRxSrvCallWinnerNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550824) routine is used by RDBSS to notify a network mini-redirector that it was the winner when multiple redirectors could fulfill the request. The winning network mini-redirector is expected to create the SRV\_CALL and establish a connection with the server.

Under the implementation of RDBSS in Windows Server 2003, Windows XP, and Windows 2000, each network mini-redirector has its own copy of RDBSS so there are no competing network redirectors at the RDBSS layer. Each network mini-redirector (network provider) and its local copy of RDBSS is called in turn based on the order in a registry setting: The order in which providers are queried is controlled by the following registry value:

```
ProviderOrder
```

This registry value is located under the following registry key:

```
HKLM\CurrentControlSet\Control\NetworkProvider\Order
```

The [**MRxSrvCallWinnerNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550824) routine will be called after every request to create a SRV\_CALL structure.

The following table lists the routines that can be implemented by a network mini-redirector for connection and name resolution operations.

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
<td align="left">[<strong>MRxCreateSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549864)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a SRV_CALL structure and establish connection with a server.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxCreateVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549869)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a V_NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxExtractNetRootName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550649)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extract the name from the NET_ROOT structure for a given pathname.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxFinalizeNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550653)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a NET_ROOT object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxFinalizeSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550656)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a SRV_CALL structure used for establishing connection with a server.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxFinalizeVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550663)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a V_NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxPreparseName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550750)</td>
<td align="left"><p>RDBSS calls this routine to give a network mini-redirector the opportunity to preparse a name.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSrvCallWinnerNotify</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550824)</td>
<td align="left"><p>This routine was originally designed to be called by RDBSS to notify a network mini-redirector that it was the winner when multiple redirectors could fulfill the request. The winning network mini-redirector is expected to create the SRV_CALL structure and establish a connection with the server.</p>
<p>Under the current implementation of RDBSS each network mini-redirector has its own copy of RDBSS, so there are no competing network redirectors at the RDBSS layer. This routine will be called before every request to create a SRV_CALL structure.</p>
<p>When multiple redirectors are installed for handling the same UNC namespace, the redirector to service a request is chosen by MUP based on the order of redirectors specified in the registry.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


