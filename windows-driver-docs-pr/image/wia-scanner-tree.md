---
title: WIA scanner tree
description: The WIA scanner tree provides information about the root item (scanner) and each child item that consists of properties common to both camera and scanner.
ms.date: 07/06/2020
ms.localizationpriority: medium
---

# WIA scanner tree

The following figure shows a scanner and an image that it produced.

![diagram illustrating a scanner and an image that it produced.](images/art-scanner.png)

The next figure shows a Microsoft Windows Me or Windows XP scanner, or a scanner on Windows Vista if that scanner has no document feeder, duplexer or film scanner.

WIA represents the scanner and its image shown in the preceding figure as an item tree, as in the following figure.

![diagram illustrating how wia represents the scanner and its image as an item tree.](images/art-4.png)

The root item, which is the scanner itself, consists of common device properties (properties that are common to both cameras and scanners), and scanner-specific device properties. Similarly, each child item consists of properties common to both camera and scanner items, as well as properties that are specific to scanner items.

Through the WIA service, an application can request the following from a scanner item:

- Query scanner capabilities

- Set scanner device properties

- Request a data transfer

In Windows Me and Windows XP, directly below the root item, a typical scanner object has a single item, the scanner item, which represents the data-collecting functionality of the device. An application sets up a scan by setting the properties of the scanner item. The scan is executed when the application requests data, through the WIA service, from the item.

In Windows Me and Windows XP, applications typically expect flatbed scanners, including those with automatic document feeders (ADFs), to be represented by two items--a root item and a single child. All data transfers are performed from the child item. A driver may choose to create other items for its private use, and these items can be made transfer-capable. (To do so, set the WiaItemTypeTransfer bit of the item type flag in a call to [**wiasCreateChildAppItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatechildappitem). This constant is documented in the Microsoft Windows SDK documentation.) However, applications generally do not know about these private items, and do not know how to manipulate them. For a scanner with an ADF, in Windows Me or Windows XP, the ADF functionality is exposed and controlled by adding the WIA\_DPS\_DOCUMENT\_HANDLING\_*XXX* properties to the scanner's root item, rather than to the scanner's child item. For more information about these properties, see [WIA Properties](./wia-properties.md). For information about a scanner with an ADF in Windows Vista, see [WIA Feeder Scanners](wia-feeder-scanners.md).

If a device has a flatbed and an ADF, and can do DUPLEX scans, in Windows Me or Windows XP, a driver would report the [**WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES**](./wia-dps-document-handling-capabilities.md) property as (FEED &#x7c; FLAT &#x7c; DUP).

Make sure that the valid values for [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](./wia-dps-document-handling-select.md) are set correctly. Note that all documents scanned in a single scan job will exist in a single child item in the item tree. For information about a scanner with an ADF and a duplexer on Windows Vista, see [WIA Feeder Scanners](wia-feeder-scanners.md).

As an example, suppose that an application intends to perform a duplex scan of three pages from the ADF. To accomplish this, the application would set the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to (FEEDER &#x7c; DUPLEX), and would set the [**WIA\_DPS\_PAGES**](./wia-dps-pages.md) property to 3. If the application wants to scan the front of the page first, it should set the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to (FEEDER &#x7c; DUPLEX &#x7c; FRONT\_FIRST). After this is done, the application should navigate to the child item from which it would request a data transfer. The minidriver would report the front of the first page in the ADF as page 1, the back of that page as page 2, and the front of the second page in the ADF as page 3.

It is important to remember that if the device has an ADF, it must support the ADF properties.
