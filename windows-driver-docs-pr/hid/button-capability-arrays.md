---
title: Button Capability Arrays
description: Button Capability Arrays
ms.assetid: 139324e5-4d46-4d00-9f5a-fd0313fc109a
keywords:
- button capability arrays WDK HID
- arrays WDK HID
- capabilities WDK HID collections
- button usages WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Button Capability Arrays





A *button capability array* contains information about the button usages supported by a [top-level collection](top-level-collections.md) for a specific type of HID report. Information about a collection's capability is contained in its [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure.

A user-mode application or kernel-mode driver uses one of the following [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) to obtain button capability information:

-   [**HidP\_GetButtonCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539707) returns a button capability array describing all the button usages contained in a specified report type.

-   [**HidP\_GetSpecificButtonCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539733) filters the button capability information it returns by a caller-specified usage page, usage ID, and [link collection](link-collections.md).

A button capability array contains [**HIDP\_BUTTON\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539693) structures, each one of which contains the following information about a [HID usage](hid-usages.md) or [usage range](hid-usages.md#usage-range):

-   The usage page for the usage or usage range

-   The report ID of the report that contains the button data

-   The usage ID or usage range

-   A flag that indicates whether a usage is an [aliased usage](hid-usages.md#aliased-usages)

-   The link collection that contains the usage or usage range

-   The string descriptors and designators associated with the usage or usage range (see Designator Index item and String Index item)

-   The [data indices](data-indices.md) that the HID parser assigned to the usage or usage range

In general, the following conditions hold for all the usages described by a button capability array:

-   Each capability structure represents a single usage or usage range that is associated with a variable main item or an array main item.

-   Aliased usages can be used with a variable main item. A usage that is associated with an array item cannot be aliased. A usage range cannot be aliased.

-   The HID parser uses only the minimum required number of usages to assign a usage to each button. The parser assigns usages in the order in which they are specified in a report descriptor. Usages in a report descriptor that are not required, are discarded. The button capability array does not contain any information about discarded usages.

-   If the number of usages specified for a variable item is less than the number of buttons in the item, the capability array contains only one capability structure that describes one button usage (the last usage specified in the report descriptor for the variable main item). However, see [Usage Value Array](value-capability-arrays.md#usage-value-array) for information about usage values that have a report count greater than one.

-   The HID parser assigns a unique data index to each usage described in the capability array.

The following topics discuss how the capability structures are organized and set in a button capability array:

[Button Usages in a Variable Main Item](#button-usages-in-a-variable-main-item)

[Button Usages in an Array Main Item](#button-usages-in-an-array-main-item)

### <a href="" id="button-usages-in-a-variable-main-item"></a> Button Usages in a Variable Main Item

Each [usage](hid-usages.md) or [usage range](hid-usages.md#usage-range) that is specified in a report descriptor is described by its own capability structure in a button capability array.

The **IsAlias** member of capability structures is used to specify a set of *n* aliased usages as follows:

-   **IsAlias** is set to **TRUE** in the first *n*-1 capability structures added to the capability array. **IsAlias** set to **FALSE** in the *n*th capability structure. The preferred usage is the last aliased usage in the sequence.

An application or driver can determine which button usages are aliased by scanning for such sequences.

The following table summarizes an example for three aliased usages.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Aliased Usage Order in a Report Descriptor</th>
<th>Usage Order in a Capability Array</th>
<th>IsAlias Member Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>usage 1</p></td>
<td><p>usage 3</p></td>
<td><p><strong>TRUE</strong></p></td>
</tr>
<tr class="even">
<td><p>usage 2</p></td>
<td><p>usage 2</p></td>
<td><p><strong>TRUE</strong></p></td>
</tr>
<tr class="odd">
<td><p>usage 3</p></td>
<td><p>usage 1</p></td>
<td><p><strong>FALSE</strong></p></td>
</tr>
</tbody>
</table>

 

For information about how usages and data indices are cross-referenced, see [Data Indices](data-indices.md).

### <a href="" id="button-usages-in-an-array-main-item"></a> Button Usages in an Array Main Item

Each [usage](hid-usages.md) or [usage range](hid-usages.md#usage-range) for a button array main item specified in a report descriptor is described by its own capability structure in a button capability array. The order in which the capability structures are added to a capability array is the reverse of the order in which the usages are specified for a main item.

The HID parser assigns a [data index](data-indices.md) to each usage associated with the array item in the order in which the usages are specified in a report descriptor. For example, the following table shows the correspondence between a set of usages, as specified in a report descriptor, and the usages and data indices, as specified in the capability array. (In this table, *n* is the first data index that the parser assigns to the first usage associated with the array item.)

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Usage Order in Report Descriptor</th>
<th>Usage Order in Capability Array</th>
<th>DataIndex or from DataIndexMin to DatatIndexMax</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>usage 1</p></td>
<td><p>usage range 2</p></td>
<td><p>from <em>n</em>+7 to <em>n</em>+8</p></td>
</tr>
<tr class="even">
<td><p>usage range 1 (with 4 usages)</p></td>
<td><p>usage 2</p></td>
<td><p><em>n</em>+5</p></td>
</tr>
<tr class="odd">
<td><p>usage 2</p></td>
<td><p>usage range 1</p></td>
<td><p>from <em>n</em>+1 to <em>n</em>+4</p></td>
</tr>
<tr class="even">
<td><p>usage range 2 (with 2 usages)</p></td>
<td><p>usage 1</p></td>
<td><p><em>n</em></p></td>
</tr>
</tbody>
</table>

 

 

 




