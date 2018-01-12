---
title: FLT\_PARAMETERS for IRP\_MJ\_NETWORK\_QUERY\_OPEN union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_NETWORK\_QUERY\_OPEN.
ms.assetid: bafe015c-a747-4d18-95d5-adad2ad1570b
keywords: ["FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
---

# FLT\_PARAMETERS for IRP\_MJ\_NETWORK\_QUERY\_OPEN union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is IRP\_MJ\_NETWORK\_QUERY\_OPEN.

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIRP                           Irp;
    PFILE_NETWORK_OPEN_INFORMATION NetworkInformation;
  } NetworkQueryOpen;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**NetworkQueryOpen**  
Structure containing the following members.

**Irp**  
Pointer to a create IRP that represents this open operation. This IRP is to be used by the file system for common open/create code but not actually completed.

**NetworkInformation**  
Pointer to a [**FILE\_NETWORK\_OPEN\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545822)-structured buffer to receive the requested information about the file.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_NETWORK\_QUERY\_OPEN operations contains the parameters for a NetworkQueryOpen operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. The **FLT\_PARAMETERS** structure is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

&gt; \[!Note\]   The file object associated with IRP\_MJ\_NETWORK\_QUERY\_OPEN is a stack-based object.
&gt;A filter registered for the NetworkQueryOpen callback must not reference this object. That is, do not call ObReferenceObject or ObDereferenceObject on this stack-based file object. Also, do not save a pointer to the object.

 

IRP\_MJ\_NETWORK\_QUERY\_OPEN is a fast I/O operation. It is the equivalent of the FastIoQueryOpen (not FastIoQueryNetworkOpenInfo) operation. A filter must register for this operation.

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


[**FILE\_NETWORK\_OPEN\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545822)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FltQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff543439)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

[**ZwQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567052)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_NETWORK_QUERY_OPEN%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





