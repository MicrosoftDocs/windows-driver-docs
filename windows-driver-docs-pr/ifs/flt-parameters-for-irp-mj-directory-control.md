---
title: FLT_PARAMETERS for IRP_MJ_DIRECTORY_CONTROL union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_DIRECTORY\_CONTROL.
ms.assetid: 3dadd64b-7e93-4c75-808d-2f26edb3ebd7
keywords: ["FLT_PARAMETERS for IRP_MJ_DIRECTORY_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP\_MJ\_DIRECTORY\_CONTROL union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_DIRECTORY\_CONTROL**](irp-mj-directory-control.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...   ;
  union {
    struct {
      ULONG                   Length;
      PUNICODE_STRING         FileName;
      FILE_INFORMATION_CLASS  FileInformationClass;
      ULONG POINTER_ALIGNMENT FileIndex;
      PVOID                   DirectoryBuffer;
      PMDL                    MdlAddress;
    } QueryDirectory;
    struct {
      ULONG                   Length;
      ULONG POINTER_ALIGNMENT CompletionFilter;
      ULONG                   Spare1;
      ULONG POINTER_ALIGNMENT Spare2;
      PVOID                   DirectoryBuffer;
      PMDL                    MdlAddress;
    } NotifyDirectory;
  } DirectoryControl;
  ...   ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**DirectoryControl**  
Structure containing the following members.

**QueryDirectory**  
Union component used for IRP\_MN\_QUERY\_DIRECTORY operations.

**Length**  
Length, in bytes, of the buffer that the **QueryDirectory.DirectoryBuffer** member points to.

**FileName**  
Pointer to a [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure that contains the name of a file within the specified directory.

**FileInformationClass**  
Specifies one of the values described below.

| Value                          | Meaning                                                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| FileBothDirectoryInformation   | Return a [**FILE\_BOTH\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540235) structure for each file.                      |
| FileDirectoryInformation       | Return a [**FILE\_DIRECTORY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540248) structure for each file.                     |
| FileFullDirectoryInformation   | Return a [**FILE\_FULL\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540289) structure for each file.                      |
| FileIdBothDirectoryInformation | Return a [**FILE\_ID\_BOTH\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540303) structure for each file.               |
| FileIdFullDirectoryInformation | Return a [**FILE\_ID\_FULL\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540310) structure for each file.               |
| FileNamesInformation           | Return a [**FILE\_NAMES\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540329) structure for each file.                             |
| FileObjectIdInformation        | Return a [**FILE\_OBJECTID\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540335) structure for each file.                       |
| FileReparsePointInformation    | Return a single [**FILE\_REPARSE\_POINT\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540354) structure for the directory. |

 

**FileIndex**  
Index of the file where the directory scan begins. Ignored if the SL\_INDEX\_SPECIFIED flag is not set. This parameter cannot be specified in any Win32 function or kernel-mode support routine. Currently it is used only by the NT virtual DOS machine (NTVDM), which exists only on 32-bit NT-based operating systems. Note that the file index is undefined for file systems, such as NTFS, in which the position of a file within the parent directory is not fixed and can be changed at any time to maintain sort order.

**DirectoryBuffer**  
Pointer to a caller-supplied output buffer that receives the requested information about the contents of the directory.

**MdlAddress**  
Address of a memory descriptor list (MDL) that describes the buffer that the **QueryDirectory.DirectoryBuffer** member points to. This member is optional and can be **NULL**.

**NotifyDirectory**  
Union component used for IRP\_MN\_NOTIFY\_CHANGE\_DIRECTORY operations.

**Length**  
Length, in bytes, of the buffer that the **NotifyDirectory.DirectoryBuffer** member points to.

**CompletionFilter**  
Bitmask of flags that specify the types of changes to files or directories that should cause the IRPs in the notify list to be completed. The possible flag values are described following.

| Flag                                | Meaning                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------|
| FILE\_NOTIFY\_CHANGE\_FILE\_NAME    | A file has been added, deleted, or renamed in this directory.                  |
| FILE\_NOTIFY\_CHANGE\_DIR\_NAME     | A subdirectory has been created, removed, or renamed.                          |
| FILE\_NOTIFY\_CHANGE\_NAME          | This directory's name has changed.                                             |
| FILE\_NOTIFY\_CHANGE\_ATTRIBUTES    | The value of an attribute of this file, such as last access time, has changed. |
| FILE\_NOTIFY\_CHANGE\_SIZE          | This file's size has changed.                                                  |
| FILE\_NOTIFY\_CHANGE\_LAST\_WRITE   | This file's last modification time has changed.                                |
| FILE\_NOTIFY\_CHANGE\_LAST\_ACCESS  | This file's last access time has changed.                                      |
| FILE\_NOTIFY\_CHANGE\_CREATION      | This file's creation time has changed.                                         |
| FILE\_NOTIFY\_CHANGE\_EA            | This file's extended attributes have been modified.                            |
| FILE\_NOTIFY\_CHANGE\_SECURITY      | This file's security information has changed.                                  |
| FILE\_NOTIFY\_CHANGE\_STREAM\_NAME  | A file stream has been added, deleted, or renamed in this directory.           |
| FILE\_NOTIFY\_CHANGE\_STREAM\_SIZE  | This file stream's size has changed.                                           |
| FILE\_NOTIFY\_CHANGE\_STREAM\_WRITE | This file stream's data has changed.                                           |

 

**Spare1**  
Not currently used.

**Spare2**  
Not currently used.

**DirectoryBuffer**  
Pointer to a caller-supplied output buffer that receives the requested information about the contents of the directory.

**MdlAddress**  
Address of an MDL that describes the buffer that the **NotifyDirectory.DirectoryBuffer** member points to. This member is optional and can be **NULL**.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_DIRECTORY\_CONTROL operations contains the parameters for an IRP-based directory-control-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_DIRECTORY\_CONTROL is an IRP-based operation.

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
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FILE\_BOTH\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540235)

[**FILE\_DIRECTORY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540248)

[**FILE\_FULL\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540289)

[**FILE\_ID\_BOTH\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540303)

[**FILE\_ID\_FULL\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540310)

[**FILE\_NAMES\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540329)

[**FILE\_OBJECTID\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540335)

[**FILE\_REPARSE\_POINT\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540354)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FltNotifyFilterChangeDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff543377)

[**FsRtlNotifyFilterChangeDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff547010)

[**FsRtlNotifyFilterReportChange**](https://msdn.microsoft.com/library/windows/hardware/ff547018)

[**FsRtlNotifyFullChangeDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff547026)

[**FsRtlNotifyFullReportChange**](https://msdn.microsoft.com/library/windows/hardware/ff547041)

[**IRP\_MJ\_DIRECTORY\_CONTROL**](irp-mj-directory-control.md)

[**ZwQueryDirectoryFile**](https://msdn.microsoft.com/library/windows/hardware/ff567047)

 

 






