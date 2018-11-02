---
title: Version Section in a Network INF File
description: Version Section in a Network INF File
ms.assetid: c76151e9-fef2-4bfe-8587-d58d95d234bc
keywords:
- INF files WDK network , Version section
- network INF files WDK , Version section
- Version section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Version Section in a Network INF File





The **Version** section in a network INF file is based on the generic [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502).

The **Version** section in a network INF file has the following network-specific entries:

-   [Class](#class)
-   [ClassGuid](#classguid)
-   [Signature and Operating System Entries](#signature-and-operating-system-entries)
-   [PnpLockDown](#pnplockdown)
-   [CatalogFile](#catalogfile)
-   [Version Section Example](#version-section-example)

### Class

The **Version** section should contain a **Class** entry which identifies the class of network component that is installed by the file.

There are four network classes:

<a href="" id="net"></a>**Net**  
Specifies a physical or virtual network adapter. NDIS intermediate drivers, which export virtual network adapters, are included in the Net class.

<a href="" id="nettrans"></a>**NetTrans**  
Specifies a network protocol, such as TCP/IP, IPX, a connection-oriented client, or a connection-oriented call manager.

<a href="" id="netclient"></a>**NetClient**  
Specifies a network client, such as the Microsoft Client for Networks or the NetWare Client. A NetClient component is considered to be a network provider and, if it provides print services over the network, it is also considered to be a print provider.

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

<a href="" id="netservice"></a>**NetService**  
Specifies a network service, such as a file service or a print service.

**Note**  Infrared Data Association (IrDA) compliant devices are not categorized as any of the previous four network classes, even though they are installed by the network class installer. An INF file that is used to install an IrDA device should have a **Class** value of **Infrared**. This class includes both Serial-IR and Fast-IR devices.

 

**Note**  Support for IrDA miniport drivers has been removed from NDIS 6.30 (Windows 8) and later.

 

### ClassGuid

The **Version** section must contain a **ClassGuid** entry. The network class installer uses the **ClassGuid** entry to determine the class of network component being installed.

There are four network **ClassGuid** values, each of which corresponds to a network class:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Network class</th>
<th align="left">ClassGuid</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Net</strong></p></td>
<td align="left"><p>{4D36E972-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NetTrans</strong></p></td>
<td align="left"><p>{4D36E975-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NetClient</strong></p></td>
<td align="left"><p>{4D36E973-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NetService</strong></p></td>
<td align="left"><p>{4D36E974-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
</tbody>
</table>

 

An INF file for an IrDA device should have a **ClassGuid** value of

{6bdd1fc5-81d0-bec7-08002be2092f}.

### Signature and Operating System Entries

The **Signature** entry must be **$Windows NT$**.

### PnpLockDown

The **PnpLockDown** entry should be set to 1 to prevents applications from directly modifying the files that your driver package's INF file specifies. For more information about this entry, see [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502).

### CatalogFile

The **CatalogFile** entry is used to declare an optional driver-supplied .cat file. For more information, see the Vendor-supplied files section of [Components and Files Used for Network Component Installation](components-and-files-used-for-network-component-installation.md).

### Version Section Example

The following is an example of a **Version** section for an INF file that installs a network adapter:

```INF
[Version]
Signature = $Windows NT$
Class=Net
ClassGuid = {4D36E972-E325-11CE-BFC1-08002BE10318}
Provider = %Msft%
DriverVer=06/22/2010,6.1.7065.0
PnpLockDown = 1
CatalogFile = netvmini630.cat
```

**Note**  
The **Provider** entry indicates the developer of the INF file, not the developer of the component that is installed by the INF file.

 

 

 





