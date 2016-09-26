---
title: Using Report Descriptors to Support Capability Discovery (Windows 7)
description: Using Report Descriptors to Support Capability Discovery (Windows 7)
ms.assetid: 5435d73c-8e18-477c-870f-859eae12fafe
keywords: ["Windows Touch WDK , capability discovery", "Windows Touch WDK , using report descriptors for capability discovery", "capability discovery WDK Touch", "capability discovery WDK Touch , using report descriptors", "report descriptors WDK Touch", "report descriptors WDK Touch , capability discovery"]
---

# Using Report Descriptors to Support Capability Discovery (Windows 7)


This section describes how vendors use the report descriptor to support capability discovery for touch and multi-touch devices.

### <span id="report_descriptor"></span><span id="REPORT_DESCRIPTOR"></span>Report Descriptor

A vendor-supplied driver reports its device capabilities to the operating system by providing a report descriptor. For a full example of a report descriptor, see the Elotouch.c file, which is part of the [EloMT](elotouch-driver.md) sample in the Windows Driver Kit (WDK).

For Windows 7 to detect a device's ability to support multiple inputs, the driver must include the [contact identifier usage](selecting-packet-reporting-modes-in-multitouch-drivers.md) (0x51) in the report descriptor. Be aware that in [Sample Report Descriptor (Serial Reporting Mode)](sample-report-descriptor--serial-reporting-mode-.md), this usage is in the single top-level physical collection, whereas in [Sample Report Descriptor (Parallel/Hybrid Mode)](sample-report-descriptor--parallel-hybrid-mode-.md), this usage appears one time in both the logical collections that describe the multiple inputs.

### <span id="feature_report_exclusivity"></span><span id="FEATURE_REPORT_EXCLUSIVITY"></span>Feature Report Exclusivity

In Windows 7, the system opens exclusively the configuration top-level collection that contains the device mode feature report. Because the operating system opens the feature report exclusively, the report is not accessible to third-party applications.

Because Windows 7 configures the device to report data by multiple input only, the top-level collection must support the required multi-touch usages. For information about required usages, see [Supporting Usages in Multi-touch Digitizer Drivers](supporting-usages-in-multitouch-digitizer-drivers.md).

In Windows XP and Windows Vista, third-party applications can use the feature report to select the currently active input mode, for example single touch or mouse-based input. We recommend single touch for Windows XP Tablet PC Edition and Windows Vista. We recommend the mouse for Windows XP and Microsoft Windows 2000.

### <span id="feature_report_requirements"></span><span id="FEATURE_REPORT_REQUIREMENTS"></span>Feature Report Requirements

The feature report must be in its own top-level collection and must include the multiple input configuration usages.

The following example shows a feature report from Elotouch.c:

```
    0x09, 0x0E,                         // USAGE (Device Configuration)
    0xa1, 0x01,                         // COLLECTION (Application)
    0x85, REPORTID_FEATURE,             //   REPORT_ID (Configuration)
    0x09, 0x23,                         //   USAGE (Device Settings)
    0xa1, 0x02,                         //   COLLECTION (logical)    
    0x09, 0x52,                         //    USAGE (Device Mode)         
    0x09, 0x53,                         //    USAGE (Device Identifier)
    0x15, 0x00,                         //    LOGICAL_MINIMUM (0)      
    0x25, 0x0a,                         //    LOGICAL_MAXIMUM (10)
    0x75, 0x08,                         //    REPORT_SIZE (8)         
    0x95, 0x02,                         //    REPORT_COUNT (2)         
    0xb1, 0x02,                         //   FEATURE (Data,Var,Abs    
    0xc0,                               //   END_COLLECTION
    0xc0,                               // END_COLLECTION
```

### <span id="device_mode"></span><span id="DEVICE_MODE"></span>Device Mode

The Device Mode usage (0x52) can have one of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Mode</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Mouse (recommended default)</p></td>
<td align="left"><p>0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>Single-input (single touch or stylus)</p></td>
<td align="left"><p>0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Multiple input</p></td>
<td align="left"><p>0x02</p></td>
</tr>
</tbody>
</table>

 

When single-input mode is set, vendors may do one of the following:

-   Send information about the first contact only. This can be implemented in the firmware or the device driver.

-   Drop all information about other contacts in the HID minidriver. This approach reduces the logic that is required in the firmware. However, it is available only to implementers who choose to write a device driver.

When mouse mode is set, the firmware or device driver should route the data from the first contact that was detected by using the mouse top-level collection.

Choose the appropriate default device mode for your device based on your device's capabilities and the operating system versions that it supports. To provide backward compatibility with earlier versions of Windows, we recommend mouse mode as the default. With the default set to mouse mode, the device can work with any operating system.

If you can guarantee that your device will not be used on any version of Windows earlier than Windows Vista, it is better to set default to single-input mode. Windows 7 reconfigures the device for multiple input if it discovers the capability.

### <span id="device_identifier"></span><span id="DEVICE_IDENTIFIER"></span>Device Identifier

Device Identifier (0x53) is a static value (SV) when it is part of a digitizer or mouse top-level collection. It is required when a report descriptor contains multiple digitizer top-level collections of the same kind. This usage uniquely identifies the digitizer top-level collection and should appear in the feature report.

If the device can function as a mouse, the mouse collection should have the same device identifier as the corresponding digitizer collection. Devices with only one digitizer top-level collection are not required to specify a device identifier usage.

When the usage is part of a device settings logical collection, it is a dynamic value (DV). In this scenario, the usage enables the host to select the device that it wants to configure. A value of zero indicates all collections. A nonzero value indicates the top-level collection with matching device identifier.

### <span id="touch_and_pen_support"></span><span id="TOUCH_AND_PEN_SUPPORT"></span>Touch and Pen Support

If your device includes a digitizer that provides both Windows Touch and pen functionality, you must report touch and pen collections separately. If your driver might be installed on a slate Tablet PC or other computer that has no mouse, you should also report a mouse collection.

 

 




