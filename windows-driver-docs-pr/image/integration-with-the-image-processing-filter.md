---
title: Integration with the Image Processing Filter
description: Integration with the Image Processing Filter
ms.assetid: ae5c6209-c95a-424c-9151-caeb8e6b3f8c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Integration with the Image Processing Filter


Stream-based data transfers allow easy integration of the [WIA Image Processing Filter](wia-image-processing-filter.md) with a WIA driver because the stream is provided by the caller and the WIA driver takes the same action no matter what the destination stream is. That is, the driver simply asks for a stream and then writes to it, no matter what type of stream is returned to the driver.

The WIA Image Processing Filter is required to implement **IStream**. When this filter is created, it is given the application's destination stream, which it should then delegate (or forward) its calls to. In other words, when **IStream::Write** is called on the filter, it should process the buffer and then call **IStream::Write** on the destination stream with the processed buffer.

Similarly, the Image Processing Filter can give a stream to the driver so that data can be written from the driver to the Image Processing Filter, which then writes to the application's destination stream. Note that if no filter is present, the driver does not change but continues to write to the stream.

This situation is shown graphically in the following figures. The first figure illustrates a stream-based data transfer when the Image Processing Filter is not used.

![diagram illustrating an istream transfer without the image-processing filter](images/streamtrans-no-filter.png)

The second figure illustrates stream-based data transfer when the Image Processing Filter is used.

![diagram illustrating an istream transfer with the image-processing filter](images/streamtrans-with-filter.png)

Notice that the driver's behavior does not change; the driver receives a stream and writes to it whether the stream is provided by the Image Processing Filter or by an application directly. As a result, you can publish value-add image processing components separately. For example, you could provide an in-box driver that is functional but could provide better quality images when the user installs the image processing component from a CD. The driver does not need to be changed in this situation.

The **IStream** interface and its methods are described in the Microsoft Windows SDK documentation.

 

 




