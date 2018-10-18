---
title: FLT_PARAMETERS for IRP_MJ_QUERY_OPEN union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_OPEN.
ms.assetid: 5B78E1D8-F724-404D-8750-3D52BB9B4910
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_OPEN union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP_MJ_QUERY_OPEN union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is IRP_MJ_QUERY_OPEN.

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIRP                   Irp;
    PVOID                  FileInformation;
    PULONG                 Length;
    FILE_INFORMATION_CLASS FileInformationClass;
  } QueryOpen;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**Irp**  
* A pointer to the IRP associated with this operation. 

**FileInformation**  
* A pointer to a caller-allocated buffer into which the routine writes the requested information about the file object. The *FileInformationClass* member specifies the type of information that the caller requests. 

**Length**
*  The size, in bytes, of the buffer pointed to by **FileInformation**.

**FileInformationClass**
* Specifies the type of information to be returned about the file, in the buffer that FileInformation points to. Device and intermediate drivers can specify any of the following [**FILE_INFORMATION_CLASS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ne-wdm-_file_information_class) values. Other values cause the call to fail and should not be passed to PreQueryOpen/PostQueryOpen calls. 

| FILE_INFORMATION_CLASS value | Type of information returned |
| --- | --- |
| FileStatInformation | A [**FILE_STAT_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_file_stat_information) structure. This structure contains an access mask. For more information about access masks, see [ACCESS_MASK](https://docs.microsoft.com/windows-hardware/drivers/kernel/access-mask). 
| FileStatLxInformation | A [**FILE_STAT_LX_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_file_stat_lx_information) structure. This structure contains an access mask. For more information about access masks, see [ACCESS_MASK](https://docs.microsoft.com/windows-hardware/drivers/kernel/access-mask). 
| FileCaseSensitiveInformation | A [FILE_CASE_SENSITIVE_INFORMATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_file_stat_information) structure. |

## Remarks


The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP_MJ_QUERY_OPEN operations contains the parameters for an **QueryOpen** operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP_MJ_QUERY_OPEN is a file system (FSFilter) callback operation.

For more information about FSFilter callback operations, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff547172).

## Requirements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 10, version 1703 and later versions of the Windows operating system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FsRtlRegisterFileSystemFilterCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff547172)
