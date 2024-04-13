---
title: Direct3D Driver Initialization
description: Direct3D Driver Initialization
keywords:
- initializing Direct3D drivers
- Direct3D WDK Windows 2000 display , initialization
- DrvGetDirectDrawInfo
- DdGetDriverInfo
ms.date: 04/20/2017
---

# Direct3D Driver Initialization


## <span id="ddk_direct3d_driver_initialization_gg"></span><span id="DDK_DIRECT3D_DRIVER_INITIALIZATION_GG"></span>


When the driver's [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo) function is called by the Microsoft DirectDraw runtime to initialize DirectDraw support, the driver must do the following to indicate its Microsoft Direct3D capabilities:

-   Set the DDCAPS\_3D flag in the **ddCaps.dwCaps** member of the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure to indicate that the driver's hardware has 3D acceleration.

-   Set the DDSCAPS\_*Xxx* flags in the **ddCaps.ddsCaps** member of the DD\_HALINFO structure that describe the 3D capabilities of a driver's video memory surface. The flags are listed in the following table.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Flag</th>
    <th align="left">Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>DDSCAPS_3DDEVICE</p></td>
    <td align="left"><p>Indicates that a driver's surface can be used as a destination for 3D rendering.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>DDSCAPS_TEXTURE</p></td>
    <td align="left"><p>Indicates that a driver's surface can be used for 3D texture mapping.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>DDSCAPS_ZBUFFER</p></td>
    <td align="left"><p>Indicates that a driver's surface can be used as a Z-buffer.</p></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   Set the **GetDriverInfo** member of the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure to point to the driver's [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) callback. The driver must also set the DDHALINFO\_GETDRIVERINFOSET flag in the **dwFlags** member of the DD\_HALINFO structure to indicate that it has implemented the **DdGetDriverInfo** callback.

-   Allocate and initialize the members of the [**D3DHAL\_CALLBACKS**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_callbacks) structure and return this structure in the **lpD3DHALCallbacks** member of the DD\_HALINFO structure.

-   Allocate and initialize the members of the [**D3DHAL\_GLOBALDRIVERDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_globaldriverdata) structure and return this structure in the **lpD3DGlobalDriverData** member of the DD\_HALINFO structure.

To indicate that the driver is capable of working with Microsoft DirectX 7.0, it should do the following:

-   Include the D3DDEVCAPS\_DRAWPRIMITIVES2EX flag in the **dwDevCaps** member of the [**D3DDEVICEDESC\_V1**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3ddevicedesc_v1) structure that is reported during Microsoft Direct3D driver initialization.

-   Respond to the GUID\_Miscellaneous2Callbacks GUID in **DdGetDriverInfo** callback by setting the **GetDriverState**, **CreateSurfaceEx**, and **DestroyDDLocal** members of the [**DD\_MISCELLANEOUS2CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_miscellaneous2callbacks) structure. These are set to point to the appropriate callbacks for the Direct3D driver and ORed in the **dwFlags** member with the DDHAL\_MISC2CB32\_CREATESURFACEEX, DDHAL\_MISC2CB32\_GETDRIVERSTATE, and DDHAL\_MISC2CB32\_DESTROYDDLOCAL bits, respectively.

After [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo) returns, GDI calls the driver's [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) callback several times for different GUIDs to complete the driver's initialization. The **DdGetDriverInfo** callback must respond to the following GUIDs to support Direct3D:

<span id="GUID_D3DCallbacks3"></span><span id="guid_d3dcallbacks3"></span><span id="GUID_D3DCALLBACKS3"></span>GUID\_D3DCallbacks3  
The driver should allocate and initialize the members of the [**D3DHAL\_CALLBACKS3**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_callbacks3) structure and return this structure in the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) structure.

<span id="GUID_Miscellaneous2Callbacks"></span><span id="guid_miscellaneous2callbacks"></span><span id="GUID_MISCELLANEOUS2CALLBACKS"></span>GUID\_Miscellaneous2Callbacks  
The driver should allocate and initialize the members of the [**DD\_MISCELLANEOUS2CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_miscellaneous2callbacks) structure and return this structure in the **lpvData** member of the DD\_GETDRIVERINFODATA structure.

<span id="GUID_D3DExtendedCaps"></span><span id="guid_d3dextendedcaps"></span><span id="GUID_D3DEXTENDEDCAPS"></span>GUID\_D3DExtendedCaps  
The driver should allocate and initialize the appropriate members of the [**D3DHAL\_D3DEXTENDEDCAPS**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_d3dextendedcaps) structure and return this structure in the **lpvData** member of the DD\_GETDRIVERINFODATA structure.

<span id="GUID_ZPixelFormats"></span><span id="guid_zpixelformats"></span><span id="GUID_ZPIXELFORMATS"></span>GUID\_ZPixelFormats  
The driver should allocate and initialize the appropriate members of a [**DDPIXELFORMAT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ddpixelformat) structure for every Z-buffer format that the driver supports and return these structures in the **lpvData** member of the DD\_GETDRIVERINFODATA structure. The driver must respond to this GUID if it supports the D3DDP2OP\_CLEAR operation code in its implementation of [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb).

<span id="GUID_D3DParseUnknownCommandCallback"></span><span id="guid_d3dparseunknowncommandcallback"></span><span id="GUID_D3DPARSEUNKNOWNCOMMANDCALLBACK"></span>GUID\_D3DParseUnknownCommandCallback  
The driver should store the pointer to the Direct3D runtime's **D3DParseUnknownCommand** callback. The pointer is passed to the driver in the **lpvData** member of the DD\_GETDRIVERINFODATA structure. The driver's [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) callback calls the **D3DParseUnknownCommand** callback to parse commands that the driver does not recognize.

For more information, see [DirectDraw Driver Initialization](directdraw-driver-initialization.md).

 

