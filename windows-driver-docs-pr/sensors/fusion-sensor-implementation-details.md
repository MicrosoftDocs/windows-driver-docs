---
title: Fusion sensor implementation details
author: windows-driver-content
description: This section provides implementation details about the Windows fusion sensor driver stack.
ms.assetid: B53D76AC-127C-4B5A-B908-A647D2B3F164
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Fusion sensor implementation details


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This section provides implementation details about the Windows fusion sensor driver stack.

**Note**  Partners cannot, and are not required to, implement a fusion driver. Microsoft provides the fusion driver binaries and these may not be replaced by partners.

 

The following diagram shows the sensor fusion software stack.

![a diagram showing the fusion sensor stack](images/fusion-sensor-stack.png)

The fusion software stack consists of the following components:

-   The **sensor native APIs** are called by applications to access fusion and compass features and functionality. The APIs are wrappers for ReadFile and DeviceIoControl. These APIs are sent to the sensor class extension, which then processes and completes the request.

-   The **sensor class extension** provides support for any required sensor-specific extensibility.

-   The **fusion driver** is the function-specific software part of the driver. It reads the physical sensors and processes the data. The algorithm for the compass and fusion sensor is implemented in this component.

## Coordinate systems


The coordinate system shown in the following diagram is used for all physical sensors and fusion data.

![a diagram showing gyroscope device orientation](images/gyroscope-orientation.png)

The coordinate system shown in the following diagram is the convention used by the fusion algorithm and APIs for all vectors in the Earth/ground frame of reference.

![a diagram showing the earth coordinate system used by the fusion algorithm](images/earth-coordinatesystem.png)

## Data structures


The following structures and enumerations are used by the fusion data part of the logical sensor driver:

-   [**VEC3D**](https://msdn.microsoft.com/library/windows/hardware/dn946712)

-   [**COORDINATE\_AXIS**](https://msdn.microsoft.com/library/windows/hardware/dn957021)

-   [**QUATERNION**](https://msdn.microsoft.com/library/windows/hardware/dn957081)

-   [**MATRIX3X3**](https://msdn.microsoft.com/library/windows/hardware/dn957074)

-   [Fusion sensor enumerations](https://go.microsoft.com/fwlink/p/?linkid=839352) and [Fusion sensor structures](https://go.microsoft.com/fwlink/p/?linkid=839355) provide information about the entire sensor fusion data structure, which include the attitude (in multiple formats) and the linear acceleration, and the compass data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Fusion%20sensor%20implementation%20details%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


