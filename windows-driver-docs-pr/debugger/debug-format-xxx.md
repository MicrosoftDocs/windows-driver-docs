---
title: DEBUG\_FORMAT\_XXX
description: The DEBUG_FORMAT_XXX bit-flags are used by WriteDumpFile2 and WriteDumpFileWide to determine the format of a crash dump file and, for user-mode Minidumps, what information to include in the file.
ms.author: domars
ms.date: 08/20/2018
topic_type:
- apiref
api_name:
- DEBUG_FORMAT_XXX
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_FORMAT\_XXX

The DEBUG_FORMAT_XXX bit-flags are used by WriteDumpFile2 and WriteDumpFileWide to determine the format of a crash dump file and, for user-mode Minidumps, what information to include in the file.

The following bit-flags apply to all crash dump files.

<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_WRITE_CAB</p>
</td>
<td>
<p>Package the crash dump file in a CAB file.  The supplied file name or file handle is used for the CAB file; the crash dump is first created in a temporary file before being moved into the CAB file.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_CAB_SECONDARY_FILES</p>
</td>
<td>
<p>
<dl>
<dt>Include the current symbols and mapped images in the CAB file.</dt>
<dt>If DEBUG_FORMAT_WRITE_CAB is not set, this flag is ignored.</dt>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_NO_OVERWRITE</p>
</td>
<td>
<p>Do not overwrite existing files.</p>
</td>
</tr>
</table>
<p> </p>
<p>The following bit-flags can also be included for user-mode Minidumps.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_FULL_MEMORY</p>
</td>
<td>
<p>Add full memory data.  All accessible committed pages owned by the target application will be included.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_HANDLE_DATA</p>
</td>
<td>
<p>Add data about the handles that are associated with the target application.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_UNLOADED_MODULES</p>
</td>
<td>
<p>Add unloaded module information.  This information is available only in Windows Server 2003 and later versions of Windows.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_INDIRECT_MEMORY</p>
</td>
<td>
<p>Add indirect memory.  A small region of memory that surrounds any address that is referenced by a pointer on the stack or backing store is included.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_DATA_SEGMENTS</p>
</td>
<td>
<p>Add all data segments within the executable images.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_FILTER_MEMORY</p>
</td>
<td>
<p>Set to zero all of the memory on the stack and in the backing store that is not useful for recreating the stack trace.  This can make compression of the Minidump more efficient and increase privacy by removing unnecessary information.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_FILTER_PATHS</p>
</td>
<td>
<p>Remove the module paths, leaving only the module names.  This is useful for protecting privacy by hiding the directory structure (which may contain the user&#39;s name).</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_FILTER_TRIAGE</p>
</td>
<td>
<p>This format is used to filter out any data that is not a pointer to other data captured in the dump. The flag can be used to reduce the amount of private data present in the dump while still allowing crashes to be diagnosed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_PROCESS_THREAD_DATA</p>
</td>
<td>
<p>Add the process environment block (PEB) and thread environment block (TEB).  This flag can be used to provide Windows system information for threads and processes.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_PRIVATE_READ_WRITE_MEMORY</p>
</td>
<td>
<p>Add all committed private read-write memory pages.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_NO_OPTIONAL_DATA</p>
</td>
<td>
<p>
<dl>
<dt>Prevent privacy-sensitive data from being included in the Minidump.  Currently, this flag excludes from the Minidump data that would have been added due to the following flags being set:</dt>
<dt>DEBUG_FORMAT_USER_SMALL_PROCESS_THREAD_DATA,</dt>
<dt>DEBUG_FORMAT_USER_SMALL_FULL_MEMORY,</dt>
<dt>DEBUG_FORMAT_USER_SMALL_INDIRECT_MEMORY,</dt>
<dt>DEBUG_FORMAT_USER_SMALL_PRIVATE_READ_WRITE_MEMORY.</dt>
</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_FULL_MEMORY_INFO</p>
</td>
<td>
<p>Add all basic memory information.  This is the information returned by the <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces2-queryvirtual" data-raw-source="[IDebugDataSpaces2::QueryVirtual method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces2-queryvirtual)">IDebugDataSpaces2::QueryVirtual method</a>.  The information for all memory is included, not just valid memory, which allows the debugger to reconstruct the complete virtual memory layout from the Minidump.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_THREAD_INFO</p>
</td>
<td>
<p>Add additional thread information, which includes execution time, start time, exit time, start address, and exit status.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_FORMAT_USER_SMALL_CODE_SEGMENTS</p>
</td>
<td>
<p>Add all code segments with the executable images.</p>
</td>
</tr>
</table>



Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">DbgEng.h (include DbgEng.h)</td>
</tr>
</tbody>
</table>
 





