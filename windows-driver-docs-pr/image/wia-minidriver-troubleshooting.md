---
title: WIA Minidriver Troubleshooting
author: windows-driver-content
description: WIA Minidriver Troubleshooting
ms.assetid: a0944bdd-56c4-4f7b-b542-eb353cd4d1f2
---

# WIA Minidriver Troubleshooting


## <a href="" id="ddk-wia-minidriver-troubleshooting-si"></a>


By default, the WIA service logs errors to a file named *wiadebug.log* in the **%***windir***%** directory. The information that the WIA service places in this file can be very helpful during driver development. The following example depicts a typical problem and shows how the information in the *wiadebug.log* file can be used to find a solution to the problem.

A developer writes an application to test a scanner driver that is under development. As one of the tests, the developer attempts to set the scanner's dots per inch (dpi) to 1200, but notices that this action produces an error. A look at the Wiadebug.log file shows the following:

```
wiasGetChangedValueLong, validate prop 6147 failed hr: 0x80070057
wiasUpdateScanRect, CheckXResAndUpdate failed (0x80070057)
CDrvWrap::WIA_drvValidateItemProperties, Error calling driver:
drvValidateItemProperties with hr = 0x80070057 (This is normal if the app wrote an invalid value)
```

These log entries indicate that the driver is reporting that the application wrote an invalid value. It is not clear from this information what the exact problem is. If the developer increases the WIA logging level to report warnings as well as the errors, *wiadebug.log* produces output similar to the following:

```
wiasValidateItemProperties, invalid LIST value for : 
    (propID) Horizontal Resolution, value = 1200
Valid values are:
    75
    100
    150
    200
    300
    600
 wiasGetChangedValueLong, validate prop 6147 failed hr: 0x80070057
wiasUpdateScanRect, CheckXResAndUpdate failed (0x80070057)
 CDrvWrap::WIA_drvValidateItemProperties, Error calling driver: 
 drvValidateItemProperties with hr = 0x80070057 (This is normal if the app wrote an invalid value)
```

The output shows that the Horizontal Resolution property is causing the failure. The application is attempting to set the resolution to 1200, but the list of supported resolutions does not include 1200. Thus, the WIA service validation helper [**wiasValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff549454) rejects the request to set this value.

Now that the problem is identified, it is up to the developer to determine whether it is the driver or the application that must be revised. If the scanner's specifications allow it to support all resolutions between 100 and 1400 dpi, the driver should be able to handle a request for 1200 dpi. If the scanner does not support this setting, the application should be changed so it does not attempt to set the Horizontal Resolution to a value that is not valid for this property. In this case, the application should then check that a value is valid before attempting to set a property to this value.

The logging level is controlled by an entry in the registry. For WIA, this key resides in:

**HKLM\\System\\CurrentControlSet\\Control\\StillImage\\Debug\\***MODULE\_NAME***\\DebugFlags**

```

```

In this example, MODULE\_NAME is the name of the appropriate binary module. For the WIA service, this is *wiaservc.dll*. The value in **DebugFlags** controls the logging level. Three of the settings are given in the following table:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0x00000001</p></td>
<td><p>Display error messages.</p></td>
</tr>
<tr class="even">
<td><p>0x00000002</p></td>
<td><p>Display warning messages.</p></td>
</tr>
<tr class="odd">
<td><p>0x00000004</p></td>
<td><p>Display trace messages.</p></td>
</tr>
</tbody>
</table>

 

The value in **DebugFlags** is a flag value (that is, different settings may be combined with a bitwise OR operator). To turn on logging for errors, warnings, and traces all at one time, set **DebugFlags** to 0x0000007.

In order for a change in value of **DebugFlags** to take effect, the WIA service (*stisvc*) must be stopped and then restarted. See [Starting and Stopping the Still Image Service](starting-and-stopping-the-still-image-service.md) for details.

**Note**   Excessive logging can lead to a significant decrease in performance. You should increase the logging level only when attempting to solve a particular problem. After you have corrected the problem, set logging to its original level. The default logging level is one. Do not increase the logging level above three as this may cause a crash.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Minidriver%20Troubleshooting%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


