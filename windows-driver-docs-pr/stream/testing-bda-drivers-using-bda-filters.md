---
title: Testing BDA Drivers Using BDA Filters
author: windows-driver-content
description: Testing BDA Drivers Using BDA Filters
ms.assetid: 136810b7-9378-482b-8e21-a7eae0142909
keywords:
- Broadcast Driver Architecture WDK AVStream , testing drivers
- BDA WDK AVStream , testing drivers
- testing drivers WDK , BDA
- DirectShow filters WDK AVStream
- Graph Editor WDK BDA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Testing BDA Drivers Using BDA Filters


## <a href="" id="ddk-testing-bda-drivers-using-bda-filters-ksg"></a>


You can use the DirectShow Filter Graph Editor (*Graphedt.exe*) to insert a DirectShow filter instance of your BDA component in a filter graph so that you can test your component. You can obtain the Graph Editor from the Microsoft Windows Driver Kit (WDK).

You can use the Graph Editor to perform rudimentary tests of a BDA component, such as, connecting pins that are exposed by a filter instance of the component to other pins of filter types in the graph.

To use the Graph Editor to thoroughly test functionality of your BDA component, you must build a filter graph that starts with a BDA network provider filter, contains a filter instance of your BDA component, and is rendered, at least, through a demultiplexer filter (packet identifier (PID) filter) to a transport information filter (TIF). The biggest problem with using the Graph Editor is that there is no dedicated application to submit requests via the **ITuner** interface that the network provider filter implements. However, the network provider filter has associated property pages that provide some limited ability to exercise the **ITuner** interface.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Testing%20BDA%20Drivers%20Using%20BDA%20Filters%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


