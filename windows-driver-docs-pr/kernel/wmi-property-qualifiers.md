---
title: WMI Property Qualifiers
author: windows-driver-content
description: WMI Property Qualifiers
MS-HAID:
- 'WMI\_f135291c-3891-4fc1-8b8f-bf00a04e08cd.xml'
- 'kernel.wmi\_property\_qualifiers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e2d281b3-913c-43ad-921c-80dc8be09aa0
keywords: ["MOF property qualifiers WDK WMI", "property qualifiers WDK WMI", "qualifiers WDK WMI", "standard MOF qualifiers WDK WMI"]
---

# WMI Property Qualifiers


## <a href="" id="ddk-wmi-property-qualifiers-kg"></a>


The following table lists the required and optional MOF property qualifiers that can be used to define items in a WMI data or event block.

The following are standard MOF qualifiers: **key**, **read**, **write**, **ValueMap**, and **Values**. For more information about these and other standard MOF qualifiers, see [MOF Data Types](https://msdn.microsoft.com/library/aa392392).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Qualifier</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>key</strong></p></td>
<td><p>Indicates that the data item is a key property that uniquely identifies each instance of the class. Only the InstanceName property can be declared a key.</p></td>
</tr>
<tr class="even">
<td><p><strong>read</strong></p></td>
<td><p>Indicates that a WMI client can read the data item.</p></td>
</tr>
<tr class="odd">
<td><p><strong>write</strong></p></td>
<td><p>Indicates that a WMI client can set the data item.</p></td>
</tr>
<tr class="even">
<td><p><strong>BitMap</strong></p></td>
<td><p>Specifies the bit positions of the corresponding string values that are specified in <strong>BitValues</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>BitValues</strong></p></td>
<td><p>Specifies a list of string values (flag names) that represent bits set in the data item. The bit position of a flag is defined by the corresponding position specified in <strong>BitMap</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>DefineValues</strong></p></td>
<td><p>Specifies an enumerated list that the WMI tool suite compiles into a corresponding list of #define statements.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DisplayInHex</strong></p></td>
<td><p>Specifies that any WMI client that displays the property value should do so in hexadecimal.</p></td>
</tr>
<tr class="even">
<td><p><strong>DisplayName(&quot;</strong><em>string</em><strong>&quot;)</strong></p></td>
<td><p>Specifies a caption that a WMI client can use to display as the property name.</p></td>
</tr>
<tr class="odd">
<td><p><strong>MaxLen(</strong><em>uint</em><strong>)</strong></p></td>
<td><p>For string properties, <strong>MaxLen</strong> specifies the maximum length of the string in characters. The <em>uint</em> value can be any 32-bit unsigned integer. If MaxLen is omitted, or <em>uint</em> is zero, then the length of the string is unlimited.</p></td>
</tr>
<tr class="even">
<td><p><strong>Values</strong></p></td>
<td><p>Specifies a list of possible values for this data item. If the data item is an enumeration, <strong>ValueMap</strong> contains the index value that corresponds to the enumeration value specified in <strong>Values</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ValueMap</strong></p></td>
<td><p>Specifies the integer values of the corresponding string values in <strong>Values</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiDataId(</strong><em>data-item-ID</em><strong>)</strong></p></td>
<td><p>(Required) Identifies a data item within a data block. Data item IDs must be assigned to all items in a block except the required items <strong>InstanceName</strong> and <strong>Active</strong>. Data item IDs must be assigned in a contiguous series, starting with 1. An item's data ID determines the order in which the item appears in an instance of the data block; the order of items in the MOF class definition is irrelevant.</p></td>
</tr>
<tr class="odd">
<td><p><strong>WmiMethodId(</strong><em>method-item-ID</em><strong>)</strong></p></td>
<td><p>Identifies a method within a data block.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiSizeIs(&quot;</strong><em>data-item-name</em><strong>&quot;)</strong></p></td>
<td><p>Specifies the name of another data item in this block that indicates the number of elements in the variable-length array at this data item. <strong>WmiSizeIs</strong> is valid only for data items that define arrays.</p></td>
</tr>
<tr class="odd">
<td><p><strong>WmiScale(</strong><em>scale-factor</em><strong>)</strong></p></td>
<td><p>Specifies the scaling factor, as a power of 10, that the driver uses when returning the value of this data item. For example, if <em>scale-factor</em> is 5, the value returned by the driver is multiplied by 10⁵. If <strong>WmiScale</strong> is omitted, <em>scale-factor</em> can be assumed to be 0.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiTimeStamp</strong></p></td>
<td><p>Specifies that a 64-bit data item is a time stamp in units of 100 nanoseconds since 1/1/1601. <strong>WmiTimeStamp</strong> is valid only for 64-bit data items.</p></td>
</tr>
<tr class="odd">
<td><p><strong>WmiComplexity(</strong><em>level</em><strong>)</strong></p></td>
<td><p>Specifies an integer value that expresses the user complexity level of the data item. WMI clients can use that value to distinguish between data items that should be available to novice users and data items that should be restricted to more advanced users. Zero is the minimum value, and higher values indicate higher user complexity. <strong>WmiComplexity</strong> defaults to zero if not specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiVolatility(</strong><em>interval</em><strong>)</strong></p></td>
<td><p>Specifies the interval, in milliseconds, between updates of this data item. For example, if a data item is updated once each second, <em>interval</em> would be 1000. A WMI client might check <strong>WmiVolatility</strong> to determine how often to query for a potentially new value. If <strong>WmiVolatility</strong> is omitted, <em>interval</em> is undefined.</p></td>
</tr>
<tr class="odd">
<td><p><strong>WmiEventTrigger(</strong> <strong>&quot;</strong> <em>data-item-name</em><strong>&quot;)</strong></p></td>
<td><p>Specifies the name of a data item in an event block that a WMI client can set to define the trigger value for the event. For example, if the event TooHot is qualified with <strong>WmiEventTrigger</strong>(&quot;TooHotTemperature&quot;), a WMI client could set TooHotTemperature to instruct the driver to send the TooHot event when the device reached the user-specified value for TooHotTemperature. Typically a driver would define the trigger value. By exposing a <strong>WmiEventTrigger</strong> data item, the driver allows a client to control when a particular event is fired.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiEventRate(&quot;</strong><em>data-item-name</em><strong>&quot;)</strong></p></td>
<td><p>Specifies the name of a data item in an event block that a WMI client can set to control the frequency at which this event will be sent. For example, if the data item TooHot is qualified with <strong>WmiEventRate(&quot;</strong>SendEventRate<strong>&quot;)</strong>, a WMI client user could set SendEventRate to instruct the driver to send TooHot at the user-specified interval.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Property%20Qualifiers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


