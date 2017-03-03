---
Description: 'Device, configuration, and interface descriptors may contain references to string descriptors. This topic describes how to get a particular string descriptor from the device.'
MS-HAID:
- 'usb-config\_9d048bd3-a031-4cac-8990-6a6b6d444205.xml'
- 'buses.usb\_string\_descriptors'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB String Descriptors
author: windows-driver-content
---

# USB String Descriptors


Device, configuration, and interface descriptors may contain references to string descriptors. This topic describes how to get a particular string descriptor from the device.

## <a href="" id="ddk-usb-string-descriptors-kg"></a>


String descriptors are referenced by their one-based index number. A string descriptor contains one or more Unicode strings; each string is a translation of the others into another language.

Client drivers use [**UsbBuildGetDescriptorRequest**](https://msdn.microsoft.com/library/windows/hardware/ff538943), with *DescriptorType* = USB\_STRING\_DESCRIPTOR\_TYPE, to build the request to obtain a string descriptor. The *Index* parameter specifies the index number, and the *LanguageID* parameter specifies the language ID (the same values are used as in Microsoft Win32 LANGID values). Drivers can request the special index number of zero to determine which language IDs the device supports. For this special value, the device returns an array of language IDs rather than a Unicode string.

Because the string descriptor consists of variable-length data, the driver must obtain it in two steps. First the driver must issue the request, passing a data buffer large enough to hold the header for a string descriptor, a USB\_STRING\_DESCRIPTOR structure. The **bLength** member of USB\_STRING\_DESCRIPTOR specifies the size in bytes of the entire descriptor. The driver then makes the same request with a data buffer of size **bLength**.

The following code demonstrates how to request the *i*-th string descriptor, with language ID *langID*:

```
USB_STRING_DESCRIPTOR USD, *pFullUSD;
UsbBuildGetDescriptorRequest(
    pURB, // points to the URB to be filled in
    sizeof(struct _URB_CONTROL_DESCRIPTOR_REQUEST),
    USB_STRING_DESCRIPTOR_TYPE,
    i, // index of string descriptor
    langID, // language ID of string.
    &amp;USD, // points to a USB_STRING_DESCRIPTOR.
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
[USB Descriptors](usb-descriptors.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20String%20Descriptors%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


