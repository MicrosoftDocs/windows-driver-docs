---
title: FLT_FILE_NAME_OPTIONS
description: FLT\_FILE\_NAME\_OPTIONS
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_FILE\_NAME\_OPTIONS

The FLT_FILE_NAME_OPTIONS type is a bitmask of flags that specify the name format, query method, and flags for a file name information query.

```cpp
typedef ULONG FLT_FILE_NAME_OPTIONS;
#define FLT_VALID_FILE_NAME_FORMATS                       0x000000ff
    #define FLT_FILE_NAME_NORMALIZED                      0x00000001
    #define FLT_FILE_NAME_OPENED                          0x00000002
    #define FLT_FILE_NAME_SHORT                           0x00000003
#define FLT_VALID_FILE_NAME_QUERY_METHODS                 0x0000ff00
    #define FLT_FILE_NAME_QUERY_DEFAULT                   0x00000100
    #define FLT_FILE_NAME_QUERY_CACHE_ONLY                0x00000200
    #define FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY           0x00000300
    #define FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP 0x00000400
#define FLT_VALID_FILE_NAME_FLAGS                         0xff000000
    #define FLT_FILE_NAME_REQUEST_FROM_CURRENT_PROVIDER   0x01000000
    #define FLT_FILE_NAME_DO_NOT_CACHE                    0x02000000
    #define FLT_FILE_NAME_ALLOW_QUERY_ON_REPARSE          0x04000000
```

Bits 0 through 7 indicate the file format, which can be queried by using the [**FltGetFileNameFormat**](/previous-versions/ff543030(v=vs.85)) macro. For an explanation of these formats, see [**FLT_FILE_NAME_INFORMATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_file_name_information). The following values are currently defined.

| Value | Meaning |
| ----- | ------- |
| FLT_FILE_NAME_NORMALIZED | The normalized name for the file. |
| FLT_FILE_NAME_OPENED | The name that was used when the handle was opened to this file. This name is not normalized. |
| FLT_FILE_NAME_SHORT | The short (8.3) name for the file. The short name for a file does not include the volume name, directory path, or stream name. This name is not normalized. |

Bits 8 through 15 specify the file name query method to be used by the Filter Manager, which can be queried by using the [**FltGetFileNameQueryMethod**](/previous-versions/ff543040(v=vs.85)) macro. For an explanation of these values, see [**FltGetFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilenameinformation). The following values are currently defined.

| Value | Meaning |
| ----- | ------- |
| FLT_FILE_NAME_QUERY_DEFAULT | If it is not currently safe to query the file system for the file name, do nothing. Otherwise, query the Filter Manager's name cache for the file name information. If the name is not found in the cache, query the file system and cache the result. |
| FLT_FILE_NAME_QUERY_CACHE_ONLY | Query the Filter Manager's name cache for the file name information. Do not query the file system. |
| FLT_FILE_NAME_QUERY_FILESYSTEM_ONLY | Query the file system for the file name information. Do not query the Filter Manager's name cache, and do not cache the result of the file system query. |
| FLT_FILE_NAME_QUERY_ALWAYS_ALLOW_CACHE_LOOKUP | Query the Filter Manager's name cache for the file name information. If the name is not found in the cache, and it is currently safe to do so, query the file system for the file name information and cache the result. |

Bits 16 through 23 are currently unused.

Bits 24 through 31 are used by name provider minifilters to specify the file name flags. The following values are currently defined.

| Value | Meaning |
| ----- | ------- |
| FLT_FILE_NAME_REQUEST_FROM_CURRENT_PROVIDER | A name provider minifilter can use this flag to specify that a name query request should be redirected to itself (the name provider minifilter) rather than being satisfied by the name providers lower in the stack. |
| FLT_FILE_NAME_DO_NOT_CACHE | This flag denotes that the name retrieved from this query should not be cached. Name provider minifilters use this flag as they perform intermediate queries to generate a name. |
| FLT_FILE_NAME_ALLOW_QUERY_ON_REPARSE | A name provider minifilter can use this flag to specify that it is safe to query the name in the post-create path even if STATUS_REPARSE was returned. It is the caller's responsibility to ensure that the **FileObject->FileName** field was not changed. Do not use this flag with mount points or symbolic link reparse points. |

## Requirements

****Header****: fltkernel.h (include fltkernel.h)


## Related topics

[**FLT_FILE_NAME_INFORMATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_file_name_information)

[**FltGetDestinationFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetdestinationfilenameinformation)

[**FltGetFileNameFormat**](/previous-versions/ff543030(v=vs.85))

[**FltGetFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilenameinformation)

[**FltGetFileNameInformationUnsafe**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilenameinformationunsafe)

[**FltGetFileNameQueryMethod**](/previous-versions/ff543040(v=vs.85))
