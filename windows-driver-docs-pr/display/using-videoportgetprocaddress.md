---
title: Using VideoPortGetProcAddress
description: Using VideoPortGetProcAddress
ms.assetid: 48dace7e-7ba3-48bf-9788-469ff42f6fe3
keywords: ["video miniport drivers WDK Windows 2000 , multiple Windows versions, VideoPortGetProcAddress", "VideoPortGetProcAddress"]
---

# Using VideoPortGetProcAddress


## <span id="ddk_using_videoportgetprocaddress_gg"></span><span id="DDK_USING_VIDEOPORTGETPROCADDRESS_GG"></span>


A video miniport driver developed on one NT-based operating system version can be loaded and run on an earlier operating system version, as long as the miniport driver does not attempt to use functionality that is specific to the newer operating system version.

When the video miniport driver is loaded, the **VideoPortGetProcAddress** member of the [**VIDEO\_PORT\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff570531) structure contains the address of a callback routine that the video port driver exports, [**VideoPortGetProcAddress**](https://msdn.microsoft.com/library/windows/hardware/ff570315). A miniport driver can use this callback routine to find the address of a video port function exported from *videoprt.sys*. After the miniport driver has the function's address, it can use this address to call the function. This is shown in the following example code.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20VideoPortGetProcAddress%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




