---
title: Direct3D Functions Implemented by User Mode Display Drivers
description: This topic describes functions that the user-mode display driver implements and supplies to the Microsoft Direct3D runtime, and can be called by the operating system.
ms.assetid: 6A9D0944-261D-4CAD-AD1B-601369D2FD68
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Direct3D Functions Implemented by User Mode Display Drivers

This topic describes functions that the user-mode display driver implements and supplies to the Microsoft Direct3D runtime, and can be called by the operating system.

## Direct3D Version 9 Functions

This section describes the functions that the user-mode display driver DLL supplies to the Microsoft Direct3D version 9 runtime. 

The user-mode display driver DLL exports the [OpenAdapter](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3DDDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_adapterfuncs) structure when the runtime calls OpenAdapter. 

The Direct3D runtime calls the [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function from the *pfnCreateDevice* member of **D3DDDI_ADAPTERFUNCS** to create a display device that is used to handle a collection of rendering state. The user-mode display driver DLL supplies pointers to all of its display device-specific functions through members of the [D3DDDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure when the runtime calls CreateDevice.

The following functions are contained in [d3dumddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/).

|Direct3D Version 9 functions||
|:---|:---|
|PFND3DDDI_AUTHENTICATEDCHANNELKEYEXCHANGE|PFND3DDDI_BLT|
|PFND3DDDI_BUFBLT|PFND3DDDI_BUFBLT1|
|PFND3DDDI_CAPTURETOSYSMEM|PFND3DDDI_CHECKDIRECTFLIPSUPPORT|
|PFND3DDDI_CLEAR|PFND3DDDI_CLOSEADAPTER|
|PFND3DDDI_COLORFILL|PFND3DDDI_COMPOSERECTS|
|PFND3DDDI_CONFIGUREAUTHENICATEDCHANNEL|PFND3DDDI_CREATEAUTHENTICATEDCHANNEL|
|PFND3DDDI_CREATECRYPTOSESSION |PFND3DDDI_CREATEDECODEDEVICE |
|PFND3DDDI_CREATEDEVICE|PFND3DDDI_CREATEEXTENSIONDEVICE |
|PFND3DDDI_CREATELIGHT |PFND3DDDI_CREATEOVERLAY |
|PFND3DDDI_CREATEPIXELSHADER |PFND3DDDI_CREATEQUERY |
|PFND3DDDI_CREATERESOURCE |PFND3DDDI_CREATERESOURCE2 |
|PFND3DDDI_CREATEVERTEXSHADERDECL |PFND3DDDI_CREATEVERTEXSHADERFUNC |
|PFND3DDDI_CREATEVIDEOPROCESSDEVICE |PFND3DDDI_DXVAHD_CREATEVIDEOPROCESSOR|
|PFND3DDDI_CRYPTOSESSIONKEYEXCHANGE |PFND3DDDI_DECODEBEGINFRAME |
|PFND3DDDI_DECODEENDFRAME |PFND3DDDI_DECODEEXECUTE |
|PFND3DDDI_DECODEEXTENSIONEXECUTE |PFND3DDDI_DECRYPTIONBLT |
|PFND3DDDI_DELETEPIXELSHADER |PFND3DDDI_DELETEVERTEXSHADERDECL |
|PFND3DDDI_DELETEVERTEXSHADERFUNC |PFND3DDDI_DEPTHFILL |
|PFND3DDDI_DESTROYAUTHENTICATEDCHANNEL |PFND3DDDI_DESTROYCRYPTOSESSION |
|PFND3DDDI_DESTROYDECODEDEVICE |PFND3DDDI_DESTROYDEVICE |
|PFND3DDDI_DESTROYEXTENSIONDEVICE |PFND3DDDI_DESTROYLIGHT |
|PFND3DDDI_DESTROYOVERLAY |PFND3DDDI_DESTROYQUERY |
|PFND3DDDI_DESTROYRESOURCE |PFND3DDDI_DESTROYVIDEOPROCESSDEVICE |
|PFND3DDDI_DXVAHD_DESTROYVIDEOPROCESSOR |PFND3DDDI_DISCARD |
|PFND3DDDI_DRAWINDEXEDPRIMITIVE |PFND3DDDI_DRAWINDEXEDPRIMITIVE2 |
|PFND3DDDI_DRAWPRIMITIVE |PFND3DDDI_DRAWPRIMITIVE2 |
|PFND3DDDI_DRAWRECTPATCH |PFND3DDDI_DRAWTRIPATCH |
|PFND3DDDI_ENCRYPTIONBLT |PFND3DDDI_EXTENSIONEXECUTE |
|PFND3DDDI_FINISHSESSIONKEYREFRESH |PFND3DDDI_FLIPOVERLAY |
|PFND3DDDI_FLUSH |PFND3DDDI_GENERATEMIPSUBLEVELS |
|PFND3DDDI_GETCAPS |PFND3DDDI_GETCAPTUREALLOCATIONHANDLE |
|PFND3DDDI_GETENCRYPTIONBLTKEY |PFND3DDDI_GETINFO |
|PFND3DDDI_GETOVERLAYCOLORCONTROLS |PFND3DDDI_GETPITCH |
|PFND3DDDI_GETQUERYDATA |PFND3DDDI_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE |
|PFND3DDDI_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE |PFND3DDDI_ISSUEQUERY |
|PFND3DDDI_LOCK |PFND3DDDI_LOCKASYNC |
|PFND3DDDI_LOGSTRINGTABLE |PFND3DDDICB_LOGSTRINGTABLEENTRY |
|PFND3DDDI_MULTIPLYTRANSFORM |PFND3DDDI_OFFERRESOURCES |
|PFND3DDDI_OPENADAPTER |PFND3DDDI_OPENRESOURCE |
|PFND3DDDI_PRESENT1 |PFND3DDDI_SETMARKER |
|PFND3DDDI_SETMARKERMODE |PFND3DDDI_PRESENT |
|PFND3DDDI_QUERYAUTHENTICATEDCHANNEL |PFND3DDDI_QUERYRESOURCERESIDENCY |
|PFND3DDDI_RECLAIMRESOURCES |PFND3DDDI_RENAME |
|PFND3DDDI_RESOLVESHAREDRESOURCE |PFND3DDDI_SETCLIPPLANE |
|PFND3DDDI_SETCONVOLUTIONKERNELMONO |PFND3DDDI_SETDECODERENDERTARGET |
|PFND3DDDI_SETDEPTHSTENCIL |PFND3DDDI_SETDISPLAYMODE |
|PFND3DDDI_SETINDICES |PFND3DDDI_SETINDICESUM |
|PFND3DDDI_SETLIGHT |PFND3DDDI_SETMATERIAL |
|PFND3DDDI_SETOVERLAYCOLORCONTROLS |PFND3DDDI_SETPALETTE |
|PFND3DDDI_SETPIXELSHADER |PFND3DDDI_SETPIXELSHADERCONST |
|PFND3DDDI_SETPIXELSHADERCONSTB |PFND3DDDI_SETPIXELSHADERCONSTI |
|PFND3DDDI_SETPRIORITY |PFND3DDDI_SETRENDERSTATE |
|PFND3DDDI_SETRENDERTARGET |PFND3DDDI_SETSCISSORRECT |
|PFND3DDDI_SETSTREAMSOURCE |PFND3DDDI_SETSTREAMSOURCEFREQ |
|PFND3DDDI_SETSTREAMSOURCEUM |PFND3DDDI_SETTEXTURE |
|PFND3DDDI_SETTEXTURESTAGESTATE |PFND3DDDI_SETTRANSFORM |
|PFND3DDDI_SETVERTEXSHADERCONST |PFND3DDDI_SETVERTEXSHADERCONSTB |
|PFND3DDDI_SETVERTEXSHADERCONST |PFND3DDDI_SETVERTEXSHADERDECL |
|PFND3DDDI_SETVERTEXSHADERFUNC |PFND3DDDI_DXVAHD_SETVIDEOPROCESSBLTSTATE |
|PFND3DDDI_SETVIDEOPROCESSRENDERTARGET |PFND3DDDI_DXVAHD_SETVIDEOPROCESSSTREAMSTATE |
|PFND3DDDI_SETVIEWPORT |PFND3DDDI_SETZRANGE |
|PFND3DDDI_STARTSESSIONKEYREFRESH |PFND3DDDI_STATESET |
|PFND3DDDI_TEXBLT |PFND3DDDI_TEXBLT1 |
|PFND3DDDI_UNLOCK |PFND3DDDI_UNLOCKASYNC |
|PFND3DDDI_UPDATEOVERLAY |PFND3DDDI_UPDATEPALETTE |
|PFND3DDDI_UPDATEWINFO|PFND3DDDI_VALIDATEDEVICE |
|PFND3DDDI_VIDEOPROCESSBEGINFRAME |PFND3DDDI_VIDEOPROCESSBLT |
|PFND3DDDI_DXVAHD_VIDEOPROCESSBLTHD |PFND3DDDI_VIDEOPROCESSENDFRAME |
|PFND3DDDI_VOLBLT |PFND3DDDI_VOLBLT1 |

### User-Mode Display Driver Parameter Structures

This section describes structures that are used by the user-mode display driver functions. The Microsoft Direct3D runtime passes pointers to these structures in parameters of the user-mode display driver functions.

| Structures ||
|:---|:---|
|D3DDDIARG_AUTHENTICATEDCHANNELKEYEXCHANGE|D3DDDIARG_BLT|
|D3DDDIARG_BUFFERBLT|D3DDDIARG_BUFFERBLT1|
|D3DDDIARG_CAPTURETOSYSMEM|D3DDDIARG_CHECKDIRECTFLIPSUPPORT|
|D3DDDIARG_CHECKPRESENTDURATIONSUPPORT|D3DDDIARG_CLEAR|
|D3DDDIARG_COLORFILL|D3DDDIARG_COMPOSERECTS|
|D3DDDIARG_CONFIGUREAUTHENTICATEDCHANNEL|D3DDDIARG_CREATEAUTHENTICATEDCHANNEL|
|D3DDDIARG_CREATECRYPTOSESSION|D3DDDIARG_CREATEDECODEDEVICE|
|D3DDDIARG_CREATEDEVICE|D3DDDIARG_CREATEEXTENSIONDEVICE|
|D3DDDIARG_CREATELIGHT|D3DDDIARG_CREATEOVERLAY|
|D3DDDIARG_CREATEPIXELSHADER|D3DDDIARG_CREATEQUERY|
|D3DDDIARG_CREATEVERTEXSHADERDECL|D3DDDIARG_CREATEVERTEXSHADERFUNC|
|D3DDDIARG_CREATEVIDEOPROCESSDEVICE|D3DDDIARG_CRYPTOSESSIONKEYEXCHANGE|
|D3DDDIARG_DECODEBEGINFRAME|D3DDDIARG_DECODEENDFRAME|
|D3DDDIARG_DECODEEXECUTE|D3DDDIARG_DECODEEXTENSIONEXECUTE|
|D3DDDIARG_DECRYPTIONBLT|D3DDDIARG_DEPTHFILL|
|D3DDDIARG_DESTROYAUTHENTICATEDCHANNEL|D3DDDIARG_DESTROYCRYPTOSESSION|
|D3DDDIARG_DESTROYLIGHT |D3DDDIARG_DESTROYOVERLAY |
|D3DDDIARG_DISCARD |D3DDDIARG_DRAWINDEXEDPRIMITIVE |
|D3DDDIARG_DRAWINDEXEDPRIMITIVE2 |D3DDDIARG_DRAWPRIMITIVE |
|D3DDDIARG_DRAWPRIMITIVE2 |D3DDDIARG_DRAWRECTPATCH |
|D3DDDIARG_DRAWTRIPATCH |D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR |
|D3DDDIARG_DXVAHD_GETVIDEOPROCESSBLTSTATEPRIVATE |D3DDDIARG_DXVAHD_GETVIDEOPROCESSSTREAMSTATEPRIVATE |
|D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE |D3DDDIARG_DXVAHD_SETVIDEOPROCESSSTREAMSTATE |
|D3DDDIARG_DXVAHD_VIDEOPROCESSBLTHD |D3DDDIARG_ENCRYPTIONBLT |
|D3DDDIARG_EXTENSIONEXECUTE |D3DDDIARG_FINISHSESSIONKEYREFRESH |
|D3DDDIARG_FLIPOVERLAY |D3DDDIARG_GENERATEMIPSUBLEVELS |
|D3DDDIARG_GETCAPS |D3DDDIARG_GETCAPTUREALLOCATIONHANDLE |
|D3DDDIARG_GETENCRYPTIONBLTKEY |D3DDDIARG_GETOVERLAYCOLORCONTROLS |
|D3DDDIARG_GETPITCH |D3DDDIARG_GETQUERYDATA |
|D3DDDIARG_ISSUEQUERY |D3DDDIARG_LOCK |
|D3DDDIARG_LOCKASYNC |D3DDDIARG_MULTIPLYTRANSFORM |
|D3DDDIARG_OFFERRESOURCES |D3DDDIARG_OPENADAPTER |
|D3DDDIARG_OPENRESOURCE |D3DDDIARG_PRESENT |
|D3DDDIARG_PRESENT1 |D3DDDIARG_PRESENTSURFACE |
|D3DDDIARG_QUERYAUTHENTICATEDCHANNEL |D3DDDIARG_QUERYRESOURCERESIDENCY |
|D3DDDIARG_RECLAIMRESOURCES |D3DDDIARG_RENAME |
|D3DDDIARG_RENDERSTATE |D3DDDIARG_RESOLVESHAREDRESOURCE |
|D3DDDIARG_SETCLIPPLANE |D3DDDIARG_SETCONVOLUTIONKERNELMONO |
|D3DDDIARG_SETDECODERENDERTARGET |D3DDDIARG_SETDEPTHSTENCIL |
|D3DDDIARG_SETDISPLAYMODE |D3DDDIARG_SETINDICES|
|D3DDDIARG_SETLIGHT |D3DDDIARG_SETMATERIAL |
|D3DDDIARG_SETOVERLAYCOLORCONTROLS |D3DDDIARG_SETPALETTE |
|D3DDDIARG_SETPIXELSHADERCONST |D3DDDIARG_SETPRIORITY |
|D3DDDIARG_SETRENDERTARGET |D3DDDIARG_SETSTREAMSOURCE |
|D3DDDIARG_SETSTREAMSOURCEFREQ |D3DDDIARG_SETSTREAMSOURCEUM |
|D3DDDIARG_SETTRANSFORM |D3DDDIARG_SETVERTEXSHADERCONST |
|D3DDDIARG_SETVIDEOPROCESSRENDERTARGET |D3DDDIARG_STARTSESSIONKEYREFRESH |
|D3DDDIARG_STATESET |D3DDDIARG_TEXBLT |
|D3DDDIARG_TEXBLT1 |D3DDDIARG_TEXTURESTAGE|
|D3DDDIARG_UNLOCK |D3DDDIARG_UNLOCKASYNC |
|D3DDDIARG_UPDATEOVERLAY |D3DDDIARG_UPDATEPALETTE |
|D3DDDIARG_VALIDATETEXTURESTAGESTATE |D3DDDIARG_VIDEOPROCESSBLT |
|D3DDDIARG_VIDEOPROCESSENDFRAME |D3DDDIARG_VIEWPORTINFO |
|D3DDDIARG_VOLUMEBLT |D3DDDIARG_VOLUMEBLT1 |
|D3DDDIARG_WINFO |D3DDDIARG_ZRANGE |

## Direct3D Version 10 State Functions

This section describe the state functions that the user-mode display driver DLL supplies to the Microsoft Direct3D version 10 runtime. 

The user-mode display driver DLL exports the [OpenAdapter10](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10ddi_adapterfuncs) structure when the runtime calls OpenAdapter10.

The driver supplies pointers to state functions through members of the [D3D10DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10ddi_devicefuncs) structure in a call to the user-mode display driver's [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/).

|Direct3D Version 10 State Functions||
|:---|:---|
|PFND3D10DDI_CALCPRIVATEBLENDSTATESIZE |PFND3D10DDI_CALCPRIVATEDEPTHSTENCILSTATESIZE |
|PFND3D10DDI_CALCPRIVATEDEPTHSTENCILVIEWSIZE |PFND3D10DDI_CALCPRIVATEDEVICESIZE |
|PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE |PFND3D10DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT |
|PFND3D10DDI_CALCPRIVATEOPENEDRESOURCESIZE |PFND3D10DDI_CALCPRIVATEQUERYSIZE |
|PFND3D10DDI_CALCPRIVATERASTERIZERSTATESIZE |PFND3D10DDI_CALCPRIVATERENDERTARGETVIEWSIZE |
|PFND3D10DDI_CALCPRIVATERESOURCESIZE |PFND3D10DDI_CALCPRIVATESAMPLERSIZE |
|PFND3D10DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE |PFND3D10DDI_CALCPRIVATESHADERSIZE |
|PFND3D10DDI_CHECKCOUNTER |PFND3D10DDI_CHECKCOUNTERINFO |
|PFND3D10DDI_CHECKFORMATSUPPORT |PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS |
|PFND3D10DDI_CLEARDEPTHSTENCILVIEW |PFND3D10DDI_CLEARRENDERTARGETVIEW |
|PFND3D10DDI_CLOSEADAPTER |PFND3D10DDI_CREATEBLENDSTATE |
|PFND3D10DDI_CREATEDEPTHSTENCILSTATE |PFND3D10DDI_CREATEDEPTHSTENCILVIEW |
|PFND3D10DDI_CREATEDEVICE |PFND3D10DDI_CREATEELEMENTLAYOUT |
|PFND3D10DDI_CREATEGEOMETRYSHADER |PFND3D10DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT |
|PFND3D10DDI_CREATEPIXELSHADER |PFND3D10DDI_CREATEQUERY |
|PFND3D10DDI_CREATERASTERIZERSTATE |PFND3D10DDI_CREATERENDERTARGETVIEW |
|PFND3D10DDI_CREATERESOURCE |PFND3D10DDI_CREATESAMPLER |
|PFND3D10DDI_CREATESHADERRESOURCEVIEW |PFND3D10DDI_CREATEVERTEXSHADER |
|PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP |PFND3D10DDI_DESTROYBLENDSTATE |
|PFND3D10DDI_DESTROYDEPTHSTENCILSTATE |PFND3D10DDI_DESTROYDEPTHSTENCILVIEW |
|PFND3D10DDI_DESTROYDEVICE |PFND3D10DDI_DESTROYELEMENTLAYOUT |
|PFND3D10DDI_DESTROYQUERY |PFND3D10DDI_DESTROYRASTERIZERSTATE |
|PFND3D10DDI_DESTROYRENDERTARGETVIEW |PFND3D10DDI_DESTROYRESOURCE |
|PFND3D10DDI_DESTROYSAMPLER |PFND3D10DDI_DESTROYSHADER |
|PFND3D10DDI_DESTROYSHADERRESOURCEVIEW |PFND3D10DDI_DRAW |
|PFND3D10DDI_DRAWAUTO |PFND3D10DDI_DRAWINDEXED |
|PFND3D10DDI_DRAWINSTANCED |PFND3D10DDI_FLUSH |
|PFND3D10DDI_GENMIPS |PFND3D10DDI_SETCONSTANTBUFFERS |
|PFND3D10DDI_SETSAMPLERS |PFND3D10DDI_SETSHADER |
|PFND3D10DDI_SETSHADERRESOURCES |PFND3D10DDI_IA_SETINDEXBUFFER |
|PFND3D10DDI_SETINPUTLAYOUT |PFND3D10DDI_IA_SETTOPOLOGY |
|PFND3D10DDI_IA_SETVERTEXBUFFERS |PFND3D10DDI_OPENADAPTER |
|PFND3D10DDI_OPENRESOURCE |PFND3D10DDI_SETCONSTANTBUFFERS |
|PFND3D10DDI_SETSAMPLERS |PFND3D10DDI_SETSHADER |
|PFND3D10DDI_SETSHADERRESOURCES |PFND3D10DDI_QUERYBEGIN |
|PFND3D10DDI_QUERYEND |PFND3D10DDI_QUERYGETDATA |
|PFND3D10DDI_RELOCATEDEVICEFUNCS |PFND3D10DDI_RESOURCECOPY |
|PFND3D10DDI_RESOURCECOPYREGION |PFND3D10DDI_RESOURCEISSTAGINGBUSY |
|PFND3D10DDI_RESOURCEMAP |PFND3D10DDI_RESOURCEREADAFTERWRITEHAZARD |
|PFND3D10DDI_RESOURCERESOLVESUBRESOURCE |PFND3D10DDI_RESOURCEUNMAP |
|PFND3D10DDI_RESOURCEUPDATESUBRESOURCEUP |PFND3D10DDI_SETBLENDSTATE |
|PFND3D10DDI_SETDEPTHSTENCILSTATE |PFND3D10DDI_SETPREDICATION |
|PFND3D10DDI_SETRASTERIZERSTATE |PFND3D10DDI_SETRENDERTARGETS |
|PFND3D10DDI_SETSCISSORRECTS |PFND3D10DDI_SETTEXTFILTERSIZE |
|PFND3D10DDI_SETVIEWPORTS |PFND3D10DDI_SHADERRESOURCEVIEWREADAFTERWRITEHAZARD |
|PFND3D10DDI_SO_SETTARGETS |PFND3D10DDI_SETCONSTANTBUFFERS |
|PFND3D10DDI_SETSAMPLERS |PFND3D10DDI_SETSHADER |
|PFND3D10DDI_SETSHADERRESOURCES ||

### Direct3D 10 Structures and Enumerations

This section describes structures and enumerations that the user-mode display driver Microsoft Direct3D version 10 functions use. The Direct3D runtime passes these structures and enumeration values in parameters of the user-mode display driver functions.

|Direct3D Version 10 Structures and Enumerations||
|:---|:---|
| D3D10_DDI_BLEND | D3D10_DDI_BLEND_DESC |
|D3D10_DDI_BLEND_OP |D3D10_DDI_BOX |
|D3D10_DDI_COMPARISON_FUNC |D3D10_DDI_DEPTH_STENCIL_DESC |
|D3D10_DDI_DEPTH_STENCILOP_DESC|D3D10_DDI_FILTER |
|D3D10_DDI_MAP |D3D10_DDI_MAP_FLAG|
|D3D10_DDI_PRIMITIVE_TOPOLOGY |D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS |
|D3D10_DDI_QUERY_DATA_SO_STATISTICS |D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT |
|D3D10_DDI_RASTERIZER_DESC |D3D10_DDI_RESOURCE_BIND_FLAG |
|D3D10_DDI_RESOURCE_MISC_FLAG |D3D10_DDI_RESOURCE_USAGE |
|D3D10_DDI_SAMPLER_DESC |D3D10_DDI_STENCIL_OP|
|D3D10_DDI_TEXTURE_ADDRESS_MODE |D3D10_DDI_VIEWPORT|
|D3D10_DDIARG_SUBRESOURCE_UP|D3D10DDI_ADAPTERFUNCS |
|D3D10DDI_CORELAYER_DEVICECALLBACKS |D3D10DDI_COUNTER_INFO |
|D3D10DDI_DEVICEFUNCS |D3D10DDI_MAPPED_SUBRESOURCE |
|D3D10DDI_MIPINFO |D3D10DDI_QUERY |
|D3D10DDI_VERTEX_CACHE_DESC |D3D10DDIARG_BUFFER_RENDERTARGETVIEW |
|D3D10DDIARG_BUFFER_SHADERRESOURCEVIEW |D3D10DDIARG_CALCPRIVATEDEVICESIZE |
|D3D10DDIARG_CREATEDEPTHSTENCILVIEW |D3D10DDIARG_CREATEDEVICE |
|D3D10DDIARG_CREATEELEMENTLAYOUT |D3D10DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT |
|D3D10DDIARG_CREATEQUERY |D3D10DDIARG_CREATERENDERTARGETVIEW |
|D3D10DDIARG_CREATERESOURCE |D3D10DDIARG_CREATESHADERRESOURCEVIEW |
|D3D10DDIARG_INPUT_ELEMENT_DESC |D3D10DDIARG_OPENADAPTER |
|D3D10DDIARG_OPENRESOURCE |D3D10DDIARG_SIGNATURE_ENTRY |
|D3D10DDIARG_STAGE_IO_SIGNATURES |D3D10DDIARG_STREAM_OUTPUT_DECLARATION_ENTRY |
|D3D10DDIARG_TEX1D_DEPTHSTENCILVIEW |D3D10DDIARG_TEX1D_RENDERTARGETVIEW |
|D3D10DDIARG_TEX1D_SHADERRESOURCEVIEW |D3D10DDIARG_TEX2D_DEPTHSTENCILVIEW |
|D3D10DDIARG_TEX2D_RENDERTARGETVIEW |D3D10DDIARG_TEX2D_SHADERRESOURCEVIEW |
|D3D10DDIARG_TEX3D_RENDERTARGETVIEW |D3D10DDIARG_TEX3D_SHADERRESOURCEVIEW |
|D3D10DDIARG_TEXCUBE_DEPTHSTENCILVIEW |D3D10DDIARG_TEXCUBE_RENDERTARGETVIEW |
|D3D10DDIARG_TEXCUBE_SHADER|D3D10DDIRESOURCE_TYPE |

## Direct3D Version 10.1 State Functions

This section describes user-mode display driver state functions that are new for version 10.1 of the Microsoft Direct3D runtime. Otherwise, for the remainder of the user-mode display driver state functions, see [Direct3D Version 10 State Functions](#direct3d-version-10-state-functions).

The user-mode display driver DLL exports the [OpenAdapter10](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10ddi_adapterfuncs) structure when the runtime calls OpenAdapter10.

The driver supplies pointers to Direct3D version 10.1 state functions through members of the [D3D10_1DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10_1ddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/).

|Direct3D Version 10.1 State Functions||
|:---|:---|
|PFND3D10_1DDI_CALCPRIVATEBLENDSTATESIZE |PFND3D10_1DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE |
|PFND3D10_1DDI_CREATEBLENDSTATE |PFND3D10_1DDI_CREATESHADERRESOURCEVIEW |
|PFND3D10_1DDI_RELOCATEDEVICEFUNCS ||

### Direct3D 10.1 Structures and Enumerations

This section describes structures and enumerations that the user-mode display driver Microsoft Direct3D version 10.1 functions use. The Direct3D runtime passes these structures and enumeration values in parameters of the user-mode display driver functions.

|Direct3D Version 10.1 Structures and Enumerations||
|:---|:---|
|D3D10_1DDIARG_CREATESHADERRESOURCEVIEW |D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS  |
|D3D10_1DDIARG_TEXCUBE_SHADERRESOURCEVIEW |D3D10_1_DDI_BLEND_DESC |
|D3D10_1DDI_DEVICEFUNCS |D3D10_DDI_RENDER_TARGET_BLEND_DESC1 |

## Direct3D Version 11 State Functions

This section describes user-mode display driver state functions that are added for the Microsoft Direct3D Version 11.0 runtime. Otherwise, for the remainder of the user-mode display driver state functions, see [Direct3D Version 10 State Functions](#direct3d-version-10-state-functions) and [Direct3D Version 10.1 State Functions](#direct3d-version-10.1-state-functions).

The user-mode display driver DLL exports the [OpenAdapter10_2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10_2DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure when the runtime calls OpenAdapter10_2.

The driver supplies pointers to Direct3D version 11.0 state functions through members of the [D3D11DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d11ddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/).

|Direct3D Version 11 State Functions||
|:---|:---|
|PFND3D11DDI_ABANDONCOMMANDLIST |PFND3D11DDI_CALCDEFERREDCONTEXTHANDLESIZE |
|PFND3D11DDI_CALCPRIVATECOMMANDLISTSIZE |PFND3D11DDI_CALCPRIVATEDEFERREDCONTEXTSIZE |
|PFND3D11DDI_CALCPRIVATEDEPTHSTENCILVIEWSIZE |PFND3D11DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT |
|PFND3D11DDI_CALCPRIVATERESOURCESIZE |PFND3D11DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE |
|PFND3D11DDI_CALCPRIVATETESSELLATIONSHADERSIZE |PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE |
|PFND3D11DDI_CHECKDEFERREDCONTEXTHANDLESIZES |PFND3D11DDI_CLEARUNORDEREDACCESSVIEWFLOAT |
|PFND3D11DDI_CLEARUNORDEREDACCESSVIEWUINT |PFND3D11DDI_COMMANDLISTEXECUTE |
|PFND3D11DDI_COPYSTRUCTURECOUNT |PFND3D11DDI_CREATECOMMANDLIST |
|PFND3D11DDI_CREATECOMPUTESHADER |PFND3D11DDI_CREATEDEFERREDCONTEXT |
|PFND3D11DDI_CREATEDEPTHSTENCILVIEW |PFND3D11DDI_CREATEDOMAINSHADER |
|PFND3D11DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT |PFND3D11DDI_CREATEHULLSHADER |
|PFND3D11DDI_CREATERESOURCE |PFND3D11DDI_CREATESHADERRESOURCEVIEW |
|PFND3D11DDI_CREATEUNORDEREDACCESSVIEW |PFND3D10DDI_SETCONSTANTBUFFERS |
|PFND3D10DDI_SETSAMPLERS |PFND3D10DDI_SETSHADER |
|PFND3D10DDI_SETSHADERRESOURCES |PFND3D11DDI_SETSHADER_WITH_IFACES |
|PFND3D11DDI_SETUNORDEREDACCESSVIEWS |PFND3D11DDI_DESTROYCOMMANDLIST |
|PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW |PFND3D11DDI_DISPATCH |
|PFND3D11DDI_DISPATCHINDIRECT |PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT |
|PFND3D11DDI_DRAWINSTANCEDINDIRECT |PFND3D10DDI_SETCONSTANTBUFFERS |
|PFND3D10DDI_SETSAMPLERS |PFND3D10DDI_SETSHADER |
|PFND3D10DDI_SETSHADERRESOURCES |PFND3D11DDI_SETSHADER_WITH_IFACES |
|PFND3D10_2DDI_GETCAPS |PFND3D10_2DDI_GETSUPPORTEDVERSIONS |
|PFND3D11DDI_SETSHADER_WITH_IFACES |PFND3D10DDI_SETCONSTANTBUFFERS |
|PFND3D10DDI_SETSAMPLERS |PFND3D10DDI_SETSHADER |
|PFND3D10DDI_SETSHADERRESOURCES |PFND3D11DDI_SETSHADER_WITH_IFACES |
|PFND3D10DDI_OPENADAPTER |PFND3D11DDI_SETSHADER_WITH_IFACES |
|PFND3D11DDI_RECYCLEC|PFND3D11DDI_RECYCLECREATECOMMANDLIST |
|PFND3D11DDI_RECYCLECREATEDEFERREDCONTEXT |PFND3D11DDI_RELOCATEDEVICEFUNCS |
|PFND3D11DDI_SETRENDERTARGETS |PFND3D11DDI_SETRESOURCEMINLOD |
|PFND3D11DDI_SETSHADER_WITH_IFACES ||

### Direct3D 11 Structures and Enumerations

This section describe structures and enumerations that the user-mode display driver Microsoft Direct3D version 11.0 functions use. The Direct3D runtime passes these structures and enumeration values in parameters of the user-mode display driver functions.

|Direct3D Version 11 Structures and Enumerations||
|:---|:---|
|D3D10_2DDI_ADAPTERFUNCS |D3D10_2DDIARG_GETCAPS |
|D3D10_2DDICAPS_TYPE |D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG |
|D3D11_DDI_QUERY_DATA_PIPELINE_STATISTICS |D3D11DDI_3DPIPELINELEVEL |
|D3D11DDI_3DPIPELINESUPPORT_CAPS |D3D11DDI_CORELAYER_DEVICECALLBACKS |
|D3D11DDI_DEVICEFUNCS |D3D11DDI_HANDLESIZE|
|D3D11DDI_HANDLETYPE |D3D11DDI_SHADER_CAPS |
|D3D11DDI_THREADING_CAPS |D3D11DDIARG_BUFFER_RENDERTARGETVIEW |
|D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW |D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW |
|D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE |D3D11DDIARG_CREATECOMMANDLIST |
|D3D11DDIARG_CREATEDEFERREDCONTEXT |D3D11DDIARG_CREATEDEPTHSTENCILVIEW |
|D3D11DDIARG_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT |D3D11DDIARG_CREATERESOURCE |
|D3D11DDIARG_CREATESHADERRESOURCEVIEW |D3D11DDIARG_CREATEUNORDEREDACCESSVIEW |
|D3D11DDIARG_POINTERDATA |D3D11DDIARG_STREAM_OUTPUT_DECLARATION_ENTRY |
|D3D11DDIARG_TESSELLATION_IO_SIGNATURES |D3D11DDIARG_TEX1D_UNORDEREDACCESSVIEW |
|D3D11DDIARG_TEX2D_UNORDEREDACCESSVIEW |D3D11DDIARG_TEX3D_UNORDEREDACCESSVIEW |

## Direct3D Version 11.1 State Functions

The reference pages in this section describe user-mode display driver state functions that are added for the Microsoft Direct3D Version 11.1 runtime. Direct3D 11.1 was introduced with Windows 8. Otherwise, for the remainder of the available functions implemented by user-mode display drivers, see [Direct3D Version 10 State Functions](#direct3d-version-10-state-functions) and [Direct3D Version 11 State Functions](#direct3d-version-11-state-functions).

The user-mode display driver DLL exports the [OpenAdapter10_2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10_2DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure when the runtime calls OpenAdapter10_2.

The driver supplies pointers to Direct3D version 11.1 state functions through members of the [D3D11_1DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d11_1ddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/) or [d3dumddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/index).

|Direct3D Version 11.1 State Functions||
|:---|:---|
|PFND3D11_1DDI_ASSIGNDEBUGBINARY|[PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_calcprivateauthenticatedchannelsize)|
|PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE |PFND3D11_1DDI_CALCPRIVATECRYPTOSESSIONSIZE |
|PFND3D11_1DDI_CALCPRIVATEGEOMETRYSHADERWITHSTREAMOUTPUT |PFND3D11_1DDI_CALCPRIVATERASTERIZERSTATESIZE |
|PFND3D11_1DDI_CALCPRIVATESHADERSIZE |PFND3D11DDI_CALCPRIVATETESSELLATIONSHADERSIZE |
|[PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSOROUTPUTVIEWSIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessoroutputviewsize)|[PFND3D11_1DDI_CALCPRIVATEVIDEODECODERSIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideodecodersize)|
|[PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessorenumsize)|PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORINPUTVIEWSIZE |
|PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSOROUTPUTVIEWSIZE |[PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORSIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessorsize)|
|PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT |[PFND3D11_1DDI_CHECKVIDEODECODERFORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_checkvideodecoderformat)|
|[PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_checkvideoprocessorformat)|PFND3D11_1DDI_CLEARVIEW |
|PFND3D11_1DDI_CONFIGUREAUTHENTICATEDCHANNEL |PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL |
|PFND3D11_1DDI_CREATEBLENDSTATE |[PFND3D11_1DDI_CREATECRYPTOSESSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_createcryptosession)|
|PFND3D11_1DDI_CREATEDOMAINSHADER |PFND3D11_1DDI_CREATEGEOMETRYSHADER |
|PFND3D11_1DDI_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT |PFND3D11_1DDI_CREATEHULLSHADER |
|PFND3D11_1DDI_CREATEPIXELSHADER |PFND3D11_1DDI_CREATERASTERIZERSTATE |
|PFND3D11_1DDI_CREATEVERTEXSHADER |PFND3D11_1DDI_CREATEVIDEODECODER |
|PFND3D11_1DDI_CREATEVIDEODECODEROUTPUTVIEW |PFND3D11_1DDI_CREATEVIDEOPROCESSOR |
|PFND3D11_1DDI_CREAT|PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW |
|PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW |[PFND3D11_1DDI_CRYPTOSESSIONGETHANDLE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_cryptosessiongethandle)|
|PFND3D11_1DDI_SETCONSTANTBUFFERS |PFND3D11_1DDI_DECRYPTIONBLT |
|PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP |[PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyauthenticatedchannel)|
|[PFND3D11_1DDI_DESTROYCRYPTOSESSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroycryptosession)|[PFND3D11_1DDI_DESTROYVIDEODECODER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyvideodecoder)|
|[PFND3D11_1DDI_DESTROYVIDEODECODEROUTPUTVIEW](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyvideodecoderoutputview)|[PFND3D11_1DDI_DESTROYVIDEOPROCESSOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyvideoprocessor)|
|[PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyvideoprocessorenum)|[PFND3D11_1DDI_DESTROYVIDEOPROCESSORINPUTVIEW](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyvideoprocessorinputview)|
|[PFND3D11_1DDI_DESTROYVIDEOPROCESSOROUTPUTVIEW](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_destroyvideoprocessoroutputview)|[PFND3D11_1DDI_DISCARD](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_discard)|
|[PFND3D11_1DDI_SETCONSTANTBUFFERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_setconstantbuffers)|[PFND3D11_1DDI_ENCRYPTIONBLT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_encryptionblt)|
|[PFND3D11_1DDI_FINISHSESSIONKEYREFRESH](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_finishsessionkeyrefresh)|[PFND3D11_1DDI_FLUSH](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_flush)|
|[PFND3D11_1DDI_GETCAPTUREHANDLE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getcapturehandle)|[PFND3D11_1DDI_GETCERTIFICATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getcertificate)|
|[PFND3D11_1DDI_GETCERTIFICATESIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getcertificatesize)|[PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getcontentprotectioncaps)|
|[PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getcryptokeyexchangetype)|[PFND3D11_1DDI_GETENCRYPTIONBLTKEY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getencryptionbltkey)|
|[PFND3D11_1DDI_GETVIDEODECODERBUFFERINFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderbufferinfo)|[PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderbuffertypecount)|
|[PFND3D11_1DDI_GETVIDEODECODERCONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderconfig)|[PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderconfigcount)|
|[PFND3D11_1DDI_GETVIDEODECODERPROFILE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderprofile)|[PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideodecoderprofilecount)|
|[PFND3D11_1DDI_GETVIDEOPROCESSORCAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcaps)|[PFND3D11_1DDI_GETVIDEOPROCESSORCUSTOMRATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorcustomrate)|
|[PFND3D11_1DDI_GETVIDEOPROCESSORFILTERRANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorfilterrange)|[PFND3D11_1DDI_GETVIDEOPROCESSORRATECONVERSIONCAPS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_getvideoprocessorrateconversioncaps)|
|[PFND3D11_1DDI_SETCONSTANTBUFFERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_setconstantbuffers)|[PFND3D11_1DDI_NEGOTIATEAUTHENTICATEDCHANNELKEYEXCHANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_negotiateauthenticatedchannelkeyexchange)|
|[PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_negotiatecryptosessionkeyeschange)|[PFND3D11_1DDI_QUERYAUTHENTICATEDCHANNEL](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_queryauthenticatedchannel)|
|[PFND3DDDI_QUERYDLISTFORAPPLICATION1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication1)|[PFND3D11_1DDI_RELOCATEDEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_relocatedevicefuncs)|
|[PFND3D11_1DDI_RESOURCECOPYREGION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_resourcecopyregion)|[PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_resourceupdatesubresourceup)|
|[PFND3D10DDI_RETRIEVESUBOBJECT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_retrievesubobject)|[PFND3D11_1DDI_STARTSESSIONKEYREFRESH](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_startsessionkeyrefresh)|
|[PFND3D11_1DDI_VIDEODECODERBEGINFRAME](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videodecoderbeginframe)|[PFND3D11_1DDI_VIDEODECODERENDFRAME](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videodecoderendframe)|
|[PFND3D11_1DDI_VIDEODECODEREXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videodecoderextension)|[PFND3D11_1DDI_VIDEODECODERGETHANDLE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videodecodergethandle)|
|[PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videodecodersubmitbuffers)|[PFND3D11_1DDI_VIDEOPROCESSORBLT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorblt)|
|[PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorgetoutputextension)|[PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorgetstreamextension)|
|[PFND3D11_1DDI_VIDEOPROCESSORINPUTVIEWREADAFTERWRITEHAZARD](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorinputviewreadafterwritehazard)|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTALPHAFILLMODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputalphafillmode)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTBACKGROUNDCOLOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputbackgroundcolor)|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputcolorspace)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTCONSTRICTION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputconstriction)|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTEXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputextension)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTSTEREOMODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputstereomode)|[PFND3D11_1DDI_VIDEOPROCESSORSETOUTPUTTARGETRECT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputtargetrect)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMALPHA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamalpha)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMAUTOPROCESSINGMODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamautoprocessingmode)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamcolorspace)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMDESTRECT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamdestrect)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMEXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamextension)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFILTER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamfilter)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMFRAMEFORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamframeformat)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMLUMAKEY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamlumakey)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMOUTPUTRATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamoutputrate)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPALETTE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreampalette)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMPIXELASPECTRATIO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreampixelaspectratio)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMROTATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamrotation)|
|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSOURCERECT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamsourcerect)|[PFND3D11_1DDI_VIDEOPROCESSORSETSTREAMSTEREOFORMAT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetstreamstereoformat)|

### Direct3D 11.1 Structures and Enumerations

This section describe structures and enumerations that the user-mode display driver Microsoft Direct3D version 11.1 functions use. The Direct3D runtime passes these structures and enumeration values in parameters of the user-mode display driver functions.

|Direct3D Version 11.1 Structures and Enumerations||
|:---|:---|
|D3D11_1_DDI_BLEND_DESC |D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS |
|D3D11_1_DDI_COPY_FLAGS |D3D11_1_DDI_FLUSH_FLAGS |
|D3D11_1_DDI_LOGIC_OP |D3D11_1_DDI_RASTERIZER_DESC |
|D3D11_1_DDI_RENDER_TARGET_BLEND_DESC |D3D11_1DDI_AES_CTR_IV |
|D3D11_1DDI_ARCHITECTURE_INFO_DATA |D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE |
|D3D11_1DDI_AUTHENTICATED_CONFIGURE_ACCESSIBLE_ENCRYPTION|D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION|
|D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE |D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT |
|D3D11_1DDI_AUTHENTICATED_CONFIGURE_OUTPUT |D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION |
|D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE |D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE |
|D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS |D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_COUNT_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_INPUT|D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_ACESSIBILITY_OUTPUT|D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION_INPUT|D3D11_1DDI_AUTHENTICATED_QUERY_CRYPTO_SESSION_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_CURRENT_ACCESSIBILITY_ENCRYPTION_OUTPUT|D3D11_1DDI_AUTHENTICATED_QUERY_DEVICE_HANDLE_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_INPUT|D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_INPUT|D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_INPUT|D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT_ID_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_PROTECTION_OUTPUT|D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_INPUT|D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT|
|D3D11_1DDI_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT_OUTPUT|D3D11_1DDI_BUS_TYPE|
|D3D11_1DDI_CERTIFICATE_INFO|D3D11_1DDI_CERTIFICATE_TYPE|
|D3D11_1DDI_CONTENT_PROTECTION_CAPS|D3D11_1DDI_D3D11_OPTIONS_DATA|
|D3D11_1DDI_DEVICEFUNCS |D3D11_1DDI_ENCRYPTED_BLOCK_INFO|
|D3D11_1DDI_GETCAPTUREHANDLEDATA |D3D11_1DDI_OMAC |
|D3D11_1DDI_VIDEO_COLOR |D3D11_1DDI_VIDEO_COLOR_RGBA |
|D3D11_1DDI_VIDEO_COLOR_YCbCrA|D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS |
|D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC|D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO|
|D3D11_1DDI_VIDEO_DECODER_CONFIG|D3D11_1DDI_VIDEO_DECODER_DESC|
|D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC |D3D11_1DDI_VIDEO_FRAME_FORMAT |
|D3D11_1DDI_VIDEO_INPUT |D3D11_1DDI_VIDEO_OUTPUT |
|D3D11_1DDI_VIDEO_PROCESSOR_ALPHA_FILL_MODE |D3D11_1DDI_VIDEO_PROCESSOR_AUTO_STREAM_CAPS |
|D3D11_1DDI_VIDEO_PROCESSOR_CAPS |D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE |
|D3D11_1DDI_VIDEO_PROCESSOR_CONTENT_DESC |D3D11_1DDI_VIDEO_PROCESSOR_CONVERSION_CAPS |
|D3D11_1DDI_VIDEO_PROCESSOR_CUSTOM_RATE|D3D11_1DDI_VIDEO_PROCESSOR_DEVICE_CAPS |
|D3D11_1DDI_VIDEO_PROCESSOR_FEATURE_CAPS |D3D11_1DDI_VIDEO_PROCESSOR_FILTER |
|D3D11_1DDI_VIDEO_PROCESSOR_FILTER_CAPS |D3D11_1DDI_VIDEO_PROCESSOR_FILTER_RANGE |
|D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_CAPS|D3D11_1DDI_VIDEO_PROCESSOR_FORMAT_SUPPORT |
|D3D11_1DDI_VIDEO_PROCESSOR_ITELECINE_CAPS |D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE |
|D3D11_1DDI_VIDEO_PROCESSOR_OUTPUT_RATE |D3D11_1DDI_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS |
|D3D11_1DDI_VIDEO_PROCESSOR_ROTATION |D3D11_1DDI_VIDEO_PROCESSOR_STEREO_CAPS |
|D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FLIP_MODE |D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT |
|D3D11_1DDI_VIDEO_PROCESSOR_STREAM |D3D11_1DDI_VIDEO_USAGE|
|D3D11_1DDI_VIDEODEVICEFUNCS |D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL |
|D3D11_1DDIARG_CREATECRYPTOSESSION |D3D11_1DDIARG_CREATEVIDEODECODER |
|D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW |D3D11_1DDIARG_CREATEVIDEOPROCESSOR |
|D3D11_1DDIARG_CREATEVIDEOPROCESSORENUM |D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW |
|D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW |D3D11_1DDIARG_SIGNATURE_ENTRY |
|D3D11_1DDIARG_STAGE_IO_SIGNATURES |D3D11_1DDIARG_TESSELLATION_IO_SIGNATURES |
|D3D11_1DDIARG_VIDEODECODERBEGINFRAME |D3D11_1DDIARG_VIDEODECODEREXTENSION |
|D3D11_DDI_SHADER_MIN_PRECISION |D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA |
|D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE ||

## Direct3D Version 11.2 State Functions

This section describes user-mode display driver state functions that are added for the Microsoft Direct3D Version 11.2 runtime. Direct3D 11.2 was introduced with Windows 8.1. 

The driver supplies pointers to Direct3D version 11.2 state functions through members of the [D3DDDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

|Direct3D Version 11.2 State Functions||
|:---|:---|
|[PFND3DWDDM1_3DDI_SETMARKER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_setmarker)|[PFND3DWDDM1_3DDI_SETMARKERMODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_setmarkermode)|

### Direct3D 11.2 Structures and Enumerations

This section describes structures and enumerations that the user-mode display driver Microsoft Direct3D version 11.2 functions use. The Direct3D runtime passes these structures and enumeration values in parameters of the user-mode display driver functions.

|Direct3D Version 11.2 Structures and Enumerations||
|:---|:---|
|D3DWDDM1_3DDI_CHECK_MULTISAMPLE_QUALITY_LEVELS_FLAG |D3DWDDM1_3DDI_DEVICEFUNCS |
|D3DWDDM1_3DDI_D3D11_OPTIONS_DATA1 |D3DWDDM1_3DDI_MARKER_TYPE |
|D3DWDDM1_3DDI_TILE_COPY_FLAG|D3DWDDM1_3DDI_TILE_MAPPING_FLAG |
|D3DWDDM1_3DDI_TILE_RANGE_FLAG |D3DWDDM1_3DDI_TILE_REGION_SIZE |
|D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE |D3DWDDM1_3DDI_TILED_RESOURCES_SUPPORT_FLAG |


## Direct3D Version 12.0 State Functions

The reference pages in this section describe user-mode display driver state functions that are added for the Microsoft Direct3D Version 12.0 runtime. Direct3D 12.0 was introduced with Windows 10. 

The driver supplies pointers to Direct3D version 12.0 state functions through members of the [D3DWDDM2_0DDI_VIDEODEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3dwddm2_0ddi_videodevicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

|Direct3D Version 12.0 State Functions||
|:---|:---|
|[PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_checkcryptosessionstatus)|[PFND3D12DDI_OPENADAPTER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_openadapter)|
|[PFND3D12DDI_CREATEDEVICE_0003](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_createdevice_0003)|[PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_checkvideoprocessorformatconversion)|
|[PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_getcryptosessionprivatedatasize)|[PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_getdatafornewhardwarekey)|
|[PFND3DWDDM2_0DDI_GETRESOURCELAYOUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_getresourcelayout)|[PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_queryvideocapabilities)|
|[PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_sethardwareprotection)|[PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecoderenabledownsampling)|
|[PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecodersubmitbuffers1)|[PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecoderupdatedownsampling)|
|[PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorgetbehaviorhints)|[]()|
|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetoutputcolorspace1)|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetoutputshaderusage)|
|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetstreamcolorspace1)|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetstreammirror)|

### Direct3D 12.0 Structures and Enumerations

This section describes structures and enumerations that the user-mode display driver Microsoft Direct3D version 12 functions use. The Direct3D runtime passes these structures and enumeration values in parameters of the user-mode display driver functions.


| Direct3D Version 12.0 Structures and Enumerations                     |                                                                        |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------|
| D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032                       | D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032                         |
| D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP                                 | D3D12DDI_VIDEO_DECODE_CONFIGURATION                                    |
| D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032                               | D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0032                             |
| D3D12DDI_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEME_COUNT_DATA          | D3D12DDI_VIDEO_DECODE_PROFILE_FORMAT_COUNT_DATA                        |
| D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA                              | D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0033                             |
| D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032                 | D3D12DDIARG_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS_0032                 |
| D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030                               | D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032                         |
| D3D12DDI_CRYPTO_SESSION_FLAGS_0030                                    | D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030                             |
| D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030                      | D3D12DDI_CRYPTO_SESSION_TRANSFORM_SUPPORT_FLAGS_0030                   |
| D3D12DDIARG_CREATE_CRYPTO_SESSION_0030                                | D3D12DDIARG_CREATE_CRYPTO_SESSION_POLICY_0030                          |
| D3D12DDIARG_CREATE_PIPELINE_STATE_0033                                | D3D12DDIARG_CREATE_PROTECTED_RESOURCE_SESSION_0030                     |
| D3D12DDIARG_CREATE_VIDEO_DECODER_0032                                 | D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032                             |
| D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0032                               | D3D12DDIARG_OPEN_CRYPTO_SESSION_0030                                   |
| D3D12DDIARG_OPEN_CRYPTO_SESSION_POLICY_0030                           | D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030                       |
| D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033                            | D3D12DDI_VIDEO_PROCESS_INPUT_STREAM_RATE_INFO_0032                     |
| D3D12DDI_VIEW_INSTANCING_FLAGS                                        | D3D12DDI_VIEW_INSTANCING_TIER                                          |
| D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032                               | D3D12DDI_COMMAND_LIST_FUNCS_3D_0030                                    |
| D3D12DDI_COMMAND_LIST_FUNCS_3D_0032                                   | D3D12DDI_COMMAND_LIST_FUNCS_3D_0033                                    |
| D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_DECODE_0030                         | D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_DECODE_0032                          |
| D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0030                        | D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030                             |
| D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_INPUT_ARGUMENTS_0030 | D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030 |
| D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_OUTPUT_ARGUMENTS_0030       | D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030                 |
| D3D12DDI_CRYPTO_SESSION_TRANSFORM_OUTPUT_ARGUMENTS_0030               | D3D12DDI_CRYPTO_SESSION_TRANSFORM_TRANSCRYPT_OUTPUT_ARGUMENTS_0030     |
| D3D12DDI_D3D12_OPTIONS_DATA_0031                                      | D3D12DDI_D3D12_OPTIONS_DATA_0032                                       |
| D3D12DDI_D3D12_OPTIONS_DATA_0033                                      | D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030                |
| D3D12DDI_DEVICE_FUNCS_CORE_0030                                       | D3D12DDI_DEVICE_FUNCS_CORE_0033                                        |
| D3D12DDI_DEVICE_FUNCS_VIDEO_0030                                      | D3D12DDI_DEVICE_FUNCS_VIDEO_0032                                       |
| D3D12DDI_PROTECTED_RESOURCE_SESSION_SUPPORT_DATA_0030                 | D3D12DDI_VIDEO_CONTENT_PROTECTION_SYSTEM_COUNT_DATA_0030               |
| D3D12DDI_VIDEO_CONTENT_PROTECTION_SYSTEM_SUPPORT_DATA_0030            | D3D12DDI_VIDEO_CRYPTO_SESSION_SUPPORT_DATA_0030                        |
| D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030             | D3D12DDI_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEME_COUNT_DATA_0032      |
| D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032                       | D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032                     |
| D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030                       | D3D12DDI_VIDEO_DECODE_FORMAT_COUNT_DATA_0032                           |
| D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030                     | D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032                      |
| D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032                         | D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032                            |
| D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032                              | D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032                                  |
| D3D12DDI_VIDEO_SCALE_SUPPORT_0032                                     | D3D12DDI_VIEW_INSTANCE_LOCATION                                        |
| D3D12DDI_VIEW_INSTANCING_DESC                                         | D3D12DDI_WRITEBUFFERIMMEDIATE_PARAMETER_0032                           |
| D3D11_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION                        | D3D12_COMMAND_QUEUE_PRIORITY                                           |
| D3D12DDI_ALLOCATION_INFO_0022                                         | D3D12DDI_ALLOCATION_INFO_FLAGS_0022                                    |
| D3D12DDI_COMMAND_LIST_FUNCS_VIDEO                                     | D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS                                  |
| D3D12DDI_COMMAND_QUEUE_FLAGS                                          | D3D12DDI_COMMAND_QUEUE_FUNCS_VIDEO                                     |
| D3D12DDI_CORELAYER_DEVICECALLBACKS_0022                               | D3D12DDI_CREATE_SHADER_FLAGS                                           |
| D3D12DDI_DEALLOCATE_FLAGS_0022                                        | D3D12DDI_DEVICE_FUNCS_CORE_0010                                        |
| D3D12DDI_DEVICE_FUNCS_CORE_0021                                       | D3D12DDI_DEVICE_FUNCS_CORE_VIDEO_0020                                  |
| D3D12DDI_DEVICE_FUNCS_VIDEO                                           | D3D12DDI_EXTENDED_FEATURES_FUNCS_0020                                  |
| D3D12DDI_FEATURE_0020                                                 | D3D12DDI_HANDLETYPE                                                    |
| D3D12DDI_HEAP_FLAGS                                                   | D3D12DDI_PREDICATION_OP                                                |
| D3D12DDI_QUERY_HEAP_TYPE                                              | D3D12DDI_QUERY_TYPE                                                    |
| D3D12DDI_RANGE                                                        | D3D12DDI_RESOURCE_BARRIER_FLAGS                                        |
| D3D12DDI_RESOURCE_BARRIER_TYPE                                        | D3D12DDI_RESOURCE_FLAGS_0003                                           |
| D3D12DDI_RESOURCE_RANGED_BARRIER_0022                                 | D3D12DDI_RESOURCE_TRANSITION_BARRIER_0003                              |
| D3D12DDI_RESOURCE_UAV_BARRIER                                         | D3D12DDI_SHADERCACHE_CALLBACKS_0021                                    |
| D3D12DDI_SHADERCACHE_HASH                                             | D3D12DDI_SWIZZLE_BIT_ENTRY                                             |
| D3D12DDI_SWIZZLE_PATTERN                                              | D3D12DDI_SWIZZLE_PATTERN_DESC_0022                                     |
| D3D12DDI_SWIZZLE_PATTERN_FLAGS                                        | D3D12DDI_TABLE_TYPE                                                    |
| D3D12DDI_TEXTURE_LAYOUT                                               | D3D12DDI_TEXTURE_LAYOUT_CAPS_0001                                      |
| D3D12DDI_VIDEO_CODED_INTERLACE_TYPE                                   | D3D12DDI_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEMES_DATA_0010           |
| D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM                            | D3D12DDI_VIDEO_DECODE_CONFIGURATION_FLAGS                              |
| D3D12DDI_VIDEO_DECODE_CONVERSION_ARGUMENTS                            | D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA                          |
| D3D12DDI_VIDEO_DECODE_CONVERSION_FLAGS                                | D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS                         |
| D3D12DDI_VIDEO_DECODE_FORMATS_DATA                                    | D3D12DDI_VIDEO_DECODE_FRAME_PARAMETER                                  |
| D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS                          | D3D12DDI_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS                          |
| D3D12DDI_VIDEO_DECODE_PARAMETER_TYPE                                  | D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES                                 |
| D3D12DDI_VIDEO_DECODE_STATUS                                          | D3D12DDI_VIDEO_DECODE_SUPPORT_DATA                                     |
| D3D12DDI_VIDEO_DECODE_SUPPORT_FLAGS                                   | D3D12DDI_VIDEO_DECODE_TIER                                             |
| D3D12DDI_VIDEO_FIELD_TYPE                                             | D3D12DDI_VIDEO_FORMAT_DESCRIPTION                                      |
| D3D12DDI_VIDEO_FRAME_STEREO_FORMAT                                    | D3D12DDI_VIDEO_PROCESS_ALPHA_BLENDING                                  |
| D3D12DDI_VIDEO_PROCESS_ALPHA_FILL_MODE                                | D3D12DDI_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS                           |
| D3D12DDI_VIDEO_PROCESS_DEINTERLACE_FLAGS                              | D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS                           |
| D3D12DDI_VIDEO_PROCESS_FILTER_FLAGS                                   | D3D12DDI_VIDEO_PROCESS_FILTER_RANGE                                    |
| D3D12DDI_VIDEO_PROCESS_INPUT_STREAM                                   | D3D12DDI_VIDEO_PROCESS_INPUT_STREAM_FLAGS                              |
| D3D12DDI_VIDEO_PROCESS_MAX_INPUT_STREAMS_DATA                         | D3D12DDI_VIDEO_PROCESS_ORIENTATION                                     |
| D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM                                  | D3D12DDI_VIDEO_PROCESS_PALETTE                                         |
| D3D12DDI_VIDEO_PROCESS_REFERENCE_INFO_DATA                            | D3D12DDI_VIDEO_PROCESS_REFERENCES_INFO                                 |
| D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA                                   | D3D12DDI_VIDEO_PROCESS_SUPPORT_FLAGS                                   |
| D3D12DDI_VIDEO_PROCESS_TRANSFORM                                      | D3D12DDI_VIDEO_SCALE_SUPPORT                                           |
| D3D12DDI_VIDEO_SCALE_SUPPORT_FLAGS                                    | D3D12DDI_VIDEO_USAGE                                                   |
| D3D12DDIARG_CREATE_VIDEO_DECODER                                      | D3D12DDIARG_CREATECOMMANDQUEUE_0023                                    |
| D3D12DDIARG_CREATEDEVICE_0003                                         | D3D12DDIARG_GET_PAGEABLE_SIZE                                          |
| D3D12DDIARG_OPENADAPTER                                               | D3D12DDIARG_RESOURCE_BARRIER_0022                                      |
| D3D12DDIARG_VIDEO_GETCAPS                                             | D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_PARAMETERS                      |
| D3D12DDIARG_VIDEO_PROCESS_OUTPUT_STREAM_PARAMETERS                    | D3D12DDICAPS_TYPE                                                      |
| D3D12DDICAPS_TYPE_VIDEO                                               | D3D12DDICAPS_TYPE_VIDEO_0020                                           |
| D3D12DDICAPS_UMD_BASED_COMMAND_QUEUE_PRIORITY_DATA_0023               | D3D12DDICB_ALLOCATE_0022                                               |
| D3D12DDICB_RECLAIMALLOCATIONS2                                        | D3DWDDM2_0DDI_CHECK_VIDEO_PROCESSOR_FORMAT_CONVERSION                  |
| D3DWDDM2_0DDI_CONTEXTTYPE_FLAG                                        | D3DWDDM2_0DDI_CORELAYER_DEVICECALLBACKS                                |
| D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS                                   | D3DWDDM2_0DDI_DEVICEFUNCS                                              |
| D3DWDDM2_0DDI_IMAGE_INPUT                                             | D3DWDDM2_0DDI_IMAGE_OUTPUT                                             |
| D3DWDDM2_0DDI_IMAGEDEVICEFUNCS                                        | D3DWDDM2_0DDI_JPEG_COMPONENTS                                          |
| D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA                         | D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_INPUT_DATA                    |
| D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA                  | D3DWDDM2_0DDI_SWIZZLE_PATTERN_FLAGS                                    |
| D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS                           | D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING                    |
| D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY                                  | D3DWDDM2_0DDI_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION                 |
| D3DWDDM2_0DDI_VIDEO_DECODER_BUFFER_DESC1                              | D3DWDDM2_0DDI_VIDEO_DECODER_CAPS                                       |
| D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK                  | D3DWDDM2_0DDI_VIDEODEVICEFUNCS                                         |
| D3DWDDM2_0DDI_VIDEO_PROCESSOR_BEHAVIOR_HINTS                          | D3DWDDM2_0DDIARG_DECODE_JPEG                                           |
| D3DWDDM2_0DDIARG_ENCODE_JPEG                                          | D3DWDDM2_2DDI_CORELAYER_DEVICECALLBACKS                                |
| D3DWDDM2_2DDI_DEVICEFUNCS                                             | D3DWDDM2_2DDI_SHADERCACHE_HASH                                         |
| D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC                                    |                                                                        |

## See also

[Supporting the DXGI DDI](supporting-the-dxgi-ddi.md)

[Multiplane overlay support](multiplane-overlay-support.md)

[Direct3D Runtime Functions Called by User Mode Display Drivers](direct3d-runtime-functions-called-by-user-mode.md)

[Direct3D rendering performance improvements](direct3d-rendering-performance-improvements.md)
