---
title: FLT_PARAMETERS for IRP_MJ_SET_INFORMATION union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_SET\_INFORMATION.
ms.assetid: 860973bf-a98d-4495-9d6c-093ee985f360
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_SET\_INFORMATION union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_SET\_INFORMATION**](irp-mj-set-information.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                    Length;
    FILE_INFORMATION_CLASS POINTER_ALIGNMENT FileInformationClass;
    PFILE_OBJECT                             ParentOfTarget;
    union {
      struct {
        BOOLEAN ReplaceIfExists;
        BOOLEAN AdvanceOnly;
      };
      ULONG  ClusterCount;
      HANDLE DeleteHandle;
    };
    PVOID                                    InfoBuffer;
  } SetFileInformation;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**SetFileInformation**  
Structure containing the following members.

**Length**  
Length, in bytes, of the buffer at **InfoBuffer**.

**FileInformationClass**  
Type of information to be set for the file. One of the following:

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
<td align="left"><p><strong>FileAllocationInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540232" data-raw-source="[&lt;strong&gt;FILE_ALLOCATION_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540232)"><strong>FILE_ALLOCATION_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileBasicInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff545762" data-raw-source="[&lt;strong&gt;FILE_BASIC_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545762)"><strong>FILE_BASIC_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileDispositionInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff545765" data-raw-source="[&lt;strong&gt;FILE_DISPOSITION_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545765)"><strong>FILE_DISPOSITION_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileEndOfFileInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff545780" data-raw-source="[&lt;strong&gt;FILE_END_OF_FILE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545780)"><strong>FILE_END_OF_FILE_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileLinkInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540324" data-raw-source="[&lt;strong&gt;FILE_LINK_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540324)"><strong>FILE_LINK_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FilePositionInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff545848" data-raw-source="[&lt;strong&gt;FILE_POSITION_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545848)"><strong>FILE_POSITION_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileRenameInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540344" data-raw-source="[&lt;strong&gt;FILE_RENAME_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540344)"><strong>FILE_RENAME_INFORMATION</strong></a> for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileValidDataLengthInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff545873" data-raw-source="[&lt;strong&gt;FILE_VALID_DATA_LENGTH_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545873)"><strong>FILE_VALID_DATA_LENGTH_INFORMATION</strong></a> for the file.</p></td>
</tr>
</tbody>
</table>

 

**ParentOfTarget**  
For rename or link operations. If **InfoBuffer-&gt;FileName** contains a fully qualified file name, or if **InfoBuffer-&gt;RootDirectory** is non-**NULL**, this member is a file object pointer for the parent directory of the file that is the target of the operation. Otherwise it is **NULL**.

( *unnamed struct* )  
Structure containing the following members.

**ReplaceIfExists**  
For rename or link operations. Set to **TRUE** to specify that a file that already exists with the same name is to be replaced with the given file. Set to **FALSE** if the rename or link operation should fail if a file with the given name already exists.

**AdvanceOnly**  
A flag for end-of-file operations. This determines the use of the **EndOfFile** member [**FILE\_END\_OF\_FILE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545780) structure when **FileInformationClass** == **FileEndOfFileInformation**. If **TRUE**, a new valid data length for the file will be set from **EndOfFile** only if it increases the current valid data length. If **FALSE**, a new file size is set from **EndOfFile**.

**ClusterCount**  
Reserved for system use. Do not use.

**DeleteHandle**  
Reserved for system use. Do not use.

**InfoBuffer**  
Pointer to an input buffer that contains the file information to be set.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_SET\_INFORMATION operations contains the parameters for a set-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_SET\_INFORMATION is an IRP-based operation.

The **AdvanceOnly** member is set to **TRUE** by the cache manager to notify the file system to advance the current valid data length on the disk to the new valid data length in **EndOfFile**. If **AdvanceOnly** is **FALSE**, a new file size, in the **EndOfFile** member, is being set which can be larger or smaller than the current file size.

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


[**FILE\_ALLOCATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540232)

[**FILE\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545762)

[**FILE\_DISPOSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545765)

[**FILE\_END\_OF\_FILE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545780)

[**FILE\_LINK\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540324)

[**FILE\_POSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545848)

[**FILE\_RENAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540344)

[**FILE\_VALID\_DATA\_LENGTH\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545873)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IRP\_MJ\_SET\_INFORMATION**](irp-mj-set-information.md)

 

 






