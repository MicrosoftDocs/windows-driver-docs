---
title: Properties for All WIA Minidrivers
description: Properties for All WIA Minidrivers
ms.assetid: ba85dbbd-2333-4f4f-b12a-84985773eef6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Properties for All WIA Minidrivers





### Required Properties on Root or Child Items

The WIA service supplies the following properties:

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-full-item-name)

[**WIA\_IPA\_ITEM\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-flags)

[**WIA\_IPA\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-name)

[**WIA\_IPA\_ITEM\_CATEGORY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-category)

A WIA minidriver supplies the following property:

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-access-rights)

### Required Properties on Root Items

The WIA service supplies the following root item properties:

[**WIA\_DIP\_BAUDRATE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-baudrate)

[**WIA\_DIP\_DEV\_DESC**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-dev-desc)

[**WIA\_DIP\_DEV\_ID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-dev-id)

[**WIA\_DIP\_DEV\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-dev-name)

[**WIA\_DIP\_DEV\_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-dev-type)

[**WIA\_DIP\_DRIVER\_VERSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-driver-version)

[**WIA\_DIP\_HW\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-hw-config)

[**WIA\_DIP\_PORT\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-port-name)

[**WIA\_DIP\_REMOTE\_DEV\_ID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-remote-dev-id)

[**WIA\_DIP\_SERVER\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-server-name)

[**WIA\_DIP\_STI\_GEN\_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-sti-gen-capabilities)

[**WIA\_DIP\_UI\_CLSID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-ui-clsid)

[**WIA\_DIP\_VEND\_DESC**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-vend-desc)

[**WIA\_DIP\_WIA\_VERSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dip-wia-version)

### Optional Properties on Root Items

A WIA minidriver supplies the following optional properties on root items:

[**WIA\_DPA\_CONNECT\_STATUS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dpa-connect-status)

[**WIA\_DPA\_DEVICE\_TIME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dpa-device-time)

[**WIA\_DPA\_FIRMWARE\_VERSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dpa-firmware-version)

### Required Properties on Child Items Able to Transfer Data

The WIA service supplies the following property on child items:

[**WIA\_IPA\_ICM\_PROFILE\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-icm-profile-name)

A WIA minidriver supplies the following properties on child items:

[**WIA\_IPA\_BITS\_PER\_CHANNEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-bits-per-channel)

[**WIA\_IPA\_BUFFER\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-buffer-size)

[**WIA\_IPA\_BYTES\_PER\_LINE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-bytes-per-line)

[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-channels-per-pixel)

[**WIA\_IPA\_COMPRESSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-compression)

[**WIA\_IPA\_DATATYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-datatype)

[**WIA\_IPA\_DEPTH**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-depth)

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-filename-extension)

[**WIA\_IPA\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-format)

[**WIA\_IPA\_ITEM\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-size)

[**WIA\_IPA\_NUMBER\_OF\_LINES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-number-of-lines)

[**WIA\_IPA\_PIXELS\_PER\_LINE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-pixels-per-line)

[**WIA\_IPA\_PLANAR**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-planar)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-preferred-format)

[**WIA\_IPA\_TYMED**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-tymed)

### Optional Properties on Child Items Able to Transfer Data

A WIA minidriver supplies the following properties:

[**WIA\_IPA\_APP\_COLOR\_MAPPING**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-app-color-mapping)

[**WIA\_IPA\_COLOR\_PROFILE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-color-profile)

[**WIA\_IPA\_GAMMA\_CURVES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-gamma-curves)

[**WIA\_IPA\_ITEM\_TIME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-time)

[**WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-prop-stream-compat-id)

[**WIA\_IPA\_REGION\_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-region-type)

[**WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-suppress-property-page)

 

 




