---
title: FLT\_PARAMETERS for IRP\_MJ\_ACQUIRE\_FOR\_SECTION\_SYNCHRONIZATION union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_ACQUIRE\_FOR\_SECTION\_SYNCHRONIZATION.
ms.assetid: ea3ae072-4a98-48df-871a-cc7d882b96b8
keywords: ["FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FLT\_PARAMETERS for IRP\_MJ\_ACQUIRE\_FOR\_SECTION\_SYNCHRONIZATION union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is IRP\_MJ\_ACQUIRE\_FOR\_SECTION\_SYNCHRONIZATION.

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    FS_FILTER_SECTION_SYNC_TYPE SyncType;
    ULONG POINTER_ALIGNMENT     PageProtection;
  } AcquireForSectionSynchronization;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**AcquireForSectionSynchronization**  
Structure containing the following members.

**SyncType**  
Specifies the type of synchronization requested for the section. This parameter must be one of two enumerated values:

**SyncTypeCreateSection**

**SyncTypeOther**

**PageProtection**  
Specifies the type of page protection requested for the section. Must be zero if SyncType**SyncType** is SyncTypeOther. Otherwise, one of the following flags, possibly combined with PAGE\_NOCACHE:

PAGE\_READONLY

PAGE\_READWRITE

PAGE\_WRITECOPY

PAGE\_EXECUTE

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_ACQUIRE\_FOR\_SECTION\_SYNCHRONIZATION operations contains the parameters for an **AcquireForSectionSynchronization** operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_ACQUIRE\_FOR\_SECTION\_SYNCHRONIZATION is a file system (FSFilter) callback operation.

If the enumerated value of the **SyncType** member is set to **SyncTypeOther** (zero), a file system minifilter or legacy filter driver cannot fail this operation. If **SyncType** is set to **SyncTypeCreateSection**, a file system minifilter or legacy filter driver is allowed to fail with a STATUS\_INSUFFICIENT\_RESOURCES error if there is not enough memory to create the section.

For more information about FSFilter callback operations, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff547172).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows XP and later versions of the Windows operating system.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





