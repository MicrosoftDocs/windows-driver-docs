---
title: Where Windows Searches for Drivers
description: Where Windows Searches for Drivers
ms.assetid: 4c193b97-7b70-425f-99f2-ba976a4cc40a
keywords: ["driver selections WDK device installations , where Device setupsearches", "locating drivers for device installation WDK device installations , where Device setupsearches", "searching for drivers during device installation WDK device installations , where Device setupsearches"]
---

# Where Windows Searches for Drivers


After a device is attached, Windows attempts to locate a matching [driver package](driver-packages.md) from which it can install a driver for the device. Windows searches for driver packages from various locations and performs this search in two phases, as described in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Search phase</th>
<th align="left">Windows 7</th>
<th align="left">Windows 8 and later versions of Windows</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Before a driver is installed</td>
<td align="left"><p>DevicePath</p>
<p>Windows Update</p>
<p>[Driver store](driver-store.md)</p></td>
<td align="left">[Driver store](driver-store.md)</td>
</tr>
<tr class="even">
<td align="left">After initial driver is selected</td>
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>DevicePath</p>
<p>Windows Update</p></td>
</tr>
</tbody>
</table>

 

### Searching for driver packages

After a device is attached, Windows first attempts to locate and install a driver in a trusted system context without user interaction, as follows:

-   The best matching driver that already exists in the driver store is first installed onto the device, allowing the device to begin operation quickly. In parallel and in a different process, the following will happen:

-   Windows automatically downloads matching [driver packages](driver-packages.md) from Windows Update. If a matching driver package is found, Windows downloads the package and stages it to the [driver store](driver-store.md).

    Windows also searches for driver packages that were preloaded in the locations that are specified by the **DevicePath** registry value. This value is under the following subkey of the registry.

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Windows
                CurrentVersion
    ```

    By default, the **DevicePath** value specifies the %SystemRoot%\\INF directory.

    If a better matching driver package than was initially installed is found either on Windows Update or in a location that is specified by the **DevicePath** value, Windows first stages the driver package to the [driver store](driver-store.md) before the driver is installed. In this way, Windows always installs drivers from the driver store.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Where%20Windows%20Searches%20for%20Drivers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




