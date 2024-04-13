---
title: Supporting GetDriverInfo2
description: Supporting GetDriverInfo2
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , GetDriverInfo2
- GetDriverInfo2
ms.date: 04/20/2017
---

# Supporting GetDriverInfo2


## <span id="ddk_supporting_getdriverinfo2_gg"></span><span id="DDK_SUPPORTING_GETDRIVERINFO2_GG"></span>


The DirectX 8.0 DDI introduces a new mechanism for querying the driver for information. This mechanism extends the existing [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) entry point to query for additional information from the driver. Currently, this mechanism is only used for querying for DX8 style D3D caps.

**Note**   As you read the following you may question why the **GetDriverInfo2** mechanism is necessary. It would seem preferable to simply define a new **GetDriverInfo** GUID that the driver would handle by returning a D3DCAP8 structure. **GetDriverInfo2**, introduced in the following paragraphs, is a mechanism to minimize the changes required to the Windows Operating Systems to enable DirectX 8.0 level functionality and thus make redistributing the DirectX 8.0 runtime practical.

 

This extension to **GetDriverInfo** takes the form of a *DdGetDriverInfo* call with GUID\_GetDriverInfo2. When a *DdGetDriverInfo* call with that GUID is received by the driver, it must examine the data structure passed in the **lpvData** field of the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) data structure to see what information is being requested. As described below, **lpvData** can point to either a [**DD\_GETDRIVERINFO2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_dd_getdriverinfo2data) or [**DD\_STEREOMODE**](/windows/win32/api/ddrawint/ns-ddrawint-dd_stereomode) structure.

The GUID\_GetDriverInfo2 is the same GUID value as GUID\_DDStereoMode. If your driver does not handle GUID\_DDStereoMode, this is not an issue. However, if your DirectX 8.0 driver handles GUID\_DDStereoMode, note that when a call to *DdGetDriverInfo* with the GUID\_GetDriverInfo2(GUID\_DDStereoMode) is made, the runtime sets the **dwHeight** field of the DD\_STEREOMODE structure to the special value D3DGDI2\_MAGIC. This field corresponds to the **dwMagic** field of the DD\_GETDRIVERINFO2DATA structure. Therefore, by casting the **lpvData** pointer to either a pointer to a DD\_STEREOMODE structure or a pointer to a DD\_GETDRIVERINFO2DATA structure and checking the value of the corresponding field (**dwHeight** or **dwMagic**) for the value D3DGDI2\_MAGIC, you can distinguish between a call to determine stereo mode capabilities or a request of Direct3D 8.0 capabilities.

Once the driver has determined that this is a call to **GetDriverInfo2** it must then determine the type of information being requested by the runtime. This type is contained in the **dwType** field of the DD\_GETDRIVERINFO2DATA data structure.

Finally, the driver copies the requested data into the supplied buffer. It is important to note that the **lpvData** field of the DD\_GETDRIVERINFODATA data structure points to the buffer to which to copy the requested data. **lpvData** also points to the DD\_GETDRIVERINFO2DATA structure. This means that the data returned by the driver overwrites the DD\_GETDRIVERINFO2DATA structure (and, therefore, that the DD\_GETDRIVERINFO2DATA structure occupies the first few DWORDs of the buffer).

In order to be called with **GetDriverInfo2**, and report DirectX 8.0 capabilities, it is necessary for the driver to set the new flag DDHALINFO\_GETDRIVERINFO2 in the **dwFlags** field of the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure returned by the driver. If this flag is not set, the runtime does not send **GetDriverInfo2** calls to the driver and the driver is not recognized as a DirectX 8.0 level driver.

The runtime uses **GetDriverInfo2** with type D3DGDI2\_TYPE\_DXVERSION to notify the driver of the current DX runtime version being used by the application. The runtime provides a pointer to a [**DD\_DXVERSION**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_dd_dxversion) structure in the **lpvData** field of DD\_GETDRIVERINFODATA.

 

