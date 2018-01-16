---
title: FLT\_FILE\_NAME\_OPTIONS
description: FLT\_FILE\_NAME\_OPTIONS
ms.assetid: 6e21c11e-d2c8-4c57-8225-1fbc365cbbac
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FLT\_FILE\_NAME\_OPTIONS


## <a href="" id="ddk-flt-file-name-options-if"></a>


The FLT\_FILE\_NAME\_OPTIONS type is a bitmask of flags that specify the name format, query method, and flags for a file name information query.

```
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
<td align="left"><p>If it is not currently safe to query the file system for the file name, do nothing. Otherwise, query the Filter Manager's name cache for the file name information. If the name is not found in the cache, query the file system and cache the result.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLT_FILE_NAME_QUERY_CACHE_ONLY</p></td>
<td align="left"><p>Query the Filter Manager's name cache for the file name information. Do not query the file system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY</p></td>
<td align="left"><p>Query the file system for the file name information. Do not query the Filter Manager's name cache, and do not cache the result of the file system query.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP</p></td>
<td align="left"><p>Query the Filter Manager's name cache for the file name information. If the name is not found in the cache, and it is currently safe to do so, query the file system for the file name information and cache the result.</p></td>
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
<td align="left"><p>A name provider minifilter can use this flag to specify that it is safe to query the name in the post-create path even if STATUS_REPARSE was returned. It is the caller's responsibility to ensure that the <strong>FileObject-&gt;FileName</strong> field was not changed. Do not use this flag with mount points or symbolic link reparse points.</p>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_FILE_NAME_OPTIONS%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





