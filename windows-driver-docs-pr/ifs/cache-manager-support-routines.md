---
title: Cache Manager Support Routines
description: Cache Manager Support Routines
ms.assetid: 9ff905d9-8f85-4841-8bf5-437ccc3b3921
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Cache Manager Support Routines

The following system-supplied Cache Manager functions and macros can be called by kernel-mode file systems and file system filter drivers. They are listed in alphabetic order.

**Header File:** *ntifs.h*

**Prefix: Cc*Xxx***

| Function or Macro | Description |
| ----------------- | ----------- |
| **CcCanIWrite** | Determines whether the caller can write to a cached file. |
| **CcCoherencyFlushAndPurgeCache** | Flushes and/or purges the cache to ensure cache coherency. |
| **CcCopyRead** | Copies data from a cached file to a user buffer. |
| **CcCopyReadEx** | Copies data from a cached file to a user buffer. The operation's I/O byte count is charged to the issuing thread. |
| **CcCopyWrite** | Copies data from a user buffer to a cached file. |
| **CcCopyWriteEx** | Copies data from a user buffer to a cached file. The operation's I/O byte count is charged to the issuing thread. |
| **CcCopyWriteWontFlush** | Determines whether the amount of data to be copied in a call to **CcCopyWrite** is small enough to not require immediate flushing to disk if **CcCopyWrite** is called with *Wait* set to **FALSE**. |
| **CcDeferWrite** | Defers writing to a cached file. |
| **CcFastCopyRead** | Performs a fast copy read from a cached file to a buffer in memory. |
| **CcFastCopyWrite** | Performs a fast copy write from a buffer in memory to a cached file. |
| **CcFlushCache** | Flushes all or a portion of a cached file to disk.
| **CcGetDirtyPages** | Searches for dirty pages in all files that match a given log handle. |
| **CcGetFileObjectFromBcb** | Given a pointer to a pinned buffer control block (BCB) for a file, returns a pointer to the file object that the cache manager is using for that file. |
| **CcGetFileObjectFromSectionPtrs** | Given a pointer to the section object pointers for a cached file, returns a pointer to the file object that the cache manager is using for the file. |
| **CcGetFileObjectFromSectionPtrsRef** | When passed a pointer to a SECTION_OBJECT_POINTERS structure for a cached file, returns a pointer to the file object that the cache manager is using for the cached file. |
| **CcGetFileSizePointer** | Returns the size of a file, given a pointer to a file object for the file. |
| **CcGetFlushedValidData** | Determines how much of a cached file has been flushed to disk. |
| **CcInitializeCacheMap** | File systems call this routine to cache a file. |
| **CcIsFileCached** | Determines whether a file is cached or not. |
| **CcIsThereDirtyData** | Determines whether a mounted volume contains any files that have dirty data in the system cache. |
| **CcIsThereDirtyDataEx** | Determines whether a mounted volume contains any files that have dirty data in the system cache, including temporary files. |
| **CcMapData** | Maps a specified byte range of a cached file to a buffer in memory. |
| **CcPinMappedData** | Pins the specified byte range of a cached file. |
| **CcPinRead** | Pins the specified byte range of a cached file and reads the pinned data into a buffer in memory. |
| **CcPreparePinWrite** | Pins the specified byte range of a cached file for write access. |
| **CcPurgeCacheSection** | Purges all or a portion of a cached file from the system cache. |
| **CcReadAhead** | Performs read-ahead (also called "lazy read") on a cached file. |
| **CcRemapBcb** | Maps a buffer control block (BCB) an additional time to preserve it through several calls that perform additional maps and unpins. |
| **CcRepinBcb** | Pins a BCB an additional time to prevent it from being freed by a subsequent call to **CcUnpinData**. |
| **CcScheduleReadAhead** | Performs read-ahead (also called "lazy read") on a cached file. **CcScheduleReadAhead** should never be called directly; call **CcReadAhead** instead. |
| **CcScheduleReadAheadEx** | Performs read-ahead (also called "lazy read") on a cached file. The I/O byte count for the operation is charged to the issuing thread. |
| **CcSetAdditionalCacheAttributes** | Enables or disables read-ahead (also called "lazy read") or write-behind (also called "lazy write") on a cached file. |
| **CcSetAdditionalCacheAttributesEx** | Enables extended cache behavior on a cached file. |
| **CcSetBcbOwnerPointer** | Sets the owner thread pointer for a pinned buffer control block (BCB). |
| **CcSetDirtyPageThreshold** | Sets a per-file dirty page threshold on a cached file. |
| **CcSetDirtyPinnedData** | Marks as dirty the buffer control block (BCB) for a pinned buffer whose contents have been modified. |
| **CcSetFileSizes** | Updates the cache maps and section object for a cached file whose size has changed. |
| **CcSetLogHandleForFile** | Sets a log handle for a file. |
| **CcSetReadAheadGranularity** | Sets the read-ahead granularity for a cached file. |
| **CcUninitializeCacheMap** | Stops the caching of a cached file. |
| **CcUnpinData** | Releases cached file data that was mapped or pinned by an earlier call to **CcMapData**, **CcPinRead**, or **CcPreparePinWrite**. |
| **CcUnpinDataForThread** | Releases pages of a cached file whose buffer control block (BCB) was modified by an earlier call to **CcSetBcbOwnerPointer**. | **CcUnpinRepinnedBcb** | Unpins a repinned buffer control block (BCB). |
| **CcWaitForCurrentLazyWriterActivity** | Puts the caller into a wait state until the current batch of lazy writer activity is completed. |
| **CcZeroData** | Zeros the specified range of bytes in a cached or noncached file. |

The following **Cc*Xxx*** routines provide a memory descriptor list (MDL) interface for transfers to and from the cache. These routines are primarily intended for file servers. Everyone else should use FSRTL and FASTIO interfaces.

| Function | Description |
| -------- | ----------- |
| **CcPrepareMdlWrite** | Provides direct access to cached file memory so that the caller can write data to the file. |
| **CcMdlRead** | Provides direct access to cached file memory so that the caller can read data from the file. |
| **CcMdlReadComplete** | Frees the MDL created by **CcMdlRead** for a cached file. |
| **CcMdlWriteAbort** | Frees the MDL created by an earlier call to **CcPrepareMdlWrite.** |
| **CcMdlWriteComplete** | Frees the MDL created by **CcPrepareMdlWrite** for a cached file. |
| **CcMdlRead** | Provides direct access to cached file memory so that the caller can read data from the file. |
