---
title: Minifilter Driver Support Routines
description: Minifilter Driver Support Routines
ms.assetid: ef3db0c7-7892-44dc-90ab-a1046e7d4af8
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# FltXxx Minifilter Support Routines

The following system-supplied **Flt**_Xxx_ support functions and macros can be called by kernel-mode minifilter drivers, but not be other device drivers. They are listed in alphabetic order.

**Header File:** *fltkernel.h*

**Prefix: Flt**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **FLT_IS_FASTIO_OPERATION** | Determines whether the given callback data structure represents a fast I/O operation. |
| **FLT_IS_FS_FILTER_OPERATION** | Determines whether the given callback data structure represents a legacy file system filter (FSFilter) callback operation. |
 | **FLT_IS_IRP_OPERATION** | Determines whether the given callback data structure represents an I/O request packet (IRP)-based I/O operation. |
 | **FLT_IS_REISSUED_IO** | Determines whether the given callback data structure represents a reissued I/O operation. |
 | **FLT_IS_SYSTEM_BUFFER** | Tests the system buffer flag in a callback data structure. |
 | **FltAcknowledgeEcp** | Marks an extra create parameter context structure (ECP) as acknowledged. |
 | **FltAcquirePushLockExclusive** | Acquires the given push lock for exclusive access by the calling thread. |
 | **FltAcquirePushLockShared** | Acquires the given push lock for shared access by the calling thread. |
 | **FltAcquireResourceExclusive** | Acquires the given resource for exclusive access by the calling thread. |
 | **FltAcquireResourceShared** | Acquires the given resource for shared access by the calling thread. |
 | **FltAdjustDeviceStackSizeForIoRedirection** | Increases the size of the source device stack to allow a minifilter to redirect I/O from a specified source instance to a specified target instance when the target stack is deeper than the source stack. |
 | **FltAllocateCallbackData** | Allocates a callback data structure that a minifilter driver can use to initiate an I/O request. |
 | **FltAllocateCallbackDataEx** | Allocates a callback data structure and can preallocate memory for additional structures that a minifilter driver can use to initiate an I/O request. |
 | **FltAllocateContext** | Allocates a context structure for a specified context type. |
 | **FltAllocateDeferredIoWorkItem** | Allocates a deferred-I/O work item. |
| **FltAllocateExtraCreateParameter** | Allocates paged memory pool for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure. |
 | **FltAllocateExtraCreateParameterFromLookasideList** | Allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure and generates a pointer to that structure. |
 | **FltAllocateExtraCreateParameterList** | Allocates paged pool memory for an extra create parameter (ECP) list structure and generates a pointer to that structure. |
 | **FltAllocateFileLock** | Allocates and initializes a new FILE_LOCK structure. |
 | **FltAllocateGenericWorkItem** | Allocates a generic work item. |
 | **FltAllocatePoolAlignedWithTag** | Allocates a device-aligned buffer for use in a noncached I/O operation. |
 | **FltApplyPriorityInfoThread** | Used by a minifilter driver to apply priority information to a thread. |
 | **FltAttachVolume** | Creates a new minifilter driver instance and attaches it to the given volume. |
 | **FltAttachVolumeAtAltitude** | A debugging support routine that attaches a minifilter driver instance to a volume at a specified altitude, overriding any settings in the minifilter driver's INF file. |
 | **FltBuildDefaultSecurityDescriptor** | Builds a default security descriptor for use with **FltCreateCommunicationPort.** |
 | **FltCancelFileOpen** | Causes a newly opened or created file to be closed. |
 | **FltCancelIo** | Cancels an I/O operation. |
 | **FltCancellableWaitForMultipleObjects** | Executes a cancelable wait operation (a wait that can be terminated) on one or more dispatcher objects. |
**FltCancellableWaitForSingleObject** | Executes a cancelable wait operation (a wait that can be terminated) on a dispatcher object. |
| **FltCbdqDisable** | Disables a minifilter driver's callback data queue. |
| **FltCbdqEnable** | Enables a callback data queue that was disabled by a previous call to **FltCbdqDisable**. |
| **FltCbdqInitialize** | Initializes a minifilter driver's callback data queue dispatch table. |
| **FltCbdqInsertIo** | Inserts the callback data structure for an I/O operation into a minifilter driver's callback data queue. |
| **FltCbdqRemoveIo** | Removes a particular item from a minifilter driver's callback data queue. |
| **FltCbdqRemoveNextIo** | Removes the next matching item in a minifilter driver's callback data queue. |
| **FltCheckAndGrowNameControl** | Checks whether the buffer in a FLT_NAME_CONTROL structure is large enough to hold the specified number of bytes. If not, **FltCheckAndGrowNameControl** replaces it with a larger system-allocated buffer. |
| **FltCheckLockForReadAccess** | Determines whether the caller has read access to a locked byte range of a file. |
| **FltCheckLockForWriteAccess** | Determines whether the caller has write access to a locked byte range of a file. |
| **FltCheckOplock** | Synchronizes the callback data structure for an IRP-based file I/O operation with the file's current opportunistic lock (oplock) state. |
| **FltCheckOplockEx** | Synchronizes the callback data structure for an IRP-based file I/O operation that has the current opportunistic lock (oplock) state of the file. |
| **FltClearCallbackDataDirty** | Clears the callback dirty flag in a callback data structure. |
| **FltClearCancelCompletion** | Clears a cancel routine that was specified for an I/O operation. |
| **FltClose** | Closes a file handle that was opened by **FltCreateFile** **FltCreateFileEx**, or **FltCreateFileEx2**. |
| **FltCloseClientPort** | Coses a communication client port. |
| **FltCloseCommunicationPort** | Closes a minifilter driver's communication server port. |
| **FltCloseSectionForDataScan** | Closes a section object associated with a file stream. |
| **FltCommitComplete** | Acknowledges a TRANSACTION_NOTIFY_COMMIT notification. |
| **FltCommitFinalizeComplete** | Acknowledges a TRANSACTION_NOTIFY_COMMIT_FINALIZE notification. |
| **FltCompareInstanceAltitudes** | Compares the altitudes of two minifilter driver instances. |
| **FltCompletePendedPostOperation** | Resumes completion processing for an I/O operation that was pended in a minifilter driver's postoperation callback routine. |
| **FltCompletePendedPreOperation** | Resumes processing for an I/O operation that was pended in a minifilter driver's preoperation callback (PFLT_PRE_OPERATION_CALLBACK) routine. |
| **FltCreateCommunicationPort** | Creates a communication server port on which a minifilter driver can receive connection requests from user-mode applications. |
| **FltCreateFile** | Creates a new file or opens an existing file. |
| **FltCreateFileEx** | Creates a new file or opens an existing file. |
| **FltCreateFileEx2** | Creates a new file or opens an existing file. This routine also includes an optional create context parameter. |
| **FltCreateMailslotFile** | Creates a new mailslot server or opens an existing mailslot. |
| **FltCreateNamedPipeFile** | Creates a new pipe or opens an existing pipe. |
| **FltCreateSectionForDataScan** | Creates a section object for a file. The filter manager can optionally synchronize I/O with the section created. |
| **FltCreateSystemVolumeInformationFolder** | Verifies the existence of the "System Volume Information" folder on a file system volume. If the folder is not present, then the folder is created. |
| **FltCurrentBatchOplock** | Determines whether there are any batch or filter opportunistic locks (oplocks) on a file. |
| **FltCurrentOplock** | Determines whether there are any opportunistic locks (oplocks) on a file. |
| **FltCurrentOplockH** | Determines whether there are any CACHE_HANDLE_LEVEL opportunistic locks (oplocks) on a file. |
| **FltDecodeParameters** | Returns pointers to the memory descriptor list (MDL) address, buffer pointer, buffer length, and desired access parameters for an I/O operation. This saves minifilter drivers from having a switch statement to find the position of these parameters in helper routines that access the MDL address, buffer pointer, buffer length, and desired access for multiple operation types. |
| **FltDeleteContext** | Marks a specified context for deletion. |
| **FltDeleteExtraCreateParameterLookasideList** | Frees an extra create parameter (ECP) lookaside list. |
| **FltDeleteFileContext** | Retrieves and deletes a file context that a given minifilter driver has set for a given file. |
| **FltDeleteInstanceContext** | Removes a context from a given instance and marks the context for deletion. |
| **FltDeletePushLock** | Deletes a given push lock. |
| **FltDeleteStreamContext** | Removes a context that a given minifilter driver instance has set for a given stream and marks the context for deletion. |
| **FltDeleteStreamHandleContext** | Removes a context that a given minifilter driver instance has set for a given stream handle and marks the context for deletion. |
| **FltDeleteTransactionContext** | Removes a context from a given transaction and marks the context for deletion. |
| **FltDeleteVolumeContext** | Removes a context that a given minifilter driver has set for a given volume and marks the context for deletion. |
| **FltDetachVolume** | Detaches a minifilter driver instance from a volume. |
| **FltDeviceIoControlFile** | Sends a control code directly to a specified device driver, causing the corresponding driver to perform the specified action. |
| **FltDoCompletionProcessingWhenSafe** | If it is safe to do so, executes a minifilter driver postoperation callback routine. |
| **FltEnlistInTransaction** | Enlists a minifilter driver in a given transaction. |
| **FltEnumerateFilterInformation** | Provides information about all the registered filter drivers (including minifilter and legacy filter drivers) in the system. |
| **FltEnumerateFilters** | Enumerates all registered minifilter drivers in the system. |
| **FltEnumerateInstanceInformationByDeviceObject** | Provides information about minifilter driver instances and legacy filter drivers that are attached to the volume related to a specified device object. |
| **FltEnumerateInstanceInformationByFilter** | Provides information about instances of a given minifilter driver. |
| **FltEnumerateInstanceInformationByVolume** | Provides information about minifilter driver instances and legacy filter drivers (Windows Vista only) that are attached to a given volume. |
| **FltEnumerateInstanceInformationByVolumeName** | Provides information about minifilter driver instances and legacy filter drivers that are attached to the volume with the specified name. |
| **FltEnumerateInstances** | Enumerates minifilter driver instances for a given minifilter driver or volume. |
| **FltEnumerateVolumeInformation** | Provides information about volumes that are known to the filter manager. |
| **FltEnumerateVolumes** | Enumerates all volumes in the system. |
| **FltFastIoMdlRead** | Returns a memory descriptor list (MDL) that points directly to the specified byte range in the file cache. |
| **FltFastIoMdlReadComplete** | Completes the read operation that the **FltFastIoMdlRead** routine initiated. |
| **FltFastIoMdlWriteComplete** | Frees the resources that **FltFastIoPrepareMdlWrite** allocated. |
| **FltFastIoPrepareMdlWrite** | Returns a linked list of memory descriptor lists (MDLs) that point to the specified range of cached file data to write data directly to the cache. |
| **FltFlushBuffers** | Send a flush request for a given file to the file system. |
| **FltFindExtraCreateParameter** | Searches a given ECP list for an ECP context structure of a given type and returns a pointer to this structure if it is found. |
| **FltFreeCallbackData** | Frees a callback data structure allocated by the **FltAllocateCallbackData** routine. |
| **FltFreeDeferredIoWorkItem** | Frees a work item allocated by the **FltAllocateDeferredIoWorkItem** routine. |
| **FltFreeExtraCreateParameter** | Frees the memory for an ECP context structure. |
| **FltFreeExtraCreateParameterList** | Frees an extra create parameter (ECP) list structure. |
| **FltFreeFileLock** | Uninitializes and frees an initialized FILE_LOCK structure. |
| **FltFreeGenericWorkItem** | Frees a work item allocated by the **FltAllocateGenericWorkItem** routine. |
| **FltFreePoolAlignedWithTag** | Frees a cache-aligned buffer that was allocated by a previous call to **FltAllocatePoolAlignedWithTag**. |
| **FltFreeSecurityDescriptor** | Frees a security descriptor allocated by the **FltBuildDefaultSecurityDescriptor** routine. |
| **FltFsControlFile** | Sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action. |
| **FltGetActivityIdCallbackData** | Retrieves the current activity ID associated with a request in a minifilter's callback data. |
| **FltGetBottomInstance** | Returns an opaque instance pointer for the minifilter driver instance, if there is one, that is attached at the bottom of the instance stack for a given volume. |
| **FltGetContexts** | Retrieves a minifilter driver's contexts for the objects related to the current operation. |
| **FltGetContextsEx** | Retrieves a minifilter driver's contexts for the objects related to the current operation. |
| **FltGetDestinationFileNameInformation** | Constructs a full destination path name for a file or directory that is being renamed or for which an NTFS hard link is being created. |
| **FltGetDeviceObject** | Returns a pointer to the Filter Manager's volume device object (VDO) for a given volume. |
| **FltGetDiskDeviceObject** | Returns a pointer to the disk device object associated with a given volume. |
| **FltGetEcpListFromCallbackData** | Returns a pointer to an extra create parameter context structure (ECP) list that is associated with a given create operation callback-data object. |
| **FltGetFileContext** | Retrieves a context that was set for a file by a given minifilter driver instance. |
| **FltGetFileNameFormat** | Returns the name format portion of an **FLT_FILE_NAME_OPTIONS value. |
| **FltGetFileNameInformation** | Returns name information for a file or directory. |
| **FltGetFileNameInformationUnsafe** | Returns name information for an open file or directory. |
| **FltGetFileNameQueryMethod** | Returns the name query method portion of an FLT_FILE_NAME_OPTIONS value. |
| **FltGetFileSystemType** | Takes a volume or instance object and provides the file system type of the volume. |
| **FltGetFilterFromInstance** | Returns an opaque filter pointer for the minifilter driver that created the given instance. |
| **FltGetFilterFromName** | Returns an opaque filter pointer for a registered minifilter driver whose name matches the value in the *FilterName* parameter. |
| **FltGetFilterInformation** | Provides information about a minifilter driver. |
| **FltGetInstanceContext** | Retrieves a context that was set for an instance by a given minifilter driver. |
| **FltGetInstanceInformation** | Returns information about a minifilter driver instance. |
| **FltGetIoPriorityHint** | Gets IO priority information from callback data. |
| **FltGetIoPriorityHintFromCallbackData** | Gets IO priority information from callback data. |
| **FltGetIoPriorityHintFromFileObject** | Gets IO priority information from a file object. |
| **FltGetIoPriorityHintFromThread** | Gets IO priority information from a thread. |
| **FltGetIrpName** | Returns the name for a major function code as a printable string. |
| **FltGetLowerInstance** | Returns an opaque instance pointer for the next lower minifilter driver instance, if there is one, that is attached below a given minifilter driver instance on the same volume. |
| **FltGetNewSystemBufferAddress** | Retrieves the *AssociatedIrp.SystemBuffer* buffer, which the file system has allocated. A minifilter driver's post-callback routine calls this function. |
| **FltGetNextExtraCreateParameter** | Returns a pointer to the next (or first) extra create parameter context structure (ECP) in a given ECP list. |
| **FltGetRequestorProcess** | Returns a process pointer for the thread that requested a given I/O operation. |
| **FltGetRequestorProcessId** | Returns the unique 32-bit process ID for the process associated with the thread that requested a given I/O operation. |
| **FltGetRequestorProcessIdEx** | Returns the kernel-mode handle for the process that is associated with the thread that requested a given I/O operation. |
| **FltGetRequestorSessionId** | Returns the session ID of the process that originally requested the specified I/O operation. |
| **FltGetRoutineAddress** | Returns a pointer to a routine specified by the **FltMgrRoutineName** parameter. |
| **FltGetSectionContext** | Retrieves a section context that was created for a file stream by a specified minifilter driver instance. |
| **FltGetStreamContext** | Retrieves a context that was set for a file stream by a given minifilter driver instance. |
| **FltGetStreamHandleContext** | Retrieves a context that was set for a stream handle by a given minifilter driver instance. |
| **FltGetSwappedBufferMdlAddress** | Returns the memory descriptor list (MDL) address for a buffer that was swapped in by a minifilter driver. |
| **FltGetTopInstance** | Returns an opaque instance pointer for the minifilter driver instance that is attached at the top of the instance stack for a given volume. |
| **FltGetTransactionContext** | Retrieves a context that was set for a transaction by a given minifilter driver. |
| **FltGetTunneledName** | Retrieves the tunneled name for a file, given the normalized name returned for the file by a previous call to **FltGetFileNameInformation**, **FltGetFileNameInformationUnsafe**, or **FltGetDestinationFileNameInformation**. |
| **FltGetUpperInstance** | Returns an opaque instance pointer for the next higher minifilter driver instance, if there is one, that is attached above a given minifilter driver instance on the same volume. |
| **FltGetVolumeContext** | Retrieves a context that was set for a volume by a given minifilter driver. |
| **FltGetVolumeFromDeviceObject** | Returns an opaque pointer for the volume represented by a volume device object (VDO). |
| **FltGetVolumeFromFileObject** | Returns an opaque pointer for the volume that a given file stream resides on. |
| **FltGetVolumeFromInstance** | Returns an opaque pointer for the volume that a given minifilter driver instance is attached to.|
| **FltGetVolumeFromName** | Returns an opaque pointer for the volume whose name matches the value of the *VolumeName* parameter. |
| **FltGetVolumeGuidName** | Returns the volume name for a given volume, in volume globally unique identifier (GUID) format. |
| **FltGetVolumeInformation** | Provides information about a given volume. |
| **FltGetVolumeInstanceFromName** | Returns an opaque instance pointer for the given minifilter driver instance on the given volume. |
| **FltGetVolumeName** | Gets the volume name for a given volume. |
| **FltGetVolumeProperties** | Returns volume property information for the given volume. |
| **FltInitExtraCreateParameterLookasideList** | Initializes a paged or non-paged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size. |
| **FltInitializeFileLock** | Initializes an opaque FILE_LOCK structure that the caller has allocated from paged pool. |
| **FltInitializeOplock** | Initializes an opportunistic lock (oplock) pointer. |
| **FltInitializePushLock** | Initializes a push lock variable. |
| **FltInsertExtraCreateParameter** | Inserts an extra create parameter (ECP) context structure into an ECP list. |
| **FltIs32bitProcess** |Checks whether the originator of the current I/O operation is a 32-bit user-mode application. |
| **FltIsCallbackDataDirty** | Tests the FLTFL_CALLBACK_DATA_DIRTY flag in a callback data structure. |
| **FltIsDirectory** | Determines whether a given file object represents a directory. |
| **FltIsEcpAcknowledged** | Determines if a given extra create parameter context structure (ECP) has been marked as acknowledged. |
| **FltIsEcpFromUserMode** | Determines if an extra create parameter context structure (ECP) originated from user mode. |
| **FltIsFltMgrVolumeDeviceObject** | Determines whether the given device object belongs to filter manager and if the device object is a volume device object. |
| **FltIsIoCanceled** | Checks if an IRP-based operation has been canceled. |
| **FltIsIoRedirectionAllowed** | Determines whether I/O can be redirected from the specified source filter instance to another specified filter instance. |
| **FltIsIoRedirectionAllowedForOperation** | Determines whether I/O can be redirected from the filter instance associated with the specified FLT_CALLBACK_DATA structure to the specified filter instance. |
| **FltIsOperationSynchronous** | Determines whether a given callback data structure (FLT_CALLBACK_DATA) represents a synchronous or asynchronous I/O operation. |
| **FltIsVolumeSnapshot** | Determines whether a volume or minifilter driver instance is attached to a snapshot volume. |
| **FltIsVolumeWritable** | Determines whether the disk device that corresponds to a volume or minifilter driver instance is writable. |
| **FltLoadFilter** | Dynamically loads a minifilter driver into the currently running system. |
| **FltLockUserBuffer** | Locks the user buffer for a given I/O operation. |
| **FltNotifyFilterChangeDirectory** | Creates a notify structure for an IRP_MN_NOTIFY_CHANGE_DIRECTORY operation and adds it to the specified notify list. |
| **FltObjectDereference** | Removes a rundown reference from an opaque filter, instance, or volume pointer. |
| **FltObjectReference** | Adds a rundown reference to an opaque filter, instance, or volume pointer. |
| **FltOpenVolume** | Returns a handle and a file object pointer for the file system volume that a given minifilter driver instance is attached to. |
| **FltOplockBreakH** | Breaks CACHE_HANDLE_LEVEL opportunistic locks (oplocks). |
| **FltOplockBreakToNone** | Breaks all opportunistic locks (oplocks) immediately without regard for any oplock key. |
| **FltOplockBreakToNoneEx** | Breaks all opportunistic locks (oplocks) immediately without regard for any oplock key. |
| **FltOplockFsctrl** | Performs various opportunistic lock (oplock) operations on behalf of a minifilter driver. |
| **FltOplockFsctrlEx** | Performs various opportunistic lock (oplock) operations on behalf of a minifilter driver. |
| **FltOplockIsFastIoPossible** | Checks a file's opportunistic lock (oplock) state to determine whether fast I/O can be performed on the file. |
| **FltOplockIsSharedRequest** | Determines if a request for an opportunistic lock (oplock) wants a shared oplock. |
| **FltOplockKeysEqual** | Compares the opportunistic lock (oplock) keys that are stored in the file object extensions of two file objects. |
| **FltParseFileName** | Parses the extension, stream, and final component from a file name string. |
| **FltParseFileNameInformation** | Parses the contents of a FLT_FILE_NAME_INFORMATION structure. |
| **FltPerformAsynchronousIo** | Initiates an asynchronous I/O operation. |
| **FltPerformSynchronousIo** | Initiates a synchronous I/O operation after calling **FltAllocateCallbackData** to allocate a callback data structure for the operation. |
| **FltPrepareComplete** | Acknowledges a TRANSACTION_NOTIFY_PREPARE notification. |
| **FltPrepareToReuseEcp** | Resets an extra create parameter (ECP) context structure, which prepares it for reuse. |
| **FltPrePrepareComplete** | Acknowledges a TRANSACTION_NOTIFY_PREPREPARE notification. |
| **FltProcessFileLock** | Processes and completes a file lock operation. |
| **FltPropagateActivityIdToThread** | Associates the activity ID from the IRP in the minifilter's callback data with the current thread. |
| **FltPurgeFileNameInformationCache** | Purges from the Filter Manager's name cache all file name information structures that were generated from names provided by the given minifilter driver instance. |
| **FltQueryDirectoryFile** | Returns various kinds of information about files in the directory specified by a given file object. |
| **FltQueryEaFile** | Returns information about extended-attribute (EA) values for a file. |
| **FltQueryInformationFile** | Retrieves information for a given file. |
| **FltQueryQuotaInformationFile** | Retrieves quota entries associated with a file object. |
| **FltQuerySecurityObject** | Retrieves a copy of an object's security descriptor. |
| **FltQueryVolumeInformation** | Retrieves information about the volume that the given instance is attached to. |
| **FltQueryVolumeInformationFile** | Retrieves volume information for a given file, directory, storage device, or volume. |
| **FltQueueDeferredIoWorkItem** | Posts an IRP-based I/O operation to a work queue. |
| **FltQueueGenericWorkItem** | Posts a work item that is not associated with a specific I/O operation to a work queue. |
| **FltReadFile** | Reads data from an open file, stream, or device. |
| **FltReadFileEx** | Reads data from an open file, stream, or device. This function extends **FltReadFile** to allow the optional use of an MDL for read data instead of a mapped buffer address. |
| **FltReferenceContext** | Increments the reference count on a context structure. |
| **FltReferenceFileNameInformation** | Increments the reference count on a file name information structure. |
| **FltRegisterFilter** | Registers a minifilter driver. |
| **FltRegisterForDataScan** | Enables data scanning for the volume attached to the minifilter instance. |
| **FltReissueSynchronousIo** | Initiates a new synchronous I/O operation that uses the parameters from a previously synchronized I/O operation. |
| **FltReleaseContext** | Decrements the reference count on a context. |
| **FltReleaseContexts** | Releases each context in a given FLT_RELATED_CONTEXTS structure. |
| **FltReleaseContextsEx** | Releases each context in a given FLT_RELATED_CONTEXTS_EX structure. |
| **FltReleaseFileNameInformation** | Releases a file name information structure. |
| **FltReleasePushLock** | Releases a specified push lock owned by the current thread. |
| **FltReleaseResource** | Releases a specified resource owned by the current thread. |
| **FltRemoveExtraCreateParameter** | Searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list. |
| **FltRequestOperationStatusCallback** | Returns status information for the given I/O operation. |
| **FltRetainSwappedBufferMdlAddress** | Prevents the Filter Manager from freeing the memory descriptor list (MDL) for a buffer that was swapped in by a minifilter driver. |
| **FltRetrieveIoPriorityInfo** | Retrieves priority information from a thread. |
| **FltReuseCallbackData** | Reinitializes a callback data structure so that it can be reused. |
| **FltRollbackComplete** | Acknowledges a TRANSACTION_NOTIFY_ROLLBACK notification. |
| **FltRollbackEnlistment** | Rolls back or aborts a transaction on behalf of a minifilter driver. |
| **FltSendMessage** | Sends a message to a waiting user-mode application on behalf of a minifilter driver or a minifilter driver instance. |
| **FltSetActivityIdCallbackData** | Sets an activity ID for an IRP in a minifilter's callback data. |
| **FltSetCallbackDataDirty** | A minifilter driver's preoperation or postoperation callback routine calls **FltSetCallbackDataDirty** to indicate that it has modified the contents of the callback data structure. |
| **FltSetCancelCompletion** | Specifies a cancel routine to be called if a given I/O operation is canceled. |
| **FltSetEaFile** | Sets extended-attribute (EA) values for a file. |
| **FltSetEcpListIntoCallbackData** | Attaches an extra create parameter context structure (ECP) list to a create operation callback-data object. |
| **FltSetFileContext** | Sets a context for a file. |
| **FltSetInformationFile** | Sets information for a given file. |
| **FltSetInstanceContext** | Sets a context for a minifilter driver instance. |
| **FltSetIoPriorityHintIntoCallbackData** | Sets the I/O priority information in callback data. |
| **FltSetIoPriorityHintIntoFileObject** | Sets the I/O priority information in a file object. |
| **FltSetIoPriorityHintIntoThread** | Sets the IO priority information in a thread. |
| **FltSetQuotaInformationFile** | Modifies quota entries for a file object. |
| **FltSetSecurityObject** | Sets an object's security state. |
| **FltSetStreamContext** | Sets a context for a file stream. |
| **FltSetStreamHandleContext** | Sets a context for a stream handle. |
| **FltSetTransactionContext** | Sets a context on a transaction. |
| **FltSetVolumeContext** | Sets a context for a volume. |
| **FltSetVolumeInformation** | Changes various kinds of information about the volume that the given instance is attached to. |
| **FltStartFiltering** | Starts filtering for a registered minifilter driver. |
| **FltSupportsFileContexts** | Determines whether the file system supports file contexts for a given file. |
| **FltSupportsFileContextsEx** | Determines whether the file system or the filter manager support file contexts for a given file. |
| **FltSupportsStreamContexts** | Determines whether stream contexts are supported on a given file object. |
| **FltSupportsStreamHandleContexts** | Determines whether stream handle contexts are supported on a given file object. |
| **FltTagFile** | Sets a reparse tag on a file or directory. |
| **FltUninitializeFileLock** | Uninitializes a FILE_LOCK structure. |
| **FltUninitializeOplock** | Uninitializes an opportunistic lock (oplock) pointer. |
| **FltUnloadFilter** | A minifilter driver that has loaded a supporting minifilter driver by calling **FltLoadFilter** can unload the minifilter driver by calling **FltUnloadFilter**. |
| **FltUnregisterFilter** | A registered minifilter driver calls **FltUnregisterFilter** to unregister itself so that the Filter Manager no longer calls it to process I/O operations. |
| **FltUntagFile** | Removes a reparse point from a file or directory. |
| **FltWriteFile** | Writes data to an open file, stream, or device. |
| **FltWriteFileEx** | Writes data to an open file, stream, or device. This function extends **FltWriteFile** to allow the optional use of an MDL for write data instead of a mapped buffer address. |
| **IS_ALIGNED** | Determines whether the first argument is aligned on the specified power-of-2 boundary.
