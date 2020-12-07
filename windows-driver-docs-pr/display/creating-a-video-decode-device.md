---
title: Creating a Video Decode Device
description: Creating a Video Decode Device
keywords:
- video decoding WDK DirectX VA , creating decode devices
- decoding video WDK DirectX VA , creating decode devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Video Decode Device


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateDecodeDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdecodedevice) function to create a decode device for video acceleration (VA). When the Direct3D runtime is finished with the decode device, it calls the user-mode display driver's [**DestroyDecodeDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_destroydecodedevice) function.

 

