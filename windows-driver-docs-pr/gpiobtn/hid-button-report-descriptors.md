---
title: HID button report descriptors
author: windows-driver-content
description: This topic contains sample HID button report descriptors.
ms.assetid: FB1D482A-A147-4362-969F-7A37E5ECF0B4
---

# HID button report descriptors


This topic contains sample HID button report descriptors.

``` syntax
0x05, 0x01,                  // USAGE_PAGE (Generic Desktop)
0x09, 0x06,                 // USAGE (Keyboard)
0xa1, 0x01,                 // COLLECTION (Application)
0x85, REPORTID_KEYBOARD,      // REPORT_ID
0x05, 0x07,                 // USAGE_PAGE (Key Codes)
0x09, 0x4c,                 // USAGE (Del Key)
0x09, 0x69,                 // USAGE (F14 Key)
0x09, 0x6a,                 // USAGE (F15 Key)
0x09, 0xe0,                 // USAGE (Left Ctrl Key)
0x09, 0xe2,                 // USAGE (Left Alt Key)
0x09, 0xe3,                 // USAGE (Left Windows Key)
0x15, 0x00,                 // LOGICAL_MINIMUM (0)
0x25, 0x01,                 // LOGICAL_MAXIMUM (1)
0x75, 0x01,                 // REPORT_SIZE (1)
0x95, 0x06,                 // REPORT_COUNT (5)
0x81, 0x02,                 // INPUT (Data, Var, Abs)
0x95, 0x1a,                 // REPORT_COUNT (27)
0x81, 0x03,                 // INPUT (Cnst, Var, Abs)
0xc0,                          // END_COLLECTION
    
0x05, 0x0C,          // USAGE_PAGE (Consumer devices)
0x09, 0x01,          // USAGE (Consumer Control)
0xa1, 0x01,          // COLLECTION (Application)
0x85, REPORTID_VOLUME, // REPORT_ID
0x09, 0xe9,              // USAGE (Volume up)
0x09, 0xea,              // USAGE (Volume down)
0x15, 0x00,          // LOGICAL_MINIMUM (0)
0x25, 0x01,          // LOGICAL_MAXIMUM (1)
0x75, 0x01,              // REPORT_SIZE (1)
0x95, 0x02,              // REPORT_COUNT (2)
0x81, 0x02,              // INPUT (Data, Var, Abs)
0x95, 0x1e,              // REPORT_COUNT (30)
0x81, 0x03,          // INPUT (Cnst, Var, Abs)
0xc0,                   // END_COLLECTION
    
0x05, 0x01,             // USAGE_PAGE (Generic Desktop)
0x09, 0x80,             // USAGE (System Control)
0xa1, 0x01,             // COLLECTION (Application)
0x85, REPORTID_POWER, // REPORT_ID
0x09, 0x81,             // USAGE (System power down)
0x09, 0x83,             // USAGE (System wake up)
0x15, 0x00,             // LOGICAL_MINIMUM (0)
0x25, 0x01,             // LOGICAL_MAXIMUM (1)
0x75, 0x01,             // REPORT_SIZE (1)
0x95, 0x02,             // REPORT_COUNT (2)
0x81, 0x02,             // INPUT (Data,Var,Abs)
0x95, 0x1e,             // REPORT_COUNT (30)
0x81, 0x03,             // INPUT (Cnst,Var,Abs)
0xc0,           // END_COLLECTION
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20HID%20button%20report%20descriptors%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


