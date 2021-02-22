---
title: Imaging device driver design guide
description: Imaging device driver design guide
ms.assetid: dfdeeec8-bd06-452a-9189-87b20ce27699
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Imaging device driver design guide


This section contains information about Windows Image Acquisition (WIA) drivers, Still Image (STI) drivers, and Web Services on Devices (WSD.)

> [!NOTE]
> The WIA programming interface is used to develop imaging drivers for modern Windows operating systems. 
> The STI programming interface was used to develop imaging drivers in legacy Windows operating systems. 
> The STI programming interface documentation will be archived in a future release. 

## In this section

- [Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md)

- [Windows Image Acquisition Drivers](windows-image-acquisition-drivers.md)

- [WIA Properties](about-wia-properties.md)

- [64-Bit and WIA](64-bit-and-wia.md)

- [WIA Compatibility Layer](wia-compatibility-layer.md)

- [WIA Driver Filters](wia-driver-filters.md)

- [WIA Item Trees](wia-item-trees.md)

- [WIA with Web Services for Devices](wia-with-web-services-for-devices.md)

- [Developing a WIA Driver](developing-a-wia-driver.md)

- [Developing a WIA Camera Driver](developing-a-wia-camera-driver.md)

- [WIA Minidriver Best Practices](wia-minidriver-best-practices.md)

- [WIA Microdriver Commands](wia-microdriver-commands.md)

- [Building, Troubleshooting and Debugging WIA Minidrivers](building--troubleshooting-and-debugging-wia-minidrivers.md)

- [WIA Samples and Tools](wia-samples-and-tools.md)

- [Still Image Drivers](still-image-drivers.md)

- [Web Services on Devices](web-services-on-devices.md)

- [Web Services on Devices Reference](web-services-on-devices-reference.md)

## WIA and STI Driver Reference

The following table contains reference information for Windows Image Acquisition (WIA) drivers and for Still Imaging (STI) drivers. These drivers control devices, including scanners and cameras, that capture still images. For more information about these drivers, see [Windows Image Acquisition Drivers](./windows-image-acquisition-drivers.md) and [Still Image Drivers](./still-image-drivers.md).

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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv" data-raw-source="[IWiaMiniDrv Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv)">IWiaMiniDrv Interface</a></p></td>
<td><p>Interface for managing all communications between a WIA minidriver and the WIA service.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/index" data-raw-source="[WIA Driver Services Library Functions](/windows-hardware/drivers/ddi/wiamdef/index)">WIA Driver Services Library Functions</a></p></td>
<td><p>Helper functions used by a WIA minidriver to manage device items and data transfers.</p></td>
</tr>
<tr class="even">
<td><p><a href="wia-properties.md" data-raw-source="[WIA Properties](wia-properties.md)">WIA Properties</a></p></td>
<td><p>Properties of WIA devices, including status, capabilities, and device identification information.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[WIA Utility Library Functions and Classes](/windows-hardware/drivers/ddi/_image/index)">WIA Utility Library Functions and Classes</a></p></td>
<td><p>Utility functions and classes used by a WIA minidriver to support debugging and to perform common tasks.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback" data-raw-source="[IWiaMiniDrvCallBack Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback)">IWiaMiniDrvCallBack Interface</a></p></td>
<td><p>Callback interface for transferring status and image data between the WIA service and a WIA minidriver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem" data-raw-source="[IWiaDrvItem Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem)">IWiaDrvItem Interface</a></p></td>
<td><p>Interface used by a WIA minidriver to manage a tree of WIA driver items.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiaerrorhandler" data-raw-source="[IWiaErrorHandler Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiaerrorhandler)">IWiaErrorHandler Interface</a></p></td>
<td><p>Interface used by a WIA minidriver to provide error status and to support error recovery.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiaimagefilter" data-raw-source="[IWiaImageFilter Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiaimagefilter)">IWiaImageFilter Interface</a></p></td>
<td><p>Interface implemented by an image processing filter and called by the WIA service to communicate with the filter.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[IWiaLog Interface and Diagnostic Log Macros](/windows-hardware/drivers/ddi/_image/index)">IWiaLog Interface and Diagnostic Log Macros</a></p></td>
<td><p>Interface and macros used by a WIA minidriver to record trace, error, and warning messages to a diagnostic log file.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiasegmentationfilter" data-raw-source="[IWiaSegmentationFilter Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiasegmentationfilter)">IWiaSegmentationFilter Interface</a></p></td>
<td><p>Interface used by a WIA minidriver to detect regions in a segmented image.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiatransfercallback" data-raw-source="[IWiaTransferCallback Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiatransfercallback)">IWiaTransferCallback Interface</a></p></td>
<td><p>Interface implemented by an image processing filter and called by the WIA service to initiate the processing of image streams.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[WIA Microdriver Functions, Structures, and Commands](/windows-hardware/drivers/ddi/_image/index)">WIA Microdriver Functions, Structures, and Commands</a></p></td>
<td><p>Functions, structures, and commands used by WIA microdrivers.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiadevd/index" data-raw-source="[WIA User Interface Extensions](/windows-hardware/drivers/ddi/wiadevd/index)">WIA User Interface Extensions</a></p></td>
<td><p>Interface used by device vendors to provide custom user interfaces for their devices.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[WIA Structures](/windows-hardware/drivers/ddi/_image/index)">WIA Structures</a></p></td>
<td><p>Structures used by driver-level WIA methods and functions.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[Still Image Interfaces](/windows-hardware/drivers/ddi/_image/index)">Still Image Interfaces</a></p></td>
<td><p>Interfaces, structures, data types, and control codes used by STI drivers.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/image/scan-service--ws-scan--schema" data-raw-source="[Web Services on Devices Reference](./scan-service--ws-scan--schema.md)">Web Services on Devices Reference</a></p></td>
<td><p>Web Services on Devices information, including Scan Service (WS-SCAN)</p></td>
</tr>
</tbody>
</table>

## Related sections

- [Imaging DDI reference](/windows-hardware/drivers/ddi/_image)