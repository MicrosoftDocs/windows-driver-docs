---
title: Bluetooth Proximity Profile
description: The Proximity Profile defines two roles intended to allow devices to detect their proximity.
ms.assetid: 6BA67CA4-AAE4-4D01-97A4-65970704E7ED
---

# Bluetooth Proximity Profile


The Proximity Profile defines two roles intended to allow devices to detect their proximity.

The two roles are called:

-   The Proximity Reporter
-   The Proximity Monitor

![role relationship](images/bthleproximityroles.png)

## <span id="Proximity_Reporter"></span><span id="proximity_reporter"></span><span id="PROXIMITY_REPORTER"></span>Proximity Reporter


The Proximity Reporter is required to be a GATT server.

The Proximity Reporter supports the following GATT services:

-   Link Loss Service (mandatory)
-   Immediate Alert Service (optional)
-   Tx Power Service (optional)

## <span id="Proximity_Monitor"></span><span id="proximity_monitor"></span><span id="PROXIMITY_MONITOR"></span>Proximity Monitor


The Proximity Monitor is the GATT client. It should create and maintain a connection to the proximity Reporter as well as monitor the Radio Signal Strength Information (or RSSI) of the connection to calculate the signal’s path loss. If the optional "Tx Power Service" is available on the Proximity Reporter, it can also use this additional information to normalize the RSSI value by subtracting the RSSI from the Tx Power Level.

## <span id="_support_for_gatt_in_windows_8.1"></span><span id="_SUPPORT_FOR_GATT_IN_WINDOWS_8.1"></span> Support for GATT in Windows 8.1


When a GATT device is paired with Windows 8.1, the device becomes part of the system and Windows will provide *device objects* to represent both the device and the primary services reported by the device.

The [**Windows.Devices.Bluetooth.GenericAttributeProfile namespace**](https://msdn.microsoft.com/library/windows/apps/dn297685). describes the Generic Attribute Profile APIs app developers can use in Windows 8.1.

One of the first steps when developing a device app is to identify which Bluetooth services the app needs in order to accomplish the scenarios a user cares about. For the Proximity Profile, the device app needs to use the "Link Loss Service" and optionally the "Immediate Alert Service" and "Tx Power Service".

In order for the device app to determine if any devices paired with Windows implement the "Link Loss Service" the app should use the APIs available in the [**Windows.Devices.Enumeration namespace**](https://msdn.microsoft.com/library/windows/apps/br225459), namely the DeviceInformation.FindAllAsync method.

The [**DeviceInformation.FindAllAsync method**](https://msdn.microsoft.com/library/windows/apps/br225433) takes an *AQS (Advanced Query Syntax)* device selector as a parameter in order to filter only devices which contain the "Link Loss Service". Device app developers can also use the [**GetDeviceSelectorFromUuid**](https://msdn.microsoft.com/library/windows/apps/dn297476) or [**GetDeviceSelectorFromShortId**](https://msdn.microsoft.com/library/windows/apps/dn297475) methods of the [**GattDeviceService**](https://msdn.microsoft.com/library/windows/apps/dn297468) class, so they don’t need to manually construct the AQS filter.

The "Link Loss Service" is a Bluetooth GATT service defined by the Bluetooth SIG, and as such a *Short Id* can be used instead of a *fully-qualified UUID*.

The *Short Id* service IDs assigned for a Proximity profile service are:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Service Name</th>
<th align="left">Short Id</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Link Loss</p></td>
<td align="left"><p>0x1803</p></td>
</tr>
<tr class="even">
<td align="left"><p>Immediate Alert</p></td>
<td align="left"><p>0x1802</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Tx Power</p></td>
<td align="left"><p>0x1804</p></td>
</tr>
</tbody>
</table>

 

The Bluetooth SIG maintains the most up to date [list of services](http://go.microsoft.com/fwlink/p/?linkid=320723).

After a developer has determined which service s/he wants to use, s/he can call [**GattDeviceService.FromIdAsync**](https://msdn.microsoft.com/library/windows/apps/dn297473) to obtain an instance of the service.

Once the developer has obtained a valid GattDeviceService object, s/he can use it to communicate with the device using the [**Windows.Devices.Bluetooth.GenericAttributeProfile**](https://msdn.microsoft.com/library/windows/apps/dn297685) API.

These APIs enable access to specific services and their objects (for example Included Services, Characteristics, and Descriptors), as well as read and write capabilities.

The [Bluetooth Generic Attribute Profile - Heart Rate Service](http://go.microsoft.com/fwlink/p/?linkid=301978) sample demonstrates some of these techniques.

## <span id="Using_Power_Efficiently"></span><span id="using_power_efficiently"></span><span id="USING_POWER_EFFICIENTLY"></span>Using Power Efficiently


Support for Bluetooth Low Energy in Windows 8.1 has a strong focus on using power efficiently. This includes reducing the power consumption for the local Bluetooth radio adapter as well as using the CPU to be as little as possible.

Therefore, to establish a Bluetooth LE connection an app needs to register a handler for the [**GattCharacteristic.ValueChanged**](https://msdn.microsoft.com/library/windows/apps/dn263767) event. Alternately, the app must call any of the [**GattCharacteristic.ReadValueAsync**](https://msdn.microsoft.com/library/windows/apps/dn263752), [**GattCharacteristic.WriteValueAsync**](https://msdn.microsoft.com/library/windows/apps/dn263770) or [**GattCharacteristic.WriteClientCharacteristicConfigurationDescriptorAsync**](https://msdn.microsoft.com/library/windows/apps/dn263769) methods without specifying the BluetoothCacheMode.Cached option.

**Note**  In order to minimize power consumption, Windows does not actively monitor the RSSI value of the link by polling the local Bluetooth radio controller.

 

Power considerations are described in [Proximity Profile Implementation Details](proximity-profile-implementation-details.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Bluetooth%20Proximity%20Profile%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




