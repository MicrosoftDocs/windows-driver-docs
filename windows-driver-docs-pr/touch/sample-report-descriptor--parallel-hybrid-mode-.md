---
title: Sample Report Descriptor - Parallel/Hybrid Mode (Windows 7)
description: Sample Report Descriptor - Parallel/Hybrid Mode (Windows 7)
ms.assetid: 0144c939-b713-43d0-9460-b84854d1ca5d
keywords: ["Windows Touch WDK , multitouch digitizer drivers, sample report descriptor (parallel/hybrid mode)", "multitouch digitizer drivers WDK , sample report descriptor (parallel/hybrid mode)", "parallel report WDK Touch", "hybrid report WDK Touch"]
---

# Sample Report Descriptor - Parallel/Hybrid Mode (Windows 7)


This sample descriptor can serve as a starting point for creating a parallel or hybrid report descriptor. The mode used depends on the relationship between the maximum count and the contact count.

A hybrid report contains a contact count that is greater than the number of contacts that fit into one packet. A parallel report contains all contact information in a single packet. For more information, see [Selecting Packet Reporting Modes in Multi-touch Drivers](selecting-packet-reporting-modes-in-multitouch-drivers.md).

This report descriptor has a top-level collection with two embedded logical collections. Each logical collection represents data that can be received from a single physical contact. Be aware that the contact count usage is not contained in either logical collection; instead, it follows as part of the top-level collection.

```
    0x05, 0x0d,                         // USAGE_PAGE (Digitizers)
    0x09, 0x04,                         // USAGE (Touch Screen)
    0xa1, 0x01,                         // COLLECTION (Application)
    0x85, REPORTID_PEN,                 //   REPORT_ID (Touch)
    0x09, 0x22,                         //   USAGE (Finger)
    0xa1, 0x02,                         //     COLLECTION (Logical)
    0x09, 0x42,                         //       USAGE (Tip Switch)
    0x15, 0x00,                         //       LOGICAL_MINIMUM (0)
    0x25, 0x01,                         //       LOGICAL_MAXIMUM (1)
    0x75, 0x01,                         //       REPORT_SIZE (1)
    0x95, 0x01,                         //       REPORT_COUNT (1)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x09, 0x32,                         //       USAGE (In Range)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x09, 0x47,                         //       USAGE (Confidence)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x95, 0x05,                         //       REPORT_COUNT (5)
    0x81, 0x03,                         //       INPUT (Cnst,Ary,Abs)
    0x75, 0x08,                         //       REPORT_SIZE (8)
    0x09, 0x51,                         //       USAGE (Contact Identifier)
    0x95, 0x01,                         //       REPORT_COUNT (1)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x05, 0x01,                         //       USAGE_PAGE (Generic Desk..
    0x26, 0xff, 0x7f,                   //       LOGICAL_MAXIMUM (32767)
    0x75, 0x10,                         //       REPORT_SIZE (16)
    0x55, 0x00,                         //       UNIT_EXPONENT (0)
    0x65, 0x00,                         //       UNIT (None)
    0x09, 0x30,                         //       USAGE (X)
    0x35, 0x00,                         //       PHYSICAL_MINIMUM (0)
    0x46, 0x00, 0x00,                   //       PHYSICAL_MAXIMUM (0)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x09, 0x31,                         //       USAGE (Y)
    0x46, 0x00, 0x00,                   //       PHYSICAL_MAXIMUM (0)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0xc0,                               //    END_COLLECTION
    0xa1, 0x02,                         //    COLLECTION (Logical)
    0x05, 0x0d,                         //     USAGE_PAGE (Digitizers)
    0x09, 0x42,                         //       USAGE (Tip Switch)
    0x15, 0x00,                         //       LOGICAL_MINIMUM (0)
    0x25, 0x01,                         //       LOGICAL_MAXIMUM (1)
    0x75, 0x01,                         //       REPORT_SIZE (1)
    0x95, 0x01,                         //       REPORT_COUNT (1)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x09, 0x32,                         //       USAGE (In Range)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x09, 0x47,                         //       USAGE (Confidence)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x95, 0x05,                         //       REPORT_COUNT (5)
    0x81, 0x03,                         //       INPUT (Cnst,Ary,Abs)
    0x75, 0x08,                         //       REPORT_SIZE (8)
    0x09, 0x51,                         //       USAGE (Contact Identifier)
    0x95, 0x01,                         //       REPORT_COUNT (1)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x05, 0x01,                         //       USAGE_PAGE (Generic Desk..
    0x26, 0xff, 0x7f,                   //       LOGICAL_MAXIMUM (32767)
    0x75, 0x10,                         //       REPORT_SIZE (16)
    0x55, 0x00,                         //       UNIT_EXPONENT (0)
    0x65, 0x00,                         //       UNIT (None)
    0x09, 0x30,                         //       USAGE (X)
    0x35, 0x00,                         //       PHYSICAL_MINIMUM (0)
    0x46, 0x00, 0x00,                   //       PHYSICAL_MAXIMUM (0)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0x09, 0x31,                         //       USAGE (Y)
    0x46, 0x00, 0x00,                   //       PHYSICAL_MAXIMUM (0)
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
    0xc0,                               //    END_COLLECTION
    0x05, 0x0d,                         //    USAGE_PAGE (Digitizers)
    0x09, 0x54,                         //    USAGE (Contact Count)
    0x95, 0x01,                         //    REPORT_COUNT (1)
    0x75, 0x08,                         //    REPORT_SIZE (8)
    0x15, 0x00,                         //    LOGICAL_MINIMUM (0)
    0x25, 0x08,                         //    LOGICAL_MAXIMUM (8)
    0x81, 0x02,                         //    INPUT (Data,Var,Abs)
    0x09, 0x55,                         //    USAGE(Contact Count Maximum)
    0xb1, 0x02,                         //    FEATURE (Data,Var,Abs)
    0xc0,                               // END_COLLECTION
```

 

 




