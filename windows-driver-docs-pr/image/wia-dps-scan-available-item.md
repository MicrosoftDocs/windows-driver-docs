---
title: WIA\_DPS\_SCAN\_AVAILABLE\_ITEM
description: The WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property provides the name of the input source for a push-scan operation that the application performs under program control. The WIA minidriver creates and maintains this property.
ms.assetid: 747cd5bb-4746-4086-8a87-08a6728125bc
keywords: ["WIA_DPS_SCAN_AVAILABLE_ITEM Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SCAN_AVAILABLE_ITEM
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_SCAN\_AVAILABLE\_ITEM


The WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property provides the name of the input source for a push-scan operation that the application performs under program control. The WIA minidriver creates and maintains this property.

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

In Windows 7 and later, WIA\_DPS\_SCAN\_AVAILABLE\_ITEM is an optional property of the root item in the WIA item tree of a WIA scanner device. An application can query this property to determine the input source (flatbed, automatic document feeder, or film-scanning adapter) to scan from, or the storage location to transfer data from.

Some WIA scanner devices enable a user to select an input source for a scanning job from the device's front panel, or to implicitly select an input source, for example, by inserting a document into a feeder on the device. When the user presses the start-scan button on the device, the application must determine which input source the user has selected so that it can initiate a scanning operation on this source.

A scan event notifies the application that the user has initiated a scan, but the event does not supply the name of the WIA item that represents the input source. The application's event handler can query the root item's WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property to get the name of the input source item.

The root item in a WIA tree has one or more child items (flatbed item, feeder item, and film item) that represent input sources on the device. Each of these items might be a parent to child items that represent parts or regions of the input source. A flatbed item that is a child of the root item and that represents the flatbed as a whole can have children (which are also flatbed items) that represent the individual regions of the flatbed surface. A feeder item that is a child of the root item and that represents an automatic document feeder can have children that represent the scanners for the front and back sides of the document pages that pass through the feeder. A film item that is a child of the root item and that represents the film-scanning adapter as a whole can have children (which are also film items) that represent individual film frames. Depending on the scanning operation requested by the user, the WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property can name a flatbed, feeder, or film item that is a child of the root, or it can name a child of one of these items. For more information about these items, see [WIA Item Categories](https://msdn.microsoft.com/library/windows/hardware/ff552678).

When a scan event occurs, the driver immediately sets the WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property value to a WIA item name (exactly as reported by the [**WIA\_IPA\_ITEM\_NAME**](wia-ipa-item-name.md) property of the item) that identifies the input source from which the scan job is available, if this information is known. Otherwise, if the input source is unknown, the driver sets the property value to an empty string. When the application consumes the scan event, the state of the scan event changes from signaled to nonsignaled, and the driver resets the WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property value to an empty string.

For more information about this property, see [Identifying the Input Source for a Scan Event](https://msdn.microsoft.com/library/windows/hardware/ff542704).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPA\_ITEM\_NAME**](wia-ipa-item-name.md)

 

 






