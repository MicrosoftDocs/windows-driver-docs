---
title: MUP Changes in Microsoft Windows Vista
description: MUP Changes in Microsoft Windows Vista
ms.assetid: 8ca2f9bc-14f1-45d3-a397-f3e5459cf8ec
keywords:
- kernel network redirectors WDK , MUP
- MUP WDK network redirectors
- multiple UNC provider WDK network redirectors
- UNC WDK network redirectors
- kernel network redirectors WDK , Windows Vista redirector model
- legacy redirectors WDK file systems
- prefix resolution WDK network redirectors
- prefix cache WDK network redirectors
- double filtering WDK network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MUP Changes in Microsoft Windows Vista


Windows Vista implements a number of changes to the multiple UNC provider (MUP) that can affect network redirectors.

MUP and the Distributed File System (DFS) client are in separate binary files. The MUP component is in mup.sys and the DFS client is in dfsc.sys. On Windows Server 2003, Windows XP, and Windows 2000, the MUP kernel component, mup.sys, also contained the DFS client.

A new redirector model is defined on Windows Vista:

-   MUP registers as a file system with the I/O manager by calling [**IoRegisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548494).

-   A network redirector registers with MUP using [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184) , a new routine introduced in Windows Vista.

-   A network redirector passes an unnamed device object to [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184).

-   A network redirector passes a device name to [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184).

-   A network redirector does not register as a file system with the I/O manager (does not call [**IoRegisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548494)).

-   All calls from MUP to a network redirector, including prefix resolution, IOCTLs, and FSCTLs, are made with APCs enabled. All calls from other components to MUP are expected to be made with APCs enabled. When calls are used with [**FsRtlCancellableWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff545738) or [**FsRtlCancellableWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff545731), new routines introduced in Windows Vista, this will ensure that long waits can be aborted if a thread that issued an I/O request is terminated.

-   Prefix resolution is performed using IOCTL\_REDIR\_QUERY\_PATH\_EX, a new IOCTL introduced in Windows Vista.

-   A network redirector device name registered with MUP becomes a symbolic link to the MUP device object.

For a network redirector conforming to the Windows Vista redirector model, MUP creates a symbolic link in the object manager namespace with the device name specified by the network redirector in the call to [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184). The target of this symbolic link is the MUP device object (\\Device\\Mup).

The advantage of registering MUP as a file system and the device name of the network redirector being a symbolic link to the MUP device object is that all remote file system I/O operations, and not just name-based operations, go through MUP. So file system filter drivers that need to be on the remote file system stack can simply attach to the MUP device object. It is not necessary for file system filter drivers to hardcode provider device object names (\\Device\\LanmanRedirector, for example) into their driver anymore. In this way, file system filter drivers can monitor all I/O operations issued to all network redirectors by a single attachment. This also eliminates duplicate I/O operations seen by file system filter drivers prior to Windows Vista, which attached separately to DFS (mup.sys) and individual network redirectors (\\Device\\LanmanRedirector, for example) in order to monitor I/O operations to both.

A file system filter driver that is attached to the MUP device object can selectively filter the traffic that is sent to specific network redirectors. In this situation, the filter driver maps the device names of the network redirectors of interest to provider identifiers by calling the [**FsRtlMupGetProviderIdFromName**](https://msdn.microsoft.com/library/windows/hardware/ff546971) routine. The filter driver can then determine whether it should filter the traffic for a particular file object by comparing the provider identifier that is obtained by calling the [**FsRtlMupGetProviderInfoFromFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff546981) routine with the provider identifiers of the network directors of interest.

For a network redirector conforming to the Windows Vista redirector model:

-   All file objects on the remote file system stack resolve to MUP. Hence, [**IoGetDeviceAttachmentBaseRef**](https://msdn.microsoft.com/library/windows/hardware/ff548365) returns the device object for MUP, not the network redirector that owns the file object. However, the content of the file object is still owned by the network redirector.

-   An IRP\_MJ\_CREATE issued to the device name of a network redirector (\\Device\\LanmanRedirector\\server\\share, for example) will be targeted to that network redirector without going through MUP prefix resolution, exactly as it was on Windows Server 2003, Windows XP, and Windows 2000.

Network redirectors that are not based on the Windows Vista RDBSS (linking dynamically or statically) are termed "legacy redirectors". These legacy network redirectors include:

-   Network redirectors written for Windows Server 2003, Windows XP, and Windows 2000 that register directly with MUP using [**FsRtlRegisterUncProvider**](https://msdn.microsoft.com/library/windows/hardware/ff547178).

-   Network mini-redirectors written for Windows Server 2003, Windows XP, and Windows 2000 that statically link with the rdbsslib.lib library for Windows Server 2003, Windows XP, or Windows 2000.

-   Network redirectors written for Windows Vista that register directly with MUP using [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184).

Network mini-redirectors that dynamically link against the Windows Vista RDBSS (rdbss.sys) automatically conform to the Windows Vista redirector model because RDBSS registers with MUP using [*FsRtlRegisterUncProviderEx*](https://msdn.microsoft.com/library/windows/hardware/ff547184). Network mini-redirectors that statically link against the Windows Vista RDBSS (rdbsslib.lib) also automatically conform to the Windows Vista redirector model because RDBSS registers with MUP using **FsRtlRegisterUncProviderEx**.

A legacy network redirector written for Windows Vista that registers directly with MUP must comply with the Windows Vista redirector model.

Network redirectors written for Windows Server 2003, Windows XP, and Windows 2000 that register with MUP directly using the [**FsRtlRegisterUncProvider**](https://msdn.microsoft.com/library/windows/hardware/ff547178) continue to work exactly the same way as they did on Windows Server 2003, Windows XP, and Windows 2000. Network mini-redirectors written for Windows Server 2003, Windows XP, and Windows 2000 that statically link with the rdbsslib.lib library for Windows Server 2003, Windows XP, and Windows 2000 continue to work exactly the same way as they did on Windows Server 2003, Windows XP, and Windows 2000. These legacy network redirectors and mini-redirectors exhibit the following behavior:

-   They will be visible to file system filter drivers that monitor file system registration.

-   Their device objects are named. The device names are not symbolic links and do not point to \\Device\\MUP.

-   File objects resolve to the named device object of the network redirector.

-   MUP is involved only in the prefix resolution operation. Once the network provider has been identified, MUP "gets out of the way" by returning STATUS\_REPARSE. All subsequent operations will not pass through MUP.

This behavior has been retained to prevent double filtering that would otherwise happen if the provider device name were a symbolic link to \\Device\\MUP. This double filtering would occur for the following reasons:

-   The file system filter driver is already attached to \\Device\\MUP.

-   The file system filter driver attaches to any registering file system. Since network redirectors that use named device objects register themselves as file systems, a file system filter driver would end up filtering the same I/O twice.

Calls to and from MUP on Windows Vista are made with APCs enabled, which has the following impacts:

-   It is important to protect, if required, code paths that get called from MUP against thread suspension by appropriate means, especially IOCTL\_REDIR\_QUERY\_PATH handlers. Note that a thread suspend is a potentially "unbounded wait" operation that can last a long time.

-   It is important to ensure that any "wait for I/O" operation involving user-mode threads (as opposed to system threads) always uses "cancellable waits". See the [**FsRtlCancellableWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff545738) and [**FsRtlCancellableWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff545731) routines for details.

-   Deadlocks might occur when a thread gets suspended holding some important lock. It is important to run tests in the presence of user-mode threads getting suspended arbitrarily to check for deadlock conditions.

-   It is important to run tests to verify whether "wait for I/O operations" are really cancellable and that a user-mode application can terminate a thread quickly enough so that the application does not appear to be in a "non-responding" state when attempting to terminate said thread.

The prefix cache size and timeout used by MUP on Windows Vista are now controlled by the following registry values:

-   PrefixCacheSizeInKB

-   PrefixCacheTimeoutInSeconds.

These registry values can be changed dynamically without a reboot. These registry values are under the following registry key:

```cpp
HKLM\System\CurrentControlSet\Services\Mup\Parameters.
```

The ProviderOrder registry value that determines the order in which MUP issues prefix resolution requests to individual redirectors can be changed dynamically without rebooting the system. This registry value is located under the following registry key:

```cpp
HKLM\CurrentControlSet\Control\NetworkProvider\Order
```

On Windows Vista, MUP performs prefix resolution differently depending on whether the network redirector registered with MUP by calling [**FsRtlRegisterUncProvider**](https://msdn.microsoft.com/library/windows/hardware/ff547178) or [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184). Legacy network redirectors that register with MUP by calling **FsRtlRegisterUncProvider** will receive an [**IOCTL\_REDIR\_QUERY\_PATH**](https://msdn.microsoft.com/library/windows/hardware/ff548313) request for prefix resolution. This is the same method that is used on Windows Server 2003, Windows XP, and Windows 2000.

Network redirectors that conform to the Windows Vista redirector model and register with MUP by calling [**FsRtlRegisterUncProviderEx**](https://msdn.microsoft.com/library/windows/hardware/ff547184) will receive an [**IOCTL\_REDIR\_QUERY\_PATH\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff548320) request for prefix resolution. Note that on Windows Vista, network mini-redirectors statically linked with rdbsslib.lib or dynamically linked with rdbss.sys will call **FsRtlRegisterUncProviderEx** indirectly through RDBSS.

The input and output buffers for IOCTL\_REDIR\_QUERY\_PATH\_EX are as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left">Parameter available at</td>
<td align="left">Data structure format</td>
</tr>
<tr class="even">
<td align="left"><p>Input buffer</p></td>
<td align="left"><p>IrpSp-&gt; Parameters.DeviceIoControl.Type3InputBuffer</p></td>
<td align="left"><p>QUERY_PATH_REQUEST_EX</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Output buffer</p></td>
<td align="left"><p>IRP-&gt;UserBuffer</p></td>
<td align="left"><p>QUERY_PATH_RESPONSE</p></td>
</tr>
</tbody>
</table>



The IOCTL and the data structures are defined in ntifs.h. The buffers are allocated from non-paged pool.

Network redirectors should only honor kernel-mode senders of this IOCTL, by verifying that **Irp-&gt;RequestorMode** is **KernelMode**.

MUP uses the QUERY\_PATH\_REQUEST\_EX data structure for the request information.

```cpp
typedef struct _QUERY_PATH_REQUEST_EX {
  PIO_SECURITY_CONTEXT  pSecurityContext;
 ULONG  EaLength;
 PVOID  pEaBuffer;
  UNICODE_STRING  PathName;
} QUERY_PATH_REQUEST_EX, *PQUERY_PATH_REQUEST_EX;
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>pSecurityContext</strong></p></td>
<td align="left"><p>A pointer to the security context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>EaLength</strong></p></td>
<td align="left"><p>The length, in bytes, of the extended attributes buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>pEaBuffer</strong></p></td>
<td align="left"><p>Pointer to the extended attributes buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>PathName</strong></p></td>
<td align="left"><p>A non-NULL terminated Unicode string of the form &amp;lt;server&gt;&amp;lt;share&gt;&amp;lt;path&gt;.</p></td>
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
<th align="left">Structure member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>LengthAccepted</strong></p></td>
<td align="left"><p>The length, in bytes, of the prefix claimed by the provider from the Unicode string path specified in the <strong>PathName</strong> member of the QUERY_PATH_REQUEST_EX structure.</p></td>
</tr>
</tbody>
</table>



Note that IOCTL\_REDIR\_QUERY\_PATH\_EX is a METHOD\_NEITHER IOCTL. This means that the input and output buffers might not be at the same address. A common mistake by UNC providers is to assume that the input buffer and the output buffer are the same and use the input buffer pointer to provide the response.

When a UNC provider receives an IOCTL\_REDIR\_QUERY\_PATH\_EX request, it has to determine whether it can handle the UNC path specified in the **PathName** member of the QUERY\_PATH\_REQUEST\_EX structure. If so, the UNC provider has to update the **LengthAccepted** member of the QUERY\_PATH\_RESPONSE structure with the length, in bytes, of the prefix it has claimed and complete the IRP with STATUS\_SUCCESS. If the provider cannot handle the UNC path specified, it must fail the IOCTL\_REDIR\_QUERY\_PATH\_EX request with an appropriate NTSTATUS error code and must not update the **LengthAccepted** member of the QUERY\_PATH\_RESPONSE structure. Providers must not modify any of the other members or the **PathName** string under any condition.

On Windows Vista, a network mini-redirector based on using RDBSS that indicates support as a UNC provider will receive this prefix claim as if it were a regular tree connect create, similar to a user-mode Createfile call with FILE\_CREATE\_TREE\_CONNECTION flag set. RDBSS will send an [**MRxCreateSrvCall**](https://msdn.microsoft.com/library/windows/hardware/ff549864) request to the network mini-redirector followed by a call to [**MRxSrvCallWinnerNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550824) and [**MRxCreateVNetRoot**](https://msdn.microsoft.com/library/windows/hardware/ff549869). This prefix claim will not be received as a call to [**MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]**](https://msdn.microsoft.com/library/windows/hardware/ff550715). When a network mini-redirector registers with RDBSS, the driver dispatch table for the network mini-redirector will be copied over by RDBSS to point to internal RDBSS entry points. RDBSS then receives this IOCTL\_REDIR\_QUERY\_PATH\_EX internally for the network mini-redirector and calls **MRxCreateSrvCall**, **MRxSrvCallWinnerNotify**, and **MRxCreateVNetRoot**. The original IOCTL\_REDIR\_QUERY\_PATH\_EX IRP will be contained in the RX\_CONTEXT passed to the **MRxCreateSrvCall** routine. In addition, the following members in the RX\_CONTEXT passed to **MRxCreateSrvCall** will be modified:

The **MajorFunction** member is set to IRP\_MJ\_CREATE even though the original IRP was IRP\_MJ\_DEVICE\_CONTROL.

The **PrefixClaim.SuppliedPathName.Buffer** member is set to the **PathName.Buffer** member of the QUERY\_PATH\_REQUEST\_EX structure.

The **PrefixClaim.SuppliedPathName.Length** member is set to the **PathName.Length** member of the QUERY\_PATH\_REQUEST\_EX structure.

The **Create.ThisIsATreeConnectOpen** member is set to the **TRUE**.

The **Create.ThisIsAPrefixClaim** member is set to the **TRUE**.

The **Create.NtCreateParameters.SecurityContext** member is set to the **SecurityContext** member of the QUERY\_PATH\_REQUEST\_EX structure.

The **Create.EaBuffer** member is set to the **pEaBuffer** member of the QUERY\_PATH\_REQUEST\_EX structure.

The **Create.EaLength** member is set to the **EaLength** member of the QUERY\_PATH\_REQUEST\_EX structure.

The **Create.Flags** member will have the RX\_CONTEXT\_CREATE\_FLAG\_UNC\_NAME bit set.

If the network mini-redirector wants to see details of the prefix claim, it can read these members in the RX\_CONTEXT structure that is passed to [**MRxCreateSrvCall**](https://msdn.microsoft.com/library/windows/hardware/ff549864). Otherwise, it can just attempt to connect to the server share and return STATUS\_SUCCESS if the **MRxCreateSrvCall** call was successful. RDBSS will make the prefix claim on behalf of the network mini-redirector.








