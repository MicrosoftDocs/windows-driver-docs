---
title: WIA Flatbed Driver
author: windows-driver-content
description: WIA Flatbed Driver
ms.assetid: 83c35b1f-10e0-47e1-97cc-5a7a79fb8088
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Flatbed Driver


## <a href="" id="ddk-wia-flatbed-driver-si"></a>


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

```
[DeviceData]
Resolutions="75, 100, 300, 600, 1200"
```

**Note**   Remember to put a space after each comma.
It is possible to use the **IWiaItem::DeviceDlg** method (described in the Microsoft Windows SDK documentation) to get user input on selecting a "custom" resolution.

 

### ADF

Only simple Automatic Document Feeder (ADF) control is supported.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Flatbed%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


