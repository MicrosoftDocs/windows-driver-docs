---
title: Supporting Usages in Digitizer Report Descriptors
description: Supporting Usages in Digitizer Report Descriptors
ms.assetid: FDB04122-FC8D-4B98-8C33-3DD6FB0F9940
---

# Supporting Usages in Digitizer Report Descriptors


A *Usage* is the name of a value, button, or collection in a HID report. The host makes use of the following usages when extracting data from a pen or touch device.

| Member     | Description                                                                                                        | Page      | ID   | Device     |
|------------|--------------------------------------------------------------------------------------------------------------------|-----------|------|------------|
| X          | X coordinate of the contact position.                                                                              | Desktop   | 0x30 | Pen, Touch |
| Y          | Y coordinate of the contact position.                                                                              | Desktop   | 0x31 | Pen, Touch |
| Tip        | Set if the finger or pen is on the surface of the digitizer.                                                       | Digitizer | 0x42 | Pen, Touch |
| In-range   | Set when the finger or pen is detected while hovering over the digitizer or in contact with the digitizer surface. | Digitizer | 0x32 | Pen, Touch |
| Confidence | Set when contact is a finger (not a palm or any other part of the hand that should not trigger finger input).      | Digitizer | 0x47 | Touch      |
| Width      | Width of contact.                                                                                                  | Digitizer | 0x48 | Touch      |
| Height     | Height of contact.                                                                                                 | Digitizer | 0x49 | Touch      |
| Scan Time  | Relative scan time.                                                                                                | Digitizer | 0x56 | Touch      |
| Pressure   | Amount of pressure the user is applying to the contact point.                                                      | Digitizer | 0x30 | Pen, Touch |
| Barrel     | Set if the button on the barrel of a stylus is pressed                                                             | Digitizer | 0x44 | Pen        |
| Azimuth    | The counter-clockwise rotation of the cursor about the Z-axis.                                                     | Digitizer | 0x3f | Pen, Touch |
| Invert     | Set when the opposite end of the pen is hovering over the digitizer.                                               | Digitizer | 0x3c | Pen        |
| Eraser     | Set when the opposite end of the pen is on the surface of the digitizer.                                           | Digitizer | 0x45 | Pen        |
| X Tilt     | The angle between the Y-Z plane and the plane containing the pointer device axis and the Y axis.                   | Digitizer | 0x3d | Pen        |
| Y Tilt     | The angle between the X-Z plane and the pointer device plane; a positive Y tilt is toward the user.                | Digitizer | 0x3e | Pen        |
| Twist      | Clockwise rotation of the cursor about its own axis.                                                               | Digitizer | 0x41 | Pen        |

 

**Note**  Usages listed in the table above are known to Windows and are delivered to applications using the WM\_POINTER message.

 

**Note**  Pointer devices are free to support additional usages (including vendor-specific usages). Additional usages are not delivered to applications in WM\_POINTER messages. The value of these usages can be retrieved by using the [**GetRawPointerDeviceData**](https://msdn.microsoft.com/library/windows/desktop/hh802887) function. In order to make the usages accessible from the **GetRawPointerDeviceData** function, the usages must be located in the same report as the X and Y usages.

 

### <span id="hid_descriptor"></span><span id="HID_DESCRIPTOR"></span>HID Descriptor for Digitizers

Starting with Windows 8, a touch digitizer must appear as a touch screen (page = 0x0D, usage = 0x04). A stylus digitizer must appear as an integrated pen (page = 0x0D, usage = 0x02) or an external pen (page = 0x0D, usage = 0x01). Integrated touch and pen devices are mapped to the display that they are physically connected to. External pen devices are mapped to the virtual desktop.

### <span id="required_hid_usages"></span><span id="REQUIRED_HID_USAGES"></span>Required HID Usages for Digitizers

The following usages are required for all digitizers. Devices that do not support all of the required usages will not work on Windows 8:

<span id="X_and_Y"></span><span id="x_and_y"></span><span id="X_AND_Y"></span>**X** and **Y**  
**X** and **Y** report the coordinates of contact. In Windows 8, a device can report two points for each contact. The first point (known as T) is considered the point that the user intended to touch while the second point (known as C) is considered the center of the contact. Devices that are capable of reporting T and C should have a usage array of two X values and two Y values. The values in the first position in the arrays are interpreted as the coordinates for T and the values in the second position are interpreted as the coordinates for C. (the report count for both usages is 2 to indicate the presence of a usage array). Devices that report C must also report the **Width** and **Height** usages. The host uses C to build the bounding rectangle around the contact. If the device only reports one X and Y pair, the host uses that pair for T and C. The sample touch descriptor includes usage arrays for both **X** and **Y**. The following extracts from the sample descriptor illustrate the difference between a device that supports only T and a device that supports T and C.

A device that reports only T must not have a usage array for the X and Y properties (that is, the report count for each usage is 1 as indicated in the following.)

``` syntax
0x05, 0x01,                         //       USAGE_PAGE (Generic Desk..
    0x26, 0xff, 0x0f,                   //       LOGICAL_MAXIMUM (4095)         
    0x75, 0x10,                         //       REPORT_SIZE (16)             
    0x55, 0x0e,                         //       UNIT_EXPONENT (-2)           
    0x65, 0x13,                         //       UNIT(Inch,EngLinear)                  
    0x09, 0x30,                         //       USAGE (X)                    
    0x35, 0x00,                         //       PHYSICAL_MINIMUM (0)         
    0x46, 0xb5, 0x04,                   //       PHYSICAL_MAXIMUM (1205)
    0x95, 0x01,                         //       REPORT_COUNT (1)         
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)         
    0x46, 0x8a, 0x03,                   //       PHYSICAL_MAXIMUM (906)
    0x09, 0x31,                         //       USAGE (Y)                    
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
```

A device that supports T and C uses usage arrays for reporting the X and Y values. The report count for both **X** and **Y** is 2.

``` syntax
0x05, 0x01,                         //       USAGE_PAGE (Generic Desk..
    0x26, 0xff, 0x0f,                   //       LOGICAL_MAXIMUM (4095)         
    0x75, 0x10,                         //       REPORT_SIZE (16)             
    0x55, 0x0e,                         //       UNIT_EXPONENT (-2)           
    0x65, 0x13,                         //       UNIT(Inch,EngLinear)                  
    0x09, 0x30,                         //       USAGE (X)                    
    0x35, 0x00,                         //       PHYSICAL_MINIMUM (0)         
    0x46, 0xb5, 0x04,                   //       PHYSICAL_MAXIMUM (1205)
    0x95, 0x02,                         //       REPORT_COUNT (2)         
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)         
    0x46, 0x8a, 0x03,                   //       PHYSICAL_MAXIMUM (906)
    0x09, 0x31,                         //       USAGE (Y)                    
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
```

**Note**  These examples take advantage of the HID rule that global items stay the same for every main item until they are changed. This allows both **X** and **Y** usages to share just one entry for the report count.

 

Pen devices should use the first example for their descriptors since C isn’t relevant for these devices.

The following global items must be specified for the **X** and **Y** usages:

-   Logical minimum
-   Logical maximum
-   Physical minimum
-   Physical maximum
-   Unit
-   Unit Exponent

The physical range for the device and the units must be accurately reported. If the information is inaccurate, the device will not work correctly. Devices must also report data within the logical range that is specified in the report descriptor. Any reported value outside this range will be considered as invalid data and the value will be changed to the nearest boundary value (logical minimum or logical maximum).

<span id="Tip"></span><span id="tip"></span><span id="TIP"></span>**Tip**  
Use the **Tip** switch to indicate finger or pen contact and lift-off from the digitizer surface. There should be a main item with a report size of 1. When delivering reports, the bit position should be set when the finger or pen is in contact with the digitizer surface. Otherwise, the bit should be cleared.

<span id="Scan_Time"></span><span id="scan_time"></span><span id="SCAN_TIME"></span>**Scan Time**  
**Scan Time** reports relative time in units of 100 microseconds. It represents the delta from the first frame that was reported after a device starts reporting data subsequent to a period of inactivity. The first scan time received is treated as a base time for subsequent reported times. The deltas between reported scan times should reflect the scanning frequency of the digitizer. It is important to note that unlike other usages, the host does not allow any flexibility for the unit for the scan time usage. The value is expected to roll over, as only 1 byte is allocated to the counter. The scan time value should be the same for all contacts within a frame. This requirement also applies to devices that report data using the hybrid mode

**Note**  This usage is only required for touch devices.

 

<span id="In-range"></span><span id="in-range"></span><span id="IN-RANGE"></span>**In-range**  
If the device supports Z-axis detection, the digitizer must set the **In-range** usage in the input report when the transducer is within the region where digitizing is possible. If the device does not support Z-axis detection, the driver should not include the **In-range** usage in its report descriptor.

Earlier versions of Windows have different guidelines for how touch digitizer drivers should handle in-range reporting.

Devices that support pen and touch should support NULL states for the **X** and **Y** usages in the top level collection for the pen. When the pen is detected at a height where the X and Y values cannot be accurately detected, the device should report NULL values for X and Y and set the **In-range** usage. NULL values simply mean values outside the specified logical range for these usages provided that the device has indicated that it supports NULL for the relevant usage. The device can then report accurate X and Y values once the stylus is close enough to the surface to make this possible. This protocol allows the host to implement palm rejection when the pen is in range.

It should be noted that the host will recognize the values outside the logical range as signifying the implementation of this protocol only if the report descriptor specifically includes the bit signifying the fact that X and Y support **NULL** states. Otherwise, values outside the logical range are simply moved to the nearest boundary value. The following extracts from report descriptors illustrate the difference between a device that supports **NULL** for X and Y and one that doesn’t. It should be noted that NULL support is only needed in the pen top level collection. Touch top level collections don’t need to support **NULL** for X and Y for this purpose.

Report extract with **NULL** support for X and Y:

``` syntax
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
```

Report extract without NULL support for X and Y:

``` syntax
0x05, 0x01,                         //       USAGE_PAGE (Generic Desk..
    0x26, 0xff, 0x0f,                   //       LOGICAL_MAXIMUM (4095)         
    0x75, 0x10,                         //       REPORT_SIZE (16)             
    0x55, 0x0e,                         //       UNIT_EXPONENT (-2)           
    0x65, 0x13,                         //       UNIT(Inch,EngLinear)                  
    0x09, 0x30,                         //       USAGE (X)                    
    0x35, 0x00,                         //       PHYSICAL_MINIMUM (0)         
    0x46, 0xb5, 0x04,                   //       PHYSICAL_MAXIMUM (1205)
    0x95, 0x01,                         //       REPORT_COUNT (1)         
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)         
    0x46, 0x8a, 0x03,                   //       PHYSICAL_MAXIMUM (906)
    0x09, 0x31,                         //       USAGE (Y)                    
    0x81, 0x02,                         //       INPUT (Data,Var,Abs)
```

See the Touch and Pen Support section for a full descriptor of a pen device that supports NULL values for **X** and **Y**.

**Note**  This usage is required for all pen devices but is optional for touch devices.

 

### <span id="optional_hid_usages"></span><span id="OPTIONAL_HID_USAGES"></span>Optional HID Usages

The following usages are optional, but you should implement them if the digitizer hardware supports them. Digitizers that do not support these usages should not include them in the report descriptor.

<span id="Width_and_Height"></span><span id="width_and_height"></span><span id="WIDTH_AND_HEIGHT"></span>**Width** and **Height**  
The **Width** and **Height** usages represent the width and height of the bounding box around the touch contact. The reported values should never be 0 except when an “UP” event is being reported, in which case they should be 0.

**Width** and **Height** are also exposed to application developers through the WM\_POINTER message.

<span id="Confidence"></span><span id="confidence"></span><span id="CONFIDENCE"></span>**Confidence**  
**Confidence** is a suggestion from the device about whether the touch contact was an intended or accidental touch. If you are confident that the touch is intended, then set the confidence usage to 1 (true). Your device should reject accidental touches as thoroughly as it can while the latency stays within the required range. If you are not certain that the touch is intended, and your device did not reject the touch as accidental, then set the confidence usage to 0 (false). If your device always rejects accidental touches, you do not need to include the confidence usage.

<span id="Pressure"></span><span id="pressure"></span><span id="PRESSURE"></span>**Pressure**  
**Pressure** is a measurement of the force that the finger or pen exerts against the digitizer surface. There are no restrictions on the range allowed for pressure. However, the range specified by a device will be normalized to a range of 0 – 1024 when delivering data to client applications.

<span id="Barrel"></span><span id="barrel"></span><span id="BARREL"></span>**Barrel**  
**Barrel** should be set when the pen barrel button is pressed. Otherwise, it should be reset. Barrel is used by Windows to modify the function of the tip for a primary action (tap, drag) or a secondary action (right tap, right drag).

Although **Pressure** and **Barrel** are optional usages, implementing them for pen digitizers is recommended. Additional value is added for these usages: pressure defines pen stroke width, making it more realistic, and the barrel switch allows right mouse button functionality when using the pen.

<span id="X_Tilt"></span><span id="x_tilt"></span><span id="X_TILT"></span>**X Tilt**  
**X Tilt** represents the plane angle between the Y-Z plane and the plane containing the transducer axis and the Y axis.

The physical range and logical range must be specified. The physical range must be -90 to 90. The logical range must be large enough to deliver data that is accurate to at least two decimal places. Radians can also be used for the physical range. The following list shows a typical logical and physical combination.

-   Logical minimum: -9000
-   Logical maximum: 9000
-   Unit: Degrees
-   Unit Exponent: -2
-   Physical minimum: -9000
-   Physical maximum: 9000

<span id="Y_Tilt"></span><span id="y_tilt"></span><span id="Y_TILT"></span>**Y Tilt**  
**Y Tilt** represents the plane angle between the X-Z plane and the plane containing the transducer X planes.

The physical range and logical range must be specified. The physical range must be between –90 to 90. The logical range must be large enough to deliver data that is accurate to at least two decimal places. Radians can also be used for the physical range. The following list shows a typical logical and physical combination.

-   Logical minimum: 0
-   Logical maximum: 18000
-   Unit: Degrees
-   Unit Exponent: -2
-   Physical minimum: -9000
-   Physical maximum: 9000

<span id="Twist"></span><span id="twist"></span><span id="TWIST"></span>**Twist**  
**Twist** specifies the clockwise rotation of the cursor around its own major axis.

The physical range and logical range must be specified. The physical range must be 0 to 360. The logical range must be large enough to deliver data that is accurate to at least two decimal places. Radians can also be used for the physical range. In this case, the logical range must be large enough to report values that are accurate to at least four decimal places. The following list shows a typical logical and physical combination.

-   Logical minimum: 0
-   Logical maximum: 62831
-   Unit: Radians
-   Unit exponent: -4
-   Physical minimum: 0
-   Physical maximum: 62831

<span id="Azimuth"></span><span id="azimuth"></span><span id="AZIMUTH"></span>**Azimuth**  
**Azimuth** specifies the counter-clockwise rotation of the cursor around the Z-axis through a full circular range. The physical range and logical range must be specified. The physical range must be 0 to 360 while the logical range must be large enough large enough to deliver data that is accurate to at least two decimal places. Radians can also be used for the physical range. In this case, the logical range must be large enough to report values that are accurate to at least 4 decimal places. The following list shows a typical logical and physical combination.

-   Logical minimum: 0
-   Logical maximum: 36000
-   Unit: Degrees
-   Unit Exponent: -2
-   Physical minimum: 0
-   Physical maximum: 36000

**Note**  The Unit Exponent must be -2 when Unit is Degrees and -4 when Unit is Radians.

 

 

 




