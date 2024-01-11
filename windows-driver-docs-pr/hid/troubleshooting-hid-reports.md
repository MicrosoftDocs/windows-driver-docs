---
title: Troubleshooting HID Reports
description: Describes the most common problems that user-mode applications and kernel-mode drivers might encounter when attempting to extract or set HID usages.
keywords:
- HID reports WDK , troubleshooting
- reports WDK HID , troubleshooting
- troubleshooting reports WDK HID
- dropped HID reports WDK
- errors WDK HID reports
ms.date: 01/11/2024
---

# Troubleshooting HID reports

This article describes the most common problems that user-mode applications and kernel-mode drivers might encounter when attempting to extract or set [HID usages](hid-usages.md).

## HID report ID errors

When an application or driver receives a HID report from a HID collection, it can be any report that the collection contains (because a collection can return reports in any order). The **HidP_Get***Xxx* routines return the following status values, which indicate report ID errors:

HIDP_STATUS_INCOMPATIBLE_REPORT_ID  
A requested usage is in a report supported by the HID collection, but not in the report that the application or driver specified.

HIDP_STATUS_USAGE_NOT_FOUND  
A requested usage is not in any report supported by the top-level collection.

For example, the following figure shows a HID collection that contains two reports.

:::image type="content" source="images/reportid.png" alt-text="Diagram illustrating an hid collection containing two reports.":::

Based on this example, assume an application or driver received a report from a collection and calls **[HidP_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)** to extract the current value of "Value X." If the report's ID is seven, the routine returns HIDP_STATUS_INCOMPATIBLE_REPORT_ID, which indicates that the device supports Value X, but that Value X is not present in the report. On the other hand, if the application or driver requests the value of "Value Z," the routine returns HIDP_STATUS_USAGE_NOT_FOUND, which indicates that Value Z is not in any report supported by the collection.

When an application or driver uses **HidP_Set***Xxx* routines to set usages in a report, the routines can also return the same two status values. The meaning of HIDP_STATUS_USAGE_NOT_FOUND is the same as with the **HidP_Get***Xxx* routines. However, the meaning of HIDP_STATUS_INCOMPATIBLE_REPORT_ID is different. This status value indicates that the report was previously configured with a report ID, and the usage specified by the caller does not belong to that report ID. Using the previous figure as an example, after an application or driver uses **[HidP_SetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages)** to set "Button 2" in a zero-initialized report, the report is configured with a report ID of seven. If the application or driver subsequently attempts to use **[HidP_SetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)** to set "Value X" in the same report, the routine will return HIDP_STATUS_INCOMPATIBLE_REPORT_ID.

If a **HidP_***Xxx* routine returns HIDP_STATUS_INCOMPATIBLE_REPORT_ID, the caller should take one of the following actions:

- If the caller is setting usages, it should allocate a new report of the correct length, zero-initialize it, and then call the routine again. The caller can send the report to the collection after successfully setting all usages in the report.

- If the caller is extracting usages, it should call the routine with a different report obtained from the collection.

### Dropped HID reports

When the [HID Client Drivers](hid-client-drivers.md) obtains input reports from a HID collection, the reports are stored in a ring buffer maintained by the HID class driver. This mechanism reduces the possibility that an application or driver will miss input reports that it requires.

By default, the HID class driver maintains an input report ring buffer that holds 32 reports. If a collection transmits data to the HID class driver faster than a user-mode application or kernel-mode driver retrieves it from the buffer, input reports are lost because of buffer overflow. To reduce the possibility of buffer overflow, an application or driver can reconfigure the size, in number of reports, of the buffer. Drivers retrieve and change the size of the buffer by using an **[IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_get_num_device_input_buffers)** request and an **[IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_set_num_device_input_buffers)** request. Applications do the same operation by calling **[HidD_GetNumInputBuffers](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getnuminputbuffers)** and **[HidD_SetNumInputBuffers](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setnuminputbuffers)**.
