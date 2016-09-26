---
title: Sample Report Descriptor - Serial Reporting Mode (Windows 7)
description: Sample Report Descriptor - Serial Reporting Mode (Windows 7)
ms.assetid: 563ecefc-8a42-477e-97ce-710ed1c97b35
keywords: ["Windows Touch WDK , multitouch digitizer drivers, sample report descriptor (serial reporting mode)", "multitouch digitizer drivers WDK , sample report descriptor (serial reporting mode)", "serial report WDK Touch"]
---

# Sample Report Descriptor - Serial Reporting Mode (Windows 7)


The following example shows a sample report descriptor for serial reporting mode. It contains a top-level collection with a single embedded physical collection:

```
    0x05, 0x0d,                         // USAGE_PAGE (Digitizers)
    0x09, 0x04,                         // USAGE (Touch Screen)
    0xa1, 0x01,                         // COLLECTION (Application)
    0x85, REPORTID_MTOUCH,              //   REPORT_ID (Touch)
    0x09, 0x22,                         //   USAGE (Finger)
    0xa1, 0x00,                         //   COLLECTION (Physical)
    0x09, 0x42,                         //     USAGE (Tip Switch)
    0x15, 0x00,                         //     LOGICAL_MINIMUM (0)
    0x25, 0x01,                         //     LOGICAL_MAXIMUM (1)
    0x75, 0x01,                         //     REPORT_SIZE (1)
    0x95, 0x01,                         //     REPORT_COUNT (1)
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)
    0x95, 0x03,                         //     REPORT_COUNT (3)
    0x81, 0x03,                         //     INPUT (Cnst,Ary,Abs)
    0x09, 0x32,                         //     USAGE (In Range)
    0x09, 0x47,                         //     USAGE (Confidence)
    0x95, 0x02,                         //     REPORT_COUNT (2)
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)
    0x95, 0x0a,                         //     REPORT_COUNT (10)
    0x81, 0x03,                         //     INPUT (Cnst,Ary,Abs)
    0x05, 0x01,                         //     USAGE_PAGE (Generic Desk..
    0x26, 0xff, 0x7f,                   //     LOGICAL_MAXIMUM (32767)
    0x75, 0x10,                         //     REPORT_SIZE (16)
    0x95, 0x01,                         //     REPORT_COUNT (1)
    0x65, 0x00,                         //     UNIT (None)
    0x09, 0x30,                         //     USAGE (X)
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)
    0x09, 0x31,                         //     USAGE (Y)
    0x46, 0x00, 0x00,                   //     PHYSICAL_MAXIMUM (0)
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)
    0x05, 0x0d,                         //     USAGE PAGE (Digitizers)
    0x09, 0x48,                         //     USAGE (Width)
    0x09, 0x49,                         //     USAGE (Height)
    0x95, 0x01,                         //     REPORT_COUNT (2)
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)
    0x81, 0x03,                         //     INPUT (Cnst,Ary,Abs)
    0x09, 0x51,                         //     USAGE (Contact Identifier)
    0x75, 0x10,                         //     REPORT_SIZE (16) 
    0x95, 0x02,                         //     REPORT_COUNT (1)
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)
    0x09, 0x55,                         //    USAGE(Maximum Count)
    0x15, 0x00,                         //   LOGICAL_MINIMUM (0)
    0x25, 0x08,                         //   LOGICAL_MAXIMUM (255)
    0x75, 0x08,                         //   REPORT_SIZE (8)
    0x95, 0x01,                         //   REPORT_COUNT (1)
    0xb1, 0x02,                         //   FEATURE (Data,Var,Abs)
    0xc0,                               //   END_COLLECTION
    0xc0,                               // END_COLLECTION
```

 

 




