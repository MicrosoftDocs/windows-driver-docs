---
title: File System Runtime Library Support Routines
description: File System Runtime Library Support Routines
ms.assetid: e3c2e109-891a-494a-b62c-e6ccc7afc9d8
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# File System Runtime Library Support Routines

The following system-supplied File System Runtime Library support functions and macros can be called by kernel-mode file systems and file system filter drivers. They are listed in alphabetic order.

**Header File:** *ntifs.h*

**Prefix: FsRtl*Xxx***

| Function or Macro | Description |
| ----------------- | ----------- |
| **FsRtlAcknowledgeEcp** | Marks an extra create parameter (ECP) context structure as acknowledged. |
| **FsRtlAcquireFileExclusive** | Reserved for system use. |
| **FsRtlAddLargeMcbEntry** | Adds a new mapping to an existing map control block (MCB). |
| **FsRtlAddMcbEntry** | Obsolete. |
| **FsRtlAddToTunnelCache** | Caches a file name that is removed from a directory when a file is renamed or deleted. |
| **FsRtlAllocateExtraCreateParameter** | Allocates memory for a user-defined extra create parameter (ECP) context structure and generates a pointer to that structure. |
| **FsRtlAllocateExtraCreateParameterFromLookasideList** | Allocates memory pool from a given lookaside list for an extra create parameter (ECP) context structure, and generates a pointer to that structure. |
| **FsRtlAllocateExtraCreateParameterList** | Allocates paged pool memory for an ECP_LIST structure and generates a pointer to that structure. |
| **FsRtlAllocateFileLock** | Allocates and initializes a new FILE_LOCK structure. |
| **FsRtlAllocatePool** | Obsolete. |
| **FsRtlAllocatePoolWithQuota** | Obsolete. |
| **FsRtlAllocatePoolWithQuotaTag** | Allocates pool memory, charging quota against the current process. |
| **FsRtlAllocatePoolWithTag** | Allocates pool memory. |
| **FsRtlAllocateResource** | Obsolete. |
| **FsRtlAreNamesEqual** | Determines whether two Unicode strings are equal. |
| **FsRtlAreThereCurrentFileLocks** | Checks whether any byte range locks exist for the specified file. |
| **FsRtlAreThereCurrentOrInProgressFileLocks** | Determines if there are byte range locks assigned to a file or any lock operations in progress for that file.
| **FsRtlAreThereWaitingFileLocks** | Checks a file lock queue for any waiting file locks. |
| **FsRtlAreVolumeStartupApplicationsComplete** | Determines whether volume startup applications have completed processing. |
| **FsRtlBalanceReads** | Signals to a fault-tolerant disk driver that it is now safe to start balancing reads from a mirrored drive. |
| **FsRtlCancellableWaitForMultipleObjects** | Executes a cancelable wait operation (a wait that can be terminated) on one or more dispatcher objects. |
| **FsRtlCancellableWaitForSingleObject** | Executes a cancelable wait operation (a wait that can be terminated) on a dispatcher object. |
| **FsRtlChangeBackingFileObject** | Replaces the current file object with a new file object. |
| **FsRtlCheckLockForReadAccess** | Determines whether the process associated with a given IRP has read access to a locked region of a file. |
| **FsRtlCheckLockForWriteAccess** | Determines whether the process associated with a given IRP has write access to a locked region of a file. |
| **FsRtlCheckLockForOplockRequest** | Checks for locks within the allocation size of a file. The file lock object is checked for the presence of byte range locks that would prevent an oplock request from being granted. |
| **FsRtlCheckOplock** | Synchronizes the IRP for a file I/O operation with the file's current opportunistic lock (oplock) state. |
| **FsRtlCheckOplockEx** | Synchronizes the IRP for a file I/O operation with the current opportunistic lock (oplock) state of the file. |
| **FsRtlCheckUpperOplock** | Provides opportunistic lock (oplock) checking in secondary, or layered, file systems when the oplocks they hold change state. |
| **FsRtlCompleteRequest** | Completes an IRP with the specified status. |
| **FsRtlCopyRead** | Copies data from a cached file to a user buffer. |
| **FsRtlCopyWrite** | Copies data from a user buffer to a cached file. |
| **FsRtlCreateSectionForDataScan** | Creates a section object. Use this routine with extreme caution. |
| **FsRtlCurrentBatchOplock** | A file system or filter driver calls this routine to determine whether there are any batch or filter opportunistic locks (oplocks) on a file. |
| **FsRtlCurrentOplock** | A file system or filter driver calls this routine to determine whether there are any opportunistic locks (oplocks) on a file. |
| **FsRtlCurrentOplockH** | A file system or filter driver calls this routine to determine whether there are any CACHE_HANDLE_LEVEL opportunistic locks (oplocks) on a file. |
| **FsRtlDeleteExtraCreateParameterLookasideList** | Frees an extra create parameter (ECP) lookaside list. |
| **FsRtlDeleteKeyFromTunnelCache** | Deletes any tunnel cache entries for files in a directory that is being deleted. |
| **FsRtlDeleteTunnelCache** | Deletes a tunnel cache. |
| **FsRtlDeregisterUncProvider** | Deregisters a redirector that was registered as a Universal Naming Convention (UNC) provider with the multiple UNC provider (MUP). |
| **FsRtlDissectDbcs** | Given an ANSI or double-byte character set (DBCS) pathname string, this routine returns two strings: one containing the first file name found in the string, the other containing the remaining unparsed portion of the pathname string. |
| **FsRtlDissectName** | Given a Unicode pathname string, this routine returns two strings: one containing the first file name found in the string, the other containing the remaining unparsed portion of the pathname string. |
| **FsRtlDoesDbcsContainWildCards** | Determines whether an ANSI or double-byte character set (DBCS) string contains wildcard characters. |
| **FsRtlDoesNameContainWildCards** | Determines whether a Unicode string contains wildcard characters. |
| **FsRtlEnterFileSystem** | Temporarily disables the delivery of normal kernel-mode asynchronous procedure calls (APC). Special kernel-mode APCs are still delivered.
| **FsRtlExitFileSystem** | Re-enables the delivery of normal kernel-mode APCs that were disabled by a preceding call to **FsRtlEnterFileSystem**. |
| **FsRtlFastCheckLockForRead** | Determines whether the specified process has read access to a locked byte range of a file. |
| **FsRtlFastCheckLockForWrite** | Determines whether the specified process has write access to a locked byte range of a file. |
| **FsRtlFastLock** | Used by file systems and filter drivers to request a byte-range lock for a file stream. |
| **FsRtlFastUnlockAll** | Releases all byte-range locks that were acquired by the specified process for a file. |
| **FsRtlFastUnlockAllByKey** | Releases all byte-range locks that were acquired by the specified process, with the specified key value, for a file. |
| **FsRtlFastUnlockSingle** | Releases a byte-range lock that was acquired by the specified process, with the specified key value, file offset, and length, for a file. |
| **FsRtlFindExtraCreateParameter** | Searches a given ECP list for an ECP context structure of a given type and returns a pointer to this structure if it is found. |
| **FsRtlFindInTunnelCache** | Searches for a matching entry in the tunnel cache that matches the specified name. |
| **FsRtlFreeExtraCreateParameter** | Frees the memory for an ECP context structure. |
| **FsRtlFreeExtraCreateParameterList** | Frees an extra create parameter (ECP) list structure. |
| **FsRtlFreeFileLock** | Uninitializes and frees a file lock structure. |
| **FsRtlGetEcpListFromIrp** | Returns a pointer to an extra create parameter (ECP) context structure list that is associated with a given IRP_MJ_CREATE operation. |
| **FsRtlGetFileSize** | Used to get the size of a file. |
| **FsRtlGetNextExtraCreateParameter** | Returns a pointer to the next (or first) extra create parameter (ECP) context structure in a given ECP list. |
| **FsRtlGetNextFileLock** | Used to enumerate the byte-range locks that currently exist for a specified file. |
| **FsRtlGetNextLargeMcbEntry** | Retrieves a mapping run from a map control block (MCB). |
| **FsRtlGetNextMcbEntry** | Obsolete. |
| **FsRtlGetPerFileContextPointer** | Returns a *FileContextSupportPointer* for an open file. |
| **FsRtlGetPerStreamContextPointer** | Returns the file system's stream context for a file stream. |
| **FsRtlGetSectorSizeInformation** | Retrieves the physical and logical sector size information for a storage volume. |
| **FsRtlGetSupportedFeatures** | Returns the supported features of a volume attached to the specified device object. |
| **FsRtlIncrementCcFastMdlReadWait** | Increments the cache manager's CcFastMdlReadWait performance counter member in a processor control block (PRCB) object. |
| **FsRtlIncrementCcFastReadNotPossible** | Increments the **CcFastReadNotPossible** performance counter in a per processor control block of cache manager system counters. |
| **FsRtlIncrementCcFastReadNoWait** | Increments the **CcFastReadNoWait** performance counter in a per processor control block of cache manager system counters. |
| **FsRtlIncrementCcFastReadResourceMiss** | Increments the **CcFastReadNotPossible** performance counter in a per processor control block of cache manager system counters. |
| **FsRtlIncrementCcFastReadWait** | Increments the **CcFastReadWait** performance counter in a per processor control block of cache manager system counters. |
| **FsRtlInitExtraCreateParameterLookasideList** | Initializes a paged or nonpaged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size. |
| **FsRtlInitializeExtraCreateParameter** | Initializes an extra create parameter (ECP) context structure. |
| **FsRtlInitializeExtraCreateParameterList** | Initializes an extra create parameter (ECP) context structure list. |
| **FsRtlInitializeFileLock** | Initializes a FILE_LOCK structure. |
| **FsRtlInitializeLargeMcb** | Initializes a map control block (MCB) structure. |
| **FsRtlInitializeMcb** | Obsolete. |
| **FsRtlInitializeOplock** | Initializes an opportunistic lock (oplock) pointer. |
| **FsRtlInitializeTunnelCache** | Initializes a new tunnel cache for a volume. |
| **FsRtlInitPerFileContext** | Initializes a FSRTL_PER_FILE_CONTEXT structure. |
| **FsRtlInitPerFileObjectContext** | Initializes a FSRTL_PER_FILEOBJECT_CONTEXT structure. |
| **FsRtlInitPerStreamContext** | Initializes a filter driver context structure. |
| **FsRtlInsertExtraCreateParameter** | Inserts an extra create parameter (ECP) context structure into an ECP list. |
| **FsRtlInsertPerFileContext** | Associates a FSRTL_PER_FILE_CONTEXT object with a driver-specified context object for a file. |
| **FsRtlInsertPerFileObjectContext** | For a "legacy" file system filter driver, the | **FsRtlInsertPerFileObjectContext function associates context information with a file object. |
| **FsRtlInsertPerStreamContext** | Associates a file system filter driver's per-stream context structure with a file stream. |
| **FsRtlIsAnsiCharacterLegal** | Determines whether a character is a legal ANSI character. |
| **FsRtlIsAnsiCharacterLegalFat** | Determines whether an ANSI character is legal for FAT file names. |
| **FsRtlIsAnsiCharacterLegalHpfs** | Determines whether an ANSI character is legal for HPFS file names. |
| **FsRtlIsAnsiCharacterLegalNtfs** | Determines whether an ANSI character is legal for NTFS file names. |
| **FsRtlIsAnsiCharacterLegalNtfsStream** | Determines whether an ANSI character is legal for NTFS stream names. |
| **FsRtlIsAnsiCharacterWild** | Determines whether an ANSI character is a wildcard character. |
| **FsRtlIsDbcsInExpression** | Determines whether an ANSI or double-byte character set (DBCS) string matches the specified pattern. |
| **FsRtlIsEcpAcknowledged** | Determines if a given extra create parameter (ECP) context structure has been marked as acknowledged. |
| **FsRtlIsEcpFromUserMode** | Determines whether an extra create parameter (ECP) context structure originated from user mode. |
| **FsRtlIsFatDbcsLegal** | Determines whether the specified ANSI or double-byte character set (DBCS) string is a legal FAT file name. |
| **FsRtlIsHpfsDbcsLegal** | Determines whether the specified ANSI or double-byte character set (DBCS) string is a legal HPFS file name. |
| **FsRtlIsLeadDbcsCharacter** | Determines whether a character is a lead byte (the first byte of a character) in a double-byte character set (DBCS). |
| **FsRtlIsNameInExpression** | Determines whether a Unicode string matches the specified pattern. |
| **FsRtlIsNtstatusExpected** | Determines whether the specified exception is handled by the exception filter. |
| **FsRtlIsPagingFile** | Determines whether a given file is a paging file. |
| **FsRtlIssueDeviceIoControl** | Sends a synchronous device I/O control request to a target device object. |
| **FsRtlIsSystemPagingFile** | Determines whether a given file is currently a system paging file. |
| **FsRtlIsTotalDeviceFailure** | Determines whether a media or other hardware failure has occurred. |
| **FsRtlIsUnicodeCharacterWild** | Determines whether a Unicode character is a wildcard character. |
| **FsRtlLogCcFlushError** | Logs a lost delayed-write error and displays a dialog box to the user. |
| **FsRtlLookupLargeMcbEntry** | Given a virtual block number (VBN) and a map control block (MCB), this routine searches the MCB for mapping information corresponding to the specified VBN. |
| **FsRtlLookupLastLargeMcbEntry** | Retrieves the last mapping entry stored in the map control block (MCB). |
| **FsRtlLookupLastLargeMcbEntryAndIndex** | Retrieves the last mapping entry stored in a given map control block (MCB). |
| **FsRtlLookupLastMcbEntry** | Obsolete. |
| **FsRtlLookupMcbEntry** | Obsolete. |
| **FsRtlLookupPerFileContext** | Returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a specified file. |
| **FsRtlLookupPerFileObjectContext** | For a "legacy" file system filter driver, this function retrieves context information previously associated with a file object. |
| **FsRtlLookupPerStreamContext** | Retrieves a per-stream context structure for a file stream. |
| **FsRtlLookupPerStreamContextInternal** | Reserved for system use. |
| **FsRtlMdlReadCompleteDev** | Completes the read operation that the **FsRtlMdlReadDev** routine initiated. |
| **FsRtlMdlReadDev** | Returns a memory descriptor list (MDL) that points directly to the specified byte range in the file cache. |
| **FsRtlMdlReadEx** | Performs a fast cached MDL read. If the requested data is not cached, the routine reverts to an IRP based MDL read operation. |
| **FsRtlMdlWriteCompleteDev** | Frees the resources that **FsRtlPrepareMdlWriteDev** allocated. |
| **FsRtlMupGetProviderIdFromName** | Gets the provider identifier of a network redirector that is registered with the multiple UNC provider (MUP) from the device name of the network redirector. |
| **FsRtlMupGetProviderInfoFromFileObject** | Gets information about a network redirector that is registered with the multiple UNC provider (MUP) from a file object for a file that is located on a remote file system. |
| **FsRtlNormalizeNtstatus** | Translates an arbitrary exception into a status value that is handled by the exception filter. |
| **FsRtlNotifyCleanup** | When the last handle to a file object is released, this routine removes the file object's notify structure, if present, from the specified notify list. |
| **FsRtlNotifyCleanupAll** | Temoves all members of the specified notification list. |
| **FsRtlNotifyFilterChangeDirectory** | Creates a notify structure for an IRP_MN_NOTIFY_CHANGE_DIRECTORY request and adds it to the specified notify list. |
| **FsRtlNotifyFilterReportChange** | Completes IRP_MN_NOTIFY_CHANGE_DIRECTORY requests that are pending in the specified notify list. |
| **FsRtlNotifyFullChangeDirectory** | Creates a notify structure for a notification request and adds it to the specified notify list. |
| **FsRtlNotifyFullReportChange** | Completes pending notify change IRPs. |
| **FsRtlNotifyInitializeSync** | Allocates and initializes a synchronization object for a notify list. |
| **FsRtlNotifyUninitializeSync** | Deallocates the synchronization object for a notify list. |
| **FsRtlNotifyVolumeEvent** | Notifies any registered applications that a volume event is occurring. |
| **FsRtlNotifyVolumeEventEx** | Notifies any registered applications that a volume event is occurring. Volume events include the volume being locked, unlocked, mounted, or made read-only. |
| **FsRtlNumberOfRunsInLargeMcb** | Returns the number of runs in a map control block (MCB). |
| **FsRtlNumberOfRunsInMcb** | Obsolete. |
| **FsRtlOplockBreakH** | Breaks CACHE_HANDLE_LEVEL opportunistic locks (oplocks). |
| **FsRtlOplockBreakToNone** | Obsolete. |
| **FsRtlOplockBreakToNoneEx** | Breaks all opportunistic locks (oplocks) immediately without regard for any oplock key. |
| **FsRtlOplockFsctrl** | Performs various opportunistic lock (oplock) operations on behalf of a file system or filter driver. |
| **FsRtlOplockFsctrlEx** | Performs various opportunistic lock (oplock) operations on behalf of a file system or filter driver. |
| **FsRtlOplockIsFastIoPossible** | Checks a file's opportunistic lock (oplock) state to determine whether fast I/O can be performed on the file. |
| **FsRtlOplockIsSharedRequest** | Determines if a request for an opportunistic lock (oplock) wants a shared oplock. |
| **FsRtlOplockKeysEqual** | Compares the opportunistic lock (oplock) keys that are stored in the file object extensions of two file objects. |
| **FsRtlPostPagingFileStackOverflow** | Posts a paging file stack overflow item to the stack overflow thread. |
| **FsRtlPostStackOverflow** | Posts a stack overflow item to the stack overflow thread. |
| **FsRtlPrepareMdlWriteDev** | Returns a linked list of memory descriptor lists (MDLs) that point to the specified range of cached file data to write data directly to the cache. |
| **FsRtlPrepareMdlWriteEx** | Returns a linked list of memory descriptor lists (MDLs) that point to the specified range of cached file data to write data directly to the cache. If the cache support for the write is not available, the routine reverts to an IRP based MDL write operation. |
| **FsRtlPrepareToReuseEcp** | Resets an extra create parameter (ECP) context structure, which prepares it for reuse. |
| **FsRtlPrivateLock** | Obsolete. |
| **FsRtlProcessFileLock** | Processes and completes an IRP for a file lock operation. |
| **FsRtlQueryCachedVdl** | Retrieves the current valid data length (VDL) for a cached file. |
| **FsRtlRegisterFileSystemFilterCallbacks** | File system filter drivers and file systems call this routine to register notification callback routines to be invoked when the underlying file system performs certain operations. |
| **FsRtlRegisterUncProvider** | Registers a network redirector as a universal naming convention (UNC) provider with the system multiple UNC provider (MUP). |
| **FsRtlRegisterUncProviderEx** | Registers a network redirector as a universal naming convention (UNC) provider with the system multiple UNC provider (MUP). |
| **FsRtlReleaseFile** | Reserved for system use. |
| **FsRtlRemoveDotsFromPath** | Removes unnecessary occurrences of '.' and '..' from the specified path. |
| **FsRtlRemoveExtraCreateParameter** | Searches an ECP list for an ECP context structure and, if found, detaches it from the ECP list. |
| **FsRtlRemoveLargeMcbEntry** | Removes one or more mappings from a map control block (MCB). |
| **FsRtlRemoveMcbEntry** | Obsolete. |
| **FsRtlRemovePerFileContext** | Returns a pointer to a **FSRTL_PER_FILE_CONTEXT object** that is associated with a file. **FsRtlRemovePerFileContext** removes the **FSRTL_PER_FILE_CONTEXT** object from the list it occupies, along with the associated driver specific context information. |
| **FsRtlRemovePerFileObjectContext** | For a "legacy" file system filter driver, this function unlinks a per-file-object context information structure from the list of per-file-object contexts previously associated with a file object. |
| **FsRtlRemovePerStreamContext** | Removes a per-stream context structure from the list of per-stream contexts associated with a file stream. |
| **FsRtlResetLargeMcb** | Truncates a map control block (MCB) structure to contain zero mapping pairs. It does not shrink the mapping pairs array. |
| **FsRtlSetEcpListIntoIrp** | Attaches an extra create parameter (ECP) context structure list to an IRP_MJ_CREATE operation. |
| **FsRtlSetupAdvancedHeader** | Used by file systems to initialize an **FSRTL_ADVANCED_FCB_HEADER structure for use with filter contexts. |
| **FsRtlSetupAdvancedHeaderEx** | Used by file systems to initialize an | **FSRTL_ADVANCED_FCB_HEADER** structure for use with both stream and file contexts. |
| **FsRtlSplitLargeMcb** | Inserts a hole into the mappings in a map control block (MCB). |
| **FsRtlSupportsPerFileContexts** | Checks if per file context information is supported by the file system that is associated with a specified FILE_OBJECT. |
| **FsRtlSupportsPerStreamContexts** | Determines whether a file system supports per-stream contexts for a given file stream. |
| **FsRtlTeardownPerFileContexts** | File systems call this routine to free **FSRTL_PER_FILE_CONTEXT** objects that are associated with a file control block (FCB) structure. |
| **FsRtlTeardownPerStreamContexts** | Frees all per-stream context structures associated with a given | **FsRtl_ADVANCED_FCB_HEADER structure. |
| **FsRtlTestAnsiCharacter** | Determines whether an ANSI or double-byte character set (DBCS) character meets the specified criteria. |
| **FsRtlTruncateLargeMcb** | Truncates a large map control block (MCB). |
| **FsRtlTruncateMcb** | Obsolete. |
| **FsRtlUninitializeFileLock** | Uninitializes a FILE_LOCK structure. |
| **FsRtlUninitializeLargeMcb** | Uninitializes a large map-control block (MCB). |
| **FsRtlUninitializeMcb** | Obsolete. |
| **FsRtlUninitializeOplock** | Uninitializes an opportunistic lock (oplock) pointer. |
| **FsRtlUpperOplockFsctrl** Processes opportunistic lock (oplock) requests and acknowledgments for secondary, or layered, file systems. |
| **FsRtlValidateReparsePointBuffer**| Verifies that the specified reparse point buffer is valid. |
