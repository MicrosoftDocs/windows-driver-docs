---
title: FLT_PARAMETERS for IRP_MJ_PNP union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_PNP.
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


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP\_MJ\_PNP**](irp-mj-pnp.md).

## Syntax

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

## Members

**Pnp**  
**StartDevice**  
Union component used for the IRP\_MN\_START\_DEVICE operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md).

**QueryDeviceRelations**  
Union component used for the IRP\_MN\_QUERY\_DEVICE\_RELATIONS operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](../kernel/irp-mn-query-device-relations.md).

**QueryInterface**  
Union component used for the IRP\_MN\_QUERY\_INTERFACE operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_INTERFACE**](../kernel/irp-mn-query-interface.md).

**DeviceCapabilities**  
Union component used for the IRP\_MN\_QUERY\_CAPABILITIES operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md).

**FilterResourceRequirements**  
Union component used for the IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md).

**ReadWriteConfig**  
Union component used for the IRP\_MN\_READ\_CONFIG and IRP\_MN\_WRITE\_CONFIG operations. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_READ\_CONFIG**](../kernel/irp-mn-read-config.md) and [**IRP\_MN\_WRITE\_CONFIG**](../kernel/irp-mn-write-config.md).

**SetLock**  
Union component used for the IRP\_MN\_SET\_LOCK operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_SET\_LOCK**](../kernel/irp-mn-set-lock.md).

**QueryId**  
Union component used for the IRP\_MN\_QUERY\_ID operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_ID**](../kernel/irp-mn-query-id.md).

**QueryDeviceText**  
Union component used for the IRP\_MN\_QUERY\_DEVICE\_TEXT operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_QUERY\_DEVICE\_TEXT**](../kernel/irp-mn-query-device-text.md).

**UsageNotification**  
Union component used for the IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION operation. For more information about the parameters for this operation, see the reference entry for [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](../kernel/irp-mn-device-usage-notification.md).

## Remarks

The [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP\_MJ\_PNP**](irp-mj-pnp.md) operations contains the parameters for an IRP-based Plug and Play (PnP) operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

The IRP\_MJ\_PNP operation is an IRP-based operation.

## Requirements

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


[**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

[**IRP\_MJ\_PNP (WDK Kernel-Mode Driver Architecture Reference)**](../kernel/irp-mj-pnp.md)

[**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](../kernel/irp-mn-device-usage-notification.md)

[**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md)

[**IRP\_MN\_QUERY\_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md)

[**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](../kernel/irp-mn-query-device-relations.md)

[**IRP\_MN\_QUERY\_DEVICE\_TEXT**](../kernel/irp-mn-query-device-text.md)

[**IRP\_MN\_QUERY\_ID**](../kernel/irp-mn-query-id.md)

[**IRP\_MN\_QUERY\_INTERFACE**](../kernel/irp-mn-query-interface.md)

[**IRP\_MN\_READ\_CONFIG**](../kernel/irp-mn-read-config.md)

[**IRP\_MN\_SET\_LOCK**](../kernel/irp-mn-set-lock.md)

[**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md)

[**IRP\_MN\_WRITE\_CONFIG**](../kernel/irp-mn-write-config.md)

 

