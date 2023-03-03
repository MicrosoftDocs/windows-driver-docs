---
title: Imaging device driver design guide
description: Provides information about Windows Image Acquisition (WIA) drivers, Still Image (STI) drivers, and Web Services on Devices (WSD).
ms.date: 03/03/2023
---

# Imaging device driver design guide

This section contains information about Windows Image Acquisition (WIA) drivers, Still Image (STI) drivers, and Web Services on Devices (WSD).

> [!NOTE]
> The WIA programming interface is used to develop imaging drivers for modern Windows operating systems.
> The STI programming interface was used to develop imaging drivers in legacy Windows operating systems.
> The STI programming interface documentation will be archived in a future release.

## In this section

[Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md)

[Windows Image Acquisition Drivers](windows-image-acquisition-drivers.md)

[WIA Properties](about-wia-properties.md)

[64-Bit and WIA](64-bit-and-wia.md)

[WIA Compatibility Layer](wia-compatibility-layer.md)

[WIA Driver Filters](wia-driver-filters.md)

[WIA Item Trees](wia-item-trees.md)

[WIA with Web Services for Devices](wia-with-web-services-for-devices.md)

[Developing a WIA Driver](developing-a-wia-driver.md)

[Developing a WIA Camera Driver](developing-a-wia-camera-driver.md)

[WIA Minidriver Best Practices](wia-minidriver-best-practices.md)

[WIA Microdriver Commands](wia-microdriver-commands.md)

[Building, Troubleshooting and Debugging WIA Minidrivers](building--troubleshooting-and-debugging-wia-minidrivers.md)

[WIA Samples and Tools](wia-samples-and-tools.md)

[Still Image Drivers](still-image-drivers.md)

[Web Services on Devices](web-services-on-devices.md)

[Web Services on Devices Reference](web-services-on-devices-reference.md)

## WIA and STI Driver Reference

The following table contains reference information for Windows Image Acquisition (WIA) drivers and for Still Imaging (STI) drivers. These drivers control devices, including scanners and cameras, that capture still images. For more information about these drivers, see [Windows Image Acquisition Drivers](./windows-image-acquisition-drivers.md) and [Still Image Drivers](./still-image-drivers.md).

The following sections describe the interfaces, functions, structures, and properties used by WIA and STI drivers.

| Section | Description |
|--|--|
| [Device Interface Classes for Imaging Devices](device-interface-classes-for-imaging-devices.md) | Device class GUID for imaging devices. |
| [IWiaMiniDrv Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) | Interface for managing all communications between a WIA minidriver and the WIA service. |
| [WIA Driver Services Library Functions](/windows-hardware/drivers/ddi/wiamdef/index) | Helper functions used by a WIA minidriver to manage device items and data transfers. |
| [WIA Properties](wia-properties.md) | Properties of WIA devices, including status, capabilities, and device identification information. |
| [WIA Utility Library Functions and Classes](/windows-hardware/drivers/ddi/_image/index) | Utility functions and classes used by a WIA minidriver to support debugging and to perform common tasks. |
| [IWiaMiniDrvCallBack Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback) | Callback interface for transferring status and image data between the WIA service and a WIA minidriver. |
| [IWiaDrvItem Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem) | Interface used by a WIA minidriver to manage a tree of WIA driver items. |
| [IWiaErrorHandler Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiaerrorhandler) | Interface used by a WIA minidriver to provide error status and to support error recovery. |
| [IWiaImageFilter Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiaimagefilter) | Interface implemented by an image processing filter and called by the WIA service to communicate with the filter. |
| [IWiaLog Interface and Diagnostic Log Macros](/windows-hardware/drivers/ddi/_image/index) | Interface and macros used by a WIA minidriver to record trace, error, and warning messages to a diagnostic log file. |
| [IWiaSegmentationFilter Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiasegmentationfilter) | Interface used by a WIA minidriver to detect regions in a segmented image. |
| [IWiaTransferCallback Interface](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwiatransfercallback) | Interface implemented by an image processing filter and called by the WIA service to initiate the processing of image streams. |
| [WIA Microdriver Functions, Structures, and Commands](/windows-hardware/drivers/ddi/_image/index) | Functions, structures, and commands used by WIA microdrivers. |
| [WIA User Interface Extensions](/windows-hardware/drivers/ddi/wiadevd/index) | Interface used by device vendors to provide custom user interfaces for their devices. |
| [WIA Structures](/windows-hardware/drivers/ddi/_image/index) | Structures used by driver-level WIA methods and functions. |
| [Still Image Interfaces](/windows-hardware/drivers/ddi/_image/index) | Interfaces, structures, data types, and control codes used by STI drivers. |
| [Web Services on Devices Reference](./scan-service--ws-scan--schema.md) | Web Services on Devices information, including Scan Service (WS-SCAN) |

## Related sections

[Imaging DDI reference](/windows-hardware/drivers/ddi/_image)
