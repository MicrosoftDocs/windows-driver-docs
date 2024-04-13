---
title: Interpreting HID Reports
description: Interpreting HID Reports
keywords:
- HID reports WDK , interpreting
- reports WDK HID , interpreting
ms.date: 09/10/2020
---

# Interpreting HID Reports

This section describes how user-mode applications and kernel-mode drivers use the **HidP\_*Xxx*** [HIDClass support routines](/windows-hardware/drivers/ddi/_hid) to interpret control data in a HID report.

## Extracting Value Data by Specifying Its Usage

To extract value data from a HID report, an application or driver can use one of the following HID support routines:

- [HidP_GetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)
Returns a signed and scaled value.

- [HidP_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)
Returns a nonscaled value in an unsigned format or a scaled value that is out of its Normal range.

- [HidP_GetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)
Returns a usage value array.

To use **HidP_GetUsageValueArray** applications and drivers must allocate a zero-initialized buffer, which is large enough to hold the usage value array. The required size in bytes is the product of the **BitSize** and **ReportCount** members of the usage value array's [HIDP_VALUE_CAPS](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_value_caps) structure, rounded up to the nearest byte.

## Extracting Button Usages That Are Set to ON

To extract the HID usages of buttons that are set to ON (1), applications and drivers call one of the following HID support routines:

- [HidP_GetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions) (or [HidP_GetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusages))
Returns the usage ID of all buttons on a specified usage page that are set to ON.

- [HidP_GetButtonsEx](/windows-hardware/drivers/ddi/hidpi/#hidp_getbuttonsex) (or [HidP_GetUsagesEx](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagesex))
Returns the usage page and usage ID of all buttons that are set to ON.

These routines return an array of all usage information for all buttons that are currently set to ON. Implicitly, buttons whose usage is not returned by these routines are set to OFF (zero).

To call these routines, applications and drivers must first allocate and zero-initialize the buffer used to return the array of button usages. An application or driver calls [HidP_MaxUsageListLength](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxusagelistlength) to determine the number of button usages in a specified usage page in the report. If the application or driver specifies a usage page of zero, the routine returns the number of all the button usages in the report.

The required buffer size, in bytes, is the following:

- (For [HidP_GetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)) The value returned by **HidP_MaxUsageListLength** times sizeof(USAGE)

- (For [HidP_GetButtonsEx](/windows-hardware/drivers/ddi/hidpi/#hidp_getbuttonsex)) The value returned by **HidP_MaxUsageListLength** times sizeof(USAGE_AND_PAGE)

After an application or driver has used these routines to obtain information about which buttons are currently set to ON, it can determine the difference between the current state and the previous state of the buttons by calling one of the following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines). These routines return the difference between two arrays of usage information:

- [HidP_UsageListDifference](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_usagelistdifference)

- [HidP_UsageAndPageListDifference](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_usageandpagelistdifference)

## Extracting and Setting Control Data by Data Indices

To use data indices to extract and set control data in a HID report, an application or driver can use the following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines):

- [HidP_GetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getdata)

- [HidP_SetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setdata)

These routines are particularly useful to an application or driver that provides a "value-added" service. For example, one that provides a custom interface to all the controls supported by a HIDClass device. Microsoft DirectInput is one example.

By calling these routines, an application or driver can most efficiently obtain and set all values in a report. For example, to obtain all value data by their [HID usages](./hid-usages.md) it has to call [HidP_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue) for each usage. However, to obtain all value data by data index, it only has to call **HidP_GetData** once.

An application or driver uses the data indices specified in a collection's [Button Capability Arrays](./button-capability-arrays.md) and [Value Capability Arrays](./value-capability-arrays.md) to identify HID usages.

## Setting Value Data by Specifying Its Usage

An application or driver can set a value in a properly-initialized HID report by calling one of the following HID support routines:

- [HidP_SetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setscaledusagevalue)
Sets a signed and scaled value in a report.

- [HidP_SetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)
Sets a value in a report.

- [HidP_SetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevaluearray)
Sets a usage value array in a report.

## Setting Button State by Specifying Its Usage

An application or driver can set the state of buttons in a properly-initialized HID report by calling one of the following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines):

- [HidP_SetButtons](/windows-hardware/drivers/ddi/hidpi/#hidp_setbuttons) (or [HidP_SetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages))
Sets a specified set of buttons to ON (1).

- [HidP_UnsetButtons](/windows-hardware/drivers/ddi/hidpi/#hidp_unsetbuttons) (or [HidP_UnsetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages))
Sets a specified set of buttons to OFF (zero).

## Extracting and Setting HID Control Data by Data Indices

To use data indices to extract and set control data in a HID report, an application or driver can use the following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines):

- [HidP_GetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getdata)

- [HidP_SetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setdata)

These routines are particularly useful to an application or driver that provides a "value-added" service. For example, one that provides a custom interface to all the controls supported by a HIDClass device. Microsoft DirectInput is one example.

By calling these routines, an application or driver can most efficiently obtain and set all values in a report. For example, to obtain all value data by their HID usages, it has to call [HidP_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue) for each usage. However, to obtain all value data by data index, it only has to call **HidP_GetData** once.

An application or driver uses the data indices specified in a collection's [Button Capability Arrays](./button-capability-arrays.md) and [Value Capability Arrays](./value-capability-arrays.md) to identify HID usages.

## See also

[Initializing HID Reports](initializing-hid-reports.md)
