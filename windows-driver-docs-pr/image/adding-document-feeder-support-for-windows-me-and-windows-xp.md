---
title: Adding document feeder support for Windows Me and Windows XP
description: Adding document feeder support for Windows Me and Windows XP
ms.date: 07/06/2020
ms.localizationpriority: medium
---

# Adding document feeder support

A document feeder is a unit attached to or built into a scanner that automatically feeds paper documents in a position to be scanned. For a scanner with a document feeder, the functionality is exposed and controlled through the addition of the properties contained in the following list. For Windows Me and Windows XP, the following properties are located on the root item:

- [**WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE**](./wia-dps-horizontal-sheet-feed-size.md)

- [**WIA\_DPS\_VERTICAL\_SHEET\_FEED\_SIZE**](./wia-dps-vertical-sheet-feed-size.md)

- [**WIA\_DPS\_MIN\_HORIZONTAL\_SHEET\_FEED\_SIZE**](./wia-dps-min-horizontal-sheet-feed-size.md)

- [**WIA\_DPS\_MIN\_VERTICAL\_SHEET\_FEED\_SIZE**](./wia-dps-min-vertical-sheet-feed-size.md)

- [**WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION**](./wia-dps-sheet-feeder-registration.md)

- [**WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES**](./wia-dps-document-handling-capabilities.md)

- [**WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS**](./wia-dps-document-handling-status.md)

- [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](./wia-dps-document-handling-select.md)

- [**WIA\_DPS\_PAGES**](./wia-dps-pages.md)

For Windows Me and Windows XP, the following optional document feeder properties are located on the child item:

- [**WIA\_DPS\_PAGE\_SIZE**](./wia-dps-page-size.md)

- [**WIA\_DPS\_PAGE\_WIDTH**](./wia-dps-page-width.md)

- [**WIA\_DPS\_PAGE\_HEIGHT**](./wia-dps-page-height.md)

- [**WIA\_IPS\_ORIENTATION**](./wia-ips-orientation.md)

If a device has a flatbed, a document feeder, and a duplexer, the driver reports the WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property as `FEED | FLAT | DUP`. Make sure that the valid values for WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT are set correctly.

As an example, suppose an application intends to perform a duplex scan of three pages from the document feeder. To accomplish this, the application sets the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to (FEEDER | DUPLEX) and sets the WIA\_DPS\_PAGES property to 3. If the application intends to scan the front of the page first, it should set the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to `FEEDER | DUPLEX | FRONT\_FIRST`. After this is done, the application should navigate to the child item from which it should request a data transfer. The minidriver reports the front of the first page in the feeder as page one, the back of that page as page two, and the front of the second page in the feeder as page three.

It is important to remember that if the device has a document feeder, it must support the document feeder properties.

## Acquiring data from a document feeder

There are a few changes that must be made in the implementation of the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method when the scanner acquires images from a document feeder.

1. An application reads the WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property to determine whether the scanner supports scanning using the document feeder.

1. An application reads the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to determine whether the scanner is configured to scan using the document feeder.

1. An application determines whether there is paper in the document feeder by reading WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS. If there is no paper in the feeder, set the WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS to the proper status code and return WIA\_ERROR\_PAPER\_EMPTY from **IWiaMiniDrv::drvAcquireItemData** immediately after an acquisition takes place.

1. Check the WIA\_DPS\_PAGES property to determine the scanning behavior. If this property is zero, scan all pages until the feeder is empty. If it is positive, scan only the number of pages indicated by the value contained in the WIA\_DPS\_PAGES property.

1. Scan the requested number of pages by controlling a loop, continually scanning, and sending data (one page at a time) to the WIA application by calling the [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback) method. The following code example shows how this might work:

    ```cpp
    for(int x=1; x=Pagecount; x++)
    {
        \\ Tell scanner to scan an image.
        \\ Receive image data from scanner.
        \\ Send the just-scanned image to the registered application.
    }
    ```

1. If [**WIA\_IPA\_TYMED**](./wia-ipa-tymed.md) is set to TYMED\_CALLBACK or TYMED\_MULTIPAGE\_CALLBACK, then an extra message (IT\_MSG\_NEW\_PAGE) must be sent after one page has been scanned and before the next one is to be scanned. This is done by calling the [**wiasSendEndOfPage**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassendendofpage) WIA service utility function.

The number of pages that a document feeder driver returns depends on the setting of the WIA\_DPS\_PAGES property.

## If WIA\_DPS\_PAGES is zero

1. If the scanner is unable to scan the first page, return an error code immediately. This includes paper jams and when the scanner runs out of paper.

1. If the scanner successfully scans the first page and is able to continue scanning but has run out of paper, return the success code WIA\_STATUS\_END\_OF\_MEDIA. This signals the application that the transfer was successful, but the scanner has run out of paper. Some applications respond to WIA\_ERROR\_PAPER\_EMPTY in the same way as they would to WIA\_STATUS\_END\_OF\_MEDIA.

1. If the scanner successfully scans the first page and is able to continue scanning but encounters an error that does not result in data loss, return WIA\_STATUS\_END\_OF\_MEDIA. This allows the application to recover and to save any pages scanned before the error occurred. Any subsequent scans should return an error code immediately until the scanner has properly recovered from the failure.

1. If the scanner successfully scans the first page and is able to continue scanning but encounters an error that does result in data loss, return an error code immediately.

## If WIA\_DPS\_PAGES is positive

1. All rules for which WIA\_DPS\_PAGES is zero apply.

1. If the scanner runs out of paper before the requested number of pages are scanned, return WIA\_STATUS\_END\_OF\_MEDIA. This allows the application to close the scanning session, thus preserving the number of pages it already scanned successfully. Some applications respond to WIA\_ERROR\_PAPER\_EMPTY the same way as they would to WIA\_STATUS\_END\_OF\_MEDIA.
