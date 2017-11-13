---
title: Imaging Devices Reference
description: Imaging Devices Reference
MS-HAID:
- 'stillimref\_5a13bf79-d566-4835-8065-08cdcdb9d441.xml'
- 'image.imaging\_devices\_reference'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2ee6ce92-44dc-4c59-a438-f65b41f3b43a
---

# Imaging Devices Reference


## <span id="ddk_still_image_reference_si"></span><span id="DDK_STILL_IMAGE_REFERENCE_SI"></span>


This section contains reference information for the following technologies:

[Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md)

[IWiaMiniDrv Interface](https://msdn.microsoft.com/library/windows/hardware/ff545027)

[Still Image Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff548281)

[Web Services on Devices Reference](https://msdn.microsoft.com/library/windows/hardware/ff549148)

### <span id="wia_and_sti_driver_reference_table"></span><span id="WIA_AND_STI_DRIVER_REFERENCE_TABLE"></span>WIA and STI Driver Reference Table

The following table contains reference information for Windows Image Acquisition (WIA) drivers and for Still Imaging (STI) drivers. These drivers control devices, including scanners and cameras, that capture still images. For more information about these drivers, see [Windows Image Acquisition Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553346) and [Still Image Drivers](https://msdn.microsoft.com/library/windows/hardware/ff548278).

The following sections describe the interfaces, functions, structures, and properties used by WIA and STI drivers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Section</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md)</p></td>
<td><p>Device class GUID for imaging devices.</p></td>
</tr>
<tr class="even">
<td><p>[IWiaMiniDrv Interface](https://msdn.microsoft.com/library/windows/hardware/ff545027)</p></td>
<td><p>Interface for managing all communications between a WIA minidriver and the WIA service.</p></td>
</tr>
<tr class="odd">
<td><p>[WIA Driver Services Library Functions](https://msdn.microsoft.com/library/windows/hardware/ff551473)</p></td>
<td><p>Helper functions used by a WIA minidriver to manage device items and data transfers.</p></td>
</tr>
<tr class="even">
<td><p>[WIA Properties](wia-properties.md)</p></td>
<td><p>Properties of WIA devices, including status, capabilities, and device identification information.</p></td>
</tr>
<tr class="odd">
<td><p>[WIA Utility Library Functions and Classes](https://msdn.microsoft.com/library/windows/hardware/ff553303)</p></td>
<td><p>Utility functions and classes used by a WIA minidriver to support debugging and to perform common tasks.</p></td>
</tr>
<tr class="even">
<td><p>[IWiaMiniDrvCallBack Interface](https://msdn.microsoft.com/library/windows/hardware/ff543943)</p></td>
<td><p>Callback interface for transferring status and image data between the WIA service and a WIA minidriver.</p></td>
</tr>
<tr class="odd">
<td><p>[IWiaDrvItem Interface](https://msdn.microsoft.com/library/windows/hardware/ff543896)</p></td>
<td><p>Interface used by a WIA minidriver to manage a tree of WIA driver items.</p></td>
</tr>
<tr class="even">
<td><p>[IWiaErrorHandler Interface](https://msdn.microsoft.com/library/windows/hardware/ff543907)</p></td>
<td><p>Interface used by a WIA minidriver to provide error status and to support error recovery.</p></td>
</tr>
<tr class="odd">
<td><p>[IWiaImageFilter Interface](https://msdn.microsoft.com/library/windows/hardware/ff543921)</p></td>
<td><p>Interface implemented by an image processing filter and called by the WIA service to communicate with the filter.</p></td>
</tr>
<tr class="even">
<td><p>[IWiaLog Interface and Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff543937)</p></td>
<td><p>Interface and macros used by a WIA minidriver to record trace, error, and warning messages to a diagnostic log file.</p></td>
</tr>
<tr class="odd">
<td><p>[IWiaSegmentationFilter Interface](https://msdn.microsoft.com/library/windows/hardware/ff545035)</p></td>
<td><p>Interface used by a WIA minidriver to detect regions in a segmented image.</p></td>
</tr>
<tr class="even">
<td><p>[IWiaTransferCallback Interface](https://msdn.microsoft.com/library/windows/hardware/ff545043)</p></td>
<td><p>Interface implemented by an image processing filter and called by the WIA service to initiate the processing of image streams.</p></td>
</tr>
<tr class="odd">
<td><p>[WIA Microdriver Functions, Structures, and Commands](https://msdn.microsoft.com/library/windows/hardware/ff552720)</p></td>
<td><p>Functions, structures, and commands used by WIA microdrivers.</p></td>
</tr>
<tr class="even">
<td><p>[WIA User Interface Extensions](https://msdn.microsoft.com/library/windows/hardware/ff553281)</p></td>
<td><p>Interface used by device vendors to provide custom user interfaces for their devices.</p></td>
</tr>
<tr class="odd">
<td><p>[WIA Structures](https://msdn.microsoft.com/library/windows/hardware/ff552803)</p></td>
<td><p>Structures used by driver-level WIA methods and functions.</p></td>
</tr>
<tr class="even">
<td><p>[Still Image Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff548281)</p></td>
<td><p>Interfaces, structures, data types, and control codes used by STI drivers.</p></td>
</tr>
<tr class="odd">
<td><p>[Web Services on Devices Reference](https://msdn.microsoft.com/library/windows/hardware/ff547963)</p></td>
<td><p>Web Services on Devices information, including Scan Service (WS-SCAN) and Distributed Scan Management (DSM)</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Imaging%20Devices%20Reference%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




