---
title: Winsock Sections in a Network INF File
description: Winsock Sections in a Network INF File
ms.assetid: 179a8570-287b-446e-8b56-a9f23071e84d
keywords:
- INF files WDK network , Winsock sections
- network INF files WDK , Winsock sections
- Winsock sections WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winsock Sections in a Network INF File




An INF file for a **NetTrans** component that provides a Winsock interface must specify this Winsock dependency. Such an INF file must contain a *Winsock-install* section. To create a Winsockinstall section, add the .Winsock extension to the *DDInstall* section name for the protocol. For example, if the *DDInstall* section for a protocol is named **Ipx**, the *Winsock-install* section for that protocol must be named Ipx.Winsock.

> [!NOTE] 
> Winsock dependency has been deprecated in Windows 8 and later.


A *Winsock-install* section must contain an **AddSock** directive. The **AddSock** directive specifies a vendor-named section that contains values to be added to the component's **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*TransportDriverName*\\Params\\Winsock** key.

The vendor-named section referenced by the **AddSock** directive must contain the following required values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>TransportService</p></td>
<td align="left"><p>A REG_SZ value that specifies the service name of the protocol. This must be the same as the <strong>Ndi\Service</strong> value for the protocol. For more information, see <a href="adding-service-related-values-to-the-ndi-key.md" data-raw-source="[Adding Service-Related Values to the Ndi Key](adding-service-related-values-to-the-ndi-key.md)">Adding Service-Related Values to the Ndi Key</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HelperDllName</p></td>
<td align="left"><p>A REG_EXPAND_SZ value that specifies the path to the Windows Sockets helper (WSH) DLL for the protocol. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566260" data-raw-source="[WSH DLL Function Summary](https://msdn.microsoft.com/library/windows/hardware/ff566260)">WSH DLL Function Summary</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxSockAddrLength</p></td>
<td align="left"><p>A REG_DWORD value that specifies the largest valid SOCKADDR size, in bytes, for the WSH DLL</p></td>
</tr>
<tr class="even">
<td align="left"><p>MinSockAddrLength</p></td>
<td align="left"><p>A REG_DWORD value that specifies the smallest valid SOCKADDR size, in bytes, for the WSH DLL</p></td>
</tr>
</tbody>
</table>

 

If an optional **ProviderId** for a namespace provider is specified, the following values must also be specified:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ProviderId</p></td>
<td align="left"><p>A REG_SZ value that specifies the Globally Unique Identifier (GUID) that identifies the namespace provider. The GUID is used as a key to all subsequent references to the namespace provider. Obtain the GUID by running the uuidgen.exe utility. For more information about this utility, see the Microsoft Windows SDK.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LibraryPath</p></td>
<td align="left"><p>A REG_EXPAND_SZ value that specifies the complete path to the namespace provider DLL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DisplayString</p></td>
<td align="left"><p>A localizable string that specifies the name displayed for the namespace provider in the user interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SupportedNameSpace</p></td>
<td align="left"><p>A REG_DWORD value which specifies the namespace that is supported by the namespace provider.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>An optional REG_DWORD value that specifies the version number of the namespace provider. If this value is not specified, the default value (1) is used for the version number.</p></td>
</tr>
</tbody>
</table>

 

The following namespace values can be assigned to SupportedNameSpace and are defined in Winsock2.h:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Namespace</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>NS_ALL</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_SAP</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_NDS</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_PEER_BROWSE</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_TCPIP_LOCAL</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_TCPIP_HOSTS</p></td>
<td align="left"><p>11</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_DNS</p></td>
<td align="left"><p>12</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_NETBT</p></td>
<td align="left"><p>13</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_WINS</p></td>
<td align="left"><p>14</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_NBP</p></td>
<td align="left"><p>20</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_MS</p></td>
<td align="left"><p>30</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_STDA</p></td>
<td align="left"><p>31</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_CAIRO</p></td>
<td align="left"><p>32</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_X500</p></td>
<td align="left"><p>40</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NS_NIS</p></td>
<td align="left"><p>41</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS_WRQ</p></td>
<td align="left"><p>50</p></td>
</tr>
</tbody>
</table>

 

For more information about namespace providers, see the Windows SDK documentation.

The following example shows Winsock sections for an IPX protocol:

```INF
[Ipx.Winsock]
AddSock = Install.IpxWinsock
 
[Install.IpxWinsock]
TransportService = nwlinkipx
HelperDllName = "%%SystemRoot%%\System32\wshisn.dll"
MaxSockAddrLength = 0x10
MinSockAddrLength = 0xe
ProviderId = "GUID"
LibraryPath = "%SystemRoot%\\System32\\nwprovau.dll"
DisplayString = %NwlnkIpx_Desc%
SupportedNameSpace = 1
Version = 2
```

An INF file can remove a Winsock dependency for a protocol by including a *Winsock-remove* section. To create a *Winsock-remove* section, add the .Winsock extension to the *Remove* section name for the protocol. For example, if the *Remove* section for a protocol is named Ipx.Remove, the *Winsock-remove* section for the protocol must be named Ipx.Remove.Winsock.

The *Winsock-remove* section contains a **DelSock** directive that specifies an INF-writer-named section. The INF-writer-named section must specify the transport service to remove. If a **ProviderId** was previously registered for the protocol, the vendor-named section must also specify the **ProviderId** to remove.

The following example shows two sections that remove the Winsock dependency for an IPX protocol:

```INF
[Ipx.Remove.Winsock]
DelSock = Remove.IpxWinsock
 
[Remove.IpxWinsock]
TransportService = nwlinkipx
ProviderId = "GUID"
```

 

 





