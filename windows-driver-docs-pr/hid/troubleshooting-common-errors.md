---
title: Troubleshooting common errors
author: windows-driver-content
description: This section covers common issues that hardware vendors and driver developers may encounter when debugging their I²C firmware or driver software.
ms.assetid: F53BD17C-ABBC-495F-895A-99BFC7E29B71
---

# Troubleshooting common errors


This section covers common issues that hardware vendors and driver developers may encounter when debugging their I²C firmware or driver software.

## Troubleshooting common errors


### <a href="" id="hidi2c-driver-does-not-load"></a>HIDI²C Driver Does not Load

If the I²C Controller driver loaded, but the device does not appear in the Windows Device Manager, refer to the following.

The above issue typically occurs if there's an invalid ASL code for the host or the device. To determine whether the problem was due to a failure to match the INF, refer to the setupapi.dev.log file. Another indicator that the problem is due to a mismatch is *Error Code 10* in Windows Device Manager.

To resolve this issue, ensure the following.

-   The \_CID value must be **PNP0C50**.
-   The I²C **controller** and **device characteristics** in the BIOS must be accurate.
-   The **HID descriptor address** (for the device) in the BIOS must be accurate.
-   The GPIO Interrupt must be correctly identified and marked as **Exclusive, Level, ActiveLow**.

Refer to section 13 of the HID I2C Protocol Spec for more detail. (This specification will be available at a later date.)

### Invalid report descriptor

If the host failed to retrieve the correct report descriptor from the device, ensure that the following are true.

1.  The enumeration sequence must finish running before the report descriptor is retrieved.
2.  The byte offsets 4 and 6 in the HID descriptor must be valid. (Pay particular attention to the length.)

If you verified that the correct report descriptor was retrieved from the device, but there still appears to be a related issue, ensure that the following are true.

1.  The wReportDescLength field is accurate.
2.  The HID Report is correctly formatted. (To verify this, test an alternative bus like USB.)

### FAQ

This section highlights questions frequently asked by hardware vendors and driver developers.

1.  Will the Windows 8 inbox HIDI²C driver work for HID devices connected over I²C?
    -   Yes, it will work provided the firmware is compliant with this HID I²C Protocol Specification

2.  What is the data structure communicated between devices (such as Keyboards) and OS drivers?
    -   The data structure would be in the form of an input report defined by a report descriptor, according to HID standard. The device itself rather than HIDI²C defines the input report structure. You simply report the keyboard usages as you would with a USB keyboard, and then provide the descriptor and corresponding INPUT reports as per the HID I²C Specification

3.  If multiple reports are being buffered at the same time, what should the device do?
    -   If multiple reports are being buffered, the device should keep the interrupt asserted until the last report has been read (acknowledged). As long as there is more data to report after a given read operation, the device should keep the line asserted using a level-trigger GPIO setting.

4.  Is it accurate to say that we should get the same DevicePath in the case of USB and I²C connectivity?
    -   No, the device path will NOT be identical between USB and I²C. The differences are minor but noteworthy. Please refer to the Hardware ID section in the Windows Driver Kit (WDK) for more details.

5.  What is the required I²C transfer limit in order for HIDI²C devices to leverage the Windows inbox HIDI²C driver?
    -   All I²C controllers are required to support transfers up to 4 KB. The maximum HID report descriptor length is 4 KB.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Troubleshooting%20common%20errors%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


