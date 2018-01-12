---
title: FLT\_PARAMETERS for IRP\_MJ\_PREPARE\_MDL\_WRITE union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_PREPARE\_MDL\_WRITE.
ms.assetid: eebbb8d4-f46d-4aee-aeb3-7edcbd23207a
keywords: ["FLT_PARAMETERS for IRP_MJ_PREPARE_MDL_WRITE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
---

# FLT\_PARAMETERS for IRP\_MJ\_PREPARE\_MDL\_WRITE union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is IRP\_MJ\_PREPARE\_MDL\_WRITE.

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    LARGE_INTEGER           FileOffset;
    ULONG POINTER_ALIGNMENT Length;
    ULONG POINTER_ALIGNMENT Key;
    PMDL                    *MdlChain;
  } PrepareMdlWrite;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**PrepareMdlWrite**  
Structure containing the following members.

**FileOffset**  
Starting byte within the cached file.

**Length**  
Length, in bytes, of the data to be written to the cached file.

**Key**  
Key value associated with a byte-range lock on the target file. If the range to be written overlaps or is a subrange of an exclusively locked range within the file, this parameter must be the key for that exclusive lock,. The exclusive lock must be held by the parent process of the calling thread; otherwise, this parameter is ignored.

**MdlChain**  
Pointer to a variable that receives a pointer to a chain of one or more memory descriptor lists (MDL) that describe the pages containing the data to be written.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_PREPARE\_MDL\_WRITE operations contains the parameters for a fast I/O **PrepareMdlWrite** operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

If a fast I/O IRP\_MJ\_PREPARE\_MDL\_WRITE request fails, the issuer of the I/O determines how to reissue the request. A minifilter may not always get an IRP-based IRP\_MJ\_MDL\_WRITE. For instance, the IRP request could be reissued as IRP\_MJ\_WRITE/IRP\_MN\_MDL.

IRP\_MJ\_PREPARE\_MDL\_WRITE is a fast I/O operation.

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


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_PREPARE_MDL_WRITE%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





