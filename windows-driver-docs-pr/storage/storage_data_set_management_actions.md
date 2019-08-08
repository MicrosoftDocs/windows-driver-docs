---
title: Storage Data Set Management (DSM) Actions
description: A data set management (DSM) action is a management action that a driver performs on the device's data-set attributes.
ms.assetid: cc64c7ad-7d1c-45c7-b236-a43e57086f8d
keywords: Storage Data Set Management Actions, Data Set Management Actions, DSM Actions
ms.localizationpriority: medium
ms.date: 07/31/2019
---

# Data Set Management (DSM) Actions

A data set management (DSM) action is a management action that a driver performs on the device's data-set attributes. DSM actions are defined by Microsoft. This functionality is available starting with Windows 7.

The management action is a DEVICE_DSM_ACTION constant that specifies the action to perform along with any action-specific flags. The following diagram shows the layout of the DEVICE_DSM_ACTION constant.

![DEVICE_DSM_ACTION Constant](../images/device_dsm_action_constant.jpg)

This constant is passed in the **Action** member of the [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure contained in the system buffer of an [IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ni-ntddstor-ioctl_storage_manage_data_set_attributes) request. If the action requires additional parameters, a parameter block will immediately follow the DEVICE_DSM_INPUT structure. Data set ranges, if any, will immediately follow the parameter block. The system buffer structure is shown in the following diagram.

![DSM IOCTL Input Buffer](../images/dsm_ioctl_inputbuffer.jpg)

Currently, the only defined action-specific flag is **DeviceDsmActionFlag_NonDestructive** (shown in the above figure). If a bitwise **OR** of the DEVICE_DSM_ACTION constant value and the **DeviceDsmActionFlag_NonDestructive** flag is performed, the specified action is nondestructive (no data will be altered). If this flag is set, the driver can safely forward the [IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ni-ntddstor-ioctl_storage_manage_data_set_attributes) request to the next lower driver in the stack even if the driver does not handle the specified action.

> [!NOTE]
> Before it forwards the [IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ni-ntddstor-ioctl_storage_manage_data_set_attributes) request, the driver still performs the normal processing of the block of data set ranges that are specified in the [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure. This block is located at **DataSetRangesOffset** and consists of one or more contiguous entries formatted as [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structures. The length, in bytes, of the data set ranges is set in the **DataSetRangesLength** member of DEVICE_DSM_INPUT.

The process flow of a DSM action is shown in the following diagram, where *Sender* is the action requestor and *Handler* processes the requested action (there can be more than one *Handler* in the stack):

![DSM Action Flow](../images/dsm_action_flow.jpg)

1) *Sender* allocates a [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure, initializes it with the action to be performed, and provides any additional action-specific information as needed in the parameter block and ranges block.
2) *Sender* sends an IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES request, passing the initialized input data in the IOCTL's *InputBuffer*.
3) *Handler* validates the input by calling [**DeviceDsmValidateInput**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/nf-ntddstor-devicedsmvalidateinput).
4) If the input is valid, *Handler* unpacks the input and handles the DSM action.
5) If the action requires output, *Handler* creates output and returns it.
6) *Sender* validates the output by calling [**DeviceDsmValidateOutput**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/nf-ntddstor-devicedsmvalidateoutput).
7) If the output is valid, *Sender* unpacks the output.

The following table lists all DEVICE_DSM_ACTION constants and describes the associated actions.

| DEVICE_DSM_ACTION Constant | Description |
| -------------------------- | ----------- |
| **DeviceDsmAction_None** (0) | For structure initialization purposes only. |
| **DeviceDsmAction_Trim** (1) | The driver will perform a trim operation. |
| **DeviceDsmAction_Notification** (2 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will perform a notification operation. For this action, the **ParameterBlockOffset** and **ParameterBlockLength** members of the [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure specify the parameters of the notification operation. These parameters are formatted as a [DEVICE_DSM_NOTIFICATION_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_dsm_notification_parameters) structure. Supported in Windows 7 and later versions of Windows. |
| **DeviceDsmAction_OffloadRead** (3 \| **DeviceDsmActionFlag_NonDestructive**) | The driver performs an offload read operation. For this action, the **ParameterBlockOffset** and **ParameterBlockLength** members of the [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure specify the parameters of the offload read operation. These parameters are formatted as a [DEVICE_DSM_OFFLOAD_READ_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_dsm_offload_read_parameters) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_OffloadWrite** (4) | The driver will perform an offload write operation. For this action, the **ParameterBlockOffset** and **ParameterBlockLength** members of the [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure specify the parameters of the offload write operation. These parameters are formatted as a [DEVICE_DSM_OFFLOAD_WRITE_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_dsm_offload_write_parameters) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_Allocation** (5 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will perform a logical block provisioning operation. The logical block range is specified in a single [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_Repair** (6 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will perform a storage spaces repair operation. The logical block range is specified in a single [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structure. The number of repair copies is specified in a DEVICE_DATA_SET_REPAIR_PARAMETERS structure located in the input buffer as specified by the **ParameterBlockOffset** member of the [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_Scrub** (7 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will perform a storage spaces scrub operation. The logical block range is specified in a single [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_DrtQuery** (8 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will perform a query for the logical block range specified and checks if it is included in storage spaces dirty range tracking. The synchronization status of the range is returned in the **OperationStatus** member of the [DEVICE_DSM_INPUT_OUTPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes_output) structure. The logical block range is specified, on input, in a single [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_DrtClear** (9 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will clear dirty range status for the for the logical block range specified. The logical block range is specified in a single [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_DrtDisable** (10 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will disable dirty range tracking for the logical block range specified. The logical block range is specified in a single [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structure. Supported in Windows 8 and later versions of Windows. |
| **DeviceDsmAction_TieringQuery** (11 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_Map** (12 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_RegenerateParity** (13 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_NvCache_Change_Priority** (14 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will change the caching priority of specified ranges of logical blocks. The new target priority is set in a [DEVICE_DSM_NVCACHE_CHANGE_PRIORITY_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_dsm_nvcache_change_priority_parameters) structure which is located at **ParameterBlockOffset** in [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes). The logical block ranges to change priority for are given in one or more [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structures. Supported in Windows 8.1 and later versions of Windows. |
| **DeviceDsmAction_NvCache_Evict** (15 \| **DeviceDsmActionFlag_NonDestructive**) | The driver will evict data from the caching medium. To evict all data, set the DEVICE_DSM_FLAG_ENTIRE_DATA_SET_RANGE flag in the **Flags** member of [DEVICE_DSM_INPUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_manage_data_set_attributes) and do not include any [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structures. Specific logical block ranges to evict are given in one or more [DEVICE_DATA_SET_RANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddstor/ns-ntddstor-_device_data_set_range) structures. The **DeviceDsmAction_NvCache_Evict** action is executed synchronously. No other actions are serviced until the evict action has either succeeded or failed. In order to limit its impact on applications using the device, each **DeviceDsmAction_NvCache_Evict** action issued should include relatively small data ranges. They should not exceed 10 MB and ideally be smaller than 2 MB. This will minimize the chance that user level applications will experience noticeable delays when accessing data on the device. Supported in Windows 8.1 and later versions of Windows. |
| **DeviceDsmAction_TopologyIdQuery** (16 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_GetPhysicalAddresses** (17 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_ScopeRegen** (18 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_ReportZones** (19 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_OpenZone** (20 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_FinishZone** (21 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_CloseZone** (22 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_ResetWritePointer** (23) |  |
| **DeviceDsmAction_GetRangeErrorInfo** (24 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_WriteZeroes** (25) |  |
| **DeviceDsmAction_LostQuery** (26 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_GetFreeSpace** (27 \| **DeviceDsmActionFlag_NonDestructive**) |  |
| **DeviceDsmAction_ConversionQuery** (28 \| **DeviceDsmActionFlag_NonDestructive**) |  |
