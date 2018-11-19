---
title: WIA Flatbed Driver
description: WIA Flatbed Driver
ms.assetid: 83c35b1f-10e0-47e1-97cc-5a7a79fb8088
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Flatbed Driver





The system-supplied WIA Flatbed Driver and the vendor-supplied microdriver combine to make a WIA minidriver. The WIA Flatbed Driver receives requests from the WIA service and routes the requests to the WIA microdriver through the microdriver functions. The WIA Flatbed Driver sends requests to the WIA microdriver, which sends responses back to the WIA Flatbed Driver. The WIA Flatbed Driver then sends these responses to the WIA service.

The following is a description of the capabilities of the WIA Flatbed Driver:

### Minimum WHQL WIA Properties

The WIA Flatbed Driver implements only a subset of the available properties and does not allow for any extensions by the vendor. It implements only those properties required by the WHQL specification. See the WHQL requirement specification for details.

### Supported Data Types

The following data types are supported:

-   1-bit black/white

-   8-bit grayscale

-   24-bit color

The microdriver can exclude data types not supported by the device.

### File Formats

The default file format is bitmap (BMP). Other format support can be added using the [WIA microdriver optional command](https://msdn.microsoft.com/library/windows/hardware/ff546016) CMD\_SETFORMAT.

### Supported Transfer Types

Both the file transfer and callback transfer types are supported.

### Resolution

By default, the following resolutions are supported: 75, 100, 150, 200, 300, and 600 dpi.

Because the range of resolutions varies based on the device, you can specify the list of possible resolutions by adding an entry such as the following to your setup information (INF) file:

```INF
[DeviceData]
Resolutions="75, 100, 300, 600, 1200"
```

**Note**   Remember to put a space after each comma.
It is possible to use the **IWiaItem::DeviceDlg** method (described in the Microsoft Windows SDK documentation) to get user input on selecting a "custom" resolution.

 

### ADF

Only simple Automatic Document Feeder (ADF) control is supported.

 

 




