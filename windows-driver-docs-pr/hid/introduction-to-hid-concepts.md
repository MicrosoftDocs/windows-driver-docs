---
title: HID Application Programming Interface (API)
description: Introduction to Human Interface Devices (HID) API.
ms.assetid: 477FF911-5A17-4EA5-9403-1D7B4E8B3BA5
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

- [HidD\_GetAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getattributes)
- [HidD\_GetHidGuid](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_gethidguid)
- [HidD\_GetIndexedString](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getindexedstring)
- [HidD\_GetManufacturerString](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getmanufacturerstring)
- [HidD\_GetPhysicalDescriptor](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getphysicaldescriptor)
- [HidD\_GetPreparsedData](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getpreparseddata)
- [HidD\_GetProductString](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getproductstring)
- [HidD\_GetSerialNumberString](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getserialnumberstring)
- [HidD\_GetNumInputBuffers](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getnuminputbuffers)
- [HidD\_SetNumInputBuffers](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setnuminputbuffers)

## Data Movement

These HID APIs are used to move data between an application and a selected device.

- [HidD\_GetInputReport](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getinputreport)
- [HidD\_SetFeature](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setfeature)
- [HidD\_SetOutputReport](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_setoutputreport)
- [ReadFile](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-readfile)
- [WriteFile](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-writefile)

## Report Creation and Interpretation

Developers of custom hardware know the size and format of each Report issued by their device. In this case the application can cast the input and output Report buffers to structs and consume the data.

Developers of HID applications intended to communicate with all devices that expose common functionality (for example a music application that must detect when a play button is pressed) may not know the size and format of the HID Reports. This category of application understands certain Top Level Collections and certain usages.

To interpret the Reports received from a device or to create Reports to be sent the application must leverage the Report Descriptor to determine if and where a particular Usage is located in the Reports and (potentially) the units of values in the Reports. In these cases HID parsing is required. Windows provides a HID parser for use by drivers and applications via APIs (HidP\_\*) that can be used to discover the types of usages supported by a device, determine the state of such usages in a Report, or to build a Report to change the state of a usage in the device.

These are the HID parser APIs.

- [HidP\_GetButtonCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getbuttoncaps)
- [HidP\_GetButtons](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)
- [HidP\_GetButtonsEx](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)
- [HidP\_GetCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getcaps)
- [HidP\_GetData](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getdata)
- [HidP\_GetExtendedAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getextendedattributes)
- [HidP\_GetLinkCollectionNodes](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getlinkcollectionnodes)
- [HidP\_GetScaledUsageValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)
- [HidP\_GetSpecificButtonCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificbuttoncaps)
- [HidP\_GetSpecificValueCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificvaluecaps)
- [HidP\_GetUsages](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusages)
- [HidP\_GetUsagesEx](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagesex)
- [HidP\_GetUsageValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)
- [HidP\_GetUsageValueArray](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)
- [HidP\_GetValueCaps](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getvaluecaps)
- [HidP\_InitializeReportForID](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_initializereportforid)
- [HidP\_IsSameUsageAndPage](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_usage_and_page)
- [HidP\_MaxDataListLength](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxdatalistlength)
- [HidP\_MaxUsageListLength](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_maxusagelistlength)
- [HidP\_SetButtons](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)
- [HidP\_SetData](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setdata)
- [HidP\_SetScaledUsageValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setscaledusagevalue)
- [HidP\_SetUsages](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages)
- [HidP\_SetUsageValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)
- [HidP\_SetUsageValueArray](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevaluearray)
- [HidP\_UnsetButtons](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)
- [HidP\_UnsetUsages](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages)
- [HidP\_UsageAndPageListDifference](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff539824(v=vs.85))
- [HidP\_UsageListDifference](https://docs.microsoft.com/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_usagelistdifference)
