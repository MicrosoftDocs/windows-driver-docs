---
title: About the Parameter Types
author: windows-driver-content
description: About the Parameter Types
ms.assetid: 392ea7b9-df6f-4d47-9367-a167c0656dd4
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# About the Parameter Types


You should understand how the sensor class extension uses some data types as method parameters. The following table describes these data types.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Parameter names</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912)</p></td>
<td><p>pClientFile</p></td>
<td><p>This UMDF COM interface represents a file object that the platform associates with a client application. Although sensor method calls always supply this type as a valid interface pointer, it is intended to be used as an ID for the application. The address that the pointer contains is a unique number that can identify the client application. Be aware that this value is distinct from the address of the pointer itself. Do not use the address-of operator (&amp;) to retrieve an ID. Use the pointer itself.</p>
<p>If you choose to use this pointer to access the underlying object, remember to call AddRef through the pointer initially, and to call Release when you have finished.</p></td>
</tr>
<tr class="even">
<td><p><strong>LPWSTR</strong></p></td>
<td><p>pwszSensorID</p></td>
<td><p>This string is a unique ID that is provided by the driver for a particular sensor. This ID must be unique for each sensor on a particular device.</p></td>
</tr>
<tr class="odd">
<td><p>[IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486)</p></td>
<td><p>ppDataValues</p>
<p>ppPropertyValues</p>
<p>pPropertiesToSet</p>
<p>ppResults</p></td>
<td><p>This WPD interface provides a convenient way to create a property bag of name/value pairs. <strong>PROPERTYKEY</strong>s represent names and <strong>PROPVARIANT</strong>s represent values. The DDI uses this interface both to set and retrieve sets of values, or for a single value.</p>
<p>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with <strong>CLSID_PortableDeviceValues</strong>.</p></td>
</tr>
<tr class="even">
<td><p>[IPortableDeviceValuesCollection](http://go.microsoft.com/fwlink/p/?linkid=131487)</p></td>
<td><p>pEventCollection</p>
<p>ppSensorObjectCollection</p></td>
<td><p>This WPD interface contains a collection of [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) objects. DDI methods that use this interface enable you to provide several sets of data at the same time, such as multiple events or information about multiple sensors.</p>
<p>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with <strong>CLSID_PortableDeviceValuesCollection</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>[IPortableDeviceKeyCollection](http://go.microsoft.com/fwlink/p/?linkid=131484)</p></td>
<td><p>pDataFields</p>
<p>pProperties</p>
<p>ppSupportedDataFields</p>
<p>ppSupportedProperties</p></td>
<td><p>This WPD interface contains a collection of <strong>PROPERTYKEY</strong>s. These keys represent property names that can be stored by [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486). The DDI uses this collection object both for setting and retrieving sets of property names, or a single name.</p>
<p>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with <strong>CLSID_PortableDeviceKeyCollection</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20the%20Parameter%20Types%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


