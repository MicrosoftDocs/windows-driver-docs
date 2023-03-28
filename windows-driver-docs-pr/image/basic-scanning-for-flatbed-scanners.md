---
title: Basic Scanning for Flatbed Scanners
description: Basic Scanning for Flatbed Scanners
ms.date: 03/27/2023
---

# Basic Scanning for Flatbed Scanners

A WIA application enumerates the root item and top-level child item in the scanner item tree to determine the supported features of the scanner. The application then uses this child item as the scanning source. For example, flatbed scanner items are used for scanning from the flatbed, while feeder items are used for scanning from the document feeder, and so on.

The programming and scanning behavior of the flatbed item in Windows Vista is identical to the overload system that is used by Windows XP and Windows Me. This overload system programs the first child item in the item tree by putting all of the WIA attribute flags on it.

An application will normally perform the following operations when it programs the scanner's flatbed, but not necessarily in this order:

- Enumerate top-level WIA items and look for items that are marked with the **WiaItemTypeProgrammableDataSource** item flag and with the [**WIA_IPA_ITEM_CATEGORY**](./wia-ipa-item-category.md) property set to WIA_CATEGORY_FLATBED.

- Read the valid values for the [**WIA_IPA_TYMED**](./wia-ipa-tymed.md) and [**WIA_IPA_FORMAT**](./wia-ipa-format.md) properties.

- Choose either a memory transfer or file transfer type by setting the WIA_IPA_TYMED property. For more information about the available types of transfers, see [Data Transfers](data-transfers.md). For **IStream**-based transfers, WIA_IPA_TYMED is set by default to TYMED_FILE and should not be changed.

- Choose the final format of the data by setting the WIA_IPA_FORMAT property.

- Choose the image settings, such as [**WIA_IPA_DEPTH**](./wia-ipa-depth.md) and [**WIA_IPA_DATATYPE**](./wia-ipa-datatype.md).

- Transfer the data using this WIA item.

The driver will normally perform the following operations when it uses the scanner's flatbed to scan:

1. Call [**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties) and [**IWiaMiniDrv::drvReadItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvreaditemproperties). The WIA driver should validate any property settings during the application's property-setting phase.

2. Call [**IWiaMiniDrv::drvWriteItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties). The WIA item context that is passed in belongs to the flatbed scanner item so that the driver knows that the application intends to use the scanner's flatbed to scan.

3. Call [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata). The WIA item context that is passed in belongs to the flatbed scanner item, so the driver can easily determine that the application intends to scan by using the flatbed platen.

4. Program the device and scan from the flatbed, using the current flatbed item properties. If the WIA driver is not in flatbed scanning mode, it should attempt to switch to this mode for the scan. There is no special setting for the application to toggle to use the flatbed. Using the flatbed item to scan is a contract between the application and the driver; they agree that the flatbed is to be used for the data transfer.

The driver must use the WIA properties on the flatbed scanner item as settings to be applied to the flatbed part of the scanner before the scan. The WIA application is required to always trust the headers of the data that is returned by the WIA driver. For example, if a scanner determines that it cannot scan an image of a specified width and, as a result, rounds the value to a width that it can scan, the driver should update the image headers with the modified width information. This update ensures that correct information is available to the application. The WIA driver should attempt to update the WIA properties with the actual information that is returned from the device.

## Advanced Scanning for Flatbed Scanners

Multi-region scanning from the flatbed is possible either though manual configuration or by automatically using the [WIA Segmentation Filter](wia-segmentation-filter.md). Note that the segmentation filter is no different from an application in what it can and cannot do. The same procedures that are described for the segmentation filter can be run directly by the application to create child items for new scan regions.
