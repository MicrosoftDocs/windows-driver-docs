---
title: Direct3D 11 video playback improvements
description: With wider adoption of Microsoft Direct3D 10 technologies in mainstream apps, some app developers want to treat all content the same.
ms.assetid: BB32F074-16E8-46E4-B9CF-6AEBE331B549
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D 11 video playback improvements


With wider adoption of Microsoft Direct3D 10 technologies in mainstream apps, some app developers want to treat all content the same. This is challenging to do with video on the Microsoft Direct3D 9 API when all 2-D and 3-D content is processed through the Direct3D 10 or 11 APIs. Because Windows 8 introduces video on Microsoft Direct3D 11, applications can use a single API to perform all graphical operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Minimum Windows Display Driver Model (WDDM) version</td>
<td align="left">1.2</td>
</tr>
<tr class="even">
<td align="left">Minimum Windows version</td>
<td align="left">8</td>
</tr>
<tr class="odd">
<td align="left">Driver implementation—Full graphics and Render only</td>
<td align="left">Mandatory for all WDDM 1.2 drivers with Microsoft Direct3D 10-, 10.1-, 11-, or 11.1-capable hardware (or later)</td>
</tr>
<tr class="even">
<td align="left"><a href="https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>Device.Graphics ¦ DX11 Video Decode FeatureLevel 9</strong></p>
<p><strong>Device.Graphics ¦ DX11 VideoProcessing</strong></p></td>
</tr>
</tbody>
</table>

 

These are key benefits to using Direct3D 11:

-   Direct3D 11 video simplifies interoperability between Microsoft Media Foundation and Microsoft DirectX technologies.
-   Using multiple APIs is harder to program, so using video on Direct3D 11 simplifies the programming experience and makes the app more efficient. The API provides more flexibility in using decoded and processed video.
-   The Direct3D 11 API for stereoscopic 3-D video unpacks stereo frames into left- and right-eye images.
-   It has parity with DirectX Video Acceleration (DXVA) 2.0 and DXVA-HD in decoding and video processing capabilities.
-   It works in Session 0 for transcoding scenarios.

## <span id="Direct3D_11_video_device_driver_interfaces__DDIs_"></span><span id="direct3d_11_video_device_driver_interfaces__ddis_"></span><span id="DIRECT3D_11_VIDEO_DEVICE_DRIVER_INTERFACES__DDIS_"></span>Direct3D 11 video device driver interfaces (DDIs)


These device driver interfaces (DDIs) are new or updated for Windows 8:

-   [*CalcPrivateCryptoSessionSize*](https://msdn.microsoft.com/library/windows/hardware/hh451606)
-   [*CalcPrivateAuthenticatedChannelSize*](https://msdn.microsoft.com/library/windows/hardware/hh451604)
-   [*CalcPrivateVideoDecoderOutputViewSize*](https://msdn.microsoft.com/library/windows/hardware/hh451608)
-   [*CalcPrivateVideoDecoderSize*](https://msdn.microsoft.com/library/windows/hardware/hh451610)
-   [*CalcPrivateVideoProcessorEnumSize*](https://msdn.microsoft.com/library/windows/hardware/hh451611)
-   [*CalcPrivateVideoProcessorInputViewSize*](https://msdn.microsoft.com/library/windows/hardware/hh451612)
-   [*CalcPrivateVideoProcessorOutputViewSize*](https://msdn.microsoft.com/library/windows/hardware/hh451613)
-   [*CalcPrivateVideoProcessorSize*](https://msdn.microsoft.com/library/windows/hardware/hh451614)
-   [*CheckFormatSupport*](https://msdn.microsoft.com/library/windows/hardware/ff539390)
-   [*CheckVideoDecoderFormat*](https://msdn.microsoft.com/library/windows/hardware/hh451615)
-   [*CheckVideoProcessorFormat*](https://msdn.microsoft.com/library/windows/hardware/hh451616)
-   [*ConfigureAuthenticatedChannel(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh451617)
-   [*CreateAuthenticatedChannel(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh451618)
-   [*CreateCryptoSession*](https://msdn.microsoft.com/library/windows/hardware/hh451619)
-   [*CreateResource2*](https://msdn.microsoft.com/library/windows/hardware/hh406287)
-   [*CreateVideoDecoder*](https://msdn.microsoft.com/library/windows/hardware/hh451620)
-   [*CreateVideoDecoderOutputView*](https://msdn.microsoft.com/library/windows/hardware/hh451621)
-   [*CreateVideoProcessor*](https://msdn.microsoft.com/library/windows/hardware/hh451622)
-   [*CreateVideoProcessorEnum*](https://msdn.microsoft.com/library/windows/hardware/hh451623)
-   [*CreateVideoProcessorInputView*](https://msdn.microsoft.com/library/windows/hardware/hh451624)
-   [*CreateVideoProcessorOutputView*](https://msdn.microsoft.com/library/windows/hardware/hh451625)
-   [*CryptoSessionGetHandle*](https://msdn.microsoft.com/library/windows/hardware/hh451626)
-   [*DecryptionBlt(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh451628)
-   [*DestroyAuthenticatedChannel*](https://msdn.microsoft.com/library/windows/hardware/hh451630)
-   [*DestroyCryptoSession*](https://msdn.microsoft.com/library/windows/hardware/hh451632)
-   [*DestroyVideoDecoder*](https://msdn.microsoft.com/library/windows/hardware/hh451634)
-   [*DestroyVideoDecoderOutputView*](https://msdn.microsoft.com/library/windows/hardware/hh451636)
-   [*DestroyVideoProcessor*](https://msdn.microsoft.com/library/windows/hardware/hh451638)
-   [*DestroyVideoProcessorEnum*](https://msdn.microsoft.com/library/windows/hardware/hh451639)
-   [*DestroyVideoProcessorInputView*](https://msdn.microsoft.com/library/windows/hardware/hh451642)
-   [*DestroyVideoProcessorOutputView*](https://msdn.microsoft.com/library/windows/hardware/hh451644)
-   [*EncryptionBlt(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh451646)
-   [*FinishSessionKeyRefresh*](https://msdn.microsoft.com/library/windows/hardware/hh451648)
-   [*GetCaptureHandle*](https://msdn.microsoft.com/library/windows/hardware/hh451650)
-   [*GetCertificate*](https://msdn.microsoft.com/library/windows/hardware/hh451652)
-   [*GetCertificateSize*](https://msdn.microsoft.com/library/windows/hardware/hh451654)
-   [*GetContentProtectionCaps*](https://msdn.microsoft.com/library/windows/hardware/hh451656)
-   [*GetCryptoKeyExchangeType*](https://msdn.microsoft.com/library/windows/hardware/hh451658)
-   [*GetEncryptionBltKey*](https://msdn.microsoft.com/library/windows/hardware/hh451660)
-   [*GetVideoDecoderBufferInfo*](https://msdn.microsoft.com/library/windows/hardware/hh451661)
-   [*GetVideoDecoderBufferTypeCount*](https://msdn.microsoft.com/library/windows/hardware/hh451663)
-   [*GetVideoDecoderConfig*](https://msdn.microsoft.com/library/windows/hardware/hh451665)
-   [*GetVideoDecoderConfigCount*](https://msdn.microsoft.com/library/windows/hardware/hh451668)
-   [*GetVideoDecoderProfile*](https://msdn.microsoft.com/library/windows/hardware/hh451670)
-   [*GetVideoDecoderProfileCount*](https://msdn.microsoft.com/library/windows/hardware/hh451672)
-   [*GetVideoProcessorCaps*](https://msdn.microsoft.com/library/windows/hardware/hh451674)
-   [*GetVideoProcessorCustomRate*](https://msdn.microsoft.com/library/windows/hardware/hh451676)
-   [*GetVideoProcessorFilterRange*](https://msdn.microsoft.com/library/windows/hardware/hh451689)
-   [*GetVideoProcessorRateConversionCaps*](https://msdn.microsoft.com/library/windows/hardware/hh451690)
-   [*NegotiateAuthenticatedChannelKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/hh451691)
-   [*NegotiateCryptoSessionKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/hh451692)
-   [*QueryAuthenticatedChannel(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh451694)
-   [*RetrieveSubObject(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh439849)
-   [*StartSessionKeyRefresh*](https://msdn.microsoft.com/library/windows/hardware/hh451696)
-   [*VideoDecoderBeginFrame*](https://msdn.microsoft.com/library/windows/hardware/hh451697)
-   [*VideoDecoderEndFrame*](https://msdn.microsoft.com/library/windows/hardware/hh451698)
-   [*VideoDecoderExtension*](https://msdn.microsoft.com/library/windows/hardware/hh451699)
-   [*VideoDecoderGetHandle*](https://msdn.microsoft.com/library/windows/hardware/hh451700)
-   [*VideoDecoderSubmitBuffers*](https://msdn.microsoft.com/library/windows/hardware/hh451701)
-   [*VideoProcessorBlt*](https://msdn.microsoft.com/library/windows/hardware/hh451703)
-   [*VideoProcessorGetOutputExtension*](https://msdn.microsoft.com/library/windows/hardware/hh451705)
-   [*VideoProcessorGetStreamExtension*](https://msdn.microsoft.com/library/windows/hardware/hh439773)
-   [*VideoProcessorInputViewReadAfterWriteHazard*](https://msdn.microsoft.com/library/windows/hardware/hh439775)
-   [*VideoProcessorSetOutputAlphaFillMode*](https://msdn.microsoft.com/library/windows/hardware/hh439778)
-   [*VideoProcessorSetOutputBackgroundColor*](https://msdn.microsoft.com/library/windows/hardware/dn459003)
-   [*VideoProcessorSetOutputColorSpace*](https://msdn.microsoft.com/library/windows/hardware/hh439782)
-   [*VideoProcessorSetOutputConstriction*](https://msdn.microsoft.com/library/windows/hardware/hh439784)
-   [*VideoProcessorSetOutputExtension*](https://msdn.microsoft.com/library/windows/hardware/hh439786)
-   [*VideoProcessorSetOutputStereoMode*](https://msdn.microsoft.com/library/windows/hardware/hh439788)
-   [*VideoProcessorSetOutputTargetRect*](https://msdn.microsoft.com/library/windows/hardware/hh439790)
-   [*VideoProcessorSetStreamAlpha*](https://msdn.microsoft.com/library/windows/hardware/hh439792)
-   [*VideoProcessorSetStreamAutoProcessingMode*](https://msdn.microsoft.com/library/windows/hardware/hh439794)
-   [*VideoProcessorSetStreamColorSpace*](https://msdn.microsoft.com/library/windows/hardware/hh439796)
-   [*VideoProcessorSetStreamDestRect*](https://msdn.microsoft.com/library/windows/hardware/dn459004)
-   [*VideoProcessorSetStreamExtension*](https://msdn.microsoft.com/library/windows/hardware/hh439800)
-   [*VideoProcessorSetStreamFilter*](https://msdn.microsoft.com/library/windows/hardware/hh439802)
-   [*VideoProcessorSetStreamFrameFormat*](https://msdn.microsoft.com/library/windows/hardware/hh439804)
-   [*VideoProcessorSetStreamLumaKey*](https://msdn.microsoft.com/library/windows/hardware/hh439805)
-   [*VideoProcessorSetStreamOutputRate*](https://msdn.microsoft.com/library/windows/hardware/hh439807)
-   [*VideoProcessorSetStreamPalette*](https://msdn.microsoft.com/library/windows/hardware/hh439809)
-   [*VideoProcessorSetStreamPixelAspectRatio*](https://msdn.microsoft.com/library/windows/hardware/hh439811)
-   [*VideoProcessorSetStreamRotation*](https://msdn.microsoft.com/library/windows/hardware/hh439813)
-   [*VideoProcessorSetStreamSourceRect*](https://msdn.microsoft.com/library/windows/hardware/hh439815)
-   [*VideoProcessorSetStreamStereoFormat*](https://msdn.microsoft.com/library/windows/hardware/hh439817)
-   [**D3D10\_DDI\_RESOURCE\_BIND\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/ff541995)
-   [**D3D10\_DDI\_RESOURCE\_MISC\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/ff542004)
-   [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_ALPHA\_FILL\_MODE**](https://msdn.microsoft.com/library/windows/hardware/hh450963)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_AUTO\_STREAM\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450966)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450968)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_COLOR\_SPACE**](https://msdn.microsoft.com/library/windows/hardware/hh450970)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_CONTENT\_DESC**](https://msdn.microsoft.com/library/windows/hardware/hh450972)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_CONVERSION\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450975)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_CUSTOM\_RATE**](https://msdn.microsoft.com/library/windows/hardware/hh450977)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450978)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_FEATURE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450980)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_FILTER**](https://msdn.microsoft.com/library/windows/hardware/hh450982)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_FILTER\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450983)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_FILTER\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh450985)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_FORMAT\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450986)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_FORMAT\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/hh450987)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_ITELECINE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450988)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_OUTPUT\_RATE**](https://msdn.microsoft.com/library/windows/hardware/hh450989)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_RATE\_CONVERSION\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450990)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/hh451019)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_STEREO\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh451023)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_STEREO\_FLIP\_MODE**](https://msdn.microsoft.com/library/windows/hardware/hh451025)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_STEREO\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/hh451029)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/hh451033)
-   [**D3D11\_1DDI\_VIDEO\_USAGE**](https://msdn.microsoft.com/library/windows/hardware/hh451037)
-   [**D3D11\_1DDI\_VIDEODEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/hh406452)
-   [**D3D11\_1DDIARG\_CREATEAUTHENTICATEDCHANNEL**](https://msdn.microsoft.com/library/windows/hardware/hh406306)
-   [**D3D11\_1DDIARG\_CREATECRYPTOSESSION**](https://msdn.microsoft.com/library/windows/hardware/hh406308)
-   [**D3D11\_1DDIARG\_CREATEVIDEODECODER**](https://msdn.microsoft.com/library/windows/hardware/hh406310)
-   [**D3D11\_1DDIARG\_CREATEVIDEODECODEROUTPUTVIEW**](https://msdn.microsoft.com/library/windows/hardware/hh406312)
-   [**D3D11\_1DDIARG\_CREATEVIDEOPROCESSOR**](https://msdn.microsoft.com/library/windows/hardware/hh406314)
-   [**D3D11\_1DDIARG\_CREATEVIDEOPROCESSORENUM**](https://msdn.microsoft.com/library/windows/hardware/hh406316)
-   [**D3D11\_1DDIARG\_CREATEVIDEOPROCESSORINPUTVIEW**](https://msdn.microsoft.com/library/windows/hardware/hh406318)
-   [**D3D11\_1DDIARG\_CREATEVIDEOPROCESSOROUTPUTVIEW**](https://msdn.microsoft.com/library/windows/hardware/hh406320)
-   [**D3D11\_1DDIARG\_SIGNATURE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh406322)
-   [**D3D11\_1DDIARG\_STAGE\_IO\_SIGNATURES**](https://msdn.microsoft.com/library/windows/hardware/hh406324)
-   [**D3D11\_1DDIARG\_TESSELLATION\_IO\_SIGNATURES**](https://msdn.microsoft.com/library/windows/hardware/hh406326)
-   [**D3D11\_1DDIARG\_VIDEODECODERBEGINFRAME**](https://msdn.microsoft.com/library/windows/hardware/hh406328)
-   [**D3D11\_1DDIARG\_VIDEODECODEREXTENSION**](https://msdn.microsoft.com/library/windows/hardware/hh406330)
-   [**D3D11\_DDI\_SHADER\_MIN\_PRECISION**](https://msdn.microsoft.com/library/windows/hardware/hh451059)
-   [**D3D11\_DDI\_SHADER\_MIN\_PRECISION\_SUPPORT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/hh451062)
-   [**D3D11\_DDI\_VIDEO\_DECODER\_BUFFER\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh451066)
-   [**D3D11DDI\_HANDLETYPE**](https://msdn.microsoft.com/library/windows/hardware/ff542152)
-   [**D3D11DDIARG\_CREATEDEFERREDCONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff542044)
-   [**D3D11DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542062)
-   [**D3DDDI\_RESOURCEFLAGS2**](https://msdn.microsoft.com/library/windows/hardware/hh439286)
-   [**D3DDDIARG\_CREATERESOURCE2**](https://msdn.microsoft.com/library/windows/hardware/hh451074)
-   [**DXVAHDDDI\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/hh464119)
-   [**DXVAHDDDI\_STREAM\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff563068)
-   [**DXVAHDDDI\_STREAM\_STATE\_ROTATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/hh464120)
-   [**DXVAHDDDI\_VPDEVCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff563113)
-   [**FORMATOP**](https://msdn.microsoft.com/library/windows/hardware/ff566438)

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


Direct3D 11 API support is required on all Windows 8 hardware.

For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ DX11 Video Decode FeatureLevel 9** and **Device.Graphics ¦ DX11 VideoProcessing**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





