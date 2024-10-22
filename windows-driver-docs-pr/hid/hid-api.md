---
title: HID Application Programming Interface (API)
description: Introduction to Human Interface Devices (HID) API.
ms.date: 06/26/2024
keywords:
- Human Interface Devices
- HID
- keyboards
- mice
- sensory data
- accelerometers
- gyroscope
---

# HID application programming interface (API)

There are three categories of HID APIs:

1. Device discovery and setup
1. Data movement
1. Report creation and interpretation

## Device discovery and setup

These HID APIs are used to identify the properties of a HID device and to establish communication with that device. Applications use these APIs to identify a top level collection.

- [HidD_GetAttributes](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getattributes)
- [HidD_GetHidGuid](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_gethidguid)
- [HidD_GetIndexedString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getindexedstring)
- [HidD_GetManufacturerString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getmanufacturerstring)
- [HidD_GetPhysicalDescriptor](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getphysicaldescriptor)
- [HidD_GetPreparsedData](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getpreparseddata)
- [HidD_GetProductString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getproductstring)
- [HidD_GetSerialNumberString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getserialnumberstring)
- [HidD_GetNumInputBuffers](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getnuminputbuffers)
- [HidD_SetNumInputBuffers](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setnuminputbuffers)

## Data movement

The following HID APIs are used to move data between an application and a selected device.

- [HidD_GetInputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getinputreport)
- [HidD_SetFeature](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setfeature)
- [HidD_SetOutputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setoutputreport)
- [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile)
- [WriteFile](/windows/win32/api/fileapi/nf-fileapi-writefile)

## Report creation and interpretation

Developers of custom hardware know the size and format of each report issued by their device. In this case, the application can cast the input and output report buffers as structs and consume the data.

Developers of HID applications intended to communicate with all devices that expose common functionality might not know the size and format of the HID reports. This category of application understands certain top level collections and certain usages.

To interpret the reports received from a device or to create reports to be sent the application must use the report descriptor to determine if and where a particular usage is located in the reports and the units of values in the reports. In these cases, HID parsing is required. Windows provides a HID parser for use by drivers and applications via APIs (HidP_*) that can be used to discover the types of usages supported by a device, determine the state of such usages in a report, or to build a report to change the state of a usage in the device.

Here's the list of HID parser APIs:

- [HidP_GetButtonArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getbuttonarray)
- [HidP_GetButtonCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getbuttoncaps)
- [HidP_GetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP_GetButtonsEx](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP_GetCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getcaps)
- [HidP_GetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getdata)
- [HidP_GetExtendedAttributes](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getextendedattributes)
- [HidP_GetLinkCollectionNodes](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getlinkcollectionnodes)
- [HidP_GetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)
- [HidP_GetSpecificButtonCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificbuttoncaps)
- [HidP_GetSpecificValueCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificvaluecaps)
- [HidP_GetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusages)
- [HidP_GetUsagesEx](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagesex)
- [HidP_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)
- [HidP_GetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)
- [HidP_GetValueCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getvaluecaps)
- [HidP_GetVersion](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getversion)
- [HidP_InitializeReportForID](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_initializereportforid)
- [HidP_MaxDataListLength](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxdatalistlength)
- [HidP_MaxUsageListLength](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxusagelistlength)
- [HidP_SetButtonArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setbuttonarray)
- [HidP_SetButtons](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setbuttons)
- [HidP_SetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setdata)
- [HidP_SetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setscaledusagevalue)
- [HidP_SetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages)
- [HidP_SetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)
- [HidP_SetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevaluearray)
- [HidP_TranslateUsagesToI8042ScanCodes](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_translateusagestoi8042scancodes)
- [HidP_UnsetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP_UnsetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages)
- [HidP_UsageAndPageListDifference](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_usageandpagelistdifference)
- [HidP_UsageListDifference](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_usagelistdifference)

## Related topics

- [hidpi.h header](/windows-hardware/drivers/ddi/hidpi/)
- [hidsdi.h header](/windows-hardware/drivers/ddi/hidsdi/)
