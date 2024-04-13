---
title: USB String Descriptors
description: Device, configuration, and interface descriptors may contain references to string descriptors. This topic describes how to get a particular string descriptor from the device.
ms.date: 01/17/2024
---

# USB String Descriptors

Device, configuration, and interface descriptors may contain references to string descriptors. This topic describes how to get a particular string descriptor from the device.

String descriptors are referenced by their one-based index number. A string descriptor contains one or more Unicode strings; each string is a translation of the others into another language.

Client drivers use **[UsbBuildGetDescriptorRequest](/previous-versions/ff538943(v=vs.85))**, with *DescriptorType* = USB_STRING_DESCRIPTOR_TYPE, to build the request to obtain a string descriptor. The *Index* parameter specifies the index number, and the *LanguageID* parameter specifies the language ID (the same values are used as in Microsoft Win32 LANGID values). Drivers can request the special index number of zero to determine which language IDs the device supports. For this special value, the device returns an array of language IDs rather than a Unicode string.

Because the string descriptor consists of variable-length data, the driver must obtain it in two steps. First the driver must issue the request, passing a data buffer large enough to hold the header for a string descriptor, a USB_STRING_DESCRIPTOR structure. The **bLength** member of USB_STRING_DESCRIPTOR specifies the size in bytes of the entire descriptor. The driver then makes the same request with a data buffer of size **bLength**.

The following code demonstrates how to request the *i*-th string descriptor, with language ID *langID*:

```cpp
USB_STRING_DESCRIPTOR USD, *pFullUSD;
UsbBuildGetDescriptorRequest(
    pURB, // points to the URB to be filled in
    sizeof(struct _URB_CONTROL_DESCRIPTOR_REQUEST),
    USB_STRING_DESCRIPTOR_TYPE,
    i, // index of string descriptor
    langID, // language ID of string.
    &USD, // points to a USB_STRING_DESCRIPTOR.
    NULL,
    sizeof(USB_STRING_DESCRIPTOR),
    NULL
);
pFullUSD = ExAllocatePool(NonPagedPool, USD.bLength);
UsbBuildGetDescriptorRequest(
    pURB, // points to the URB to be filled in
    sizeof(struct _URB_CONTROL_DESCRIPTOR_REQUEST),
    USB_STRING_DESCRIPTOR_TYPE,
    i, // index of string descriptor
    langID, // language ID of string
    pFullUSD,
    NULL,
    USD.bLength,
    NULL
);
```

## Related topics

- [USB Descriptors](usb-descriptors.md)
