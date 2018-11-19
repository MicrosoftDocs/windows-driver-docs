---
title: Support for UNC Naming and MUP
description: Support for UNC Naming and MUP
ms.assetid: 07c4a498-10c7-41b2-aaeb-73cab946f392
keywords:
- kernel network redirectors WDK , UNC naming
- kernel network redirectors WDK , MUP
- MUP WDK network redirectors
- multiple UNC provider WDK network redirectors
- UNC WDK network redirectors
- names WDK file systems
- prefix resolution WDK network redirectors
- prefix cache WDK network redirectors
- serial prefix resolution WDK network redirectors
- parallel prefix resolution WDK network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for UNC Naming and MUP


The multiple UNC provider (MUP) is a kernel-mode component responsible for channeling all remote file system accesses using a Universal Naming Convention (UNC) name to a network redirector (the UNC provider) that is capable of handling the remote file system requests. MUP is involved when a UNC path is used by an application as illustrated by the following example that could be executed from a command line:

```cpp
notepad \\server\public\readme.txt
```

MUP is not involved during an operation that creates a mapped drive letter (the "NET USE" command, for example). This operation is handled by the multiple provider router (MPR) and a user-mode WNet provider DLL for the network redirector. However, a user-mode WNet provider DLL can communicate directly with a kernel-mode network redirector driver during this operation.

On Microsoft Windows Server 2003, Windows XP, and Windows 2000, remote file operations performed on a mapped drive that does not represent a Distributed File System (DFS) drive don't go through MUP. These operations go directly to the network provider that handled the drive letter mapping.

For network redirectors that conform to the Windows Vista redirector model, MUP is involved even when a mapped network drive is used. File operations performed on the mapped drive go through MUP to the network redirector. Note that in this case MUP simply passes the operation to the network redirector involved.

MUP is part of the *mup.sys* binary, which also includes the Microsoft DFS client in Windows Server 2003, Windows XP, and Windows 2000.

A kernel network redirector will normally also have a user-mode WNet provider DLL to support establishing connections to remote resources (mapping drive letters to remote resources, for example). The MPR is a user-mode DLL that establishes network connections based on queries to WNet providers. Calls to the MPR would result from any of the following:

A "net use x: \\\\server\\share" command issued from a command prompt.

A network drive letter connection established from Windows Explorer

Direct calls to WNet functions.

A network redirector must register with MUP to handle UNC names. There can be multiple UNC providers registered with MUP. These UNC providers can be one or more of the following:

-   Network mini-redirectors based on RDBSS

-   Legacy redirectors not based on RDBSS

MUP determines which provider can handle a UNC path in a name-based operation, typically an IRP\_MJ\_CREATE request. This is referred to as "prefix resolution." Prior to Windows Vista, the prefix resolution operation serves two purposes:

-   The name-based operation which resulted in the prefix resolution is routed to the provider claiming the prefix. If successful, MUP ensures that subsequent handle-based operations (IRP\_MJ\_READ and IRP\_MJ\_WRITE, for example) go to the same provider completely bypassing MUP.

-   The provider and the prefix it claimed are entered in a prefix cache maintained by MUP. For subsequent name-based operations, MUP uses this prefix cache to determine whether a provider has already claimed a prefix before attempting to perform a prefix resolution. Each entry in this prefix cache is subject to a timeout (referred to as TTL) once it is added to the cache. An entry is thrown away after this timeout expires, at which point of time MUP will perform prefix resolution again for this prefix on a subsequent name-based operation.

MUP performs prefix resolution by issuing an [**IOCTL\_REDIR\_QUERY\_PATH**](https://msdn.microsoft.com/library/windows/hardware/ff548313) request to network redirectors registered with MUP. The input and output buffers for IOCTL\_REDIR\_QUERY\_PATH are as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Parameter available at</th>
<th align="left">Data structure format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Input buffer</strong></p></td>
<td align="left"><p>IrpSp-&gt; Parameters.DeviceIoControl.Type3InputBuffer</p></td>
<td align="left"><p>QUERY_PATH_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Output buffer</strong></p></td>
<td align="left"><p>IRP-&gt;UserBuffer</p></td>
<td align="left"><p>QUERY_PATH_RESPONSE</p></td>
</tr>
</tbody>
</table>



The IOCTL and the data structures are defined in *ntifs.h*. The buffers are allocated from non-paged pool.

Network redirectors should only allow kernel-mode senders of this IOCTL, by verifying that the **RequesterMode** member of the IRP structure is **KernelMode**.

MUP uses the QUERY\_PATH\_REQUEST data structure for the request information.

```cpp
typedef struct _QUERY_PATH_REQUEST {
    ULONG                PathNameLength;
    PIO_SECURITY_CONTEXT SecurityContext;
    WCHAR                FilePathName[1];
} QUERY_PATH_REQUEST, *PQUERY_PATH_REQUEST;
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>PathNameLength</strong></p></td>
<td align="left"><p>The length, in bytes, of the Unicode string contained in the <strong>FilePathName</strong> member.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SecurityContext</strong></p></td>
<td align="left"><p>A pointer to the security context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FilePathName</strong></p></td>
<td align="left"><p>A non-NULL terminated Unicode string of the form &amp;lt;server&gt;&amp;lt;share&gt;&amp;lt;path&gt;. The length of the string, in bytes, is specified by the <strong>PathNameLength</strong> member.</p></td>
</tr>
</tbody>
</table>



UNC providers should use the QUERY\_PATH\_RESPONSE data structure for the response information.

```cpp
typedef struct _QUERY_PATH_RESPONSE {
    ULONG  LengthAccepted;
} QUERY_PATH_RESPONSE, *PQUERY_PATH_RESPONSE;
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>LengthAccepted</strong></p></td>
<td align="left"><p>The length, in bytes, of the prefix claimed by the provider from the Unicode string path specified in the <strong>FilePathName</strong> member of the QUERY_PATH_REQUEST structure.</p></td>
</tr>
</tbody>
</table>



Note that IOCTL\_REDIR\_QUERY\_PATH is a METHOD\_NEITHER IOCTL. This means that the input and output buffers might not be at the same address. A common mistake by UNC providers is to assume that the input buffer and the output buffer are the same and use the input buffer pointer to provide the response.

When a UNC provider receives an IOCTL\_REDIR\_QUERY\_PATH request, it has to determine whether it can handle the UNC path specified in the **FilePathName** member of the QUERY\_PATH\_REQUEST structure. If so, it has to update the **LengthAccepted** member of the QUERY\_PATH\_RESPONSE structure with the length, in bytes, of the prefix that it has claimed, and complete the IRP with STATUS\_SUCCESS. If the provider cannot handle the specified UNC path, it must fail the IOCTL\_REDIR\_QUERY\_PATH request with an appropriate NTSTATUS error code and must not update the **LengthAccepted** member of the QUERY\_PATH\_RESPONSE structure. Providers must not modify any of the other members or the **FilePathName** string under any condition.

If the \\\\server\\share prefix name is not recognized in response to an IRP\_MJ\_CREATE or other IRPs that are using UNC names, the recommended NTSTATUS code to return is one of the following:

<span id="STATUS_BAD_NETWORK_PATH"></span><span id="status_bad_network_path"></span>STATUS\_BAD\_NETWORK\_PATH  
The network path cannot be located. The machine name (\\\\server, for example) is not valid or the network redirector cannot resolve the machine name (using whatever name resolution mechanisms are available).

<span id="STATUS_BAD_NETWORK_NAME"></span><span id="status_bad_network_name"></span>STATUS\_BAD\_NETWORK\_NAME  
The specified share name cannot be found on the remote server. The machine name (\\\\server, for example) is valid, but specified share name cannot be found on the remote server.

<span id="STATUS_INSUFFICIENT_RESOURCES"></span><span id="status_insufficient_resources"></span>STATUS\_INSUFFICIENT\_RESOURCES  
There were insufficient resources available to allocate memory for buffers.

<span id="STATUS_INVALID_DEVICE_REQUEST"></span><span id="status_invalid_device_request"></span>STATUS\_INVALID\_DEVICE\_REQUEST  
An IOCTL\_REDIR\_QUERY\_PATH request should only come from MUP and the requester mode of the IRP should always be **KernelMode**. This error code is returned if the requester mode of the calling thread was not **KernelMode**.

<span id="STATUS_INVALID_PARAMETER"></span><span id="status_invalid_parameter"></span>STATUS\_INVALID\_PARAMETER  
The **PathNameLength** member in the QUERY\_PATH\_REQUEST structure exceeds the maximum allowable length, UNICODE\_STRING\_MAX\_BYTES, for a Unicode string.

<span id="STATUS_LOGON_FAILURE_or_STATUS_ACCESS_DENIED"></span><span id="status_logon_failure_or_status_access_denied"></span><span id="STATUS_LOGON_FAILURE_OR_STATUS_ACCESS_DENIED"></span>STATUS\_LOGON\_FAILURE or STATUS\_ACCESS\_DENIED  
If the prefix resolution operation failed due to invalid or incorrect credentials, the provider should return the exact error code returned by the remote server; these error codes must not be translated to STATUS\_BAD\_NETWORK\_NAME or STATUS\_BAD\_NETWORK\_PATH. Error codes like STATUS\_LOGON\_FAILURE and STATUS\_ACCESS\_DENIED serve as a feedback mechanism to the user indicating the requirement to use appropriate credentials. These error codes are also used in certain cases to prompt the user automatically for credentials. Without these error codes, the user might assume that the machine is not accessible.

If the network redirector is unable to resolve a prefix, it must return an NTSTATUS code that closely matches the intended semantics from the above list of recommended NTSTATUS codes. A network redirector must not return the actual encountered error (STATUS\_CONNECTION\_REFUSED, for example) directly to MUP if the NTSTATUS code is not from the above list.

The length of the prefix claimed by the provider depends on an individual UNC provider. Most providers usually claim the \\\\&lt;servername&gt;\\&lt;sharename &gt; part of a path of the form \\\\&lt;servername&gt;\\&lt;sharename&gt;\\&lt;path&gt;. For example, if a provider claimed \\\\server\\public given a path \\\\server\\public\\dir1\\dir2, all name-based operations for the prefix \\\\server\\public (\\server\\public\\file1, for example) will be routed to that provider automatically without any prefix resolution since the prefix is already in the prefix cache. However, a path with the prefix \\server\\marketing\\presentation will go through prefix resolution.

If a network redirector claims a server name (\\\\server, for example), all requests for shares on this server will go to this network redirector. This behavior is only acceptable if there is no possibility of another share on the same server being accessed by a different network redirector. For example, a network redirector claiming \\\\server of a UNC path will prevent access by other network redirectors to other shares on this server (WebDAV access to \\\\server\\web, for example).

Any legacy network redirector (not based on using RDBSS) that registers as a UNC provider with MUP by calling [**FsRtlRegisterUncProvider**](https://msdn.microsoft.com/library/windows/hardware/ff547178) will receive the IOCTL\_REDIR\_QUERY\_PATH request.

A network mini-redirector that indicates support as a UNC provider will receive this prefix claim as if it were an IRP\_MJ\_CREATE call. This create request is similar to a user-mode **Createfile** call with FILE\_CREATE\_TREE\_CONNECTION flag set on. A network mini-redirector will not receive the prefix claim as a call to [**MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]**](https://msdn.microsoft.com/library/windows/hardware/ff550715). For a prefix claim, RDBSS will send an [**MRxCreateSrvCall**](https://msdn.microsoft.com/library/windows/hardware/ff549864) request to the network mini-redirector followed by a call to [**MRxSrvCallWinnerNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550824) and [**MRxCreateVNetRoot**](https://msdn.microsoft.com/library/windows/hardware/ff549869). When a network mini-redirector registers with RDBSS, the driver dispatch table for the network mini-redirector will be copied over by RDBSS to point to internal RDBSS entry points. RDBSS then receives this IOCTL\_REDIR\_QUERY\_PATH internally for the network mini-redirector and calls **MRxCreateSrvCall**, **MRxSrvCallWinnerNotify**, and **MRxCreateVNetRoot**. The original IOCTL\_REDIR\_QUERY\_PATH IRP will be contained in the RX\_CONTEXT structure passed to the **MRxCreateSrvCall** routine. In addition, the following members in the RX\_CONTEXT passed to **MRxCreateSrvCall** will be modified:

The **MajorFunction** member is set to IRP\_MJ\_CREATE even though the original IRP was IRP\_MJ\_DEVICE\_CONTROL.

The **PrefixClaim.SuppliedPathName.Buffer** member is set to the **FilePathName** member of the QUERY\_PATH\_REQUEST structure.

The **PrefixClaim.SuppliedPathName.Length** member is set to the **PathNameLength** member of the QUERY\_PATH\_REQUEST structure.

The **Create.NtCreateParameters.SecurityContext** member is set to the **SecurityContext** member of the QUERY\_PATH\_REQUEST structure.

The **Create.ThisIsATreeConnectOpen** member is set to **TRUE**.

The **Create.Flags** member has the RX\_CONTEXT\_CREATE\_FLAG\_UNC\_NAME bit set.

If the network mini-redirector wants to see details of the prefix claim, it can read these members in the RX\_CONTEXT passed to **MRxCreateSrvCall**. Otherwise it can just attempt to connect to the server share and return STATUS\_SUCCESS if the **MRxCreateSrvCall** call was successful. RDBSS will make the prefix claim on behalf of the network mini-redirector.

There is one case where a network mini-redirector could receive this IOCTL directly. A network mini-redirector could save a copy of its driver dispatch table before initializing and registering with RDBSS. After calling [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693) to register with RDBSS, the network mini-redirector could save a copy of the new driver dispatch table entry points installed by RDBSS and restore its original driver dispatch table. The restored driver dispatch table would need to be modified so that after checking the received IRP for those of interest to the network mini-redirector, the call is forwarded to the RDBSS driver dispatch entry points. RDBSS will copy over the driver dispatch table of a network mini-redirector when the driver initializes RDBSS and calls **RxRegisterMinrdr**. A network mini-redirector that links against *rdbsslib.lib* must save its original driver dispatch table before calling [**RxDriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff554404) from its **DriverEntry** routine to initialize the RDBSS static library and restore its driver dispatch table after calling **RxRegisterMinrdr**. This is because RDBSS copies over the network mini-redirector dispatch table in both the **RxDriverEntry** and **RxRegisterMinrdr** routines.

The order in which providers are queried during prefix resolution is controlled by the REG\_SZ ProviderOrder registry value stored under the following key:

```cpp
HKLM\System\CurrentControlSet\Control\NetworkProvider\Order
```

Individual provider names in the ProviderOrder registry value are separated by commas without any leading or trailing white space.

For example, this value could contain the string:

```cpp
RDPNP,LanmanWorkstation,WebClient
```

Given a UNC path \\\\&lt;server&gt;\\&lt;share&gt;\\&lt;path&gt;, MUP issues a prefix resolution request if the prefix (\\\\server\\share or \\\\server, for example) is not found in the MUP prefix cache. MUP sends a prefix resolution request to each provider in the following order until a provider claims the prefix (or all providers have been queried):

1.  TS client (RDPNP)

2.  SMB redirector (LanmanWorkstation)

3.  WebDAV redirector (WebClient)

Changes to the ProviderOrder registry value require a reboot to take effect in MUP on Windows Server 2003, Windows XP, and Windows 2000.

MUP uses each provider name listed to find the provider's registry key under the following registry key:

```cpp
HKLM\System\CurrentControlSet\Services\<ProviderName>
```

MUP then reads the DeviceName value under the NetworkProvider subkey to find the device name with which the provider will register. When the provider actually registers, MUP matches the device name passed in with the list of device names of known providers and places the provider in an ordered list for the purposes of prefix resolution. The order of providers in this list is based on the order specified in the ProviderOrder registry value discussed above.

Note that this provider order is also honored by the Multiple Provider Router (MPR), the user-mode DLL that establishes network connections based on queries to WNet providers.

Prior to Windows Server 2003 with Service Pack 1 and Windows XP with Service Pack 2, MUP behavior was to issue prefix resolution requests to all the providers "in parallel" in the order specified in the ProviderOrder registry value, and then wait for all of the providers to complete the prefix resolution operation. Thus, even if the first provider claimed the prefix, MUP still waits for all the other providers to complete the prefix resolution operation. When multiple providers respond with a prefix claim, MUP selects the provider based on the order specified in ProviderOrder registry value.

On Windows XP Service Pack 2 and later and on Windows Server 2003 Service Pack 1 and later, this behavior changed slightly. MUP issues the prefix resolution request serially and stops as soon as the first provider claims the prefix. Thus, in the above example, if RDPNP claims a prefix, MUP will not call the SMB or WebDAV redirectors.

The primary reason this behavior was changed is that a "serial prefix resolution" scheme prevents cases of a network redirector with lower priority in the ProviderOrder value from causing performance issues for a network redirector of higher priority in the ProviderOrder value. For example, consider a remote server, with a firewall in place, configured to block certain types of TCP/IP packets (access to HTTP, for example), but to allow others (SMB access, for example). In this case, even if the SMB network redirector is configured as the first provider in the ProviderOrder value and claims the prefix quickly, the WebDAV redirector might significantly delay the completion of the prefix resolution by waiting for the TCP connection to timeout.








