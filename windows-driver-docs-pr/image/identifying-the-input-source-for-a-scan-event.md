---
title: Identifying the Input Source for a Scan Event
description: Identifying the Input Source for a Scan Event
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# Identifying the Input Source for a Scan Event

A *push-scan* operation is a scanning operation that the user initiates from a WIA scanner device instead of from the user interface of a WIA application running on a desktop computer. When the user presses the start-scan button on the device, the application receives a scan event to notify it that the user has requested a scanning operation. In response to this event, the application can perform the push-scan operation in one of the following two ways:

- If the device supports [auto-configured scanning](auto-configured-scanning.md), the application can request a data transfer from the [auto item](auto-item.md) to acquire an image from the currently selected input source (flatbed, automatic document feeder, or film-scanning adapter). In response, the device automatically configures its scan settings (excluding the few properties that can be configured only by the application, which are described in [WIA Properties Supported by an Auto Item](wia-properties-supported-by-an-auto-item.md)) and then acquires the image.

- The application can perform the scanning operation under direct program control. First, the application configures the properties of the WIA item (flatbed item, feeder item, or film item) that represents the currently selected input source. Next, the application acquires an image by requesting a data transfer from this item.

For more information about WIA items, see [WIA Item Categories](wia-item-categories.md).

When a scan event occurs, the application receives a notification that includes a WIA event identifier (a GUID value) to specify the nature of the event. The WIA minidriver can assign a custom WIA event identifier GUID to an event, or the minidriver can use one of the WIA\_EVENT\_SCAN\_*XXX* GUID constants defined in header file *Wiadef.h*. For more information about these constants, see [WIA Event Identifiers](/windows/win32/wia/-wia-wia-event-identifiers).

Although the WIA event identifier for a scan event provides information about the event, it does not identify the input source to use for the scanning operation. For auto-configured scanning, the application does not need this information. However, to perform a scan under direct program control, the application must know which input source to use. The application must have a way to obtain this information from the device if the device has more than one input source and the user can select the input source from the device instead of from the user interface of the application. When selecting an input source from the device, the user can select the source either explicitly (by pressing a button on the device's front panel) or implicitly (for example, by inserting a document into a feeder on the device).

When a scan event occurs, an application can query the WIA scanner device's WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property to identify the selected input source, if the device supports this property. WIA\_DPS\_SCAN\_AVAILABLE\_ITEM is an optional property of the root item in a device's WIA item tree. For more information about this property, see [**WIA\_DPS\_SCAN\_AVAILABLE\_ITEM**](./wia-dps-scan-available-item.md).

The WSD scan class driver implements the WIA\_DPS\_SCAN\_AVAILABLE\_ITEM property as a standard driver feature, as described in the preceding paragraph, instead of as a custom driver extension. For more information about the WSD scan class driver, see [WIA with Web Services for Devices](wia-with-web-services-for-devices.md). For more information about WDP for scanners, see [Web Services for Devices Scan Service Schema](./scan-service--ws-scan--schema.md).
