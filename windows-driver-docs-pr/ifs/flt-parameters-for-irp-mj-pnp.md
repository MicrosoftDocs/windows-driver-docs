---
title: FLT_PARAMETERS for IRP_MJ_PNP union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_PNP.
keywords: ["FLT_PARAMETERS for IRP_MJ_PNP union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_PNP union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_PNP**](irp-mj-pnp.md).

## Syntax

``` C
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

- **StartDevice**: Union component used for the IRP_MN_START_DEVICE operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md).

- **QueryDeviceRelations**: Union component used for the IRP_MN_QUERY_DEVICE_RELATIONS operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_QUERY_DEVICE_RELATIONS**](../kernel/irp-mn-query-device-relations.md).

- **QueryInterface**: Union component used for the IRP_MN_QUERY_INTERFACE operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_QUERY_INTERFACE**](../kernel/irp-mn-query-interface.md).

- **DeviceCapabilities**: Union component used for the IRP_MN_QUERY_CAPABILITIES operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_QUERY_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md).

- **FilterResourceRequirements**: Union component used for the IRP_MN_FILTER_RESOURCE_REQUIREMENTS operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_FILTER_RESOURCE_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md).

- **ReadWriteConfig**: Union component used for the IRP_MN_READ_CONFIG and IRP_MN_WRITE_CONFIG operations. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_READ_CONFIG**](../kernel/irp-mn-read-config.md) and [**IRP_MN_WRITE_CONFIG**](../kernel/irp-mn-write-config.md).

- **SetLock**: Union component used for the IRP_MN_SET_LOCK operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_SET_LOCK**](../kernel/irp-mn-set-lock.md).

- **QueryId**: Union component used for the IRP_MN_QUERY_ID operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md).

- **QueryDeviceText**: Union component used for the IRP_MN_QUERY_DEVICE_TEXT operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_QUERY_DEVICE_TEXT**](../kernel/irp-mn-query-device-text.md).

- **UsageNotification**: Union component used for the IRP_MN_DEVICE_USAGE_NOTIFICATION operation. For more information about the parameters for this operation, see the reference entry for [**IRP_MN_DEVICE_USAGE_NOTIFICATION**](../kernel/irp-mn-device-usage-notification.md).

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_PNP**](irp-mj-pnp.md) operations contains the parameters for an IRP-based Plug and Play (PnP) operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

The IRP_MJ_PNP operation is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_PNP**](irp-mj-pnp.md)

[**IRP_MJ_PNP (WDK Kernel-Mode Driver Architecture Reference)**](../kernel/irp-mj-pnp.md)

[**IRP_MN_DEVICE_USAGE_NOTIFICATION**](../kernel/irp-mn-device-usage-notification.md)

[**IRP_MN_FILTER_RESOURCE_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md)

[**IRP_MN_QUERY_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md)

[**IRP_MN_QUERY_DEVICE_RELATIONS**](../kernel/irp-mn-query-device-relations.md)

[**IRP_MN_QUERY_DEVICE_TEXT**](../kernel/irp-mn-query-device-text.md)

[**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md)

[**IRP_MN_QUERY_INTERFACE**](../kernel/irp-mn-query-interface.md)

[**IRP_MN_READ_CONFIG**](../kernel/irp-mn-read-config.md)

[**IRP_MN_SET_LOCK**](../kernel/irp-mn-set-lock.md)

[**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md)

[**IRP_MN_WRITE_CONFIG**](../kernel/irp-mn-write-config.md)
