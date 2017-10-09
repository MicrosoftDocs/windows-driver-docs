---
title: DIF\_DETECT
description: DIF\_DETECT
ms.assetid: 866a99fc-f48e-447d-b5eb-6339dc98d3f2
keywords: ["DIF_DETECT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_DETECT
api_location:
- Setupapi.h
api_type:
- HeaderDef
---

# DIF\_DETECT


A DIF\_DETECT request directs an installer to detect non-PnP devices of a particular class and add the devices to the device information set. This request is used for non-PnP devices.

### When Sent

When the **Add Hardware Wizard** is detecting non-PnP devices.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class Co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device Co-installer</p></td>
<td align="left"><p>Does not handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247). There is a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) associated with the *DeviceInfoSet*.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
None

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters associated with the *DeviceInfoSet*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP\_DETECTDEVICE\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552341) structure is associated with the *DeviceInfoSet*. The parameters contain a callback routine that the class installer calls to indicate the progress of the detection operation.

### Installer Output

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
An installer adds a device information element to the *DeviceInfoSet* for each device it detects, regardless of whether a device was previously detected and installed.

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters for the *DeviceInfoSet* or for new device information elements it creates.

### Installer Return Value

If a co-installer does not detect devices, it returns NO\_ERROR from its preprocessing pass. If a co-installer detects devices, it can do so during preprocessing or postprocessing and return NO\_ERROR or a Win32 error code.

If a class installer detects devices, it returns NO\_ERROR or an appropriate Win32 error code. If a class installer does not handle this DIF request, it returns ERROR\_DI\_DO\_DEFAULT.

### Default DIF Code Handler

None

### Installer Operation

In response to a DIF\_DETECT request an installer can detect devices of its setup class.

If an installer detects devices, it should do at least the following:

-   Call the **DetectProgressNotify** callback routine in the [**SP\_DETECTDEVICE\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552341) class installation parameters, if detection will potentially take a noticeable amount of time.

-   For each device the installer detects, it should:
    -   Create a device information element ([**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952)).
    -   Provide information for driver selection.

        The installer can manually select the driver for the device or the installer can set the device's hardware ID that Windows will use to find an INF for the device. An installer sets the hardware ID by calling [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169) with a *Property* value of SPDRP\_HARDWAREID.

    -   Possibly set some device installation parameters.

-   Return NO\_ERROR for successful detection or return a Win32 error code.

If one or more installers detects device(s) in response to this DIF code, Windows compares the list of detected devices to its current list of devices. If the installers detected a new device, Windows attempts to install the device. If the installers omitted a device that appears in Setup's list, Windows typically removes the device.

To detect non-PnP devices during GUI-mode setup, an installer must handle the [**DIF\_FIRSTTIMESETUP**](dif-firsttimesetup.md) request. GUI-mode setup does not send a DIF\_DETECT request to the installer.

For more information about DIF codes, see [Handling DIF Codes](https://msdn.microsoft.com/library/windows/hardware/ff546094).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Supported in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**DIF\_DETECT**](dif-detect.md)

[**DIF\_FIRSTTIMESETUP**](dif-firsttimesetup.md)

[**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952)

[**SP\_DETECTDEVICE\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552341)

[**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_DETECT%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





