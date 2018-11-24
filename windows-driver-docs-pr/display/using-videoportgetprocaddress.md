---
title: Using VideoPortGetProcAddress
description: Using VideoPortGetProcAddress
ms.assetid: 48dace7e-7ba3-48bf-9788-469ff42f6fe3
keywords:
- video miniport drivers WDK Windows 2000 , multiple Windows versions, VideoPortGetProcAddress
- VideoPortGetProcAddress
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using VideoPortGetProcAddress


## <span id="ddk_using_videoportgetprocaddress_gg"></span><span id="DDK_USING_VIDEOPORTGETPROCADDRESS_GG"></span>


A video miniport driver developed on one NT-based operating system version can be loaded and run on an earlier operating system version, as long as the miniport driver does not attempt to use functionality that is specific to the newer operating system version.

When the video miniport driver is loaded, the **VideoPortGetProcAddress** member of the [**VIDEO\_PORT\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff570531) structure contains the address of a callback routine that the video port driver exports, [**VideoPortGetProcAddress**](https://msdn.microsoft.com/library/windows/hardware/ff570315). A miniport driver can use this callback routine to find the address of a video port function exported from *videoprt.sys*. After the miniport driver has the function's address, it can use this address to call the function. This is shown in the following example code.

```cpp
  // Useful typedef for a function pointer type
  //   that points to a function with same argument types
  //   as VideoPortCreateSecondaryDisplay
typedef VP_STATUS ( *pFunc(PVOID, PVOID *, ULONG));

  // Declare a pointer to a function
pFunc pVPFunction;

  // Declare a pointer to a VIDEO_PORT_CONFIG_INFO struct
PVIDEO_PORT_CONFIG_INFO pConfigInfo;

  // Call through VideoPortGetProcAddress callback
  //   to get address of VideoPortCreateSecondaryDisplay
pVPFunction = (pFunc)
  ( *(pConfigInfo->VideoPortGetProcAddress)(
                        pDeviceExt, 
                       "VideoPortCreateSecondaryDisplay")
  );
if (NULL == pVPFunction) {
  // Video port does not export the function
  ...
}
else {
  Status = pVPFunction(DevExtension, 
                      &SecondDevExtension,
                       VIDEO_DUALVIEW_REMOVABLE);
} 
```

After the call through the *VideoPortGetProcAddress* callback routine has executed, *pVPFunction* either is **NULL** or contains the address of the **VideoPortCreateSecondaryDisplay** function. If *pVPFunction* is **NULL**, the video port driver does not export the function you are trying to find, and the miniport driver must not attempt to use it. If *pVPFunction* is not **NULL**, you can use this pointer to call **VideoPortCreateSecondaryDisplay** as shown in the preceding example.

 

 





