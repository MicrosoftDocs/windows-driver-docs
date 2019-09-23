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


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP\_MJ\_PNP**](irp-mj-pnp.md).

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
Union component used for the IRP\_MN\_START\_DEVICE operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_START\_DEVICE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-start-device).

**QueryDeviceRelations**  
Union component used for the IRP\_MN\_QUERY\_DEVICE\_RELATIONS operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-device-relations).

**QueryInterface**  
Union component used for the IRP\_MN\_QUERY\_INTERFACE operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_INTERFACE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-interface).

**DeviceCapabilities**  
Union component used for the IRP\_MN\_QUERY\_CAPABILITIES operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-capabilities).

**FilterResourceRequirements**  
Union component used for the IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-filter-resource-requirements).

**ReadWriteConfig**  
Union component used for the IRP\_MN\_READ\_CONFIG and IRP\_MN\_WRITE\_CONFIG operations. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_READ\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-read-config) and [**IRP\_MN\_WRITE\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-write-config).

**SetLock**  
Union component used for the IRP\_MN\_SET\_LOCK operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_SET\_LOCK**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-set-lock).

**QueryId**  
Union component used for the IRP\_MN\_QUERY\_ID operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_ID**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-id).

**QueryDeviceText**  
Union component used for the IRP\_MN\_QUERY\_DEVICE\_TEXT operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_DEVICE\_TEXT**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-device-text).

**UsageNotification**  
Union component used for the IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-device-usage-notification).

Remarks
-------

The [**FLT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP\_MJ\_PNP**](irp-mj-pnp.md) operations contains the parameters for an IRP-based Plug and Play (PnP) operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

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


[**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://docs.microsoft.com/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](https://docs.microsoft.com/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

[**IRP\_MJ\_PNP (WDK Kernel-Mode Driver Architecture Reference)**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-pnp)

[**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-device-usage-notification)

[**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-filter-resource-requirements)

[**IRP\_MN\_QUERY\_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-capabilities)

[**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-device-relations)

[**IRP\_MN\_QUERY\_DEVICE\_TEXT**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-device-text)

[**IRP\_MN\_QUERY\_ID**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-id)

[**IRP\_MN\_QUERY\_INTERFACE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-interface)

[**IRP\_MN\_READ\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-read-config)

[**IRP\_MN\_SET\_LOCK**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-set-lock)

[**IRP\_MN\_START\_DEVICE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-start-device)

[**IRP\_MN\_WRITE\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-write-config)

 

 






