Windows 10 - UVC Camera Implementation Guide

Windows USB Video Class driver
==============================

Windows 10 provides an inbox driver for devices compliant with USB Video Class Specification (versions 1.0 to 1.5). This driver supports color and sensor type cameras. This document outlines how to expose certain capabilities of a USB Video Class compliant camera to the applications through the inbox driver.

Glossary
========

| Keyword              | Description                                                        |
|----------------------|--------------------------------------------------------------------|
| UVC                  | USB Video Class                                                    |
| UVC driver           | USBVideo.sys driver that ships with the OS                         |
| IR                   | Infra-Red                                                          |
| Color Camera         | The camera that outputs color streams. E.g. RGB or YUV camera      |
| Sensor Camera        | The camera that outputs non-color streams. E.g. IR or Depth camera |
| BOS                  | Binary Device Object Store                                         |
| MS OS 2.0 Descriptor | Microsoft platform specific BOS device capability descriptor       |

Sensor Cameras 
===============

Windows supports two categories of cameras. One is a color camera and the other one is non-color (a.k.a sensor cameras) category. RGB or YUV cameras are categorized as color cameras and non-color cameras like gray scale, IR and Depth cameras are categorized as sensor cameras. The UVC driver supports both types of cameras. We recommend the camera firmware specify a value based on which the UVC driver would register the camera under one or both supported categories.

A camera that supports color only format types should be registered under KSCATEGORY\_VIDEO\_CAMERA. A camera that supports IR or Depth only format types should be registered under KSCATEGOYR\_SENSOR\_CAMERA. A camera that supports both color and non-color format types should be registered under KSCATEGORY\_VIDEO\_CAMERA and KSCATEOGYR\_SENSOR\_CAMERA. This categorization helps applications to select the camera that they want to work with.

A UVC camera can specify its category preference through attributes, “*SensorCameraMode*” and *“SkipCameraEnumeration”*, in its BOS [MS OS 2.0 Descriptor](https://msdn.microsoft.com/en-us/library/windows/hardware/dn385747.aspx) detailed in following sections.

The attribute “*SensorCameraMode*” takes either a value 1 or 2.

A value of 1, will register the device under KSCATEGORY\_SENSOR\_CAMERA. In addition to this specify a value of 1 for *“SkipCameraEnumeration”* to make the camera available to applications looking only for sensor cameras. A camera that exposes only sensor camera media types should use this value.

A value of 2 for “*SensorCameraMode*”, will register the device under KSCATEGORY\_SENSOR\_CAMERA & KSCATEGORY\_VIDEO\_CAMERA. This will make the camera available for applications looking for either sensor and color cameras. A camera that exposes both sensor camera and color camera media types should use this value.

We recommend you specify the above-mentioned registry value using the BOS descriptor. Please refer the Appendix A for a sample BOS descriptor with PLATFORM specific MS OS 2.0 descriptor.

Note:

*If you cannot update the device firmware as mentioned above, you could use a custom INF and specify that your camera need to be registered as a sensor camera by specifying a value for SensorCameraMode and SkipCameraEnumeration as follows:*

*The custom INF file (based on the inbox UVC driver) shall include the following AddReg entry:*

SensorCameraMode: REG\_DWORD: 1 // to register as sensor camera

SkipCameraEnumeration: REG\_DWORD: 1 // make it available only for IR applications

> *An example for the custom INF section would be as follows:*
>
> *\[USBVideo.NT.HW\] *
>
> *AddReg=USBVideo.HW.AddReg*
>
> *\[USBVideo.HW.AddReg\]*
>
> *HKR,, SensorCameraMode, 0x00010001,1 ;places the value under device HW*
>
> *;Registry key *
>
> *HKR,, SkipCameraEnumeration, 0x00010001,1 ;This makes the camera available*
>
> *;only for application looking for*
>
> *;IR cameras*

*If the SensorCameraMode and SkipCameraEnumeration attributes are not specified in the firmware or in the INF then, the camera will be registered as a color camera and will be visible only to color camera aware applications. *

IR stream 
==========

Windows inbox USB Video Class driver supports cameras that capture the scene in YUV format and transmit the pixel data over USB as uncompressed YUV or as compressed MJPEG frames. Following are the format type GUIDs that should be specified in the stream’s video format descriptor:

Defined in, ddk header file ksmedia.h

KSDATAFORMAT\_SUBTYPE\_L8\_IR – uncompressed 8 bit luma plane. This type maps to [MFVideoFormat\_L8](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370819(v=vs.85).aspx).

KSDATAFORMAT\_SUBTYPE\_L16\_IR – uncompressed 16 bit luma plane.

This type maps to [MFVideoFormat\_L16](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370819(v=vs.85).aspx).

KSDATAFORMAT\_SUBTYPE\_MJPG\_IR – compressed MJPEG frames. Media

Foundation converts this into NV12

uncompressed frames and uses only the

luma plane.

When these format type GUIDs are specified in the guidFormat field of the frame descriptor, the Media Foundation capture pipeline marks the stream as IR stream. Applications written with Media Foundation FrameReader API will be able to consume the IR stream. No scaling or conversions of the IR frames are supported by the pipeline for IR streams.

*Note: A stream exposing IR format types shall not expose RGB or Depth format types. *

// e.g. Format Descriptor for UVC 1.1 frame based format

typedef struct \_VIDEO\_FORMAT\_FRAME

{

UCHAR bLength;

UCHAR bDescriptorType;

UCHAR bDescriptorSubtype;

UCHAR bFormatIndex;

UCHAR bNumFrameDescriptors;

GUID guidFormat; // this field should contain the IR subtype GUID

UCHAR bBitsPerPixel;

UCHAR bDefaultFrameIndex;

UCHAR bAspectRatioX;

UCHAR bAspectRatioY;

UCHAR bmInterlaceFlags;

UCHAR bCopyProtect;

UCHAR bVariableSize;

} VIDEO\_FORMAT\_FRAME, \*PVIDEO\_FORMAT\_FRAME;

*Note: IR streams would show up as regular capture stream in DShow. *

Depth stream
============

Windows inbox USB Video Class driver supports cameras that produce Depth streams. These cameras capture the depth information (e.g. time of flight) of the scene and transmit the depth map as uncompressed YUV frames over USB. Following are the format type GUIDs that should be specified in the stream’s video format descriptor:

Defined in, ddk header file ksmedia.h

KSDATAFORMAT\_SUBTYPE\_D16 – 16 bit depth map values. Identical to

[MFVideoFormat\_D16](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370819(v=vs.85).aspx).

- The values are in millimeters

When the format type GUID is specified in the guidFormat member of the frame descriptor, the Media Foundation capture pipeline marks the stream as depth stream. Applications written with FrameReader API will be able to consume the depth stream. No scaling or conversions of the depth frames are supported by the pipeline for depth streams.

*Note: A stream exposing Depth format types shall not expose RGB or IR format types.*

// e.g. Format Descriptor for UVC 1.1 frame based format

typedef struct \_VIDEO\_FORMAT\_FRAME

{

UCHAR bLength;

UCHAR bDescriptorType;

UCHAR bDescriptorSubtype;

UCHAR bFormatIndex;

UCHAR bNumFrameDescriptors;

GUID guidFormat;// this field should contain the Depth subtype GUID

UCHAR bBitsPerPixel;

UCHAR bDefaultFrameIndex;

UCHAR bAspectRatioX;

UCHAR bAspectRatioY;

UCHAR bmInterlaceFlags;

UCHAR bCopyProtect;

UCHAR bVariableSize;

} VIDEO\_FORMAT\_FRAME, \*PVIDEO\_FORMAT\_FRAME;

*Note: Depth streams would show up as regular capture stream in DShow. *

Grouping cameras
================

Windows supports grouping of cameras based on their container ID to aid applications work with related cameras. For example, an IR camera and a Color camera present on the same physical device can be exposed to the OS as related cameras. This will make applications like Windows Hello to make use of the related cameras for their scenarios.

The relation between the camera functions could be specified in the cameras’ BOS descriptor in firmware. The UVC driver will make use of this information and expose these camera functions as related. This will make the OS’s camera stack expose them as a related group of cameras to the applications.

The camera firmware shall specify a *UVC-FSSensorGroupID*, which is a GUID in string form with the curly parenthesis. The cameras that have the same *UVC-FSSensorGroupID* will be grouped together.

The sensor group can be given a name by specifying *UVC-FSSensorGroupName*, a Unicode string, in the firmware.

Please refer Appendix A for an illustrative example BOS that specifies *UVC-FSSensorGroupID* and *UVC-FSSensorGroupName*.

Note:

*If you cannot update the device firmware like mentioned above, you could use a custom INF and specify that your camera is part of a sensor group by specifying a sensor group ID and name as follows:*

*The custom INF file (based on the inbox UVC driver) shall include the following AddReg entry:*

FSSensorGroupID: REG\_SZ: “{your sensor group ID GUID}”

FSSensorGroupName: REG\_SZ: “your sensor group friendly name”

> *An example for the custom INF section would be as follows:*
>
> *\[USBVideo.NT.Interfaces\]*
>
> *AddInterface=%KSCATEGORY\_CAPTURE%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_RENDER%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_VIDEO%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_RENDER\_EXT%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_VIDEO\_CAMERA%,GLOBAL,USBVideo.Interface*
>
> *\[USBVideo.Interface\]*
>
> *AddReg=USBVideo.Interface.AddReg*
>
> *\[USBVideo.Interface.AddReg\]*
>
> *HKR,,CLSID,,%ProxyVCap.CLSID%*
>
> *HKR,,FriendlyName,,%USBVideo.DeviceDesc%*
>
> *HKR,,RTCFlags,0x00010001,0x00000010*
>
> *HKR,, FSSensorGroupID,0x00000000,%FSSensorGroupID%*
>
> *HKR,, FSSensorGroupName,0x00000000,%FSSensorGroupName%*

*Note: Sensor Groups are not supported in DShow capture pipeline.*

Method 2 or Method 3 Still Capture support
==========================================

UVC specification does provide a mechanism to specify if the video streaming interface supports Method 1/2/3 type still image capture. To make the OS take advantage of the device’s Method 2/3 still image capture support, through UVC driver, the device firmware could specify a value in the BOS descriptor.

The value to specify to enable Method 2/3 still image capture is a DWORD by name *UVC-EnableDependentStillImageCapture* and specify its value using the BOS descriptor. Appendix A illustrates enabling still image capture with an example BOS descriptor.

Note:

*If you cannot update the device firmware like mentioned above, you could use a custom INF to specify that your camera supports Method 2 or Method 3 still capture method. *

*The custom INF file (based on either custom UVC driver or inbox UVC driver) shall include the following AddReg entry:*

EnableDependentStillPinCapture: REG\_DWORD: 0x0 (Disabled) to 0x1 (Enabled)

> *When this entry is set to Enabled (0x1), the capture pipeline will leverage Method 2/3 for Still Image Capture (assuming the firmware also advertises support for Method 2/3 as specified by UVC spec).*
>
> *An example for the custom INF section would be as follows:*
>
> *\[USBVideo.NT.Interfaces\]*
>
> *AddInterface=%KSCATEGORY\_CAPTURE%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_RENDER%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_VIDEO%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_RENDER\_EXT%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_VIDEO\_CAMERA%,GLOBAL,USBVideo.Interface*
>
> *\[USBVideo.Interface\]*
>
> *AddReg=USBVideo.Interface.AddReg*
>
> *\[USBVideo.Interface.AddReg\]*
>
> *HKR,,CLSID,,%ProxyVCap.CLSID%*
>
> *HKR,,FriendlyName,,%USBVideo.DeviceDesc%*
>
> *HKR,,RTCFlags,0x00010001,0x00000010*
>
> *HKR,,EnableDependentStillPinCapture,0x00010001,0x00000001*

Device MFT Chaining
===================

Device MFT is the recommended user mode plugin mechanism for IHVs and OEMs to extend the camera functionality on Windows. Prior to RS2, camera pipeline supported only one DMFT extension plugin. Starting from RS2, Windows camera pipeline supports an optional chain of DMFTs with maximum of three DMFTs. This provides greater flexibility for OEMs and IHVs to provide value-add in the form of post processing camera streams. For example, a device could use PDMFT along with an IHV DMFT and an OEM DMFT. Following figure illustrates the architecture involving a chain of DMFTs.

![DMFT chain](dmft-chain.png)

Capture samples flow from camera driver to DevProxy, then go through the DMFT chains. Every DMFT in the chain has a chance to process the sample. If the DMFT doesn’t want to process the sample, it can act as a pass-through just pass the sample to next DMFT.

For controls like KsProperty, the call will go up stream – the last DMFT in the chain will get the call first, the call can be handled there or get passed to previous DMFT in the chain.

Errors will be propagated from DMFT to DTM then to applications. For IHV/OEM DMFTs, any one of the DMFT fails to instantiate will be a fatal error for DTM.

Requirements on DMFTs:

-   The input pin count of the DMFT must match with the output pin count of previous DMFT, otherwise DTM would fail during initialization. However, the input and output pin counts of same DMFT do not need to match.

-   DMFT needs to support interfaces - IMFDeviceTransform, IMFShutdown, IMFRealTimeClientEx, IKsControl and IMFMediaEventGenerator; IMFTransform may need to be supported if there is MFT0 configured or the next DMFT in the chain requires IMFTransform support.

-   On 64-bit systems that don’t make use of Frame Server, both 32-bit and 64-bit DMFTs shall be registered. Given that a USB camera might get plugged into an arbitrary system, for “external” (or non-inbox) USB cameras, the USB camera vendor should supply both 32-bit and 64-bit DMFTs.

Configuring DMFT chain
======================

> A camera device can optionally supply a DMFT COM object in a dll using a custom INF file that uses sections of the in-box USBVideo.INF. In the custom .INF file’s “Interface AddReg” section, specify the DMFT CLSIDs by adding following registry entry:

**CameraDeviceMftCLSIDChain** (REG\_MULTI\_SZ) %Dmft0.CLSID%,%Dmft.CLSID%,%Dmft2.CLSID%

> as shown in the sample .inf settings below (replace the %Dmft0.CLSID% and % Dmft1.CLSID% with actual CLSID stringsyou’re your DMFTs), there are maximum 2 CLSIDs allowed in RS2 and the first one is closest to DevProxy and the last one is the last DMFT in the chain.
>
> Platform DMFT CLSID is {3D096DDE-8971-4AD5-98F9-C74F56492630}.
>
> Some examples CameraDeviceMftCLSIDChain settings:

-   *No IHV/OEM DMFT or Platform DMFT*

    -   CameraDeviceMftCLSIDChain = “” (or no need to specify this registry entry)

-   *IHV/OEM DMFT*

    -   CameraDeviceMftCLSIDChain = %Dmft.CLSID%

-   *Platform DMFT &lt;-&gt; IHV/OEM DMFT*

    -   CameraDeviceMftCLSIDChain = “{3D096DDE-8971-4AD5-98F9-C74F56492630}”,%Dmft.CLSID%

    -   Here is a screen shot of the result registry key for an USB camera with Platform DMFT and an DMFT (with GUID {D671BE6C-FDB8-424F-81D7-03F5B1CE2CC7}) in the chain.

![Registry editor DMFT chain](dmft-registry-editor.png)

-   *IHV/OEM DMFT0 &lt;-&gt; IHV/OEM DMFT1*

    -   CameraDeviceMftCLSIDChain = %Dmft0.CLSID%,%Dmft1.CLSID%,

*Note: CameraDeviceMftCLSIDChain can have maximum 2 CLSIDs.*

*If CameraDeviceMftCLSIDChain is configured, the legacy CameraDeviceMftCLSID settings will be skipped by DTM.*

*If CameraDeviceMftCLSIDChain is not configured and the legacy CameraDeviceMftCLSID is configured, then the chain would look like (if it’s USB camera and supported by Platform DMFT and Platform DMFT is enabled) DevProxy &lt;–&gt; Platform DMFT &lt;–&gt; OEM/IHV DMFT or (if the camera is not supported by Platform DMFT or Platform DMFT is disabled) DevProxy &lt;-&gt; OEM/IHV DMFT.*

> *Sample .inf settings:*
>
> *\[USBVideo.Interface.AddReg\] *
>
> *HKR,,CLSID,,%ProxyVCap.CLSID% *
>
> *HKR,,FriendlyName,,%USBVideo.DeviceDesc% *
>
> *HKR,,RTCFlags,0x00010001,0x00000010 *
>
> *HKR,,EnablePlatformDmft,0x00010001,0x00000001 *
>
> *HKR,,DisablePlatformDmftFeatures,0x00010001,0x00000001 *
>
> *HKR,,CameraDeviceMftCLSIDChain, 0x00010000,%Dmft0.CLSID%,%Dmft1.CLSID%*

Platform Device MFT
===================

Starting in RS2, Windows provides an in-box Device MFT for UVC cameras known as Platform DMFT (PDMFT) on an opt-in basis. This DMFT allows IHVs and OEMs to take advantage of Windows provided post processing algorithms.

| Features supported by Platform DMFT                                                                                           | Windows Release |
|-------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Enables face-based Region of Interest (ROI) for 3A adjustments in ROI-capable USB cameras.                                    
                                                                                                                                
 *Note: If the camera doesn’t support UVC 1.5 based ROI then the PDMFT wouldn’t load even if the device opted in to use PDMFT*  | RS2             |

A UVC camera could opt-in to use platform DMFT by specifying the EnablePlatformDmft through BOS descriptor.

The value to specify to enable Platform DMFT is a DWORD by name *UVC-EnablePlatformDmft* and specify its value using the BOS descriptor. Appendix A illustrates enabling Platform DMFT with an example BOS descriptor.

Note:

*If you cannot update the device firmware like mentioned above, you could use a custom INF to enable Platform DMFT for the device. *

*The custom INF file (based on either custom UVC driver or inbox UVC driver) shall include the following AddReg entry:*

EnablePlatformDmft: REG\_DWORD: 0x0 (Disabled) to 0x1 (Enabled)

> *When this entry is set to Enabled (0x1), the capture pipeline will use inbox Platform DMFT for the device.*
>
> *An example for the custom INF section would be as follows:*
>
> *\[USBVideo.NT.Interfaces\]*
>
> *AddInterface=%KSCATEGORY\_CAPTURE%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_RENDER%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_VIDEO%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_RENDER\_EXT%,GLOBAL,USBVideo.Interface*
>
> *AddInterface=%KSCATEGORY\_VIDEO\_CAMERA%,GLOBAL,USBVideo.Interface*
>
> *\[USBVideo.Interface\]*
>
> *AddReg=USBVideo.Interface.AddReg*
>
> *\[USBVideo.Interface.AddReg\]*
>
> *HKR,,CLSID,,%ProxyVCap.CLSID%*
>
> *HKR,,FriendlyName,,%USBVideo.DeviceDesc%*
>
> *HKR,,RTCFlags,0x00010001,0x00000010*
>
> *HKR,,EnablePlatformDmft,0x00010001,0x00000001*
>
> *In RS2 if a device opts in to use PDMFT then all features that are supported by the PDMFT are enabled (based on the device capabilities). Granular configuration of PDMFT features is not supported.*

BOS and MS OS 2.0 descriptor
============================

UVC compliant camera can specify Windows specific device configuration values in a platform capability BOS descriptor in its firmware. Please refer the documentation on [MS OS 2.0 descriptor](https://msdn.microsoft.com/en-us/library/windows/hardware/dn385747.aspx) to understand how to specify a valid BOS descriptor that conveys the device configuration to the OS. When a valid MS OS 2.0 descriptor is specified in the firmware, the USB stack copies the configuration values into the device HW registry key show below:

HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Enum\\USB\\&lt;Device ID&gt;\\&lt;Instance ID&gt;\\Device Parameters

UVC driver reads the configuration values from the device HW registry key and configures the device on the OS accordingly. For example, if the firmware specifies the device to be registered as a sensor camera using a configuration value, UVC driver registers the device just under that category.

Configuring UVC devices through platform BOS descriptor is a mechanism we enabled in RS2 to help UVC device vendors to configure the device without the need of an INF file on Windows OS.

Configuring UVC devices through custom INF is still supported and that takes precedence over BOS descriptor based mechanism. While specifying device properties through INF, you don’t need to add the prefix “UVC-“. This prefix is only needed for device properties that are specified through BOS descriptor and that are per interface instance specific. If your device needs user mode plugins like DMFT then you do need to supply an INF for installing the DMFT. It cannot be configured using firmware.

Currently supported configuration values through BOS descriptor:\\
==================================================================

| Configuration Name                     | Type       | Description                                     |
|----------------------------------------|------------|-------------------------------------------------|
| *SensorCameraMode*                     | REG\_DWORD | Register the camera under a specific category.  |
| *UVC-FSSensorGroupID*                  
                                         
 *UVC-FSSensorGroupName*                 | REG\_SZ    | Group cameras with the same UVC-FSSensorGroupID |
| *UVC-EnableDependentStillImageCapture* | REG\_DWORD | To enable still capture Method 2/3              |
| *UVC-EnablePlatformDmft*               | REG\_DWORD | To enable Platform DMFT                         |

Detailed explanation about the supported configuration values are given in the following sections.

Note:

*When UVC driver sees the registry values with prefix “UVC-“, it populates the device’s category interface instance registry key, with the same values without the prefix. The driver will do this for any variable specified by the firmware, not just the ones listed above.*

HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\DeviceClasses\\{e5323777-f976-4f5b-9b55-b94699c46e44}\\&lt;Device Symbolic Link&gt;\\Device Parameters
*For the OS to make use of the BOS Platform Device Capability and MS OS2.0 descriptors the device descriptor shall specify the bcdUSB version to be 0x0210 or greater.*

Appendix A
==========

This section gives an example BOS descriptor and a MS OS2.0 Descriptor for an imaginary composite device with two camera functions. One function is a UVC color camera and the second function is a UVC IR camera. The sample descriptors

1.  register the color camera function under KSCATEGORY\_VIDEO\_CAMERA

2.  register the IR camera function under KSCATEGORY\_SENSOR\_CAMERA

3.  enable color camera function’s still image capture

4.  associates the color and IR camera functions as a group

Upon device enumeration, the USB stack retrieves the BOS descriptor from the device. Following the BOS descriptor is a platform specific device capability.

\#include &lt;usbspec.h&gt;

const BYTE USBVideoBOSDescriptor\[0x21\] =

{

/\* BOS Descriptor \*/

0x05, // Descriptor size

USB\_BOS\_DESCRIPTOR\_TYPE,// Device descriptor type BOS

0x21, 0x00, // Length 0x21 (33) this and all sub descriptors

0x01, // Number of device capability descriptors

/\* Platform Device Capability Descriptor \*/

0x1C, // 28 bytes bLength

USB\_DEVICE\_CAPABILITY\_DESCRIPTOR\_TYPE,// Platform Descriptor type

USB\_DEVICE\_CAPABILITY\_PLATFORM, // bDevCapabilityType PLATFORM

0, // bReserved

0xDF, 0x60, 0xDD, 0xD8, // PlatformCapabilityUUID

0x89, 0x45, // MS OS2.0 Descriptor

0xC7, 0x4C, // D8DD60DF-4589-4CC7-9CD2-659D9E648A9F

0x9C, 0xD2, 0x65, 0x9D, 0x9E, 0x64, 0x8A, 0x9F,

// CapabilityData

0x00, 0x00, 0x00, 0x0A, // dwWindowsVersion for Windows 10 and later

0xC8, 0x02, // wLength 0x2C8 (712)

0x01, // bMS\_VendorCode - any value. e.g. 0x01

0x00 // bAltEnumCmd 0

};

The BOS platform capability descriptor specifies

1.  MS OS 2.0 descriptor platform capability GUID

2.  a vendor control code bMS\_VendorCode (here is it set to 1. It can take any value the vendor prefers) to retrieve the MS OS 2.0 descriptor.

3.  This BOS descriptor is applicable for OS version Windows 10 and later.

After seeing the BOS descriptor, the USB stack will issue the vendor specific control request to retrieve the MS OS 2.0 descriptor.

Format of the control request to retrieve MS OS 2.0 vendor-specific descriptor:

| bmRequestType | BRequest            | wValue | WIndex | wLength | Data                                   |
|---------------|---------------------|--------|--------|---------|----------------------------------------|
| 1100 0000B    | **bMS\_VendorCode** | 0x00   | 0x07   | Length  | Returned MS OS 2.0 Descriptor Set blob |

**bmRequestType **

-   Data Transfer Direction – Device to Host

-   Type – Vendor

-   Recipient - Device

**bRequest**

The **bMS\_VendorCode** value returned in the descriptor set information structure.

**wValue**

Set to 0x00.

**wIndex**

0x7 for MS\_OS\_20\_DESCRIPTOR\_INDEX.

**wLength**

Length of the MS OS 2.0 descriptor set, as returned in the BOS descriptor. 0x25C (604) in this example.

The device is expected to return the MS OS 2.0 descriptor like the one specified in USBVideoMSOS20DescriptorSet.

The USBVideoMSOS20DescriptorSet describes the color and IR functions. It specifies the following MS OS 2.0 Descriptor values:

1.  Set Header

2.  Configuration Subset Header

3.  Color Camera Function Subset Header

4.  Registry Value Feature Descriptor for sensor group ID

5.  Registry Value Feature Descriptor for sensor group name

6.  Registry Value Feature Descriptor for enabling still image capture

7.  Registry Value Feature Descriptor for enabling Platform DMFT

8.  IR Camera Function Subset Header

9.  Registry Value Feature Descriptor for sensor group ID

10. Registry Value Feature Descriptor for sensor group name

11. Registry Value Feature Descriptor for registering the camera as a sensor camera

Note:

*The firmware will have a handler for the vendor request that will return the following MS OS 2.0 descriptor for the imaginary device described at the beginning of this section.*

UCHAR USBVideoMSOS20DescriptorSet\[0x2C8\] =

{

/\* Microsoft OS 2.0 Descriptor Set Header \*/

0x0A, 0x00, // wLength of MSOS20\_SET\_HEADER\_DESCRIPTOR

0x00, 0x00, // wDescriptorType == MSOS20\_SET\_HEADER\_DESCRIPTOR

0x00, 0x00, 0x00, 0x0A, // dwWindowsVersion – 0x10000000 for Windows 10

0xC8, 0x02, // wTotalLength - Total length 0x2C8 (712)

/\* Microsoft OS 2.0 Configuration Subset Header \*/

0x08, 0x00, // wLength of MSOS20\_SUBSET\_HEADER\_CONFIGURATION

0x01, 0x00, // wDescriptorType == MSOS20\_SUBSET\_HEADER\_CONFIGURATION

0x00, // bConfigurationValue set to the first configuration

0x00, // bReserved set to 0.

0xBE, 0x02, // wTotalLength - Total length 0x2BE (702)

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Color Camera Function\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

/\* Microsoft OS 2.0 Function Subset Header \*/

0x08, 0x00, // wLength of MSOS20\_SUBSET\_HEADER\_FUNCTION

0x02, 0x00, // wDescriptorType == MSOS20\_SUBSET\_HEADER\_FUNCTION

0x00, // bFirstInterface field of the first IAD

0x00, // bReserved set to 0.

0x6E, 0x01, // wSubsetLength - Length 0x16E (366)

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Register the Color Camera in a sensor group\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x80, 0x00, // wLength 0x80 (128) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x01, 0x00, // wPropertyDataType - REG\_SZ

0x28, 0x00, // wPropertyNameLength – 0x28 (40) bytes

'U', 0x00, 'V', 0x00, // Property Name - “UVC-FSSensorGroupID”

'C', 0x00, '-', 0x00,

'F', 0x00, 'S', 0x00,

'S', 0x00, 'e', 0x00,

'n', 0x00, 's', 0x00,

'o', 0x00, 'r', 0x00,

'G', 0x00, 'r', 0x00,

'o', 0x00, 'u', 0x00,

'p', 0x00, 'I', 0x00,

'D', 0x00, 0x00, 0x00,

0x4E, 0x00, // wPropertyDataLength – 0x4E (78) bytes

// FSSensorGroupID GUID in string format:

// "{20C94C5C-F402-4F1F-B324-0C1CF0257870}"

'{', 0x00, '2', 0x00, // NOTE: This is just an example GUID.

'0', 0x00, 'C', 0x00, // You need to generate and use your

'9', 0x00, '4', 0x00, // own GUID for the sensor group ID

'C', 0x00, '5', 0x00,

'C', 0x00, '-', 0x00,

'F', 0x00, '4', 0x00,

'0', 0x00, '2', 0x00,

'-', 0x00, '4', 0x00,

'F', 0x00, '1', 0x00,

'F', 0x00, '-', 0x00,

'B', 0x00, '3', 0x00,

'2', 0x00, '4', 0x00,

'-', 0x00, '0', 0x00,

'C', 0x00, '1', 0x00,

'C', 0x00, 'F', 0x00,

'0', 0x00, '2', 0x00,

'5', 0x00, '7', 0x00,

'8', 0x00, '7', 0x00,

'0', 0x00, '}', 0x00,

0x00, 0x00,

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x56, 0x00, // wLength 0x56 (86) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x01, 0x00, // wPropertyDataType - REG\_SZ

0x2C, 0x00, // wPropertyNameLength – 0x2C (44) bytes

'U', 0x00, 'V', 0x00, // Property Name - “UVC-FSSensorGroupName”

'C', 0x00, '-', 0x00,

'F', 0x00, 'S', 0x00,

'S', 0x00, 'e', 0x00,

'n', 0x00, 's', 0x00,

'o', 0x00, 'r', 0x00,

'G', 0x00, 'r', 0x00,

'o', 0x00, 'u', 0x00,

'p', 0x00, 'N', 0x00,

'a', 0x00, 'm', 0x00,

'e', 0x00, 0x00, 0x00,

0x20, 0x00, // wPropertyDataLength – 0x20 (32) bytes

// FSSensorGroupName "YourCameraGroup"

'Y', 0x00, 'o', 0x00,

'u', 0x00, 'r', 0x00,

'C', 0x00, 'a', 0x00,

'm', 0x00, 'e', 0x00,

'r', 0x00, 'a', 0x00,

'G', 0x00, 'r', 0x00,

'o', 0x00, 'u', 0x00,

'p', 0x00, 0x00, 0x00,

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Enable Still Image Capture for Color Camera\*\*\*\*\*\*\*\*\*\*\*\*/

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x54, 0x00, // wLength 0x54 (84) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x04, 0x00, // wPropertyDataType - REG\_DWORD

0x46, 0x00, // wPropertyNameLength – 0x46 (70) bytes

'U', 0x00, 'V', 0x00, // Property Name - “UVC-EnableDependentStillPinCapture”

'C', 0x00, '-', 0x00,

'E', 0x00, 'n', 0x00,

'a', 0x00, 'b', 0x00,

'l', 0x00, 'e', 0x00,

'D', 0x00, 'e', 0x00,

'p', 0x00, 'e', 0x00,

'n', 0x00, 'd', 0x00,

'e', 0x00, 'n', 0x00,

't', 0x00, 'S', 0x00,

't', 0x00, 'i', 0x00,

'l', 0x00, 'l', 0x00,

'P', 0x00, 'i', 0x00,

'n', 0x00, 'C', 0x00,

'a', 0x00, 'p', 0x00,

't', 0x00, 'u', 0x00,

'r', 0x00, 'e', 0x00,

0x00, 0x00,

0x04, 0x00, // wPropertyDataLength – 4 bytes

0x01, 0x00, 0x00, 0x00, // Enable still pin capture using Method 2 or Method 3

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Enable Platform DMFT for ROI-capable USB Camera\*\*\*\*\*\*\*\*\*\*\*\*/

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x3C, 0x00, // wLength 0x3C (60) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x04, 0x00, // wPropertyDataType - REG\_DWORD

0x2E, 0x00, // wPropertyNameLength – 0x2E (46) bytes

'U', 0x00, 'V', 0x00, // Property Name - “UVC-EnablePlatformDmft”

'C', 0x00, '-', 0x00,

'E', 0x00, 'n', 0x00,

'a', 0x00, 'b', 0x00,

'l', 0x00, 'e', 0x00,

'P', 0x00, 'l', 0x00,

'a', 0x00, 't', 0x00,

'f', 0x00, 'o', 0x00,

'r', 0x00, 'm', 0x00,

'D', 0x00, 'm', 0x00,

'f', 0x00, 't', 0x00,

0x00, 0x00,

0x04, 0x00, // wPropertyDataLength – 4 bytes

0x01, 0x00, 0x00, 0x00, // Enable Platform DMFT

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IR Camera Function\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

/\* Microsoft OS 2.0 Function Subset Header \*/

0x08, 0x00, // wLength of MSOS20\_SUBSET\_HEADER\_FUNCTION

0x02, 0x00, // wDescriptorType == MSOS20\_SUBSET\_HEADER\_FUNCTION

0x01, // bFirstInterface set of the second function

0x00, // bReserved set to 0.

0x48, 0x01, // wSubsetLength - Length 0x148 (328)

/\*\*\*\*\*\*\*\*Register the IR Camera to the same sensor group as the Color Camera\*\*\*\*\*/

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x80, 0x00, // wLength 0x80 (128) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x01, 0x00, // wPropertyDataType - REG\_SZ

0x28, 0x00, // wPropertyNameLength – 0x28 (40) bytes

'U', 0x00, 'V', 0x00, // Property Name - “UVC-FSSensorGroupID”

'C', 0x00, '-', 0x00,

'F', 0x00, 'S', 0x00,

'S', 0x00, 'e', 0x00,

'n', 0x00, 's', 0x00,

'o', 0x00, 'r', 0x00,

'G', 0x00, 'r', 0x00,

'o', 0x00, 'u', 0x00,

'p', 0x00, 'I', 0x00,

'D', 0x00, 0x00, 0x00,

0x4E, 0x00, // wPropertyDataLength – 78 bytes

// FSSensorGroupID GUID in string format:

// "{20C94C5C-F402-4F1F-B324-0C1CF0257870}"

'{', 0x00, '2', 0x00,

'0', 0x00, 'C', 0x00,

'9', 0x00, '4', 0x00,

'C', 0x00, '5', 0x00,

'C', 0x00, '-', 0x00,

'F', 0x00, '4', 0x00,

'0', 0x00, '2', 0x00,

'-', 0x00, '4', 0x00,

'F', 0x00, '1', 0x00,

'F', 0x00, '-', 0x00,

'B', 0x00, '3', 0x00,

'2', 0x00, '4', 0x00,

'-', 0x00, '0', 0x00,

'C', 0x00, '1', 0x00,

'C', 0x00, 'F', 0x00,

'0', 0x00, '2', 0x00,

'5', 0x00, '7', 0x00,

'8', 0x00, '7', 0x00,

'0', 0x00, '}', 0x00,

0x00, 0x00,

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x56, 0x00, // wLength 0x56 (86) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x01, 0x00, // wPropertyDataType - REG\_SZ

0x2C, 0x00, // wPropertyNameLength – 0x2C (44) bytes

'U', 0x00, 'V', 0x00, // Property Name - “UVC-FSSensorGroupName”

'C', 0x00, '-', 0x00,

'F', 0x00, 'S', 0x00,

'S', 0x00, 'e', 0x00,

'n', 0x00, 's', 0x00,

'o', 0x00, 'r', 0x00,

'G', 0x00, 'r', 0x00,

'o', 0x00, 'u', 0x00,

'p', 0x00, 'N', 0x00,

'a', 0x00, 'm', 0x00,

'e', 0x00, 0x00, 0x00,

0x20, 0x00, // wPropertyDataLength – 32 bytes

// FSSensorGroupName "YourCameraGroup"

'Y', 0x00, 'o', 0x00,

'u', 0x00, 'r', 0x00,

'C', 0x00, 'a', 0x00,

'm', 0x00, 'e', 0x00,

'r', 0x00, 'a', 0x00,

'G', 0x00, 'r', 0x00,

'o', 0x00, 'u', 0x00,

'p', 0x00, 0x00, 0x00,

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Make IR camera visible to applications\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x30, 0x00, // wLength 0x30 (48) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x04, 0x00, // wPropertyDataType - REG\_DWORD

0x22, 0x00, // wPropertyNameLength – 0x22 (34) bytes

'S', 0x00, 'e', 0x00,

'n', 0x00, 's', 0x00,

'o', 0x00, 'r', 0x00,

'C', 0x00, 'a', 0x00,

'm', 0x00, 'e', 0x00,

'r', 0x00, 'a', 0x00,

'M', 0x00, 'o', 0x00,

'd', 0x00, 'e', 0x00,

0x00, 0x00,

0x04, 0x00, // wPropertyDataLength – 4 bytes

0x01, 0x00, 0x00, 0x00, // This exposes the camera to OS as an IR only camera

// i.e. KSCATEGORY\_SENSOR\_CAMERA

/\* Microsoft OS 2.0 Registry Value Feature Descriptor \*/

0x3A, 0x00, // wLength 0x3A (58) in bytes of this descriptor

0x04, 0x00, // wDescriptorType – MSOS20\_FEATURE\_REG\_PROPERTY

0x04, 0x00, // wPropertyDataType - REG\_DWORD

0x2C, 0x00, // wPropertyNameLength – 0x2C (44) bytes

'S', 0x00, 'k', 0x00,

'i', 0x00, 'p', 0x00,

'C', 0x00, 'a', 0x00,

'm', 0x00, 'e', 0x00,

'r', 0x00, 'a', 0x00,

'E', 0x00, 'n', 0x00,

'u', 0x00, 'm', 0x00,

'e', 0x00, 'r', 0x00,

'a', 0x00, 't', 0x00,

'i', 0x00, 'o', 0x00,

'n', 0x00, 0x00, 0x00,

0x04, 0x00, // wPropertyDataLength – 4 bytes

0x01, 0x00, 0x00, 0x00 // This exposes the camera to applications looking for IR only cameras

};
