---
title: I/O Manager Support Routines
description: I/O Manager Support Routines
ms.assetid: f0b0099e-f920-4287-9e5d-e0fd4241f100
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# I/O Manager Support Routines

The following system-supplied I/O Manager functions and macros can be called by kernel-mode file systems and file system filter (minifilter or legacy filter) drivers. They cannot be used by device drivers. They are listed in alphabetic order.

In addition to the routines listed here, file systems and filter drivers can also call any of the Io*Xxx*** routines described in the [Windows Kernel Reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/_kernel/) section that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Io**_Xxx_, **IsReparseTag**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **IoAcquireVpbSpinLock** | Acquires the Volume Parameter Block (VPB) spin lock. |
| **IoAttachDeviceToDeviceStackSafe** | Attaches the caller's device object to the topmost device object in a driver stack. |
| **IoCancelFileOpen** | Can be used by a file system filter driver to close a file that has been opened by a file system driver in the filter driver's device stack. |
| **IoCheckDesiredAccess** | Reserved for system use. |
| **IoCheckEaBufferValidity** | Checks whether the specified extended attribute (EA) buffer is valid. |
| **IoCheckFunctionAccess** | Reserved for system use. |
| **IoCheckQuerySetFileInformation** | Reserved for system use. |
| **IoCheckQuerySetVolumeInformation** | Reserved for system use. |
| **IoCheckQuotaBufferValidity** | Checks whether the specified quota buffer is valid. |
| **IoCreateFileEx** | Either causes a new file or directory to be created, or opens an existing file, device, directory, or volume and gives the caller a handle for the file object. File system filter drivers (legacy filter drivers) call this routine. |
| **IoCreateFileSpecifyDeviceObjectHint** | Used by file system filter drivers to send a create request only to the filters below a specified device object and to the file system. |
| **IoCreateStreamFileObject** | Creates a new stream file object. |
| **IoCreateStreamFileObjectEx** | Creates a new stream file object. |
| **IoCreateStreamFileObjectEx2** | Creates a new stream file object with create options for a target device object. |
| **IoCreateStreamFileObjectLite** | Creates a new stream file object, but does not cause an IRP_MJ_CLEANUP request to be sent to the file system driver stack. |
| **IoEnumerateDeviceObjectList** | Enumerates a driver's device object list. |
| **IoEnumerateRegisteredFiltersList** | Enumerates the file system filter drivers that have registered with the system. |
| **IoFastQueryNetworkAttributes** | Reserved for system use. |
| **IoGetAttachedDevice** | Returns a pointer to the highest-level device object associated with the specified device. |
| **IoGetBaseFileSystemDeviceObject** | Reserved for system use. |
| **IoGetDeviceAttachmentBaseRef** | Returns a pointer to the lowest-level device object in a file system or device driver stack. |
| **IoGetDeviceToVerify** | Returns a pointer to the device object, representing a removable-media device, that is the target of the given thread's I/O request. |
| **IoGetDiskDeviceObject** | Retrieves a pointer to the disk device object associated with a given file system volume device object. |
| **IoGetLowerDeviceObject** | Returns a pointer to the next-lower-level device object on the driver stack. |
| **IoGetOplockKeyContext** | Returns a target oplock key context for a file object. |
| **IoGetOplockKeyContextEx** | Returns a parent and target oplock key context for a file object. |
| **IoGetRequestorProcess** | Returns a process pointer for the thread that originally requested a given I/O operation. |
| **IoGetRequestorProcessId** | Returns the unique 32-bit process ID for the thread that originally requested a given I/O operation. |
| **IoGetRequestorSessionId** | Returns the session ID for the process that originally requested a given I/O operation. |
| **IoGetTopLevelIrp** | Returns the value of the TopLevelIrp field of the current thread. |
| **IoGetTransactionParameterBloc** | Returns the transaction parameter block for a transacted file operation. |
| **IoInitializeDriverCreateContext** | Initializes a caller-allocated variable of type IO_DRIVER_CREATE_CONTEXT. |
| **IoInitializePriorityInfo** | Initializes a structure of type IO_PRIORITY_INFO. |
| **IoIsFileObjectIgnoringSharing** | Determines if a file object is set with the option to ignore file sharing access checks. |
| **IoIsFileOpenedExclusively** | Reserved for system use. |
| **IoIsFileOriginRemote** | Determines whether a given file object is for a remote create request. |
| **IoIsOperationSynchronous** | Determines whether a given IRP represents a synchronous or asynchronous I/O request. |
| **IoIsSystemThread** | Checks whether a given thread is a system thread. |
| **IoIsValidNameGraftingBuffer** | Reserved for system use. |
| **IoPageRead** | Reserved for system use. |
| **IoQueueThreadIrp** | Reserved for system use. |
| **IoQueryFileDosDeviceName** | Retrieves an MS-DOS device name for a file. |
| **IoQueryFileInformation** | Reserved for system use. |
| **IoQueryVolumeInformation** | Reserved for system use. |
| **IoRegisterFileSystem** | Adds a file system's control device object to the global file system queue. |
| **IoRegisterFsRegistrationChange** | Registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| **IoRegisterFsRegistrationChangeEx** | Registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system. |
| **IoRegisterFsRegistrationChangeMountAware** | Registers a file system filter driver's notification routine. This notification routine is called whenever a file system registers or unregisters itself as an active file system. |
| **IoReleaseVpbSpinLock** | Releases the Volume Parameter Block (VPB) spin lock. |
| **IoReplaceFileObjectName** | Replaces the name of a file object. |
| **IoSetDeviceToVerify** | Specifies a device object to be verified. The specified device object represents a removable media device. |
| **IoSetFileObjectIgnoreSharing** | Sets a file object to ignore file sharing access checks. |
| **IoSetFileOrigin** | Specifies whether a given file object is for a remote create request. |
| **IoSetInformation** | Reserved for system use. |
| **IoSetTopLevelIrp** | Sets the value of the *TopLevelIrp* field of the current thread. |
| **IoSynchronousPageWrite** | Reserved for system use. |
| **IoThreadToProcess** | Returns a pointer to the process for the specified thread. |
| **IoUnregisterFileSystem** | Removes a file system's control device object from the global file system queue. |
| **IoUnregisterFsRegistrationChange** | Unregisters file system filter driver's file system registration change notification routine. |
| **IoVerifyVolume** | Sends a volume verify request to the given removable-media device. |
| **IsReparseTagMicrosoft** | Determines whether a reparse point tag indicates a Microsoft reparse point. |
| **IsReparseTagNameSurrogate** | Determines whether a tag's associated reparse point is a surrogate for another named entity, such as a volume mount point. |
| **IsReparseTagValid** | Reserved for system use. |
