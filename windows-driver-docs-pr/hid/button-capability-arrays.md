---
title: Button Capability Arrays
description: Button capability arrays
keywords:
- button capability arrays WDK HID
- arrays WDK HID
- capabilities WDK HID collections
- button usages WDK HID
ms.date: 01/11/2024
---

# Button capability arrays

A *button capability array* contains information about the button usages supported by a [top-level collection](top-level-collections.md) for a specific type of HID report. Information about a collection's capability is contained in its **[HIDP_CAPS](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_caps)** structure.

A user-mode application or kernel-mode driver uses one of the following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid) to obtain button capability information:

- **[HidP_GetButtonCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getbuttoncaps)** returns a button capability array describing all the button usages contained in a specified report type.

- **[HidP_GetSpecificButtonCaps](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getspecificbuttoncaps)** filters the button capability information it returns by a caller-specified usage page, usage ID, and [link collection](link-collections.md).

A button capability array contains **[HIDP_BUTTON_CAPS](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_button_caps)** structures, each one of which contains the following information about a [HID usage](hid-usages.md) or [usage range](hid-usages.md#usage-range):

- The usage page for the usage or usage range

- The report ID of the report that contains the button data

- The usage ID or usage range

- A flag that indicates whether a usage is an [aliased usage](hid-usages.md#aliased-usages)

- The link collection that contains the usage or usage range

- The string descriptors and designators associated with the usage or usage range (see Designator Index item and String Index item)

- The [data indices](data-indices.md) that the HID parser assigned to the usage or usage range

In general, the following conditions hold for all the usages described by a button capability array:

- Each capability structure represents a single usage or usage range that is associated with a variable main item or an array main item.

- Aliased usages can be used with a variable main item. A usage that is associated with an array item cannot be aliased. A usage range cannot be aliased.

- The HID parser uses only the minimum required number of usages to assign a usage to each button. The parser assigns usages in the order in which they are specified in a report descriptor. Usages in a report descriptor that are not required, are discarded. The button capability array does not contain any information about discarded usages.

- If the number of usages specified for a variable item is less than the number of buttons in the item, the capability array contains only one capability structure that describes one button usage (the last usage specified in the report descriptor for the variable main item). However, see [Usage Value Array](value-capability-arrays.md#usage-value-array) for information about usage values that have a report count greater than one.

- The HID parser assigns a unique data index to each usage described in the capability array.

The following topics discuss how the capability structures are organized and set in a button capability array:

- [Button usages in a variable main item](#button-usages-in-a-variable-main-item)
- [Button usages in an array main item](#button-usages-in-an-array-main-item)

## Button usages in a variable main item

Each [usage](hid-usages.md) or [usage range](hid-usages.md#usage-range) that is specified in a report descriptor is described by its own capability structure in a button capability array.

The **IsAlias** member of capability structures is used to specify a set of *n* aliased usages as follows:

- **IsAlias** is set to **TRUE** in the first *n*-1 capability structures added to the capability array. **IsAlias** set to **FALSE** in the *n*th capability structure. The preferred usage is the last aliased usage in the sequence.

An application or driver can determine which button usages are aliased by scanning for such sequences.

The following table summarizes an example for three aliased usages.

| Aliased usage order in a report descriptor | Usage order in a capability array | IsAlias member value |
|--------------------------------------------|-----------------------------------|----------------------|
| usage 1                                    | usage 3                           | **TRUE**             |
| usage 2                                    | usage 2                           | **TRUE**             |
| usage 3                                    | usage 1                           | **FALSE**            |

For information about how usages and data indices are cross-referenced, see [Data Indices](data-indices.md).

## Button usages in an array main item

Each [usage](hid-usages.md) or [usage range](hid-usages.md#usage-range) for a button array main item specified in a report descriptor is described by its own capability structure in a button capability array. The order in which the capability structures are added to a capability array is the reverse of the order in which the usages are specified for a main item.

The HID parser assigns a [data index](data-indices.md) to each usage associated with the array item in the order in which the usages are specified in a report descriptor. For example, the following table shows the correspondence between a set of usages, as specified in a report descriptor, and the usages and data indices, as specified in the capability array. (In this table, *n* is the first data index that the parser assigns to the first usage associated with the array item.)

| Usage order in report descriptor | Usage order in capability array | DataIndex or from DataIndexMin to DataIndexMax |
|----------------------------------|---------------------------------|------------------------------------------------|
| usage 1                          | usage range 2                   | from *n*+7 to *n*+8                            |
| usage range 1 (with 4 usages)    | usage 2                         | *n*+5                                          |
| usage 2                          | usage range 1                   | from *n*+1 to *n*+4                            |
| usage range 2 (with 2 usages)    | usage 1                         | *n*                                            |
