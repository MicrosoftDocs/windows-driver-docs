---
title: The Kernel Network Mini-Redirector Driver
description: The Kernel Network Mini-Redirector Driver
ms.assetid: 13236e5f-1261-4cf1-9c3d-3f1a5ccb3323
keywords:
- network redirectors WDK , mini-redirector drivers
- redirector drivers WDK , mini-redirector drivers
- kernel network redirectors WDK , mini-redirector drivers
- mini-redirectors WDK
- mini-redirectors WDK , about kernel network mini-redirector drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Kernel Network Mini-Redirector Driver


## <span id="ddk_the_kernel_network_mini_redirector_driver_if"></span><span id="DDK_THE_KERNEL_NETWORK_MINI_REDIRECTOR_DRIVER_IF"></span>


A kernel network mini-redirector driver implements a number of callback routines that are used by the Redirected Drive Buffering Subsystem (RDBSS) to communicate with the driver. In the remainder of this document, a kernel network mini-redirector driver will be referred to as a network mini-redirector driver.

When a network mini-redirector driver first starts (in its **DriverEntry** routine), the driver calls the RDBSS [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693) routine to register the network mini-redirector driver with RDBSS. The network mini-redirector driver passes in a MINIRDR\_DISPATCH structure, which includes configuration data along with pointers to the routines that the network mini-redirector driver implements (a dispatch table).

A network mini-redirector can choose to implement only some of these routines. Any routine that is not implemented by the network mini-redirector should be set to a **NULL** pointer in the MINIRDR\_DISPATCH structure passed to **RxRegisterMinirdr**. RDBSS will only call routines implemented by the network mini-redirector.

One special category of routines implemented by a network mini-redirector are the low I/O operations that represent the traditional file I/O calls for read, write, and other file operations. All of the low I/O routines can be called asynchronously by RDBSS. A kernel driver for a network mini-redirector must make certain that any low I/O routines that are implemented can be safely called asynchronously. The low I/O routines are passed in as an array of routine pointers as part of the MINIRDR\_DISPATCH structure from the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. The value of the array entry is the low I/O operation to perform. All of the low I/O routines expect a pointer to an RX\_CONTEXT structure to be passed in as a parameter. The RX\_CONTEXT data structure has a **LowIoContext.Operation** member that also specifies the low I/O operation to perform. It is possible for several of the low I/O routines to point to the same routine in a network mini-redirector driver since this **LowIoContext.Operation** member can be used to specify the low I/O operation requested. For example, all of the low I/O calls related to file locks could call the same low I/O routine in the network mini-redirector and this routine could use the **LowIoContext.Operation** member to specify the lock or unlock operation requested.

RDBSS also assumes asynchronous operation for a few other routines implemented by a network mini-redirector. These routines are used for establishing a connection with a remote resource. Since connection operations can take a considerable amount of time to complete, RDBSS assumes these routines are implemented as asynchronous operations.

RDBSS assumes that all routines implemented by a network mini-redirector other than the low I/O and connection-related routines are based on synchronous calls. However, this is subject to change in future releases of the Windows operating system.

All of the routines implemented by a network mini-redirector return an NTSTATUS value on completion. Most routines return STATUS\_SUCCESS on success or an appropriate NTSTATUS value. In addition to return values specific to a particular routine, there are two generic categories of errors that can be returned for most routines :

-   Network errors

-   Authentication errors

Possible network errors include the following:

<span id="STATUS_IO_TIMEOUT"></span><span id="status_io_timeout"></span>STATUS\_IO\_TIMEOUT  
The I/O request to the remote server has timed out.

<span id="STATUS_BAD_NETWORK_PATH"></span><span id="status_bad_network_path"></span>STATUS\_BAD\_NETWORK\_PATH  
The I/O request was to a network path that does not exist. This error can occur if a directory was renamed or deleted.

<span id="STATUS_NETWORK_UNREACHABLE"></span><span id="status_network_unreachable"></span>STATUS\_NETWORK\_UNREACHABLE  
The network is unreachable from the client.

<span id="STATUS_REMOTE_NOT_LISTENING"></span><span id="status_remote_not_listening"></span>STATUS\_REMOTE\_NOT\_LISTENING  
The remote server is not listening for connections.

<span id="STATUS_USER_SESSION_DELETED"></span><span id="status_user_session_deleted"></span>STATUS\_USER\_SESSION\_DELETED  
The user session on the server has been deleted. The session may have timed out, the server may have been restarted causing all existing user sessions to be deleted, or an administrator on the server may have forced a delete of the user session .

<span id="STATUS_CONNECTION_DISCONNECTED"></span><span id="status_connection_disconnected"></span>STATUS\_CONNECTION\_DISCONNECTED  
The connection to the remote server was disconnected.

<span id="STATUS_NETWORK_NAME_DELETED"></span><span id="status_network_name_deleted"></span>STATUS\_NETWORK\_NAME\_DELETED  
The I/O request is for a network name that has been deleted.

Possible authentication errors include the following:

<span id="STATUS_LOGON_FAILURE"></span><span id="status_logon_failure"></span>STATUS\_LOGON\_FAILURE  
The login request to the remote server failed.

<span id="STATUS_NETWORK_CREDENTIAL_CONFLICT"></span><span id="status_network_credential_conflict"></span>STATUS\_NETWORK\_CREDENTIAL\_CONFLICT  
There was a conflict with the network credentials that were presented.

<span id="STATUS_DOWNGRADE_DETECTED"></span><span id="status_downgrade_detected"></span>STATUS\_DOWNGRADE\_DETECTED  
A change of the network protocol used by the client to communicate with the server was detected by the server and the change was to an older version of the protocol.

<span id="STATUS_LOGIN_WKSTA_RESTRICTION"></span><span id="status_login_wksta_restriction"></span>STATUS\_LOGIN\_WKSTA\_RESTRICTION  
There is a restriction on workstation logins to the server.

The following sections discuss in detail the routines that can be implemented by a network mini-redirector:

[Routines Implemented by the Kernel Network Mini-Redirector](routines-implemented-by-the-kernel-network-mini-redirector.md)

[Routines Not Used by RDBSS](routines-not-used-by-rdbss.md)

The routines implemented by a network mini-redirector can be organized into the following categories based on their function:

[Connection and Name Resolution](connection-and-name-resolution.md)

[Driver Start, Stop, and Device Control](driver-start--stop--and-device-control.md)

[File System Object Creation and Deletion](file-system-object-creation-and-deletion.md)

[File System Object I/O Routines](file-system-object-i-o-routines.md)

[File System Object Query and Set Routines](file-system-object-query-and-set-routines.md)

[Miscellaneous Network Mini-Redirector Routines](miscellaneous-network-mini-redirector-routines.md)

 

 




