---
title: Direct3D Driver Initialization
description: Direct3D Driver Initialization
ms.assetid: ef37a570-a94e-4021-b84f-4436aa454ac5
keywords:
- initializing Direct3D drivers
- Direct3D WDK Windows 2000 display , initialization
- DrvGetDirectDrawInfo
- DdGetDriverInfo
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Driver Initialization


## <span id="ddk_direct3d_driver_initialization_gg"></span><span id="DDK_DIRECT3D_DRIVER_INITIALIZATION_GG"></span>


When the driver's [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) function is called by the Microsoft DirectDraw runtime to initialize DirectDraw support, the driver must do the following to indicate its Microsoft Direct3D capabilities:

-   Set the DDCAPS\_3D flag in the **ddCaps.dwCaps** member of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to indicate that the driver's hardware has 3D acceleration.

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

-   Set the **GetDriverInfo** member of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure to point to the driver's [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback. The driver must also set the DDHALINFO\_GETDRIVERINFOSET flag in the **dwFlags** member of the DD\_HALINFO structure to indicate that it has implemented the **DdGetDriverInfo** callback.

-   Allocate and initialize the members of the [**D3DHAL\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff544716) structure and return this structure in the **lpD3DHALCallbacks** member of the DD\_HALINFO structure.

-   Allocate and initialize the members of the [**D3DHAL\_GLOBALDRIVERDATA**](https://msdn.microsoft.com/library/windows/hardware/ff545963) structure and return this structure in the **lpD3DGlobalDriverData** member of the DD\_HALINFO structure.

To indicate that the driver is capable of working with Microsoft DirectX 7.0, it should do the following:

-   Include the D3DDEVCAPS\_DRAWPRIMITIVES2EX flag in the **dwDevCaps** member of the [**D3DDEVICEDESC\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff544689) structure that is reported during Microsoft Direct3D driver initialization.

-   Respond to the GUID\_Miscellaneous2Callbacks GUID in **DdGetDriverInfo** callback by setting the **GetDriverState**, **CreateSurfaceEx**, and **DestroyDDLocal** members of the [**DD\_MISCELLANEOUS2CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551645) structure. These are set to point to the appropriate callbacks for the Direct3D driver and ORed in the **dwFlags** member with the DDHAL\_MISC2CB32\_CREATESURFACEEX, DDHAL\_MISC2CB32\_GETDRIVERSTATE, and DDHAL\_MISC2CB32\_DESTROYDDLOCAL bits, respectively.

After [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) returns, GDI calls the driver's [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback several times for different GUIDs to complete the driver's initialization. The **DdGetDriverInfo** callback must respond to the following GUIDs to support Direct3D:

<span id="GUID_D3DCallbacks3"></span><span id="guid_d3dcallbacks3"></span><span id="GUID_D3DCALLBACKS3"></span>GUID\_D3DCallbacks3  
The driver should allocate and initialize the members of the [**D3DHAL\_CALLBACKS3**](https://msdn.microsoft.com/library/windows/hardware/ff544723) structure and return this structure in the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure.

<span id="GUID_Miscellaneous2Callbacks"></span><span id="guid_miscellaneous2callbacks"></span><span id="GUID_MISCELLANEOUS2CALLBACKS"></span>GUID\_Miscellaneous2Callbacks  
The driver should allocate and initialize the members of the [**DD\_MISCELLANEOUS2CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551645) structure and return this structure in the **lpvData** member of the DD\_GETDRIVERINFODATA structure.

<span id="GUID_D3DExtendedCaps"></span><span id="guid_d3dextendedcaps"></span><span id="GUID_D3DEXTENDEDCAPS"></span>GUID\_D3DExtendedCaps  
The driver should allocate and initialize the appropriate members of the [**D3DHAL\_D3DEXTENDEDCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544753) structure and return this structure in the **lpvData** member of the DD\_GETDRIVERINFODATA structure.

<span id="GUID_ZPixelFormats"></span><span id="guid_zpixelformats"></span><span id="GUID_ZPIXELFORMATS"></span>GUID\_ZPixelFormats  
The driver should allocate and initialize the appropriate members of a [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for every Z-buffer format that the driver supports and return these structures in the **lpvData** member of the DD\_GETDRIVERINFODATA structure. The driver must respond to this GUID if it supports the D3DDP2OP\_CLEAR operation code in its implementation of [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704).

<span id="GUID_D3DParseUnknownCommandCallback"></span><span id="guid_d3dparseunknowncommandcallback"></span><span id="GUID_D3DPARSEUNKNOWNCOMMANDCALLBACK"></span>GUID\_D3DParseUnknownCommandCallback  
The driver should store the pointer to the Direct3D runtime's **D3DParseUnknownCommand** callback. The pointer is passed to the driver in the **lpvData** member of the DD\_GETDRIVERINFODATA structure. The driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback calls the **D3DParseUnknownCommand** callback to parse commands that the driver does not recognize.

For more information, see [DirectDraw Driver Initialization](directdraw-driver-initialization.md).

 

 





