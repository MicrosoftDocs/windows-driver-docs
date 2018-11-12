---
title: FLT_FILE_NAME_OPTIONS
description: FLT\_FILE\_NAME\_OPTIONS
ms.assetid: 6e21c11e-d2c8-4c57-8225-1fbc365cbbac
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_FILE\_NAME\_OPTIONS





The FLT\_FILE\_NAME\_OPTIONS type is a bitmask of flags that specify the name format, query method, and flags for a file name information query.

```cpp
typedef ULONG FLT_FILE_NAME_OPTIONS; 
#define FLT_VALID_FILE_NAME_FORMATS 0x000000ff
    #define FLT_FILE_NAME_NORMALIZED    0x01
    #define FLT_FILE_NAME_OPENED        0x02
    #define FLT_FILE_NAME_SHORT         0x03
#define FLT_VALID_FILE_NAME_QUERY_METHODS 0x0000ff00
    #define FLT_FILE_NAME_QUERY_DEFAULT     0x0100
    #define FLT_FILE_NAME_QUERY_CACHE_ONLY  0x0200
    #define FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY 0x0300
    #define FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP 0x0400
#define FLT_VALID_FILE_NAME_FLAGS 0xff000000
    #define FLT_FILE_NAME_REQUEST_FROM_CURRENT_PROVIDER 0x01000000
    #define FLT_FILE_NAME_DO_NOT_CACHE                  0x02000000
```

Bits 0 through 7 indicate the file format, which can be queried by using the [**FltGetFileNameFormat**](https://msdn.microsoft.com/library/windows/hardware/ff543030) macro. For an explanation of these formats, see [**FLT\_FILE\_NAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544633). The following values are currently defined.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_NORMALIZED</p></td>
<td align="left"><p>The normalized name for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLT_FILE_NAME_OPENED</p></td>
<td align="left"><p>The name that was used when the handle was opened to this file. This name is not normalized.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_SHORT</p></td>
<td align="left"><p>The short (8.3) name for the file. The short name for a file does not include the volume name, directory path, or stream name. This name is not normalized.</p></td>
</tr>
</tbody>
</table>

 

Bits 8 through 15 specify the file name query method to be used by the Filter Manager, which can be queried by using the [**FltGetFileNameQueryMethod**](https://msdn.microsoft.com/library/windows/hardware/ff543040) macro. For an explanation of these values, see [**FltGetFileNameInformation**](https://msdn.microsoft.com/library/windows/hardware/ff543032). The following values are currently defined.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_QUERY_DEFAULT</p></td>
<td align="left"><p>If it is not currently safe to query the file system for the file name, do nothing. Otherwise, query the Filter Manager&#39;s name cache for the file name information. If the name is not found in the cache, query the file system and cache the result.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLT_FILE_NAME_QUERY_CACHE_ONLY</p></td>
<td align="left"><p>Query the Filter Manager&#39;s name cache for the file name information. Do not query the file system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY</p></td>
<td align="left"><p>Query the file system for the file name information. Do not query the Filter Manager&#39;s name cache, and do not cache the result of the file system query.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP</p></td>
<td align="left"><p>Query the Filter Manager&#39;s name cache for the file name information. If the name is not found in the cache, and it is currently safe to do so, query the file system for the file name information and cache the result.</p></td>
</tr>
</tbody>
</table>

 

Bits 16 through 23 are currently unused.

Bits 24 through 31 are used by name provider minifilters to specify the file name flags. The following values are currently defined.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_REQUEST_FROM_CURRENT_PROVIDER</p></td>
<td align="left"><p>A name provider minifilter can use this flag to specify that a name query request should be redirected to itself (the name provider minifilter) rather than being satisfied by the name providers lower in the stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLT_FILE_NAME_DO_NOT_CACHE</p></td>
<td align="left"><p>This flag denotes that the name retrieved from this query should not be cached. Name provider minifilters use this flag as they perform intermediate queries to generate a name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_ALLOW_QUERY_ON_REPARSE</p></td>
<td align="left"><p>A name provider minifilter can use this flag to specify that it is safe to query the name in the post-create path even if STATUS_REPARSE was returned. It is the caller&#39;s responsibility to ensure that the <strong>FileObject-&gt;FileName</strong> field was not changed. Do not use this flag with mount points or symbolic link reparse points.</p>
<p>This flag is available on Microsoft Windows Server 2003 SP1 and later. This flag is also available on Windows 2000 SP4 with Update Rollup 1 and later.</p></td>
</tr>
</tbody>
</table>

 

Requirements: fltkernel.h (include fltkernel.h)

## Related topics


[**FLT\_FILE\_NAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544633)

[**FltGetDestinationFileNameInformation**](https://msdn.microsoft.com/library/windows/hardware/ff543003)

[**FltGetFileNameFormat**](https://msdn.microsoft.com/library/windows/hardware/ff543030)

[**FltGetFileNameInformation**](https://msdn.microsoft.com/library/windows/hardware/ff543032)

[**FltGetFileNameInformationUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff543035)

[**FltGetFileNameQueryMethod**](https://msdn.microsoft.com/library/windows/hardware/ff543040)

 

 






