---
title: MJPEG At Source Autodecode for USB Video Class (UVC)
description: Learn how to autodecode compressed MJPEG samples.
ms.date: 01/29/2026
ms.topic: concept-article
---

# MJPEG at source autodecode for USB video class (UVC)

Most UVC-based cameras use MJPEG compression to efficiently transfer high-resolution video over USB bandwidth. However, various components in the pipeline must decode MJPEG compressed samples before they can use video or image processing algorithms. Traditionally, each component's developers must duplicate the MJPEG decoding process throughout the stack. They must also handle quirks specific to different GPU hardware and MJPEG streams. This feature resolves these issues by handling decoding of MJPEG samples in the OS pipeline.

This feature also helps you avoid multiple decoding of the same sample in various parts of the pipeline when video processing is involved. For example, when the platform Device Media Foundation Transform (DMFT) processes face detection, it decodes the MJPEG samples, and then the app decodes the samples again. Also, various DMFTs that require access to image data decode the sample again at various stages.

## Feature description

You opt in to this feature by using the camera driver installation information (INF) file or firmware (Microsoft OS (MSOS) descriptors). When enabled, the pipeline autodecodes MJPEG MediaTypes at source, which is after the UVC driver and before the DMFT chain. The MJPEG MediaTypes are hidden from the rest of the pipeline. They're replaced with uncompressed MediaTypes of equivalent resolution and framerate.

You can choose between two uncompressed subtypes as a preferred replacement for the MJPEG MediaType.

1. NV12 – semi-planar YUV 4:2:0 format (Y planar and chroma subsampled UV interleaved - 12 bpp)
1. YUY2 – fully interleaved YUV 4:2:2 format (YUYV interleaved chroma subsampled - 16 bpp)

This opt-in mechanism instructs the OS pipeline to insert an MJPEG decoding DMFT as per different scenarios described in the following section. Opting into this feature doesn't reduce the already specified limit for number of DMFTs you can insert.

> [!NOTE]
> This feature applies only to UVC class driver-based USB video cameras.

## Functional scenarios

### Scenario 1 – DMFT chain

:::image type="content" source="images/scenario-1-dmft-chain.png" alt-text="Diagram showing the DMFT chain.":::

In this scenario, the developer already has:

- A DMFT chain specified using CameraDeviceMftClsidChain on the camera device interface.

    ***OR***

- A single custom DMFT specified using CameraDeviceMftClsid on the camera device interface registry key.

After you opt in to the MJPEG autodecode pipeline, the MJPEG decoder is inserted as the first component in the chain, and subsequent DMFT gets existing non-MJPEG MediaTypes and translated/decoded MediaTypes at their input.

### Scenario 2 – DMFT chain with PDMFT

:::image type="content" source="images/scenario-2-dmft-chain-with-pdmft.png" alt-text="Diagram showing the DMFT chain with PDMFT.":::

In this scenario, the developer already has a:

- DMFT chain specified using CameraDeviceMftClsidChain on the camera device interface registry key, and the first DMFT in the chain is the Platform DMFT (used for FaceDetection based 3A).

    ***OR***

- A single custom DMFT specified using CameraDeviceMftClsid on the camera device interface registry key along with "EnablePlatformDmft" REG_DWORD 1.

After you opt in to the MJPEG autodecode pipeline, the MJPEG decoder functionality is combined into the first component in the chain (PDMFT). Subsequent DMFT gets existing non-MJPEG MediaTypes and translated/decoded MediaTypes at their input.

### Scenario 3 – DMFT chain with custom order PDMFT

:::image type="content" source="images/scenario-3-dmft-chain-with-pdmft-in-custom-order.png" alt-text="Diagram showing the DMFT chain with PDMFT in custom order.":::

In this scenario, the developer already has a:

- DMFT chain specified using CameraDeviceMftClsidChain on the camera device interface registry key, and the Platform DMFT GUID is specified in any position except the first position.

After you opt in to the MJPEG autodecode pipeline, the MJPEG decoder is inserted as the first component in the chain, and subsequent DMFT gets existing non-MJPEG MediaTypes and translated/decoded MediaTypes at their input. Another instance of PDMFT, inserted in the order specified by the CameraDeviceMftClsidChain, performs the FaceDetection.

### Scenario 4 – No custom DMFT 

:::image type="content" source="images/scenario-4-no-custom-dmft.png" alt-text="Diagram showing no custom DMFT configuration.":::

In this scenario, the developer:

- Doesn't have any custom DMFT configuration  

    ***OR***

- Only opted into Platform DMFT for Face based 3A using "EnablePlatformDmft" REG_DWORD 1.

After you opt in to the MJPEG autodecode pipeline, the MJPEG decoder functionality is inserted as the first component in the chain. If you opted into Platform DMFT, the decoder functionality is combined into the first component (PDMFT). The Device Source makes both existing non-MJPEG MediaTypes and translated/decoded MediaTypes available.

## Opt-in methods

### INF method

If an extension INF or custom INF is shipped for the camera, the opt-in can be achieved via the interface section of the driver INF. Then interface registry entry to be added is MJPGTranslationSubType with a REG_SZ type and the valid/supported values are *NV12* or *YUY2*.

`MJPGTranslationSubType REG_SZ "NV12"`

This entry must be added to all video capture interfaces that are being registered/enabled for the device.

##### Example

```inf
; These are parts of custom inf or extention inf demonstrating the opt-in
[USBVideoExt.NT.Interfaces]
AddInterface=%KSCATEGORY_CAPTURE%,GLOBAL,USBVideoExt.Interface
AddInterface=%KSCATEGORY_VIDEO%,GLOBAL,USBVideoExt.Interface
AddInterface=%KSCATEGORY_VIDEO_CAMERA%,GLOBAL,USBVideoExt.Interface

[USBVideoExt.Interface]
AddReg=USBVideoExt.Interface.AddReg

[USBVideoExt.Interface.AddReg]
HKR,, MJPGTranslationSubType,,"NV12"
;... other interface registry entries
;
```

### Firmware method (MS OS Descriptor 2.0)

MJPEG autodecode can be opted-in by publishing MSOS descriptors.

> [!NOTE]
> The MSOS descriptor method uses a "UVC-" prefix for the property to be automatically populated to the interface registry with the prefix removed. That is, the MSOS descriptor publishes the key as *UVC- MJPGTranslationSubType* and it shall be published to the interface registry by the inbox UVC driver as *MJPGTranslationSubType*.

MS OS Descriptor 1.0 has two components:

- A fixed-length header section
- One or more variable length custom properties sections following the header section

##### Header Section

| Offset | Field | Value | Description |
|----|----|----|----|
| 0 | **wLength** | 0x000A | The length, in bytes, of this header. Shall be set to 10. |
| 2 | **wDescriptorType** | 0x0000 | MSOS20_SET_HEADER_DESCRIPTOR |
| 4 | **dwWindowsVersion** | 0x0A00000D | Windows version. Version for cu release |
| 8 | **wTotalLength** | 0x0054 | The size of entire MS OS 2.0 descriptor set. Shall be set to 84 bytes for currently supported values of subtypes |

##### Custom property section

| Offset | Field | Value | Description |
|---|---|---|---|
| 0 | **wLength** | 0x004A | The length, in bytes, of this descriptor. For currently supported values of subtypes, this shall be 74 bytes |
| 2 | **wDescriptorType** | 0x0004 | MS_OS_20_FEATURE_REG_PROPERTY |
| 4 | **wPropertyDataType** | 0x0001 | The type of registry property. REG_SZ |
| 6 | **wPropertyNameLength** | 0x0036 | The length of the property name. 54 bytes |
| 8 | **PropertyName** | 55 00 56 00 43 00 2d 00 4d 00 4a 00 50 00 47 00 54 00 72 00 61 00 6e 00 73 00 6c 00 61 00 74 00 69 00 6f 00 6e 00 53 00 75 00 62 00 54 00 79 00 70 00 65 00 00 00 | The name of registry property in Unicode format. "UVC-MJPGTranslationSubType". |
| 62 | **wPropertyDataLength** | 0x000A | The length of property data. For currently supported subtypes, this shall be 10 bytes (4 wide-chars + wide-char null terminator) |
| 64 | **PropertyData** | Variable | Property data indicating preferred subtype as a null-terminated Unicode string. For more information, see [Valid values for PropertyData](#valid-values-for-propertydata). |

###### Valid values for PropertyData

| Value | Preferred subtype |
|--|--|
| 4e 00 56 00 31 00 32 00 00 00 | "NV12" |
| 59 00 55 00 59 00 32 00 00 00 | "YUY2" |

##### Example

```cpp
UCHAR Example_MSOS20DescriptorSetForMJPEGAutoDecodeToNV12\[0x54] =
{
//
// Microsoft OS 2.0 Descriptor Set Header
//
    0x0A, 0x00, // wLength - 10 bytes
    0x00, 0x00, // MSOS20_SET_HEADER_DESCRIPTOR
0x0D, 0x00, 0x00, 0x0A, // dwWindowsVersion – 0x0A00000D for future Windows version
0x54, 0x00, // wTotalLength – 84 bytes

//
// Microsoft OS 2.0 Registry Value Feature Descriptor
//
0x4A, 0x00, // wLength- 74 bytes
0x04, 0x00, // wDescriptorType – 4 for Registry Property
0x01, 0x00, // wPropertyDataType - 1 for REG_SZ
0x36, 0x00, // wPropertyNameLength – 54 bytes
0x55, 0x00, // Propert Name – "UVC-MJPGTranslationSubType"
0x56, 0x00,
0x43, 0x00,
0x2d, 0x00,
0x4d, 0x00,
0x4a, 0x00,
0x50, 0x00,
0x47, 0x00,
0x54, 0x00,
0x72, 0x00,
0x61, 0x00,
0x6e, 0x00,
0x73, 0x00,
0x6c, 0x00,
0x61, 0x00,
0x74, 0x00,
0x69, 0x00,
0x6f, 0x00,
0x6e, 0x00,
0x53, 0x00,
0x75, 0x00,
0x62, 0x00,
0x54, 0x00,
0x79, 0x00,
0x70, 0x00,
0x65, 0x00,
0x00, 0x00,
0x0A, 0x00, // wPropertyDataLength – 10 bytes
0x4e, 0x00,
0x56, 0x00,
0x31, 0x00,
0x32, 0x00,
0x00, 0x00 // PropertyData – "NV12"
}
```

### Backward compatibility

This feature isn't available on older versions of Windows, including all versions of Windows 10 and Windows 11 versions 21H2 and 22H2. On these versions, MJPEG MediaTypes aren't automatically decoded. The MJPEG MediaTypes remain available to all components in the pipeline, and to applications.

In order to maintain backward compatibility with older Windows versions:

1. For IHVs shipping without an INF and relying on MSOS descriptors for this feature, no extra steps are needed for backward compatibility. The inbox UVC driver and pipeline components work as expected on older operating systems. Applications continue to see all MediaTypes supported by the camera (including MJPEG) as available on older versions of Windows.

1. For OEMs and IHVs shipping with an INF and custom DMFTs:

    - The DMFTs need to be functional with both, MJPEG media types (on older OS version) and the preferred translated media types opted in (on latest OS version)

    ***OR***

    - Target the INF and driver (on Windows Update) to the latest OS version. On older OS versions, the device functions as a generic UVC compatible camera using only the inbox UVC driver.
