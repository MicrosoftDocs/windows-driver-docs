---
title: FLT_PARAMETERS for IRP_MJ_PNP union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_PNP.
ms.assetid: d3ce893b-f113-4c50-8f52-30c7ced25ae0
keywords: ["FLT_PARAMETERS for IRP_MJ_PNP union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_PNP union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_PNP**](irp-mj-pnp.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...   ;
  union {
    struct  StartDevice;
    struct  QueryDeviceRelations;
    struct  QueryInterface;
    struct  DeviceCapabilities;
    struct  FilterResourceRequirements;
    struct  ReadWriteConfig;
    struct  SetLock;
    struct  QueryId;
    struct  QueryDeviceText;
    struct  UsageNotification;
  } Pnp;
  ...   ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**Pnp**  
**StartDevice**  
Union component used for the IRP\_MN\_START\_DEVICE operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749).

**QueryDeviceRelations**  
Union component used for the IRP\_MN\_QUERY\_DEVICE\_RELATIONS operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670).

**QueryInterface**  
Union component used for the IRP\_MN\_QUERY\_INTERFACE operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687).

**DeviceCapabilities**  
Union component used for the IRP\_MN\_QUERY\_CAPABILITIES operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664).

**FilterResourceRequirements**  
Union component used for the IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874).

**ReadWriteConfig**  
Union component used for the IRP\_MN\_READ\_CONFIG and IRP\_MN\_WRITE\_CONFIG operations. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) and [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769).

**SetLock**  
Union component used for the IRP\_MN\_SET\_LOCK operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_SET\_LOCK**](https://msdn.microsoft.com/library/windows/hardware/ff551742).

**QueryId**  
Union component used for the IRP\_MN\_QUERY\_ID operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679).

**QueryDeviceText**  
Union component used for the IRP\_MN\_QUERY\_DEVICE\_TEXT operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_DEVICE\_TEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551674).

**UsageNotification**  
Union component used for the IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841).

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_PNP**](irp-mj-pnp.md) operations contains the parameters for an IRP-based Plug and Play (PnP) operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

The IRP\_MJ\_PNP operation is an IRP-based operation.

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

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

[**IRP\_MJ\_PNP (WDK Kernel-Mode Driver Architecture Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550772)

[**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841)

[**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874)

[**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664)

[**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670)

[**IRP\_MN\_QUERY\_DEVICE\_TEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551674)

[**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679)

[**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687)

[**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727)

[**IRP\_MN\_SET\_LOCK**](https://msdn.microsoft.com/library/windows/hardware/ff551742)

[**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)

[**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769)

 

 






