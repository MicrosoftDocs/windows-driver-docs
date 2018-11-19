---
title: Adding Document Feeder Support for Windows Me and Windows XP
description: Adding Document Feeder Support for Windows Me and Windows XP
ms.assetid: f3be94fa-6fb7-45de-a3ce-f3d173e802cf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Document Feeder Support for Windows Me and Windows XP





A document feeder is a unit attached to or built into a scanner that automatically feeds paper documents in a position to be scanned. For a scanner with a document feeder, the functionality is exposed and controlled through the addition of the properties contained in the following list. For Windows Me and Windows XP, the following properties are located on the root item.

[**WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551401)

[**WIA\_DPS\_VERTICAL\_SHEET\_FEED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551446)

[**WIA\_DPS\_MIN\_HORIZONTAL\_SHEET\_FEED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551405)

[**WIA\_DPS\_MIN\_VERTICAL\_SHEET\_FEED\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551407)

[**WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff551430)

[**WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551379)

[**WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff551386)

[**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384)

[**WIA\_DPS\_PAGES**](https://msdn.microsoft.com/library/windows/hardware/ff551414)

For Windows Me and Windows XP, the following optional document feeder properties are located on the child item:

[**WIA\_DPS\_PAGE\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551417)

[**WIA\_DPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff551419)

[**WIA\_DPS\_PAGE\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff551416)

[**WIA\_IPS\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552625)

If a device has a flatbed, a document feeder, and a duplexer, the driver reports the WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property as (FEED | FLAT | DUP). Make sure that the valid values for WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT are set correctly.

As an example, suppose an application intends to perform a duplex scan of three pages from the document feeder. To accomplish this, the application sets the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to (FEEDER | DUPLEX) and sets the WIA\_DPS\_PAGES property to 3. If the application intends to scan the front of the page first, it should set the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to (FEEDER | DUPLEX | FRONT\_FIRST). After this is done, the application should navigate to the child item from which it should request a data transfer. The minidriver reports the front of the first page in the feeder as page one, the back of that page as page two, and the front of the second page in the feeder as page three.

It is important to remember that if the device has a document feeder, it must support the document feeder properties.

### Acquiring Data from a Document Feeder

There are a few changes that must be made in the implementation of the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method when the scanner acquires images from a document feeder.

1.  1. An application reads the WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property to determine whether the scanner supports scanning using the document feeder.

2.  2. An application reads the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property to determine whether the scanner is configured to scan using the document feeder.

3.  3. An application determines whether there is paper in the document feeder by reading WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS. If there is no paper in the feeder, set the WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS to the proper status code and return WIA\_ERROR\_PAPER\_EMPTY from **IWiaMiniDrv::drvAcquireItemData** immediately after an acquisition takes place.

4.  4. Check the WIA\_DPS\_PAGES property to determine the scanning behavior. If this property is zero, scan all pages until the feeder is empty. If it is positive, scan only the number of pages indicated by the value contained in the WIA\_DPS\_PAGES property.

5.  5. Scan the requested number of pages by controlling a loop, continually scanning, and sending data (one page at a time) to the WIA application by calling the [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946) method. The following is a code example of how this might work:

6.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><pre><code>for(int x = 1; x &lt;= Pagecount; x++){
      \\ Tell scanner to scan an image.
      \\ Receive image data from scanner.
      \\ Send the just-scanned image to the registered application.
    }</code></pre></td>
    </tr>
    </tbody>
    </table>

7.  6. If [**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656) is set to TYMED\_CALLBACK or TYMED\_MULTIPAGE\_CALLBACK, then an extra message (IT\_MSG\_NEW\_PAGE) must be sent after one page has been scanned and before the next one is to be scanned. This is done by calling the [**wiasSendEndOfPage**](https://msdn.microsoft.com/library/windows/hardware/ff549351) WIA service utility function.

The number of pages that a document feeder driver returns depends on the setting of the WIA\_DPS\_PAGES property.

### <a href="" id="if-wia-dps-pages-is-zero-"></a>If WIA\_DPS\_PAGES is zero:

1.  1. If the scanner is unable to scan the first page, return an error code immediately. This includes paper jams and when the scanner runs out of paper.

2.  2. If the scanner successfully scans the first page and is able to continue scanning but has run out of paper, return the success code WIA\_STATUS\_END\_OF\_MEDIA. This signals the application that the transfer was successful, but the scanner has run out of paper. Some applications respond to WIA\_ERROR\_PAPER\_EMPTY in the same way as they would to WIA\_STATUS\_END\_OF\_MEDIA.

3.  3. If the scanner successfully scans the first page and is able to continue scanning but encounters an error that does not result in data loss, return WIA\_STATUS\_END\_OF\_MEDIA. This allows the application to recover and to save any pages scanned before the error occurred. Any subsequent scans should return an error code immediately until the scanner has properly recovered from the failure.

4.  4. If the scanner successfully scans the first page and is able to continue scanning but encounters an error that does result in data loss, return an error code immediately.

### <a href="" id="if-wia-dps-pages-is-positive-"></a>If WIA\_DPS\_PAGES is positive:

1.  1. All rules for which WIA\_DPS\_PAGES is zero apply.

2.  2. If the scanner runs out of paper before the requested number of pages are scanned, return WIA\_STATUS\_END\_OF\_MEDIA. This allows the application to close the scanning session, thus preserving the number of pages it already scanned successfully. Some applications respond to WIA\_ERROR\_PAPER\_EMPTY the same way as they would to WIA\_STATUS\_END\_OF\_MEDIA.

 

 




