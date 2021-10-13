---
title: About Sensor Parameter Types
description: About the Parameter Types
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# About Sensor Parameter Types


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
<td><p><a href="/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile" data-raw-source="[IWDFFile](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile)">IWDFFile</a></p></td>
<td><p>pClientFile</p></td>
<td><p>This UMDF COM interface represents a file object that the platform associates with a client application. Although sensor method calls always supply this type as a valid interface pointer, it is intended to be used as an ID for the application. The address that the pointer contains is a unique number that can identify the client application. Be aware that this value is distinct from the address of the pointer itself. Do not use the address-of operator (&) to retrieve an ID. Use the pointer itself.</p>
<p>If you choose to use this pointer to access the underlying object, remember to call AddRef through the pointer initially, and to call Release when you have finished.</p></td>
</tr>
<tr class="even">
<td><p><strong>LPWSTR</strong></p></td>
<td><p>pwszSensorID</p></td>
<td><p>This string is a unique ID that is provided by the driver for a particular sensor. This ID must be unique for each sensor on a particular device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues" data-raw-source="[IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues)">IPortableDeviceValues</a></p></td>
<td><p>ppDataValues</p>
<p>ppPropertyValues</p>
<p>pPropertiesToSet</p>
<p>ppResults</p></td>
<td><p>This WPD interface provides a convenient way to create a property bag of name/value pairs. <strong>PROPERTYKEY</strong>s represent names and <strong>PROPVARIANT</strong>s represent values. The DDI uses this interface both to set and retrieve sets of values, or for a single value.</p>
<p>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with <strong>CLSID_PortableDeviceValues</strong>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevaluescollection" data-raw-source="[IPortableDeviceValuesCollection](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevaluescollection)">IPortableDeviceValuesCollection</a></p></td>
<td><p>pEventCollection</p>
<p>ppSensorObjectCollection</p></td>
<td><p>This WPD interface contains a collection of <a href="/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues" data-raw-source="[IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues)">IPortableDeviceValues</a> objects. DDI methods that use this interface enable you to provide several sets of data at the same time, such as multiple events or information about multiple sensors.</p>
<p>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with <strong>CLSID_PortableDeviceValuesCollection</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicekeycollection" data-raw-source="[IPortableDeviceKeyCollection](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicekeycollection)">IPortableDeviceKeyCollection</a></p></td>
<td><p>pDataFields</p>
<p>pProperties</p>
<p>ppSupportedDataFields</p>
<p>ppSupportedProperties</p></td>
<td><p>This WPD interface contains a collection of <strong>PROPERTYKEY</strong>s. These keys represent property names that can be stored by <a href="/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues" data-raw-source="[IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues)">IPortableDeviceValues</a>. The DDI uses this collection object both for setting and retrieving sets of property names, or a single name.</p>
<p>You can retrieve this interface from a method or, if a new object is required, by calling CoCreateInstance with <strong>CLSID_PortableDeviceKeyCollection</strong>.</p></td>
</tr>
</tbody>
</table>

