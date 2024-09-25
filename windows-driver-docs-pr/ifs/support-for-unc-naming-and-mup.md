---
title: Support for UNC Naming and MUP
description: Support for UNC Naming and MUP
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
ms.date: 09/25/2024
---

# Support for UNC Naming and MUP

This article describes how a network redirector can support [uniform naming convention (UNC)](/openspecs/windows_protocols/ms-dtyp/62e862f4-2a51-452e-8eeb-dc4ff5ee33cc) naming and the Multiple UNC Provider (MUP).

MUP is a system-supplied, kernel-mode component responsible for handling UNC paths:

* It helps locate network resources identified as using UNC.

* It channels all remote file system accesses using a UNC name to a network redirector capable of handling the remote file system requests. The network redirector is the *UNC provider*.

MUP is involved when an application uses a UNC path; for example, a command line command such as:

```cpp
notepad \\server\public\readme.txt
```

MUP receives commands containing UNC names from applications. It sends the name to each registered UNC provider and any other network providers that are installed. When a UNC provider identifies a UNC name as its own, the MUP automatically redirects future instances of that name to that provider.

MUP isn't involved during an operation that creates a mapped drive letter (the "NET USE" command, for example). Instead, the multiple provider router (MPR) and a user-mode [Windows Networking](/windows/win32/wnet/windows-networking-wnet-) (WNet) provider DLL for the network redirector handle this operation. However, a user-mode WNet provider DLL can communicate directly with a kernel-mode network redirector driver during this operation.

For network redirectors that conform to the redirector model introduced in Windows Vista, MUP is involved even when a mapped network drive is used. File operations performed on the mapped drive go through MUP to the network redirector. In this case, MUP simply passes the operation to the network redirector involved.

MUP is part of the *mup.sys* binary, which also includes the DFS (Distributed File System) client.

A kernel network redirector normally also has a user-mode WNet provider DLL to support establishing connections to remote resources (mapping drive letters to remote resources, for example). The MPR is a user-mode DLL that establishes network connections based on queries to WNet providers. Calls to the MPR are a result from any of the following operations:

* A ```net use x: \\server\share``` command issued from a command prompt.

* A network drive letter connection established from Windows Explorer.

* Direct calls to WNet functions.

A network redirector must register with MUP to handle UNC names. There can be multiple UNC providers registered with MUP. These UNC providers can be one or more of the following redirectors:

* Network mini-redirectors based on RDBSS, such as Server Message Block (SMB) redirector and WebDAV redirector.
* Legacy redirectors not based on RDBSS.

## Prefix resolution

MUP determines which provider can handle a UNC path in a name-based operation, typically an IRP_MJ_CREATE request. This determination is referred to as "prefix resolution." The prefix resolution operation serves two purposes:

* The name-based operation that resulted in the prefix resolution is routed to the provider claiming the prefix. If successful, MUP ensures that subsequent handle-based operations (IRP_MJ_READ and IRP_MJ_WRITE, for example) go to the same provider completely bypassing MUP.

* The provider and its claimed prefix are entered in a prefix cache that MUP maintains. For subsequent name-based operations, MUP uses this prefix cache to determine whether a provider has already claimed a prefix before attempting to perform a prefix resolution. Each entry in this prefix cache is subject to a timeout (referred to as *TTL*) once it's been added to the cache. An entry is thrown away after this timeout expires, at which point of time MUP performs prefix resolution again for this prefix on a subsequent name-based operation.

MUP performs prefix resolution by issuing an [**IOCTL_REDIR_QUERY_PATH**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-ioctl_redir_query_path) request to network redirectors registered with MUP. The input and output buffers for **IOCTL_REDIR_QUERY_PATH** are allocated from nonpaged pool.

Network redirectors should only allow kernel-mode senders of this IOCTL, by verifying that the **RequesterMode** member of the IRP structure is **KernelMode**.

MUP uses the [**QUERY_PATH_REQUEST**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-query_path_request) structure for the request information.

UNC providers should use the [**QUERY_PATH_RESPONSE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-query_path_response) structure for the response information.

Any legacy network redirector (not based on using RDBSS) that registers as a UNC provider with MUP by calling [**FsRtlRegisterUncProvider**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlregisteruncprovider) receives the **IOCTL_REDIR_QUERY_PATH** request.

A network mini-redirector that indicates support as a UNC provider receives this prefix claim as if it were an IRP_MJ_CREATE call. This create request is similar to a user-mode **CreateFile** call with FILE_CREATE_TREE_CONNECTION flag set on. A network mini-redirector doesn't receive the prefix claim as a call to [**MRxLowIOSubmit\[LOWIO_OP_IOCTL\]**](./mrxlowiosubmit-lowio-op-ioctl-.md). For a prefix claim, RDBSS sends an [**MRxCreateSrvCall**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_create_srvcall) request to the network mini-redirector followed by a call to [**MRxSrvCallWinnerNotify**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_srvcall_winner_notify) and [**MRxCreateVNetRoot**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_create_v_net_root). When a network mini-redirector registers with RDBSS, RDBSS copies the driver dispatch table for the network mini-redirector to point to internal RDBSS entry points. RDBSS then receives this **IOCTL_REDIR_QUERY_PATH** internally for the network mini-redirector and calls **MRxCreateSrvCall**, **MRxSrvCallWinnerNotify**, and **MRxCreateVNetRoot**. The original **IOCTL_REDIR_QUERY_PATH** IRP is contained in the RX_CONTEXT structure passed to the **MRxCreateSrvCall** routine. In addition, the following members in the RX_CONTEXT passed to **MRxCreateSrvCall** are modified:

* The **MajorFunction** member is set to IRP_MJ_CREATE even though the original IRP was IRP_MJ_DEVICE_CONTROL.
* The **PrefixClaim.SuppliedPathName.Buffer** member is set to the **FilePathName** member of the QUERY_PATH_REQUEST structure.
* The **PrefixClaim.SuppliedPathName.Length** member is set to the **PathNameLength** member of the QUERY_PATH_REQUEST structure.
* The **Create.NtCreateParameters.SecurityContext** member is set to the **SecurityContext** member of the QUERY_PATH_REQUEST structure.
* The **Create.ThisIsATreeConnectOpen** member is set to TRUE.
* The **Create.Flags** member has the RX_CONTEXT_CREATE_FLAG_UNC_NAME bit set.

If the network mini-redirector wants to see details of the prefix claim, it can read these members in the RX_CONTEXT passed to **MRxCreateSrvCall**. Otherwise it can just attempt to connect to the server share and return STATUS_SUCCESS if the **MRxCreateSrvCall** call was successful. RDBSS makes the prefix claim on behalf of the network mini-redirector.

There's one case where a network mini-redirector could receive this IOCTL directly. A network mini-redirector could save a copy of its driver dispatch table before initializing and registering with RDBSS. After calling [**RxRegisterMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxregisterminirdr) to register with RDBSS, the network mini-redirector could save a copy of the new driver dispatch table entry points installed by RDBSS and restore its original driver dispatch table. The restored driver dispatch table would need to be modified so that after checking the received IRP for those IRPs of interest to the network mini-redirector, the call is forwarded to the RDBSS driver dispatch entry points. RDBSS copies over the driver dispatch table of a network mini-redirector when the driver initializes RDBSS and calls **RxRegisterMinrdr**. A network mini-redirector that links against *rdbsslib.lib* must save its original driver dispatch table before calling [**RxDriverEntry**](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdriverentry) from its **DriverEntry** routine to initialize the RDBSS static library and restore its driver dispatch table after calling **RxRegisterMinrdr**. This requirement is because RDBSS copies over the network mini-redirector dispatch table in both the **RxDriverEntry** and **RxRegisterMinrdr** routines.

The REG_SZ ProviderOrder registry value controls the order in which providers are queried during prefix resolution. This value is stored under the following key:

```cpp
HKLM\System\CurrentControlSet\Control\NetworkProvider\Order
```

Individual provider names in the ProviderOrder registry value are separated by commas without any leading or trailing white space.

For example, this value could contain the string:

```cpp
RDPNP,LanmanWorkstation,WebClient
```

Given a UNC path \\\\\<server>\\\<share>\\\<path>, MUP issues a prefix resolution request if the prefix (\\\\server\\share or \\\\server, for example) isn't found in the MUP prefix cache. MUP sends a prefix resolution request to each provider in the following order until a provider claims the prefix, or until all providers are queried:

1. TS client (RDPNP)

2. SMB redirector (LanmanWorkstation)

3. WebDAV redirector (WebClient)

Changes to the ProviderOrder registry value require a reboot to take effect in MUP.

MUP uses each provider name listed to find the provider's registry key under the following registry key:

```cpp
HKLM\System\CurrentControlSet\Services\<ProviderName>
```

MUP then reads the DeviceName value under the NetworkProvider subkey to find the device name with which the provider will register. When the provider actually registers, MUP matches the device name passed in with the list of device names of known providers. It then places the provider in an ordered list for the purposes of prefix resolution. The order of providers in this list is based on the order specified in the ProviderOrder registry value previously discussed.

The Multiple Provider Router (MPR), the user-mode DLL that establishes network connections based on queries to WNet providers, also honors this provider order.

MUP issues the prefix resolution request serially and stops as soon as the first provider claims the prefix. Thus, in the prior example, if RDPNP claims a prefix, MUP doesn't call the SMB or WebDAV redirectors.

"Serial prefix resolution" (versus parallel) prevents a network redirector with lower ProviderOrder priority from causing performance issues for a network redirector of higher ProviderOrder priority. For example, consider a remote server, with a firewall in place, configured to block certain types of TCP/IP packets (access to HTTP, for example), but to allow others (SMB access, for example). In this case, even if the SMB network redirector is configured as the first provider in the ProviderOrder value and claims the prefix quickly, the WebDAV redirector might significantly delay the completion of the prefix resolution by waiting for the TCP connection to time out.
