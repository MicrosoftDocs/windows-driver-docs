---
title: Touch and Pen Support
description: Touch and Pen Support
ms.assetid: 184B8A9C-C9DB-42CC-B819-877BDE6E3BC1
---

# Touch and Pen Support


If your device includes a digitizer that provides both touch and pen functionality, you must report touch and pen collections separately. If your digitizer might be installed on a slate, tablet PC or other computer that has no mouse, you should also report a mouse collection.

### <span id="reporting_null_values"></span><span id="REPORTING_NULL_VALUES"></span>Reporting Null Values

To facilitate palm rejection, the pen device should report data at a vertical distance higher than it normally would. It is highly recommended that this distance be 50 mm (or as close to this as possible), as this produces a better user experience. This will allow the host to handle touch input differently when it’s aware that the pen is in range. Since most devices that are able to detect the pen at a higher vertical distance won’t be able to accurately detect the coordinates of the pen, NULL coordinates should be reported by the device. The report descriptor below shows how NULL values can be supported for X and Y. When delivering NULL data, the device simply needs to set values that are outside the specified logical range for X and Y. Both values must be NULL for the host to recognize this reporting mode.

``` syntax
0x05, 0x0d,                         // USAGE_PAGE (Digitizers)          0
    0x09, 0x02,                         // USAGE (Pen)                      2
    0xa1, 0x01,                         // COLLECTION (Application)         4
    0x85, 0x02,                         //   REPORT_ID (Pen)                6
    0x09, 0x20,                         //   USAGE (Stylus)                 8
    0xa1, 0x00,                         //   COLLECTION (Physical)          10
    0x09, 0x42,                         //     USAGE (Tip Switch)           12
    0x09, 0x44,                         //     USAGE (Barrel Switch)        14
    0x09, 0x3c,                         //     USAGE (Invert)               16
    0x09, 0x45,                         //     USAGE (Eraser Switch)        18
    0x15, 0x00,                         //     LOGICAL_MINIMUM (0)          20
    0x25, 0x01,                         //     LOGICAL_MAXIMUM (1)          22
    0x75, 0x01,                         //     REPORT_SIZE (1)              24
    0x95, 0x04,                         //     REPORT_COUNT (4)             26
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)         28
    0x95, 0x01,                         //     REPORT_COUNT (1)             30
    0x81, 0x03,                         //     INPUT (Cnst,Var,Abs)         32
    0x09, 0x32,                         //     USAGE (In Range)             34
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)         36
    0x95, 0x02,                         //     REPORT_COUNT (2)             38
    0x81, 0x03,                         //     INPUT (Cnst,Var,Abs)         40
    0x05, 0x01,                         //     USAGE_PAGE (Generic Desktop) 42
    0x09, 0x30,                         //     USAGE (X)                    44
    0x75, 0x10,                         //     REPORT_SIZE (16)             46
    0x95, 0x01,                         //     REPORT_COUNT (1)             48
    0xa4,                               //     PUSH                         50
    0x55, 0x0d,                         //     UNIT_EXPONENT (-3)           51
    0x65, 0x13,                         //     UNIT (Inch,EngLinear)        53
    0x35, 0x00,                         //     PHYSICAL_MINIMUM (0)         55
    0x46, 0x3a, 0x20,                   //     PHYSICAL_MAXIMUM (8250)      57
    0x26, 0xf8, 0x52,                   //     LOGICAL_MAXIMUM (21240)      60
    0x81, 0x42,                         //     INPUT (Data,Var,Abs)         63
    0x09, 0x31,                         //     USAGE (Y)                    65
    0x46, 0x2c, 0x18,                   //     PHYSICAL_MAXIMUM (6188)      67
    0x26, 0x6c, 0x3e,                   //     LOGICAL_MAXIMUM (15980)      70
    0x81, 0x42,                         //     INPUT (Data,Var,Abs)         73
    0xb4,                               //     POP                          75
    0x05, 0x0d,                         //     USAGE_PAGE (Digitizers)      76
    0x09, 0x30,                         //     USAGE (Tip Pressure)         78
    0x26, 0xff, 0x00,                   //     LOGICAL_MAXIMUM (255)        80
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)         83
    0x75, 0x08,                         //     REPORT_SIZE (8)              85
    0x09, 0x3d,                         //     USAGE (X Tilt)               87
    0x65, 0x14,                         //     UNIT (Degrees,EngRotation)        
    0x55, 0x0e,                         //     UNIT_EXPONENT (-2)
    0x36, 0xd8, 0xdc,                   //     PHYSICAL_MINIMUM (-9000)         
    0x46, 0x28, 0x23,                   //     PHYSICAL_MAXIMUM (9000)      
    0x16, 0xd8, 0xdc,                   //     LOGICAL_MINIMUM (-9000)      
    0x26, 0x28, 0x23,                   //     LOGICAL_MAXIMUM (9000)        
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)         
    0x09, 0x3e,                         //     USAGE (Y Tilt)               
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)         
    0x55, 0x0e,                         //     UNIT_EXPONENT (-2)
    0x35, 0x00,                         //     PHYSICAL_MINIMUM (0)         
    0x47, 0xa0, 0x8c, 0x00, 0x00,       //     PHYSICAL_MAXIMUM (36000)      
    0x15, 0x00,                         //     LOGICAL_MINIMUM (0)      
    0x27, 0xa0, 0x8c, 0x00, 0x00,       //     LOGICAL_MAXIMUM (36000)        
    0x09, 0x41,                         //     USAGE (Twist)               
    0x81, 0x02,                         //     INPUT (Data,Var,Abs)  
    0xc0,                               //   END_COLLECTION                
    0xc0,                               // END_COLLECTION                   
```

### <span id="touch_hardware_qa"></span><span id="TOUCH_HARDWARE_QA"></span>Touch Hardware Quality Assurance

When a device passes the logo requirements, Microsoft will issue a cryptographically signed binary blob to the device’s manufacturer. The manufacturer will place this blob into the device’s firmware prior to production. Within Windows, when a touch device attempts to connect, the signature will be verified.

The blob itself will consist of 256 bytes of binary data, and should be reported as illustrated by the highlighted lines in the HID descriptor below. Device manufacturers should be sure that prior to issuance of the signed binary blob from Microsoft that the sample blob provided below is presented to Windows instead.

``` syntax
0x06, 0x00, 0xff,                   //     USAGE_PAGE (Vendor Defined)  
    0x09, 0xC5,                         //     USAGE (Vendor Usage 0xC5)    
    0x15, 0x00,                         //     LOGICAL_MINIMUM (0)          
    0x26, 0xff, 0x00,                   //     LOGICAL_MAXIMUM (0xff) 
    0x75, 0x08,                         //     REPORT_SIZE (8)             
    0x96, 0x00, 0x01,                   //     REPORT_COUNT (0x100 (256))             
    0xb1, 0x02,                         //     FEATURE (Data,Var,Abs)
```

The following is the sample blob in clear text.

``` syntax
0xfc, 0x28, 0xfe, 0x84, 0x40, 0xcb, 0x9a, 0x87, 0x0d, 0xbe, 0x57, 0x3c, 0xb6, 0x70, 0x09, 0x88,
0x07, 0x97, 0x2d, 0x2b, 0xe3, 0x38, 0x34, 0xb6, 0x6c, 0xed, 0xb0, 0xf7, 0xe5, 0x9c, 0xf6, 0xc2,
0x2e, 0x84, 0x1b, 0xe8, 0xb4, 0x51, 0x78, 0x43, 0x1f, 0x28, 0x4b, 0x7c, 0x2d, 0x53, 0xaf, 0xfc,
0x47, 0x70, 0x1b, 0x59, 0x6f, 0x74, 0x43, 0xc4, 0xf3, 0x47, 0x18, 0x53, 0x1a, 0xa2, 0xa1, 0x71,
0xc7, 0x95, 0x0e, 0x31, 0x55, 0x21, 0xd3, 0xb5, 0x1e, 0xe9, 0x0c, 0xba, 0xec, 0xb8, 0x89, 0x19,
0x3e, 0xb3, 0xaf, 0x75, 0x81, 0x9d, 0x53, 0xb9, 0x41, 0x57, 0xf4, 0x6d, 0x39, 0x25, 0x29, 0x7c,
0x87, 0xd9, 0xb4, 0x98, 0x45, 0x7d, 0xa7, 0x26, 0x9c, 0x65, 0x3b, 0x85, 0x68, 0x89, 0xd7, 0x3b,
0xbd, 0xff, 0x14, 0x67, 0xf2, 0x2b, 0xf0, 0x2a, 0x41, 0x54, 0xf0, 0xfd, 0x2c, 0x66, 0x7c, 0xf8,
0xc0, 0x8f, 0x33, 0x13, 0x03, 0xf1, 0xd3, 0xc1, 0x0b, 0x89, 0xd9, 0x1b, 0x62, 0xcd, 0x51, 0xb7,
0x80, 0xb8, 0xaf, 0x3a, 0x10, 0xc1, 0x8a, 0x5b, 0xe8, 0x8a, 0x56, 0xf0, 0x8c, 0xaa, 0xfa, 0x35,
0xe9, 0x42, 0xc4, 0xd8, 0x55, 0xc3, 0x38, 0xcc, 0x2b, 0x53, 0x5c, 0x69, 0x52, 0xd5, 0xc8, 0x73,
0x02, 0x38, 0x7c, 0x73, 0xb6, 0x41, 0xe7, 0xff, 0x05, 0xd8, 0x2b, 0x79, 0x9a, 0xe2, 0x34, 0x60,
0x8f, 0xa3, 0x32, 0x1f, 0x09, 0x78, 0x62, 0xbc, 0x80, 0xe3, 0x0f, 0xbd, 0x65, 0x20, 0x08, 0x13,
0xc1, 0xe2, 0xee, 0x53, 0x2d, 0x86, 0x7e, 0xa7, 0x5a, 0xc5, 0xd3, 0x7d, 0x98, 0xbe, 0x31, 0x48,
0x1f, 0xfb, 0xda, 0xaf, 0xa2, 0xa8, 0x6a, 0x89, 0xd6, 0xbf, 0xf2, 0xd3, 0x32, 0x2a, 0x9a, 0xe4,
0xcf, 0x17, 0xb7, 0xb8, 0xf4, 0xe1, 0x33, 0x08, 0x24, 0x8b, 0xc4, 0x43, 0xa5, 0xe5, 0x24, 0xc2
```

A complete report descriptor example with the feature report containing the certification blob is shown in [Single Finger Hybrid Mode Report Descriptor](single-finger-hybrid-mode-report-descriptor.md).

 

 




