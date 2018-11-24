---
title: System-Defined ECPs
description: System-Defined ECPs
ms.assetid: 6acb4be4-a7aa-431d-b2d8-3ef6d41cb4ef
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Defined ECPs


The operating system defines the following ECPs in the *Ntifs.h* header file. These system-defined ECPs attach the specified extra information to the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation on a file. Elements of the file-system stack can query the ECPs for the extra information.

Typically, a filter that processes the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation on a file and then passes the file down to filters below it must not attach and spoof any of the following system-defined ECPs to the **IRP\_MJ\_CREATE** operation on the file. Similarly, a kernel-mode driver that processes and issues IRP\_MJ\_CREATE operations on files must not attach and spoof any of the following system-defined ECPs to the IRP\_MJ\_CREATE operations on the files. The following system-defined ECPs are read-only. You should use them to retrieve information only.

One exception to restricting a filter driver from attaching any of the following system-defined ECPs is when the filter driver implements a layered file system. It does this by owning file objects and by issuing its own [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operations on files below its filter, in response to the IRP\_MJ\_CREATE operation on a file that the filter driver services on its own file objects. Such a filter driver should propagate any ECP context structure lists (ECP\_LIST) from the original IRP\_MJ\_CREATE operation on a file to the IRP\_MJ\_CREATE operations that the filter driver issues below it. By propagating these ECP lists, the filter driver ensures that any filters below the filter that issues the IRP\_MJ\_CREATE operations are aware of the context of the original IRP\_MJ\_CREATE operation.

<span id="GUID_ECP_OPLOCK_KEY"></span><span id="guid_ecp_oplock_key"></span>GUID\_ECP\_OPLOCK\_KEY  
A GUID that identifies the [**OPLOCK\_KEY\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551003) structure and is used to attach an oplock key to the open file request. The oplock key lets an application open multiple handles to the same stream without breaking the application's own oplock.

For more information about oplocks and oplock keys, see [Oplock Semantics Overview](overview.md).

<span id="GUID_ECP_NETWORK_OPEN_CONTEXT"></span><span id="guid_ecp_network_open_context"></span>GUID\_ECP\_NETWORK\_OPEN\_CONTEXT  
A GUID that identifies the [**NETWORK\_OPEN\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff550896) structure and is used to attach extra information for network redirectors. This GUID also identifies the [**NETWORK\_OPEN\_ECP\_CONTEXT\_V0**](https://msdn.microsoft.com/library/windows/hardware/ff550899) structure for drivers that run on Windows 7 and later versions of Windows and that must interpret network ECP contexts on files that reside on Windows Vista.

<span id="GUID_ECP_PREFETCH_OPEN"></span><span id="guid_ecp_prefetch_open"></span>GUID\_ECP\_PREFETCH\_OPEN  
A GUID that identifies the [**PREFETCH\_OPEN\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551843) structure.

The prefetcher is a component of the operating system that is tightly integrated with the cache manager and the memory manager to make disk accesses more efficient and therefore improve performance. If other components interfere with the prefetcher, system performance decreases and might deadlock. Therefore, the prefetcher attaches the PREFETCH\_OPEN\_ECP\_CONTEXT structure to a file to communicate that the prefetcher performs an open request on the file. This open request is specified by the **Context** member of PREFETCH\_OPEN\_ECP\_CONTEXT. Other components, such as, file system filter drivers, can determine whether PREFETCH\_OPEN\_ECP\_CONTEXT is attached to the file and then take appropriate action.

<span id="GUID_ECP_NFS_OPEN"></span><span id="guid_ecp_nfs_open"></span>GUID\_ECP\_NFS\_OPEN  
A GUID that identifies the [**NFS\_OPEN\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff550942) structure. The Network File System (NFS) server attaches the NFS\_OPEN\_ECP\_CONTEXT structure to an open file request. The NFS server uses this GUID on any open file request that the NFS server makes to satisfy a client request. The file-system stack can then determine whether NFS\_OPEN\_ECP\_CONTEXT is attached to the open file request. Based on the information in NFS\_OPEN\_ECP\_CONTEXT the file-system stack can determine the client that requested that the file be opened and why.

<span id="GUID_ECP_SRV_OPEN"></span><span id="guid_ecp_srv_open"></span>GUID\_ECP\_SRV\_OPEN  
A GUID that identifies the [**SRV\_OPEN\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff556749) structure. A server attaches the SRV\_OPEN\_ECP\_CONTEXT structure to an open file request. The server uses this GUID on any open file request that the server makes to satisfy a conditional client request. The file-system stack can then determine whether SRV\_OPEN\_ECP\_CONTEXT is attached to the open file request. Based on the information in SRV\_OPEN\_ECP\_CONTEXT the file-system stack can determine the client that requested that the file be opened and why.

<span id="GUID_ECP_DUAL_OPLOCK_KEY"></span><span id="guid_ecp_dual_oplock_key"></span>GUID\_ECP\_DUAL\_OPLOCK\_KEY  
A GUID that identifies the [**DUAL OPLOCK\_KEY\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/hh406392) structure. Like the [**OPLOCK\_KEY\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551003) structure, **DUAL OPLOCK\_KEY\_ECP\_CONTEXT** is used to attach an oplock key to the open file request. With **DUAL OPLOCK\_KEY\_ECP\_CONTEXT**, however, a parent key can also be set to provide oplock for a target file's directory.

<span id="GUID_ECP_IO_DEVICE_HINT"></span><span id="guid_ecp_io_device_hint"></span>GUID\_ECP\_IO\_DEVICE\_HINT  
A GUID that identifies the **IO\_DEVICE\_HINT\_ECP\_CONTEXT** structure. Device hints are used to assist name provider minifilter drivers in tracking a reparse target to new device.

<span id="GUID_ECP_NETWORK_APP_INSTANCE"></span><span id="guid_ecp_network_app_instance"></span>GUID\_ECP\_NETWORK\_APP\_INSTANCE  
A GUID that identifies the [**NETWORK\_APP\_INSTANCE\_ECP\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/hh439443) structure. A client application in a failover cluster may have a set of files opened on a node in the cluster. The file objects are tagged to an application by an instance identifier in the **NETWORK\_APP\_INSTANCE\_ECP\_CONTEXT** structure. On failover, a secondary node can validate a client application's access to the opened files with the previously cached application instance identifier.

 

 




