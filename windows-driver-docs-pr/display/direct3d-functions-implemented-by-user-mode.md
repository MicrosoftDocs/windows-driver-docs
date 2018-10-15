---
title: Direct3D Functions Implemented by User Mode Display Drivers
description: This topic describes functions that the user-mode display driver implements and supplies to the Microsoft Direct3D runtime, and can be called by the operating system.
ms.assetid: 6A9D0944-261D-4CAD-AD1B-601369D2FD68
ms.author: windowsdriverdev
ms.date: 10/12/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Direct3D Functions Implemented by User Mode Display Drivers

This topic describes functions that the user-mode display driver implements and supplies to the Microsoft Direct3D runtime, and can be called by the operating system.

## Direct3D Version 9 Functions

This section describes the functions that the user-mode display driver DLL supplies to the Microsoft Direct3D version 9 runtime. 

The user-mode display driver DLL exports the [OpenAdapter](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3DDDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_adapterfuncs) structure when the runtime calls OpenAdapter. 

The Direct3D runtime calls the [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function from the *pfnCreateDevice* member of **D3DDDI_ADAPTERFUNCS** to create a display device that is used to handle a collection of rendering state. The user-mode display driver DLL supplies pointers to all of its display device-specific functions through members of the [D3DDDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure when the runtime calls CreateDevice.

The following functions are contained in [d3dumddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/).

|||
|:--|:--|
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

## Direct3D Version 10 State Functions

This section describe the state functions that the user-mode display driver DLL supplies to the Microsoft Direct3D version 10 runtime. 

The user-mode display driver DLL exports the [OpenAdapter10](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10ddi_adapterfuncs) structure when the runtime calls OpenAdapter10.

The driver supplies pointers to state functions through members of the [D3D10DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10ddi_devicefuncs) structure in a call to the user-mode display driver's [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/).

|||
|:--|:--|
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

## Direct3D Version 10.1 State Functions

This section describes user-mode display driver state functions that are new for version 10.1 of the Microsoft Direct3D runtime. Otherwise, for the remainder of the user-mode display driver state functions, see [Direct3D Version 10 State Functions](#direct3d-version-10-state-functions).

The user-mode display driver DLL exports the [OpenAdapter10](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10ddi_adapterfuncs) structure when the runtime calls OpenAdapter10.

The driver supplies pointers to Direct3D version 10.1 state functions through members of the [D3D10_1DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10_1ddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/).

|||
|:--|:--|
|PFND3D10_1DDI_CALCPRIVATEBLENDSTATESIZE |PFND3D10_1DDI_CALCPRIVATESHADERRESOURCEVIEWSIZE |
|PFND3D10_1DDI_CREATEBLENDSTATE |PFND3D10_1DDI_CREATESHADERRESOURCEVIEW |
|PFND3D10_1DDI_RELOCATEDEVICEFUNCS ||

## Direct3D Version 11 State Functions

This section describes user-mode display driver state functions that are added for the Microsoft Direct3D Version 11.0 runtime. Otherwise, for the remainder of the user-mode display driver state functions, see [Direct3D Version 10 State Functions](#direct3d-version-10-state-functions) and [Direct3D Version 10.1 State Functions](#direct3d-version-10.1-state-functions).

The user-mode display driver DLL exports the [OpenAdapter10_2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10_2DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure when the runtime calls OpenAdapter10_2.

The driver supplies pointers to Direct3D version 11.0 state functions through members of the [D3D11DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d11ddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/).

|||
|:--|:--|
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

## Direct3D Version 11.1 State Functions

The reference pages in this section describe user-mode display driver state functions that are added for the Microsoft Direct3D Version 11.1 runtime. Direct3D 11.1 was introduced with Windows 8. Otherwise, for the remainder of the available functions implemented by user-mode display drivers, see [Direct3D Version 10 State Functions](#direct3d-version-10-state-functions) and [Direct3D Version 11 State Functions](#direct3d-version-11-state-functions).

The user-mode display driver DLL exports the [OpenAdapter10_2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function and supplies pointers to adapter-specific functions through members of the [D3D10_2DDI_ADAPTERFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure when the runtime calls OpenAdapter10_2.

The driver supplies pointers to Direct3D version 11.1 state functions through members of the [D3D11_1DDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3d11_1ddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice(D3D10)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function.

The following functions are contained in [d3d10umddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/) or [d3dumddi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/index).

|||
|:--|:--|
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

## Direct3D Version 11.2 State Functions

This section describes user-mode display driver state functions that are added for the Microsoft Direct3D Version 11.2 runtime. Direct3D 11.2 was introduced with Windows 8.1. 

The driver supplies pointers to Direct3D version 11.2 state functions through members of the [D3DDDI_DEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

|||
|:--|:--|
|[PFND3DWDDM1_3DDI_SETMARKER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_setmarker)|[PFND3DWDDM1_3DDI_SETMARKERMODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm1_3ddi_setmarkermode)|


## Direct3D Version 12.0 State Functions

The reference pages in this section describe user-mode display driver state functions that are added for the Microsoft Direct3D Version 12.0 runtime. Direct3D 12.0 was introduced with Windows 10. 

The driver supplies pointers to Direct3D version 12.0 state functions through members of the [D3DWDDM2_0DDI_VIDEODEVICEFUNCS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/ns-d3d10umddi-d3dwddm2_0ddi_videodevicefuncs) structure in a call to the user-mode display driver's adapter-specific [CreateDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

|||
|:--|:--|
|[PFND3DWDDM2_0DDI_CHECKCRYPTOSESSIONSTATUS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_checkcryptosessionstatus)|[PFND3D12DDI_OPENADAPTER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_openadapter)|
|[PFND3D12DDI_CREATEDEVICE_0003](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_createdevice_0003)|[PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_checkvideoprocessorformatconversion)|
|[PFND3DWDDM2_0DDI_GETCRYPTOSESSIONPRIVATEDATASIZE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_getcryptosessionprivatedatasize)|[PFND3DWDDM2_0DDI_GETDATAFORNEWHARDWAREKEY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_getdatafornewhardwarekey)|
|[PFND3DWDDM2_0DDI_GETRESOURCELAYOUT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_getresourcelayout)|[PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_queryvideocapabilities)|
|[PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_sethardwareprotection)|[PFND3DWDDM2_0DDI_VIDEODECODERENABLEDOWNSAMPLING](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecoderenabledownsampling)|
|[PFND3DWDDM2_0DDI_VIDEODECODERSUBMITBUFFERS1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecodersubmitbuffers1)|[PFND3DWDDM2_0DDI_VIDEODECODERUPDATEDOWNSAMPLING](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecoderupdatedownsampling)|
|[PFND3DWDDM2_0DDI_VIDEOPROCESSORGETBEHAVIORHINTS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorgetbehaviorhints)|[]()|
|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTCOLORSPACE1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetoutputcolorspace1)|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETOUTPUTSHADERUSAGE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetoutputshaderusage)|
|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMCOLORSPACE1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetstreamcolorspace1)|[PFND3DWDDM2_0DDI_VIDEOPROCESSORSETSTREAMMIRROR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_0ddi_videoprocessorsetstreammirror)|





## See also

[Supporting the DXGI DDI](supporting-the-dxgi-ddi.md)

[Multiplane overlay support](multiplane-overlay-support.md)