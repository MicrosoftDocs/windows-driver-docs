---
title: Runtime Library Support Routines
description: Runtime Library Support Routines
ms.assetid: e333a222-32c0-46e7-a0b8-42287e19372d
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Runtime Library Support Routines

The following table lists the subset of system-supplied runtime library support routines that can be used by kernel-mode file systems and by minifilter and legacy filter drivers but not by device drivers.

In addition to the routines documented here, file systems and filter drivers can also call any of the **Rtl**_Xxx_ routines described in the Kernel-Mode Driver Architecture Reference section that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Rtl**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **RtlAbsoluteToSelfRelativeSD** | Creates a new security descriptor in self-relative format by using a security descriptor in absolute format as a template. |
| **RtlAddAccessAllowedAce** | Adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| **RtlAddAccessAllowedAceEx** | Adds an access-allowed access control entry (ACE) with inheritance ACE flags to an access control list (ACL). The access is granted to the specified security identifier (SID). |
| **RtlAddAce** | Adds one or more access control entries (ACEs) to a specified access control list (ACL). |
| **RtlAllocateAndInitializeSid** | Reserved for system use. |
| **RtlAllocateHeap** | Allocates a block of memory from a heap. |
| **RtlAppendStringToString** | Concatenates two counted strings. It copies bytes from the source up to the length of the destination buffer. |
| **RtlCaptureContext** | Retrieves a context record in the context of the caller. |
| **RtlCaptureStackBackTrace** | Captures a stack back trace by walking up the stack and recording the information for each frame. |
| **RtlCompareMemoryUlong** | Returns how many bytes in a block of memory match a specified pattern. |
| **RtlCompressBuffer** | Compresses a buffer and can be used by a file system driver to facilitate the implementation of file compression. |
| **RtlCompressChunks** | Reserved for system use. |
| **RtlConvertSidToUnicodeString** | Generates a printable Unicode string representation of a security identifier (SID). |
| **RtlCopyLuid** | Copies a locally unique identifier (LUID) to a buffer. |
| **RtlCopySid** | Copies the value of a security identifier (SID) to a buffer. |
| **RtlCreateAcl** | Creates and initializes an access control list (ACL). |
| **RtlCreateHeap** | Creates a heap object that can be used by the calling process. This routine reserves space in the virtual address space of the process and allocates physical storage for a specified initial portion of this block. |
| **RtlCreateSecurityDescriptorRelative** | Initializes a new security descriptor in self-relative format. On return, the security descriptor is initialized with no system ACL (SACL), no discretionary ACL (DACL), no owner, no primary group, and all control flags set to zero. |
| **RtlCreateSystemVolumeInformationFolder** | Verifies the existence of the "System Volume Information" folder on a file system volume. If the folder is not present, then the folder is created. |
| **RtlCreateUnicodeString** | Creates a new counted Unicode string. |
| **RtlCustomCPToUnicodeN** | Reserved for system use. |
| **RtlDecompressBuffer** | Decompresses an entire compressed buffer. |
| **RtlDecompressBufferEx** | Decompresses an entire compressed buffer. |
| **RtlDecompressBufferEx2** | Decompresses an entire compressed buffer, using multiple processors where possible. Multiple processor support is only implemented for kernel mode callers. |
| **RtlDecompressChunks** | Reserved for system use. |
| **RtlDecompressFragment** | Decompresses part of a compressed buffer (that is, a buffer "fragment"). |
| **RtlDecompressFragmentEx** | Decompresses part of a compressed buffer (that is, a buffer "fragment"), using multiple processors where possible. |
| **RtlDelete** | Deletes the specified node from the splay link tree. |
| **RtlDeleteAce** | Deletes an access control entry (ACE) from a specified access control list (ACL). |
| **RtlDeleteNoSplay** | Deletes the specified node from the splay link tree. |
| **RtlDeleteElementGenericTable** | Deletes an element from a generic table. |
| **RtlDeleteElementGenericTableAvl** | Deletes an element from a generic table. |
| **RtlDescribeChunk** | Reserved for system use. |
| **RtlDestroyHeap** | Destroys the specified heap object. | **RtlDestroyHeap decommits and releases all the pages of a private heap object, and it invalidates the handle to the heap. |
| **RtlDowncaseUnicodeString** | Converts the specified Unicode source string to lowercase. The translation conforms to the current system locale information. |
| **RtlEnumerateGenericTable** | Enumerates the elements in a generic table. |
| **RtlEnumerateGenericTableAvl** | Enumerates the elements in a generic table. |
| **RtlEnumerateGenericTableLikeADirectory** | Returns the elements of a generic table, one-by-one, in collation order. |
| **RtlEnumerateGenericTableWithoutSplaying** | Enumerates the elements in a generic table. |
| **RtlEnumerateGenericTableWithoutSplayingAvl** | Enumerates the elements in a generic table. |
| **RtlEqualPrefixSid** | Determines whether two security-identifier (SID) prefixes are equal. An SID prefix is the entire SID except for the last subauthority value. |
| **RtlEqualSid** | Determines whether two security identifier (SID) values are equal. Two SIDs must match exactly to be considered equal. |
| **RtlFillMemoryUlong** | Fills the specified range of memory with one or more repetitions of a ULONG value. |
| **RtlFillMemoryUlonglong** | Fills a given range of memory with one or more repetitions of a given ULONGLONG value. |
| **RtlFindUnicodePrefix** | Searches for the best match for a given Unicode file name in a prefix table. |
| **RtlFreeHeap** | Frees a memory block that was allocated from a heap by **RtlAllocateHeap**. |
| **RtlFreeOemString** | Releases storage that was allocated by any of the **Rtl..ToOemString**routines. |
| **RtlFreeSid** | Reserved for system use. |
| **RtlGenerate8dot3Name** | Generates a short (8.3) name for the specified long file name. |
| **RtlGetAce** | Obtains a pointer to an access control entry (ACE) in an access control list (ACL). |
| **RtlGetCompressionWorkSpaceSize** | Determines the correct size of the WorkSpace buffer for the **RtlCompressBuffer** and **RtlDecompressFragment** functions. |
| **RtlGetDaclSecurityDescriptor** | Returns a pointer to the discretionary ACL (DACL) for a security descriptor. |
| **RtlGetElementGenericTable** | Returns a pointer to the caller-supplied data for a particular generic table element. |
| **RtlGetElementGenericTableAvl** | Returns a pointer to the caller-supplied data for a particular generic Adelson-Velsky/Landis (AVL) table element. |
| **RtlGetGroupSecurityDescriptor** | Returns the primary group information for a given security descriptor. |
| **RtlGetOwnerSecurityDescriptor** | Returns the owner information for a given security descriptor. |
| **RtlGetSaclSecurityDescriptor** | Returns a pointer to the system ACL (SACL) for a security descriptor. |
| **RtlIdentifierAuthoritySid** | Reserved for system use. |
| **RtlInitCodePageTable** | Reserved for system use. |
| **RtlInitializeGenericTable** | Initializes a generic table. |
| **RtlInitializeGenericTableAvl** | Initializes a generic table using Adelson-Velsky/Landis (AVL) trees. |
| **RtlInitializeSid** | Initializes a security identifier (SID) structure. |
| **RtlInitializeSidEx** | Initializes a pre-allocated security identifier (SID) structure. |
| **RtlInitializeSplayLinks** | Initializes a splay link node. |
| **RtlInitializeUnicodePrefix** | Initializes a prefix table. |
| **RtlInsertAsLeftChild** | Inserts a splay link node into the tree as the left child of the specified node. |
| **RtlInsertAsRightChild** | Inserts a given splay link into the tree as the right child of a given node in that tree. |
| **RtlInsertElementGenericTable** | Adds a new element to a generic table. |
| **RtlInsertElementGenericTableAvl** | Adds a new entry to a generic table. |
| **RtlInsertElementGenericTableFullAvl** | Adds a new entry to a generic table. |
| **RtlInsertUnicodePrefix** | Inserts a new element into a Unicode prefix table. |
| **RtlIsGenericTableEmpty** | Determines if a generic table is empty. |
| **RtlIsGenericTableEmptyAvl** | Determines if a generic table is empty. |
| **RtlIsLeftChild** | Determines whether a given splay link is the left child of a node in a splay link tree. |
| **RtlIsNameLegalDOS8Dot3** | Determines whether a given name represents a valid short (8.3) file name. |
| **RtlIsRightChild** | Determines whether a given splay link is the right child of a node in a splay link tree. |
| **RtlIsRoot** | Determines whether the specified node is the root node of a splay link tree. |
| **RtlIsValidOemCharacter** | Determines if the specified Unicode character can be mapped to a valid OEM character. |
| **RtlLeftChild** | Returns a pointer to the left child of the specified splay link node. |
| **RtlLengthRequiredSid** | Returns the length, in bytes, of the buffer required to store a security identifier (SID) with a specified number of subauthorities. |
| **RtlLengthSid** | Returns the length, in bytes, of a valid security identifier (SID). |
| **RtlLookupElementGenericTable** | Searches a generic table for an element that matches the specified data. |
| **RtlLookupElementGenericTableAvl** | Searches a generic table for an element that matches the specified data. |
| **RtlLookupElementGenericTableFullAvl** | Searches a generic table for an element that matches the specified data. |
| **RtlLookupFirstMatchingElementGenericTableAvl** | Finds the left-most element in the tree that matches the indicated data. |
| **RtlMultiByteToUnicodeN** | Translates the specified source string into a Unicode string, using the current system ANSI code page (ACP). The source string is not necessarily from a multibyte character set. |
| **RtlMultiByteToUnicodeSize** | Determines the number of bytes that are required to store the Unicode translation for the specified source string. The translation is assumed to use the current system ANSI code page (ACP). The source string is not necessarily from a multibyte character set. |
| **RtlNextUnicodePrefix** | Enumerates the elements in a Unicode prefix table. |
| **RtlNtStatusToDosError** | Converts the specified NTSTATUS code to its equivalent system error code. |
| **RtlNtStatusToDosErrorNoTeb** | Reserved for system use. |
| **RtlNumberGenericTableElements** | Returns the number of elements in a generic table. |
| **RtlNumberGenericTableElementsAvl** | Returns the number of elements in a generic table. |
| **RtlOemStringToCountedUnicodeSize** | Determines the size, in bytes, that a given OEM string will be after it is translated into a counted Unicode string. |
| **RtlOemStringToCountedUnicodeString** | Translates the specified source string into a Unicode string using the current system OEM code page. |
| **RtlOemStringToUnicodeSize** | Determines the size, in bytes, that a given OEM string will be after it is translated into a null-terminated Unicode string. |
| **RtlxOemStringToUnicodeSize** | Reserved for system use. |
| **RtlOemStringToUnicodeString** | Translates a given source string into a null-terminated Unicode string using the current system OEM code page. |
| **RtlOemToUnicodeN** | Translates the specified source string into a Unicode string, using the current system OEM code page. |
| **RtlOffsetToPointer** | Returns a pointer for a given offset from a given base address. |
| **RtlParent** | Returns a pointer to the parent of the specified node in a splay link tree. |
| **RtlPointerToOffset** | Returns the offset from a given base address of a given pointer. |
| **RtlRandom** | Returns a random number that was generated from a given seed value. |
| **RtlRandomEx** | Returns a random number that was generated from a given seed value. |
| **RtlRealPredecessor** | Returns a pointer to the predecessor of the specified node in the splay link tree. |
| **RtlRealSuccessor** | Returns a pointer to the successor of the specified node in the splay link tree. |
| **RtlRemoveUnicodePrefix** | Removes an element from a prefix table. |
| **RtlReserveChunk** | Reserved for system use. |
| **RtlRightChild** | Returns a pointer to the right child of the specified splay link node. |
| **RtlSecondsSince1970ToTime** | Converts the elapsed time, in seconds, since the beginning of 1970 to an absolute system time value. |
| **RtlSecondsSince1980ToTime** | Converts the elapsed time, in seconds, since the beginning of 1980 to an absolute system time value. |
| **RtlSelfRelativeToAbsoluteSD** | Creates a new security descriptor in absolute format by using a security descriptor in self-relative format as a template. |
| **RtlSetGroupSecurityDescriptor** | Sets the primary group information of an absolute-format security descriptor. It replaces any primary group information that is already present in the security descriptor. |
| **RtlSetOwnerSecurityDescriptor** | Sets the owner information of an absolute-format security descriptor. It replaces any owner information that is already present in the security descriptor. |
| **RtlSplay** | Rebalances, or "splays," a splay link tree around the specified splay link, making that link the new root of the tree. |
| **RtlSubAuthorityCountSid** | Reserved for system use. |
| **RtlSubAuthoritySid** | Returns a pointer to a specified subauthority of a security identifier (SID). |
| **RtlSubtreePredecessor** | Returns a pointer to the predecessor of the specified node within the subtree that is rooted at that node. |
| **RtlSubtreeSuccessor** | Returns a pointer to the successor of the specified node within the subtree that is rooted at that node. |
| **RtlTimeToSecondsSince1970** | Converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1970. |
| **RtlTimeToSecondsSince1980** | Converts a given absolute system time value to the elapsed time, in seconds, since the beginning of 1980. |
| **RtlUnicodeStringToAnsiSize** | Determines the number of bytes that are required to store the ANSI translation for the specified Unicode string. |
| **RtlUnicodeStringToCountedOemString** | Translates the specified Unicode source string into a counted OEM string using the current system OEM code page. |
| **RtlUnicodeStringToOemSize** | Determines the size, in bytes, that a given Unicode string will be after it is translated into an OEM string. |
| **RtlUnicodeStringToOemSize** | Reserved for system use. |
| **RtlUnicodeStringToOemString** | Translates a given Unicode source string into an OEM string using the current system OEM code page. |
| **RtlUnicodeToCustomCPN** | Reserved for system use. |
| **RtlUnicodeToMultiByteN** | Translates the specified Unicode string into a new character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| **RtlUnicodeToMultiByteSize** | Determines the number of bytes that are required to store the multibyte translation for the specified Unicode string. The translation is assumed to use the current system ANSI code page (ACP). |
| **RtlUnicodeToOemN** | Translates a given Unicode string to an OEM string, using the current system OEM code page. |
| **RtlUpcaseUnicodeStringToCountedOemString** | Translates a given Unicode source string into an uppercase counted OEM string using the current system OEM code page. |
| **RtlUpcaseUnicodeStringToOemString** | Translates a given Unicode source string into an uppercase OEM string using the current system OEM code page. |
| **RtlUpcaseUnicodeToCustomCPN** | Reserved for system use. |
| **RtlUpcaseUnicodeToMultiByteN** | Translates the specified Unicode string into a new uppercase character string, using the current system ANSI code page (ACP). The translated string is not necessarily from a multibyte character set. |
| **RtlUpcaseUnicodeToOemN** | Translates a given Unicode string into an uppercase OEM string, using the current system OEM code page. |
| **RtlValidSid** | Validates a security identifier (SID) by verifying that the revision number is within a known range and that the number of subauthorities is less than the maximum. |
