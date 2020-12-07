---
title: Collection Capability
description: Collection Capability
keywords:
- capabilities WDK HID collections
- summary capabilities WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Collection Capability





The capability of a collection is defined by its usage, reports, link collections, and controls. To obtain a summary of a collection's capability, a user-mode application or kernel-mode driver calls [**HidP\_GetCaps**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getcaps) to obtain a [**HIDP\_CAPS**](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_caps) structure. This structure contains the following information about a collection's [link collections](link-collections.md), [button capability arrays](button-capability-arrays.md), and [value capability arrays](value-capability-arrays.md):

-   The collection's [usage page](hid-usages.md#usage-page) and [usage ID](hid-usages.md#usage-id)

-   The size, in bytes, of the collection's input, output, and feature reports (see [Introduction to HID Concepts](introduction-to-hid-concepts.md))

-   The number of [**HIDP\_LINK\_COLLECTION\_NODE**](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_link_collection_node) structures in the collection's [link collection array](link-collections.md#ddk-link-collection-array-kg)

-   For each report type, the number of [**HIDP\_BUTTON\_CAPS**](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_button_caps) structures in the button capability array returned by [**HidP\_GetButtonCaps**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getbuttoncaps)

-   For each report type, the number of [**HIDP\_VALUE\_CAPS**](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_value_caps)structures in the value capability array returned by [**HidP\_GetValueCaps**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getvaluecaps)

-   For each report type, the number of buttons and values supported by the collection, as specified by the **Number***Xxx***DataIndices** member.

 

