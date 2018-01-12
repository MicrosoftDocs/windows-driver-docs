---
title: FLT\_PARAMETERS for IRP\_MJ\_QUERY\_INFORMATION union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_QUERY\_INFORMATION.
ms.assetid: 7fcd6881-1b6e-46eb-8476-d766f6fea7ef
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_QUERY\_INFORMATION union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                    Length;
    FILE_INFORMATION_CLASS POINTER_ALIGNMENT FileInformationClass;
    PVOID                                    InfoBuffer;
  } QueryFileInformation;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**QueryFileInformation**  
Structure containing the following members.

**Length**  
Length, in bytes, of the buffer at **InfoBuffer**.

**FileInformationClass**  
Type of file information to be returned. One of the following:

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
<td align="left"><p><strong>FileAllInformation</strong></p></td>
<td align="left"><p>Return a FILE_ALL_INFORMATION structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileAttributeTagInformation</strong></p></td>
<td align="left"><p>Return a [<strong>FILE_ATTRIBUTE_TAG_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545750) structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileBasicInformation</strong></p></td>
<td align="left"><p>Return a [<strong>FILE_BASIC_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545762) structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileCompressionInformation</strong></p></td>
<td align="left"><p>Return a FILE_COMPRESSION_INFORMATION structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileEaInformation</strong></p></td>
<td align="left"><p>Return a FILE_EA_INFORMATION structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileInternalInformation</strong></p></td>
<td align="left"><p>Return a [<strong>FILE_INTERNAL_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540318) structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileMoveClusterInformation</strong></p></td>
<td align="left"><p>Return a FILE_MOVE_CLUSTER_INFORMATION structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileNameInformation</strong></p></td>
<td align="left"><p>Return a [<strong>FILE_NAME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545817) structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileNetworkOpenInformation</strong></p></td>
<td align="left"><p>Return a single [<strong>FILE_NETWORK_OPEN_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545822) structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FilePositionInformation</strong></p></td>
<td align="left"><p>Return a single [<strong>FILE_POSITION_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545848) structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileStandardInformation</strong></p></td>
<td align="left"><p>Return a single [<strong>FILE_STANDARD_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545855) structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileStreamInformation</strong></p></td>
<td align="left"><p>Return a single [<strong>FILE_STREAM_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540364) structure for the file.</p></td>
</tr>
</tbody>
</table>

 

**InfoBuffer**  
Pointer to the output buffer where the file information is to be returned.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_QUERY\_INFORMATION operations contains the parameters for a query-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_QUERY\_INFORMATION can be an IRP-based operation or a fast I/O operation.

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


[**FILE\_ATTRIBUTE\_TAG\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545750)

[**FILE\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545762)

[**FILE\_INTERNAL\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540318)

[**FILE\_NAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545817)

[**FILE\_NETWORK\_OPEN\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545822)

[**FILE\_POSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545848)

**FILE\_POSITION\_INFORMATION**
[**FILE\_STANDARD\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545855)

[**FILE\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540364)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_QUERY_INFORMATION%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





