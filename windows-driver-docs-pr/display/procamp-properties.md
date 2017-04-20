---
title: ProcAmp Properties
description: ProcAmp Properties
ms.assetid: 412c9144-dd52-4b36-bea1-b17c9c2c95b3
keywords:
- ProcAmp WDK DirectX VA , properties
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ProcAmp Properties


## <span id="ddk_procamp_properties_gg"></span><span id="DDK_PROCAMP_PROPERTIES_GG"></span>


A display driver must supply minimum, maximum, step size, and default values when the VMR queries the driver for information about ProcAmp properties. The driver can supply this information in response to a call to its [**ProcAmpControlQueryRange**](https://msdn.microsoft.com/library/windows/hardware/ff563950) function. Although the driver can return any value for the ProcAmp properties, the following are the recommended settings (all values are floats).

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Property</th>
<th align="left">Minimum</th>
<th align="left">Maximum</th>
<th align="left">Default</th>
<th align="left">Increment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Brightness</p></td>
<td align="left"><p>-100.0F</p></td>
<td align="left"><p>100.0F</p></td>
<td align="left"><p>0.0F</p></td>
<td align="left"><p>0.1F</p></td>
</tr>
<tr class="even">
<td align="left"><p>Contrast</p></td>
<td align="left"><p>0.0F</p></td>
<td align="left"><p>10.0F</p></td>
<td align="left"><p>1.0F</p></td>
<td align="left"><p>0.01F</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Saturation</p></td>
<td align="left"><p>0.0F</p></td>
<td align="left"><p>10.0F</p></td>
<td align="left"><p>1.0F</p></td>
<td align="left"><p>0.01F</p></td>
</tr>
<tr class="even">
<td align="left"><p>Hue</p></td>
<td align="left"><p>-180.0F</p></td>
<td align="left"><p>180.0F</p></td>
<td align="left"><p>0.0F</p></td>
<td align="left"><p>0.1F</p></td>
</tr>
</tbody>
</table>

 

It is important that the default values result in a *null* transform of the video stream. This allows the VMR to bypass the ProcAmp adjustment stage in its video pipeline if an application has not altered any of the ProcAmp control properties.

The VMR and the display driver perform certain validations when working with ProcAmp properties. The VMR enforces the following parameter validations before calling a driver:

-   The VMR ensures that values supplied by applications fall within the valid range as specified by the driver. The VMR clamps any application-provided values to the specified range. For example, if the maximum value for brightness is 100, and the application supplies a value of 105, the VMR clamps the application's value to 100. When the application queries the VMR to determine the current brightness setting, it receives the clamped value, in this case 100.

-   The VMR also makes any necessary rounding to the application-provided value to ensure that the values fall on the nearest location as indicated by the step size increment returned by your driver. For example, if the brightness step size increment is 0.5, the minimum permitted brightness value is -100.0, and the application supplies a value of -80.7. The VMR adjusts the application's value to the nearest valid value, -80.5 in this case.

The driver should ensure that the following relationships hold:

-   The maximum range value is greater than the minimum range value. This implies that the difference between the maximum and minimum value is greater than 0.0.

-   The default and maximum values fall on valid locations as specified by the step size increment, as shown in the following expressions:
    ```
    min + (int((default - min) / increment) * increment) == default
    min + (int((max - min) / increment) * increment) == max
    ```

-   Because applications usually use Windows' slider controls to display ProcAmp settings, and because the maximum range of Windows' slider controls is 65536, drivers should keep the number of distinct ProcAmp values to fewer than 65536. The following inequality should be true for the values chosen:
    ```
    int((max - min) / increment) < 65536.
    ```

-   For ProcAmp properties that are not supported by your hardware, the driver should return the maximum value, minimum value, and default value with a step size increment of 0.0.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20ProcAmp%20Properties%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




