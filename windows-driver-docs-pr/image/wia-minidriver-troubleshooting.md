---
title: WIA Minidriver Troubleshooting
description: WIA Minidriver Troubleshooting
ms.assetid: a0944bdd-56c4-4f7b-b542-eb353cd4d1f2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Minidriver Troubleshooting





By default, the WIA service logs errors to a file named *wiadebug.log* in the **%**<em>windir</em>**%** directory. The information that the WIA service places in this file can be very helpful during driver development. The following example depicts a typical problem and shows how the information in the *wiadebug.log* file can be used to find a solution to the problem.

A developer writes an application to test a scanner driver that is under development. As one of the tests, the developer attempts to set the scanner's dots per inch (dpi) to 1200, but notices that this action produces an error. A look at the Wiadebug.log file shows the following:

```console
wiasGetChangedValueLong, validate prop 6147 failed hr: 0x80070057
wiasUpdateScanRect, CheckXResAndUpdate failed (0x80070057)
CDrvWrap::WIA_drvValidateItemProperties, Error calling driver:
drvValidateItemProperties with hr = 0x80070057 (This is normal if the app wrote an invalid value)
```

These log entries indicate that the driver is reporting that the application wrote an invalid value. It is not clear from this information what the exact problem is. If the developer increases the WIA logging level to report warnings as well as the errors, *wiadebug.log* produces output similar to the following:

```console
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

**HKLM\\System\\CurrentControlSet\\Control\\StillImage\\Debug\\**<em>MODULE\_NAME</em>**\\DebugFlags**

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
