---
title: HID Application Programming Interface (API)
description: Introduction to Human Interface Devices (HID) API.
keywords:
- Human Interface Devices
- HID
- keyboards
- mice
- sensory data
- accelerometers
- gyroscope
ms.date: 02/28/2020
ms.localizationpriority: medium
---

# HID Application Programming Interface (API)

There are three categories of HID APIs: device discovery and setup, data movement, and report creation/interpretation.

## Device Discovery and Setup

These HID APIs are used to identify the properties of a HID device and to establish communication with that device. Applications use these APIs to identify a Top Level Collection.

- [HidD\_GetAttributes](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getattributes)
- [HidD\_GetHidGuid](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_gethidguid)
- [HidD\_GetIndexedString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getindexedstring)
- [HidD\_GetManufacturerString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getmanufacturerstring)
- [HidD\_GetPhysicalDescriptor](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getphysicaldescriptor)
- [HidD\_GetPreparsedData](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getpreparseddata)
- [HidD\_GetProductString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getproductstring)
- [HidD\_GetSerialNumberString](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getserialnumberstring)
- [HidD\_GetNumInputBuffers](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getnuminputbuffers)
- [HidD\_SetNumInputBuffers](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setnuminputbuffers)

## Data Movement

These HID APIs are used to move data between an application and a selected device.

- [HidD\_GetInputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getinputreport)
- [HidD\_SetFeature](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setfeature)
- [HidD\_SetOutputReport](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setoutputreport)
- [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile)
- [WriteFile](/windows/win32/api/fileapi/nf-fileapi-writefile)

## Report Creation and Interpretation

Developers of custom hardware know the size and format of each Report issued by their device. In this case the application can cast the input and output Report buffers to structs and consume the data.

Developers of HID applications intended to communicate with all devices that expose common functionality (for example a music application that must detect when a play button is pressed) may not know the size and format of the HID Reports. This category of application understands certain Top Level Collections and certain usages.

To interpret the Reports received from a device or to create Reports to be sent the application must leverage the Report Descriptor to determine if and where a particular Usage is located in the Reports and (potentially) the units of values in the Reports. In these cases HID parsing is required. Windows provides a HID parser for use by drivers and applications via APIs (HidP\_\*) that can be used to discover the types of usages supported by a device, determine the state of such usages in a Report, or to build a Report to change the state of a usage in the device.

These are the HID parser APIs.

- [HidP\_GetButtonCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getbuttoncaps)
- [HidP\_GetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP\_GetButtonsEx](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP\_GetCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getcaps)
- [HidP\_GetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getdata)
- [HidP\_GetExtendedAttributes](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getextendedattributes)
- [HidP\_GetLinkCollectionNodes](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getlinkcollectionnodes)
- [HidP\_GetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)
- [HidP\_GetSpecificButtonCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificbuttoncaps)
- [HidP\_GetSpecificValueCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificvaluecaps)
- [HidP\_GetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusages)
- [HidP\_GetUsagesEx](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagesex)
- [HidP\_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)
- [HidP\_GetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)
- [HidP\_GetValueCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getvaluecaps)
- [HidP\_InitializeReportForID](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_initializereportforid)
- [HidP\_IsSameUsageAndPage](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_usage_and_page)
- [HidP\_MaxDataListLength](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxdatalistlength)
- [HidP\_MaxUsageListLength](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxusagelistlength)
- [HidP\_SetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP\_SetData](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setdata)
- [HidP\_SetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setscaledusagevalue)
- [HidP\_SetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages)
- [HidP\_SetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)
- [HidP\_SetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevaluearray)
- [HidP\_UnsetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)
- [HidP\_UnsetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages)
- [HidP\_UsageAndPageListDifference](/previous-versions/windows/hardware/drivers/ff539824(v=vs.85))
- [HidP\_UsageListDifference](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_usagelistdifference)