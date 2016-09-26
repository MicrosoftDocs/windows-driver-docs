---
title: Required HID Descriptors
description: This topic describes required Human Interface Devices (HID) descriptors for the Windows Precision Touchpad HID protocol implementation.
ms.assetid: 1B1AB370-2877-4BD8-96D4-E2591136207A
---

# Required HID Descriptors


This topic describes required Human Interface Devices (HID) descriptors for the Windows Precision Touchpad HID protocol implementation.

## <span id="Required_USB_HID_Descriptor"></span><span id="required_usb_hid_descriptor"></span><span id="REQUIRED_USB_HID_DESCRIPTOR"></span>Required USB HID Descriptor


The following table shows the required USB HID descriptor. For more information, see section 6.2.1 in [Device Class Definition for Human Interface Devices (HID) Version 1.11](http://www.usb.org/developers/hidpage/HID1_11.pdf).

**Table 1 USB HID Descriptor Members**

| Member            | Size in bytes | Description              |
|-------------------|---------------|--------------------------|
| bLength           | 1             | Size of the descriptor   |
| bDescriptorType   | 1             | Type of descriptor       |
| bcdHID            | 2             | HID version number       |
| bCountryCode      | 1             | Country code             |
| bNumDescriptors   | 1             | Number of descriptors    |
| bDescriptorType   | 1             | Descriptor type          |
| bDescriptorLength | 2             | Length of the descriptor |

 

## <span id="Required_I2C_HID_Descriptor"></span><span id="required_i2c_hid_descriptor"></span><span id="REQUIRED_I2C_HID_DESCRIPTOR"></span>Required I²C HID Descriptor


The following table shows the required I²C HID descriptor.

**Table 2 HID I2C Descriptor Members**

| Member              | Size in bytes | Description                                                                    |
|---------------------|---------------|--------------------------------------------------------------------------------|
| wHIDDescLength      | 2             | The length of the complete HID descriptor (in Bytes)                           |
| bcdVersion          | 2             | The version number, in binary coded decimal (BCD) format                       |
| wReportDescLength   | 2             | The length of the Report descriptor (in Bytes)                                 |
| wReportDescRegister | 2             | The register index containing the Report descriptor                            |
| wInputRegister      | 2             | The register number to read the input report (in unsigned Bytes)               |
| wMaxInputLength     | 2             | The length of the largest input report to be read from the input register      |
| wOutputRegister     | 2             | The register number to send the output (in unsigned Bytes)                     |
| wMaxOutputLength    | 2             | The length of the largest output report to be sent                             |
| wCommandRegister    | 2             | The register number to send command requests (in unsigned Bytes)               |
| wDataRegister       | 2             | The register number to exchange data with command requests (in unsigned Bytes) |
| wVendorID           | 2             | USB-IF assigned Vendor ID                                                      |
| wDeviceID           | 2             | Device ID                                                                      |
| wVersionID          | 2             | Firmware version number                                                        |

 

## <span id="Required_Device_Attributes"></span><span id="required_device_attributes"></span><span id="REQUIRED_DEVICE_ATTRIBUTES"></span>Required Device Attributes


The following HID properties must be provided in the device attributes. The reporting of these device attributes is bus specific. Consult the HID specific guidance for your choice of bus.

**Table 3 Required Device Attribute Members**

| Member     | Description             | USB                                | I²C                                         |
|------------|-------------------------|------------------------------------|---------------------------------------------|
| wVendorID  | Vendor ID               | idVendor in USB Device Descriptor  | wVendorID in I²C HID Descriptor (see above) |
| wProduct   | Product ID              | idProduct in USB Device Descriptor | wDeviceID in I²C HID Descriptor (see above) |
| wVersionID | Firmware version number | bcdDevice in USB Device Descriptor | wVersionID I²C HID Descriptor (see above)   |

 

 

 




