---
title: Imaging Devices Reference
description: Imaging Devices Reference
ms.assetid: 2ee6ce92-44dc-4c59-a438-f65b41f3b43a
ms.date: 09/14/2017
ms.localizationpriority: medium
---

# Imaging Devices Reference

This section contains reference information for the following technologies:

[Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md)

[IWiaMiniDrv Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv)

[Still Image Interfaces](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index)

[Web Services on Devices Reference](https://docs.microsoft.com/windows-hardware/drivers/image/web-services-on-devices-reference)

## WIA and STI Driver Reference Table

The following table contains reference information for Windows Image Acquisition (WIA) drivers and for Still Imaging (STI) drivers. These drivers control devices, including scanners and cameras, that capture still images. For more information about these drivers, see [Windows Image Acquisition Drivers](https://docs.microsoft.com/windows-hardware/drivers/image/windows-image-acquisition-drivers) and [Still Image Drivers](https://docs.microsoft.com/windows-hardware/drivers/image/still-image-drivers).

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
<td><p><a href="device-interface-classes-for-imaging-devices.md" data-raw-source="[Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md)">Device Interface Classes for Imaging Devices</a></p></td>
<td><p>Device class GUID for imaging devices.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv" data-raw-source="[IWiaMiniDrv Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv)">IWiaMiniDrv Interface</a></p></td>
<td><p>Interface for managing all communications between a WIA minidriver and the WIA service.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamdef/index" data-raw-source="[WIA Driver Services Library Functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamdef/index)">WIA Driver Services Library Functions</a></p></td>
<td><p>Helper functions used by a WIA minidriver to manage device items and data transfers.</p></td>
</tr>
<tr class="even">
<td><p><a href="wia-properties.md" data-raw-source="[WIA Properties](wia-properties.md)">WIA Properties</a></p></td>
<td><p>Properties of WIA devices, including status, capabilities, and device identification information.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index" data-raw-source="[WIA Utility Library Functions and Classes](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index)">WIA Utility Library Functions and Classes</a></p></td>
<td><p>Utility functions and classes used by a WIA minidriver to support debugging and to perform common tasks.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback" data-raw-source="[IWiaMiniDrvCallBack Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback)">IWiaMiniDrvCallBack Interface</a></p></td>
<td><p>Callback interface for transferring status and image data between the WIA service and a WIA minidriver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem" data-raw-source="[IWiaDrvItem Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem)">IWiaDrvItem Interface</a></p></td>
<td><p>Interface used by a WIA minidriver to manage a tree of WIA driver items.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiaerrorhandler" data-raw-source="[IWiaErrorHandler Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiaerrorhandler)">IWiaErrorHandler Interface</a></p></td>
<td><p>Interface used by a WIA minidriver to provide error status and to support error recovery.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiaimagefilter" data-raw-source="[IWiaImageFilter Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiaimagefilter)">IWiaImageFilter Interface</a></p></td>
<td><p>Interface implemented by an image processing filter and called by the WIA service to communicate with the filter.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index" data-raw-source="[IWiaLog Interface and Diagnostic Log Macros](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index)">IWiaLog Interface and Diagnostic Log Macros</a></p></td>
<td><p>Interface and macros used by a WIA minidriver to record trace, error, and warning messages to a diagnostic log file.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiasegmentationfilter" data-raw-source="[IWiaSegmentationFilter Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiasegmentationfilter)">IWiaSegmentationFilter Interface</a></p></td>
<td><p>Interface used by a WIA minidriver to detect regions in a segmented image.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiatransfercallback" data-raw-source="[IWiaTransferCallback Interface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wia_lh/nn-wia_lh-iwiatransfercallback)">IWiaTransferCallback Interface</a></p></td>
<td><p>Interface implemented by an image processing filter and called by the WIA service to initiate the processing of image streams.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index" data-raw-source="[WIA Microdriver Functions, Structures, and Commands](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index)">WIA Microdriver Functions, Structures, and Commands</a></p></td>
<td><p>Functions, structures, and commands used by WIA microdrivers.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiadevd/index" data-raw-source="[WIA User Interface Extensions](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiadevd/index)">WIA User Interface Extensions</a></p></td>
<td><p>Interface used by device vendors to provide custom user interfaces for their devices.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index" data-raw-source="[WIA Structures](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index)">WIA Structures</a></p></td>
<td><p>Structures used by driver-level WIA methods and functions.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index" data-raw-source="[Still Image Interfaces](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_image/index)">Still Image Interfaces</a></p></td>
<td><p>Interfaces, structures, data types, and control codes used by STI drivers.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/image/scan-service--ws-scan--schema" data-raw-source="[Web Services on Devices Reference](https://docs.microsoft.com/windows-hardware/drivers/image/scan-service--ws-scan--schema)">Web Services on Devices Reference</a></p></td>
<td><p>Web Services on Devices information, including Scan Service (WS-SCAN)</p></td>
</tr>
</tbody>
</table>

 

 

 





